function mergeSettings(defaults, userSettings) {
  const merged = { ...defaults };

  for (const key in userSettings) {
    if (Object.prototype.hasOwnProperty.call(userSettings, key)) {
      merged[key] = userSettings[key];
    }
  }

  return merged;
}

if (require.main === module) {
  const defaults = { retries: 3, verbose: true, timeoutMs: 5000 };
  const user = { retries: 0, verbose: false };
  console.log(mergeSettings(defaults, user));
}

module.exports = { mergeSettings };
