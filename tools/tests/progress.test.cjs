'use strict';

const assert = require('node:assert/strict');
const test = require('node:test');
const progressApi = require('../../docs/site-assets/progress.js');

function validProgress() {
  return progressApi.createDefaultProgress('2026-09-02T00:00:00.000Z');
}

test('uses the one documented browser storage key', () => {
  assert.equal(progressApi.STORAGE_KEY, 'az305LearnerProgress.v1');
});

test('creates exactly LAB-00 through LAB-27', () => {
  const value = validProgress();
  assert.deepEqual(Object.keys(value.labs), Array.from({ length: 28 }, (_, index) => `LAB-${String(index).padStart(2, '0')}`));
});

test('allows scores only for LAB-01 through LAB-25', () => {
  const value = validProgress();
  for (const [id, record] of Object.entries(value.labs)) {
    const number = Number(id.slice(-2));
    assert.equal(Object.hasOwn(record, 'score'), number >= 1 && number <= 25, id);
  }
  assert.doesNotThrow(() => progressApi.validateProgress(value));
});

test('requires exactly five boolean checkpoints', () => {
  const value = validProgress();
  value.labs['LAB-04'].checkpoints = [false, false, false, false];
  assert.throws(() => progressApi.validateProgress(value), /exactly five booleans/);
});

test('requires completion to reflect all checkpoints', () => {
  const value = validProgress();
  value.labs['LAB-08'].completed = true;
  assert.throws(() => progressApi.validateProgress(value), /five-checkpoint completion state/);
});

test('rejects a score on a foundation lab', () => {
  const value = validProgress();
  value.labs['LAB-00'].score = 40;
  assert.throws(() => progressApi.validateProgress(value), /LAB-00/);
});

test('rejects a score outside 0 through 50', () => {
  const value = validProgress();
  value.labs['LAB-11'].score = 51;
  assert.throws(() => progressApi.validateProgress(value), /0 through 50/);
});

test('rejects missing and unexpected lab IDs', () => {
  const missing = validProgress();
  delete missing.labs['LAB-27'];
  assert.throws(() => progressApi.validateProgress(missing), /exactly LAB-00 through LAB-27/);
  const unexpected = validProgress();
  unexpected.labs['LAB-28'] = { completed: false, checkpoints: [false, false, false, false, false] };
  assert.throws(() => progressApi.validateProgress(unexpected), /exactly LAB-00 through LAB-27/);
});

test('recursively rejects secret-bearing field names', () => {
  const value = validProgress();
  value.labs['LAB-03'].notes = [{ metadata: { clientSecret: 'do-not-accept' } }];
  assert.throws(() => progressApi.validateProgress(value), /Sensitive field/);
  assert.equal(progressApi.isSensitiveKey('api_key'), true);
  assert.equal(progressApi.isSensitiveKey('azure-tenant-id'), true);
  assert.equal(progressApi.isSensitiveKey('refresh_token_value'), true);
});

test('rejects prototype-pollution fields from JSON input', () => {
  const text = JSON.stringify(validProgress()).replace('"labs":{', '"labs":{"__proto__":{"polluted":true},');
  assert.throws(() => progressApi.parseImportText(text), /Sensitive field/);
  assert.equal({}.polluted, undefined);
});

test('enforces the UTF-8 256 KiB import cap before parsing', () => {
  const oversized = 'é'.repeat((progressApi.MAX_IMPORT_BYTES / 2) + 1);
  assert.throws(() => progressApi.parseImportText(oversized), /256 KiB/);
});

test('round-trips a valid explicit export', () => {
  const value = validProgress();
  value.labs['LAB-01'].checkpoints = [true, true, true, true, true];
  value.labs['LAB-01'].completed = true;
  value.labs['LAB-01'].score = 44;
  const serialized = progressApi.serializeProgress(value, '2026-09-03T00:00:00.000Z');
  const parsed = progressApi.parseImportText(serialized);
  assert.equal(parsed.exportedAt, '2026-09-03T00:00:00.000Z');
  assert.equal(parsed.labs['LAB-01'].score, 44);
  assert.equal(parsed.labs['LAB-01'].completed, true);
});

test('reads and writes only the fixed localStorage key', () => {
  const operations = [];
  const storage = {
    values: new Map(),
    getItem(key) { operations.push(['get', key]); return this.values.get(key) ?? null; },
    setItem(key, value) { operations.push(['set', key]); this.values.set(key, value); }
  };
  const value = progressApi.safeLoad(storage);
  progressApi.safeSave(storage, value);
  assert.deepEqual(operations.map((item) => item[1]), [progressApi.STORAGE_KEY, progressApi.STORAGE_KEY]);
});

test('rejects an invalid import before stored progress can be replaced', () => {
  const original = progressApi.serializeProgress(validProgress(), '2026-09-02T00:00:00.000Z');
  const storage = {
    value: original,
    getItem() { return this.value; },
    setItem(_key, value) { this.value = value; }
  };
  const invalid = JSON.stringify({ schemaVersion: '1.0.0', exportedAt: '2026-09-02T00:00:00.000Z', labs: {} });
  assert.throws(() => {
    const parsed = progressApi.parseImportText(invalid);
    progressApi.safeSave(storage, parsed);
  }, /exactly LAB-00 through LAB-27/);
  assert.equal(storage.value, original);
});
