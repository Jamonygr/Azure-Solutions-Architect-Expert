(function az305ProgressModule(globalScope) {
  'use strict';

  const STORAGE_KEY = 'az305LearnerProgress.v1';
  const MAX_IMPORT_BYTES = 256 * 1024;
  const SCHEMA_VERSION = '1.0.0';
  const LABS = Object.freeze([
    ['LAB-00', 'Safe Bootstrap and Dual-Command Lab Contract'],
    ['LAB-01', 'Centralized Logging and Diagnostic Routing'],
    ['LAB-02', 'Monitoring, Alerting, and Operational Visibility'],
    ['LAB-03', 'Authentication and Identity Management Architecture'],
    ['LAB-04', 'Azure and Hybrid Authorization Architecture'],
    ['LAB-05', 'Secrets, Certificates, and Key Management'],
    ['LAB-06', 'Azure Resource Hierarchy and Tag Governance'],
    ['LAB-07', 'Compliance and Identity Governance'],
    ['LAB-08', 'Relational Data Platform and Service-Tier Selection'],
    ['LAB-09', 'Relational Scalability and Data Protection'],
    ['LAB-10', 'Semi-Structured Data Platform Selection'],
    ['LAB-11', 'Unstructured Data Platform Selection'],
    ['LAB-12', 'Storage Economics, Protection, and Durability'],
    ['LAB-13', 'Data Integration and Analytics Architecture'],
    ['LAB-14', 'Recovery Strategy for Azure and Hybrid Workloads'],
    ['LAB-15', 'Compute Backup, Recovery, and High Availability'],
    ['LAB-16', 'Relational Database Business Continuity'],
    ['LAB-17', 'Semi-Structured and Unstructured Data Resilience'],
    ['LAB-18', 'Compute Requirements, Virtual Machines, and Batch Architecture'],
    ['LAB-19', 'Container and Serverless Compute Architecture'],
    ['LAB-20', 'Messaging, Event-Driven, and API Integration Architecture'],
    ['LAB-21', 'Application Caching, Configuration, and Automated Delivery'],
    ['LAB-22', 'Migration Strategy and Portfolio Assessment'],
    ['LAB-23', 'IaaS, PaaS, Database, and Unstructured Data Migration'],
    ['LAB-24', 'Internet and Hybrid Connectivity with Network Performance'],
    ['LAB-25', 'Network Security, Load Balancing, and Traffic Routing'],
    ['LAB-26', 'Greenfield Multi-Region Digital Platform'],
    ['LAB-27', 'Hybrid Modernization and Migration']
  ]);
  const LAB_IDS = Object.freeze(LABS.map((entry) => entry[0]));
  const LAB_TITLES = Object.freeze(Object.fromEntries(LABS));
  const SCORED_LABS = new Set(LAB_IDS.slice(1, 26));
  const DOMAIN_GROUPS = Object.freeze([
    ['Foundation', ['LAB-00']],
    ['Identity, governance, and monitoring', LAB_IDS.slice(1, 8)],
    ['Data', LAB_IDS.slice(8, 14)],
    ['Business continuity', LAB_IDS.slice(14, 18)],
    ['Infrastructure', LAB_IDS.slice(18, 26)],
    ['Capstones', LAB_IDS.slice(26, 28)]
  ]);
  const ROOT_KEYS = new Set(['schemaVersion', 'exportedAt', 'labs']);
  const LAB_KEYS = new Set(['completed', 'checkpoints', 'score']);
  const SENSITIVE_EXACT_KEYS = new Set([
    'proto', 'prototype', 'constructor',
    'token', 'secret', 'password', 'passphrase', 'credential', 'credentials',
    'key', 'apikey', 'accesskey', 'privatekey', 'clientsecret',
    'accesstoken', 'refreshtoken', 'idtoken', 'authorization', 'cookie',
    'connectionstring', 'sharedaccesssignature', 'sas',
    'tenantid', 'subscriptionid', 'accountid', 'userid', 'email'
  ]);

  function own(object, key) {
    return Object.prototype.hasOwnProperty.call(object, key);
  }

  function canonicalKey(key) {
    return String(key).toLowerCase().replace(/[^a-z0-9]/g, '');
  }

  function isSensitiveKey(key) {
    const normalized = canonicalKey(key);
    if (SENSITIVE_EXACT_KEYS.has(normalized)) return true;
    return /(?:secret|password|passphrase|credential|token|privatekey|connectionstring|sharedaccesssignature|tenantid|subscriptionid|accountid)/.test(normalized);
  }

  function assertNoSensitiveFields(value, path, ancestors) {
    if (value === null || typeof value !== 'object') return;
    if (ancestors.has(value)) throw new Error(`Circular value at ${path}`);
    ancestors.add(value);
    if (Array.isArray(value)) {
      value.forEach((item, index) => assertNoSensitiveFields(item, `${path}[${index}]`, ancestors));
    } else {
      Object.keys(value).forEach((key) => {
        if (isSensitiveKey(key)) throw new Error(`Sensitive field is not permitted at ${path}.${key}`);
        assertNoSensitiveFields(value[key], `${path}.${key}`, ancestors);
      });
    }
    ancestors.delete(value);
  }

  function nowIso() {
    return new Date().toISOString();
  }

  function createDefaultProgress(timestamp) {
    const labs = {};
    LAB_IDS.forEach((id) => {
      labs[id] = { completed: false, checkpoints: [false, false, false, false, false] };
      if (SCORED_LABS.has(id)) labs[id].score = null;
    });
    return { schemaVersion: SCHEMA_VERSION, exportedAt: timestamp || nowIso(), labs };
  }

  function validateIsoDate(value) {
    if (typeof value !== 'string' || !/^\d{4}-\d{2}-\d{2}T/.test(value) || Number.isNaN(Date.parse(value))) {
      throw new Error('exportedAt must be an ISO 8601 date-time string');
    }
  }

  function validateProgress(candidate) {
    if (candidate === null || typeof candidate !== 'object' || Array.isArray(candidate)) {
      throw new Error('Progress import must be a JSON object');
    }
    assertNoSensitiveFields(candidate, '$', new Set());
    const rootKeys = Object.keys(candidate);
    if (rootKeys.some((key) => !ROOT_KEYS.has(key)) || rootKeys.length !== ROOT_KEYS.size) {
      throw new Error('Progress import has missing or unsupported top-level fields');
    }
    if (candidate.schemaVersion !== SCHEMA_VERSION) throw new Error(`schemaVersion must be ${SCHEMA_VERSION}`);
    validateIsoDate(candidate.exportedAt);
    if (candidate.labs === null || typeof candidate.labs !== 'object' || Array.isArray(candidate.labs)) {
      throw new Error('labs must be an object');
    }
    const receivedIds = Object.keys(candidate.labs).sort();
    if (receivedIds.length !== LAB_IDS.length || receivedIds.some((id, index) => id !== LAB_IDS[index])) {
      throw new Error('labs must contain exactly LAB-00 through LAB-27');
    }
    LAB_IDS.forEach((id) => {
      const record = candidate.labs[id];
      if (record === null || typeof record !== 'object' || Array.isArray(record)) {
        throw new Error(`${id} must be an object`);
      }
      const allowedCount = SCORED_LABS.has(id) ? 3 : 2;
      const keys = Object.keys(record);
      if (keys.some((key) => !LAB_KEYS.has(key)) || keys.length !== allowedCount) {
        throw new Error(`${id} has missing or unsupported fields`);
      }
      if (typeof record.completed !== 'boolean') throw new Error(`${id}.completed must be boolean`);
      if (!Array.isArray(record.checkpoints) || record.checkpoints.length !== 5 || record.checkpoints.some((item) => typeof item !== 'boolean')) {
        throw new Error(`${id}.checkpoints must contain exactly five booleans`);
      }
      if (record.completed !== record.checkpoints.every(Boolean)) {
        throw new Error(`${id}.completed must equal the five-checkpoint completion state`);
      }
      if (SCORED_LABS.has(id)) {
        if (!own(record, 'score')) throw new Error(`${id}.score is required`);
        if (record.score !== null && (!Number.isInteger(record.score) || record.score < 0 || record.score > 50)) {
          throw new Error(`${id}.score must be null or an integer from 0 through 50`);
        }
      } else if (own(record, 'score')) {
        throw new Error(`${id} is not scored and must not contain score`);
      }
    });
    return candidate;
  }

  function utf8ByteLength(text) {
    if (typeof TextEncoder !== 'undefined') return new TextEncoder().encode(text).byteLength;
    if (typeof Buffer !== 'undefined') return Buffer.byteLength(text, 'utf8');
    return unescape(encodeURIComponent(text)).length;
  }

  function parseImportText(text) {
    if (typeof text !== 'string') throw new Error('Import input must be text');
    if (utf8ByteLength(text) > MAX_IMPORT_BYTES) throw new Error('Import exceeds the 256 KiB limit');
    let parsed;
    try {
      parsed = JSON.parse(text.replace(/^\uFEFF/, ''));
    } catch (_error) {
      throw new Error('Import is not valid JSON');
    }
    return validateProgress(parsed);
  }

  function cloneProgress(progress) {
    return JSON.parse(JSON.stringify(progress));
  }

  function serializeProgress(progress, timestamp) {
    const output = cloneProgress(validateProgress(progress));
    output.exportedAt = timestamp || nowIso();
    return `${JSON.stringify(output, null, 2)}\n`;
  }

  function safeLoad(storage) {
    const raw = storage.getItem(STORAGE_KEY);
    if (raw === null) return createDefaultProgress();
    return parseImportText(raw);
  }

  function safeSave(storage, progress) {
    const output = cloneProgress(progress);
    output.exportedAt = nowIso();
    validateProgress(output);
    storage.setItem(STORAGE_KEY, JSON.stringify(output));
    return output;
  }

  function element(documentRef, tagName, attributes, text) {
    const node = documentRef.createElement(tagName);
    Object.entries(attributes || {}).forEach(([key, value]) => {
      if (key === 'className') node.className = value;
      else if (key === 'checked') node.checked = value;
      else node.setAttribute(key, value);
    });
    if (text !== undefined) node.textContent = text;
    return node;
  }

  function initializeCatalogFilter(documentRef) {
    const filter = documentRef.querySelector('[data-az305-catalog-filter]');
    if (!filter) return;
    const rows = Array.from(documentRef.querySelectorAll('[data-az305-catalog-row]'));
    const count = documentRef.querySelector('[data-az305-catalog-count]');
    const apply = () => {
      const query = filter.value.trim().toLowerCase();
      let visible = 0;
      rows.forEach((row) => {
        const match = !query || row.textContent.toLowerCase().includes(query);
        row.hidden = !match;
        if (match) visible += 1;
      });
      if (count) count.textContent = `${visible} of ${rows.length} labs shown`;
    };
    filter.addEventListener('input', apply);
    apply();
  }

  function initializeProgressUi(documentRef, storage, confirmReset) {
    const mount = documentRef.getElementById('az305-progress-app');
    if (!mount) return;
    mount.classList.add('az305-progress');
    let progress;
    let persistenceAvailable = true;
    let initialNotice = 'Stored only in this browser. Import and export are always explicit; CLI progress is never synchronized.';
    try {
      progress = safeLoad(storage);
      progress = safeSave(storage, progress);
    } catch (loadError) {
      progress = createDefaultProgress();
      try {
        progress = safeSave(storage, progress);
        initialNotice = `Saved browser progress failed validation and was reset locally: ${loadError.message}`;
      } catch (_storageError) {
        persistenceAvailable = false;
        initialNotice = 'Browser storage is unavailable. Changes will last only for this page session; CLI progress is never synchronized.';
      }
    }

    const toolbar = element(documentRef, 'div', { className: 'az305-progress__toolbar az305-no-print' });
    const exportButton = element(documentRef, 'button', { type: 'button' }, 'Export progress JSON');
    const importButton = element(documentRef, 'button', { type: 'button' }, 'Import progress JSON');
    const importInput = element(documentRef, 'input', { type: 'file', accept: '.json,application/json', hidden: 'hidden' });
    const resetButton = element(documentRef, 'button', { type: 'button' }, 'Reset local progress');
    toolbar.append(exportButton, importButton, importInput, resetButton);

    const overview = element(documentRef, 'div', { className: 'az305-progress__overview' });
    const completionRing = element(documentRef, 'div', {
      className: 'az305-completion-ring',
      role: 'img',
      'aria-label': '0 percent of labs complete'
    });
    const completionLabel = element(documentRef, 'span', { className: 'az305-completion-ring__label', 'aria-hidden': 'true' }, '0%');
    completionRing.append(completionLabel);
    const overviewCopy = element(documentRef, 'div', { className: 'az305-progress__overview-copy' });
    const summary = element(documentRef, 'p', { className: 'az305-progress__summary', 'aria-live': 'polite' });
    const domainProgress = element(documentRef, 'div', { className: 'az305-domain-progress', 'aria-label': 'Completion by curriculum area' });
    const domainRows = new Map();
    DOMAIN_GROUPS.forEach(([label, ids]) => {
      const row = element(documentRef, 'div', { className: 'az305-domain-progress__row' });
      const name = element(documentRef, 'span', {}, label);
      const track = element(documentRef, 'span', {
        className: 'az305-domain-progress__track',
        role: 'progressbar',
        'aria-label': `${label} completion`,
        'aria-valuemin': '0',
        'aria-valuemax': String(ids.length),
        'aria-valuenow': '0'
      });
      const fill = element(documentRef, 'span', { className: 'az305-domain-progress__fill', style: 'width: 0%' });
      const count = element(documentRef, 'span', { className: 'az305-domain-progress__count' }, `0/${ids.length}`);
      track.append(fill);
      row.append(name, track, count);
      domainProgress.append(row);
      domainRows.set(label, { ids, track, fill, count });
    });
    overviewCopy.append(summary, domainProgress);
    overview.append(completionRing, overviewCopy);
    const message = element(documentRef, 'p', { className: 'az305-progress__notice', role: 'status', 'aria-live': 'polite' }, initialNotice);
    const tableWrap = element(documentRef, 'div', { className: 'az305-table-scroll' });
    const table = element(documentRef, 'table', { className: 'az305-progress__table' });
    const thead = element(documentRef, 'thead');
    const headerRow = element(documentRef, 'tr');
    ['Lab', 'Five checkpoints', 'Complete', 'Score / 50'].forEach((label) => headerRow.append(element(documentRef, 'th', { scope: 'col' }, label)));
    thead.append(headerRow);
    const tbody = element(documentRef, 'tbody');
    table.append(thead, tbody);
    tableWrap.append(table);
    mount.replaceChildren(toolbar, overview, message, tableWrap);

    function persist() {
      if (persistenceAvailable) {
        try {
          progress = safeSave(storage, progress);
        } catch (error) {
          persistenceAvailable = false;
          message.className = 'az305-progress__error';
          message.textContent = `Local save failed: ${error.message}`;
        }
      }
      updateSummary();
    }

    function updateSummary() {
      const complete = LAB_IDS.filter((id) => progress.labs[id].completed).length;
      const percent = Math.round((complete / LAB_IDS.length) * 100);
      const scores = LAB_IDS.filter((id) => SCORED_LABS.has(id) && progress.labs[id].score !== null).map((id) => progress.labs[id].score);
      const average = scores.length ? `${(scores.reduce((sum, score) => sum + score, 0) / scores.length).toFixed(1)}/50 average across ${scores.length} scored lab${scores.length === 1 ? '' : 's'}` : 'no assessment scores recorded';
      summary.textContent = `${complete}/28 labs complete · ${average}`;
      completionRing.setAttribute('style', `--az305-progress: ${percent}%`);
      completionRing.setAttribute('aria-label', `${percent} percent of labs complete`);
      completionLabel.textContent = `${percent}%`;
      domainRows.forEach(({ ids, track, fill, count }) => {
        const groupComplete = ids.filter((id) => progress.labs[id].completed).length;
        const groupPercent = Math.round((groupComplete / ids.length) * 100);
        track.setAttribute('aria-valuenow', String(groupComplete));
        fill.setAttribute('style', `width: ${groupPercent}%`);
        count.textContent = `${groupComplete}/${ids.length}`;
      });
    }

    function renderRows() {
      tbody.replaceChildren();
      LAB_IDS.forEach((id) => {
        const record = progress.labs[id];
        const row = element(documentRef, 'tr');
        const labCell = element(documentRef, 'td');
        labCell.append(element(documentRef, 'strong', {}, id), documentRef.createTextNode(` — ${LAB_TITLES[id]}`));
        const checkpointCell = element(documentRef, 'td', { className: 'az305-progress__checks' });
        record.checkpoints.forEach((checked, index) => {
          const label = element(documentRef, 'label');
          const checkbox = element(documentRef, 'input', { type: 'checkbox', checked, 'aria-label': `${id} checkpoint ${index + 1}` });
          checkbox.addEventListener('change', () => {
            record.checkpoints[index] = checkbox.checked;
            record.completed = record.checkpoints.every(Boolean);
            completeCell.textContent = record.completed ? 'Yes' : 'No';
            persist();
          });
          label.append(checkbox, documentRef.createTextNode(String(index + 1)));
          checkpointCell.append(label);
        });
        const completeCell = element(documentRef, 'td', {}, record.completed ? 'Yes' : 'No');
        const scoreCell = element(documentRef, 'td');
        if (SCORED_LABS.has(id)) {
          const score = element(documentRef, 'input', { type: 'number', min: '0', max: '50', step: '1', inputmode: 'numeric', 'aria-label': `${id} score out of 50` });
          score.value = record.score === null ? '' : String(record.score);
          score.addEventListener('change', () => {
            if (score.value === '') record.score = null;
            else {
              const value = Number(score.value);
              if (!Number.isInteger(value) || value < 0 || value > 50) {
                score.setCustomValidity('Enter a whole number from 0 through 50.');
                score.reportValidity();
                score.value = record.score === null ? '' : String(record.score);
                return;
              }
              record.score = value;
            }
            score.setCustomValidity('');
            persist();
          });
          scoreCell.append(score);
        } else {
          scoreCell.textContent = 'Not scored';
        }
        row.append(labCell, checkpointCell, completeCell, scoreCell);
        tbody.append(row);
      });
      updateSummary();
    }

    exportButton.addEventListener('click', () => {
      const text = serializeProgress(progress);
      const blob = new Blob([text], { type: 'application/json' });
      const url = URL.createObjectURL(blob);
      const link = element(documentRef, 'a', { href: url, download: 'az305-progress.json' });
      documentRef.body.append(link);
      link.click();
      link.remove();
      URL.revokeObjectURL(url);
      message.className = 'az305-progress__notice';
      message.textContent = 'Progress was exported locally. No network request was made.';
    });

    importButton.addEventListener('click', () => importInput.click());
    importInput.addEventListener('change', async () => {
      const file = importInput.files && importInput.files[0];
      if (!file) return;
      try {
        if (file.size > MAX_IMPORT_BYTES) throw new Error('Import exceeds the 256 KiB limit');
        const imported = parseImportText(await file.text());
        progress = cloneProgress(imported);
        persist();
        renderRows();
        message.className = 'az305-progress__notice';
        message.textContent = 'Progress import passed validation and replaced browser-local progress.';
      } catch (error) {
        message.className = 'az305-progress__error';
        message.textContent = `Import rejected: ${error.message}`;
      } finally {
        importInput.value = '';
      }
    });

    resetButton.addEventListener('click', () => {
      if (!confirmReset('Reset all browser-local AZ-305 progress? This cannot be undone unless you exported it.')) return;
      progress = createDefaultProgress();
      persist();
      renderRows();
      message.className = 'az305-progress__notice';
      message.textContent = 'Browser-local progress was reset. No CLI file was changed.';
    });

    renderRows();
  }

  const api = Object.freeze({
    STORAGE_KEY,
    MAX_IMPORT_BYTES,
    SCHEMA_VERSION,
    LAB_IDS,
    SCORED_LABS,
    createDefaultProgress,
    validateProgress,
    parseImportText,
    serializeProgress,
    safeLoad,
    safeSave,
    isSensitiveKey
  });

  if (typeof module !== 'undefined' && module.exports) module.exports = api;
  globalScope.AZ305Progress = api;
  if (typeof document !== 'undefined') {
    const boot = () => {
      initializeCatalogFilter(document);
      if (typeof localStorage !== 'undefined') initializeProgressUi(document, localStorage, (message) => globalScope.confirm(message));
    };
    if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', boot, { once: true });
    else boot();
  }
}(typeof globalThis !== 'undefined' ? globalThis : this));
