import assert from 'node:assert/strict';
import { createRequire } from 'node:module';
import test from 'node:test';

const require = createRequire(import.meta.url);
const progress = require('../../docs/site-assets/progress.js');

test('progress uses the fixed browser-local contract', () => {
  assert.equal(progress.STORAGE_KEY, 'az305LearnerProgress.v1');
  assert.equal(progress.MAX_IMPORT_BYTES, 256 * 1024);
  assert.deepEqual(progress.LAB_IDS, Array.from({ length: 28 }, (_, index) => `LAB-${String(index).padStart(2, '0')}`));
  assert.deepEqual([...progress.SCORED_LABS], progress.LAB_IDS.slice(1, 26));
});

test('default progress has five checkpoints and scores only instructional labs', () => {
  const value = progress.createDefaultProgress('2026-09-02T00:00:00Z');
  progress.validateProgress(value);
  for (const id of progress.LAB_IDS) {
    assert.deepEqual(value.labs[id].checkpoints, [false, false, false, false, false]);
    assert.equal(value.labs[id].completed, false);
    if (progress.SCORED_LABS.has(id)) assert.equal(value.labs[id].score, null);
    else assert.equal(Object.hasOwn(value.labs[id], 'score'), false);
  }
});

test('import rejects oversized input and recursively sensitive fields', () => {
  assert.throws(() => progress.parseImportText('x'.repeat((256 * 1024) + 1)), /256 KiB/);
  const value = progress.createDefaultProgress('2026-09-02T00:00:00Z');
  value.labs['LAB-01'].notes = { nested: { ['client' + 'Secret']: 'synthetic' } };
  assert.throws(() => progress.validateProgress(value), /Sensitive field/);
});

test('import rejects unsupported lab IDs and completion mismatches', () => {
  const missing = progress.createDefaultProgress('2026-09-02T00:00:00Z');
  delete missing.labs['LAB-27'];
  assert.throws(() => progress.validateProgress(missing), /exactly LAB-00 through LAB-27/);

  const inconsistent = progress.createDefaultProgress('2026-09-02T00:00:00Z');
  inconsistent.labs['LAB-01'].completed = true;
  assert.throws(() => progress.validateProgress(inconsistent), /completion state/);
});

test('serialization is explicit JSON and leaves the input unchanged', () => {
  const value = progress.createDefaultProgress('2026-09-02T00:00:00Z');
  const output = progress.serializeProgress(value, '2026-09-03T00:00:00Z');
  assert.equal(value.exportedAt, '2026-09-02T00:00:00Z');
  assert.equal(JSON.parse(output).exportedAt, '2026-09-03T00:00:00Z');
  assert.ok(output.endsWith('\n'));
});
