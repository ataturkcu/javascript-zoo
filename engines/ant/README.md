# Ant

Ant-sized JavaScript runtime, notable for async/await, FFI, HTTP servers, crypto, while being under 4 MB.

* Repository:   [theMackabu/ant](https://github.com/theMackabu/ant.git) <span class="shields"><img src="https://img.shields.io/github/stars/theMackabu/ant?label=&style=flat-square" alt="Stars" title="Stars"><img src="https://img.shields.io/github/last-commit/theMackabu/ant?label=&style=flat-square" alt="Last commit" title="Last commit"></span>
* LOC:          [34461](# "cloc src")
* Language:     C
* License:      MIT
* Standard:     ES5 (ES6 Partial)
* Years:        2025-
* Interpreter:  tree-walking
* Regex engine: PCRE2

## Links

- https://s.tail.so/js-in-one-month

## Conformance

<details><summary>ES1-ES5: 100%</summary><ul>
<li>Tested version: <a href="https://github.com/theMackabu/ant/commit/124bd4ef8b1a0ff0644e27c62d554d6edf733714">2026-05-20</a> (<a href="https://github.com/ivankra/javascript-zoo-data/blob/data/es1-5/ant.json">json</a>)</li>
<li>ES1: 100% (198/198)</li>
<li>ES3: 100% (148/148)</li>
<li>ES5: 100% (74/74)</li>
</ul></details>

<details><summary>compat-table: ES6 99%, ES2016+ 95%, Next 75%, Intl 100%</summary><ul>
<li>Tested version: <a href="https://github.com/theMackabu/ant/commit/124bd4ef8b1a0ff0644e27c62d554d6edf733714">2026-05-20</a> (<a href="https://github.com/ivankra/javascript-zoo-data/blob/data/compat-table/ant.json">json</a>)</li>
<li>ES5: 100%</li>
<li>ES6: 98.6%<pre>
<a href="../../conformance/compat-table/es6/Promise.all.js">Promise.all.js</a>: FAIL: Uncaught (in promise) 'qux'; Uncaught (in promise) 'baz'
<a href="../../conformance/compat-table/es6/Promise.race.js">Promise.race.js</a>: FAIL: Uncaught (in promise) 'baz'; Uncaught (in promise) 'bar'
<a href="../../conformance/compat-table/es6/subclassing.Promise.all.js">subclassing.Promise.all.js</a>: FAIL: Uncaught (in promise) 'qux'; Uncaught (in promise) 'baz'
<a href="../../conformance/compat-table/es6/subclassing.Promise.race.js">subclassing.Promise.race.js</a>: FAIL: Uncaught (in promise) 'baz'; Uncaught (in promise) 'bar'
</pre></li>
<li>ES2016: 100%</li>
<li>ES2017: 100%</li>
<li>ES2018: 100%</li>
<li>ES2019: 93.8%<pre>
<a href="../../conformance/compat-table/es2019/Object.fromEntries.js">Object.fromEntries.js</a>: TypeError: Object.fromEntries iterable values must be entry objects
</pre></li>
<li>ES2020: 92.9%<pre>
<a href="../../conformance/compat-table/es2020/Promise.allSettled.js">Promise.allSettled.js</a>: FAIL: Uncaught (in promise) 2
</pre></li>
<li>ES2021: 100%</li>
<li>ES2022: 100%</li>
<li>ES2023: 100%</li>
<li>ES2024: 100%</li>
<li>ES2025: 72.2%<pre>
<a href="../../conformance/compat-table/es2025/Iterator.from.iterable.js">Iterator.from.iterable.js</a>: FAIL
<a href="../../conformance/compat-table/es2025/Iterator.prototype.drop.js">Iterator.prototype.drop.js</a>: FAIL
<a href="../../conformance/compat-table/es2025/Iterator.prototype.filter.js">Iterator.prototype.filter.js</a>: FAIL
<a href="../../conformance/compat-table/es2025/Iterator.prototype.flatMap.js">Iterator.prototype.flatMap.js</a>: FAIL
<a href="../../conformance/compat-table/es2025/Iterator.prototype.map.js">Iterator.prototype.map.js</a>: FAIL
<a href="../../conformance/compat-table/es2025/Iterator.prototype.take.js">Iterator.prototype.take.js</a>: FAIL
<a href="../../conformance/compat-table/es2025/Set.prototype.difference.js">Set.prototype.difference.js</a>: FAIL
<a href="../../conformance/compat-table/es2025/Set.prototype.isSupersetOf.js">Set.prototype.isSupersetOf.js</a>: FAIL
<a href="../../conformance/compat-table/es2025/Set.prototype.symmetricDifference.js">Set.prototype.symmetricDifference.js</a>: FAIL
<a href="../../conformance/compat-table/es2025/Set.prototype.union.js">Set.prototype.union.js</a>: FAIL
</pre></li>
<li>Next: 74.5%<pre>
<a href="../../conformance/compat-table/next/AsyncIterator.from.iterable.js">AsyncIterator.from.iterable.js</a>: FAIL
<a href="../../conformance/compat-table/next/AsyncIterator.from.iterator.js">AsyncIterator.from.iterator.js</a>: FAIL
<a href="../../conformance/compat-table/next/AsyncIterator.prototype.flatMap.js">AsyncIterator.prototype.flatMap.js</a>: FAIL
<a href="../../conformance/compat-table/next/Map.prototype.upsert.js">Map.prototype.upsert.js</a>: FAIL
<a href="../../conformance/compat-table/next/ShadowRealm.js">ShadowRealm.js</a>: FAIL
<a href="../../conformance/compat-table/next/class-decorators.js">class-decorators.js</a>: FAIL
<a href="../../conformance/compat-table/next/function.sent.js">function.sent.js</a>: FAIL
</pre></li>
<li>Intl: 100%</li>
</ul></details>

<details><summary>test262: 47.3%, main 56.5%, staging 38.8%, annexB 48.5%, Next 5.1%, Intl 5.4%</summary>
<ul>
<li>Tested version: <a href="https://github.com/theMackabu/ant/commit/124bd4ef8b1a0ff0644e27c62d554d6edf733714">2026-05-20</a> (<a href="https://github.com/ivankra/javascript-zoo-data/blob/data/test262/ant.json">json</a>)</li>
<li>Overall: 47.3% (25133/53167)</li>
<li>Excluding staging, annexB, Next and Intl: 56.5% (23490/41549)</li>
<li>Results per edition/feature (note: figure for each feature is across tests for all editions, not just the introducing one):</li>
<li>ES5: 70.9% (5808/8197)<pre>
caller: 78.3% (18/23)
</pre></li>
<li>ES6: 56.7% (6265/11054)<pre>
__proto__: 50% (9/18)
Array.prototype.values: 75% (3/4)
ArrayBuffer: 23.9% (64/268)
DataView: 23.2% (44/190)
DataView.prototype.getFloat32: 42.9% (3/7)
DataView.prototype.getFloat64: 20% (1/5)
DataView.prototype.getInt16: 42.9% (3/7)
DataView.prototype.getInt32: 42.9% (3/7)
DataView.prototype.getInt8: 20% (1/5)
DataView.prototype.getUint16: 42.9% (3/7)
DataView.prototype.getUint32: 42.9% (3/7)
DataView.prototype.setUint8: 60.7% (34/56)
Float32Array: 57.1% (4/7)
Float64Array: 57.1% (4/7)
Int16Array: 0% (0/2)
Int32Array: 25% (1/4)
Int8Array: 71.4% (25/35)
Map: 40% (16/40)
Object.is: 50% (1/2)
Promise: 75% (3/4)
Proxy: 47% (220/468)
Reflect: 23.7% (111/468)
Reflect.construct: 8.9% (62/696)
Reflect.set: 10.9% (5/46)
Reflect.setPrototypeOf: 21.7% (5/23)
Set: 42.1% (16/38)
String.fromCodePoint: 40.9% (9/22)
String.prototype.endsWith: 48.1% (13/27)
String.prototype.includes: 57.7% (15/26)
Symbol: 33% (493/1494)
Symbol.hasInstance: 11.8% (2/17)
Symbol.isConcatSpreadable: 55.9% (19/34)
Symbol.iterator: 43.7% (815/1865)
Symbol.match: 54.5% (48/88)
Symbol.replace: 39.8% (39/98)
Symbol.search: 51.4% (19/37)
Symbol.species: 27.5% (76/276)
Symbol.split: 56.9% (33/58)
Symbol.toPrimitive: 21.9% (51/233)
Symbol.toStringTag: 25.2% (33/131)
Symbol.unscopables: 15.9% (7/44)
TypedArray: 29.4% (738/2513)
Uint16Array: 66.7% (4/6)
Uint32Array: 0% (0/2)
Uint8Array: 45.5% (5/11)
Uint8ClampedArray: 66.7% (4/6)
WeakMap: 40.5% (32/79)
WeakSet: 44.1% (15/34)
arrow-function: 16.4% (156/949)
class: 56% (2669/4768)
computed-property-names: 77.8% (372/478)
const: 93.3% (14/15)
cross-realm: 1% (2/201)
default-parameters: 67.5% (1532/2269)
destructuring-assignment: 33.3% (47/141)
destructuring-binding: 58.7% (3899/6637)
for-of: 100% (5/5)
generators: 57.7% (2358/4085)
let: 48.1% (37/77)
new.target: 29.5% (18/61)
proxy-missing-checks: 0% (0/3)
rest-parameters: 100% (96/96)
super: 5.3% (1/19)
tail-call-optimization: 62.9% (22/35)
template: 100% (1/1)
</pre></li>
<li>ES2016: 60.8% (79/130)<pre>
Array.prototype.includes: 40.6% (28/69)
exponentiation: 57.3% (59/103)
u180e: 72% (18/25)
</pre></li>
<li>ES2017: 56.9% (434/763)<pre>
__getter__: 55.6% (15/27)
__setter__: 55.6% (15/27)
Atomics: 28.6% (108/378)
Intl.DateTimeFormat-dayPeriod: 8.3% (1/12)
SharedArrayBuffer: 22.6% (105/464)
async-functions: 60.6% (427/705)
intl-normative-optional: 50% (2/4)
</pre></li>
<li>ES2018: 46.9% (2276/4855)<pre>
IsHTMLDDA: 0% (0/42)
Promise.prototype.finally: 41.4% (12/29)
Symbol.asyncIterator: 49.6% (267/538)
async-iteration: 48.4% (2403/4968)
object-rest: 52.7% (187/355)
object-spread: 88.9% (120/135)
regexp-dotall: 58.8% (10/17)
regexp-lookbehind: 36.8% (7/19)
regexp-named-groups: 11% (11/100)
regexp-unicode-property-escapes: 54.3% (370/681)
</pre></li>
<li>ES2019: 43.8% (60/137)<pre>
Array.prototype.flat: 60% (9/15)
Array.prototype.flatMap: 38.1% (8/21)
Object.fromEntries: 32% (8/25)
String.prototype.trimEnd: 20.8% (5/24)
String.prototype.trimStart: 21.7% (5/23)
Symbol.prototype.description: 87.5% (7/8)
json-superset: 100% (4/4)
optional-catch-binding: 80% (4/5)
stable-array-sort: 100% (4/4)
stable-typedarray-sort: 100% (1/1)
string-trimming: 25.9% (14/54)
well-formed-json-stringify: 100% (1/1)
</pre></li>
<li>ES2020: 31.4% (677/2156)<pre>
BigInt: 24.5% (368/1501)
Intl.NumberFormat-unified: 0% (0/67)
Intl.RelativeTimeFormat: 0% (0/79)
Promise.allSettled: 16.7% (17/102)
String.prototype.matchAll: 50% (8/16)
Symbol.matchAll: 50.8% (32/63)
coalesce-expression: 73.1% (19/26)
dynamic-import: 27.1% (256/946)
export-star-as-namespace-from-module: 42.1% (8/19)
for-in-order: 66.7% (6/9)
globalThis: 37.8% (56/148)
import.meta: 26.1% (6/23)
optional-chaining: 51.8% (29/56)
</pre></li>
<li>ES2021: 31% (285/920)<pre>
AggregateError: 32.3% (10/31)
FinalizationRegistry: 49% (24/49)
Intl.DateTimeFormat-datetimestyle: 0% (0/16)
Intl.DateTimeFormat-formatRange: 16.2% (6/37)
Intl.DateTimeFormat-fractionalSecondDigits: 10% (1/10)
Intl.DisplayNames: 8.5% (4/47)
Intl.ListFormat: 1.2% (1/81)
Intl.Locale: 0% (0/156)
Promise.any: 17.4% (16/92)
String.prototype.replaceAll: 29.3% (12/41)
WeakRef: 48.6% (18/37)
align-detached-buffer-semantics-with-web-reality: 21.5% (34/158)
logical-assignment-operators: 83.3% (90/108)
numeric-separator-literal: 65.4% (104/159)
</pre></li>
<li>ES2022: 59.4% (3246/5465)<pre>
Array.prototype.at: 63.6% (7/11)
Intl.DateTimeFormat-extend-timezonename: 0% (0/2)
Intl.DisplayNames-v2: 0% (0/12)
Intl.Segmenter: 24.1% (19/79)
Object.hasOwn: 90.3% (56/62)
String.prototype.at: 63.6% (7/11)
TypedArray.prototype.at: 23.1% (3/13)
arbitrary-module-namespace-names: 56.2% (9/16)
class-fields-private: 53.5% (607/1134)
class-fields-private-in: 73.7% (14/19)
class-fields-public: 37.6% (774/2058)
class-methods-private: 65.7% (1123/1709)
class-static-block: 46.2% (30/65)
class-static-fields-private: 26.4% (91/345)
class-static-fields-public: 81.2% (173/213)
class-static-methods-private: 59.7% (904/1513)
error-cause: 0% (0/5)
regexp-match-indices: 61.3% (19/31)
top-level-await: 88.2% (239/271)
</pre></li>
<li>ES2023: 35.6% (146/410)<pre>
Intl-enumeration: 0% (0/35)
Intl.NumberFormat-v3: 33.3% (34/102)
array-find-from-last: 31.2% (34/109)
change-array-by-copy: 39.4% (52/132)
hashbang: 89.7% (26/29)
symbols-as-weakmap-keys: 0% (0/29)
</pre></li>
<li>ES2024: 17.9% (150/840)<pre>
Atomics.waitAsync: 15.8% (16/101)
String.prototype.isWellFormed: 0% (0/8)
String.prototype.toWellFormed: 0% (0/8)
array-grouping: 60.7% (17/28)
arraybuffer-transfer: 32.2% (19/59)
promise-with-resolvers: 33.3% (3/9)
regexp-v-flag: 43.3% (81/187)
resizable-arraybuffer: 3% (14/463)
</pre></li>
<li>ES2025: 35.2% (446/1266)<pre>
Float16Array: 13.7% (7/51)
Intl.DurationFormat: 0% (0/112)
RegExp.escape: 61.9% (13/21)
import-attributes: 19% (19/100)
iterator-helpers: 43.4% (246/567)
json-modules: 15.4% (2/13)
promise-try: 33.3% (4/12)
regexp-modifiers: 25.2% (58/230)
set-methods: 51.6% (99/192)
</pre></li>
<li>ES2026: 16.9% (61/361)<pre>
Array.fromAsync: 0% (0/95)
Error.isError: 76.9% (10/13)
Intl.Era-monthcode: 0% (0/1543)
Intl.Locale-info: 0% (0/43)
Math.sumPrecise: 0% (0/10)
iterator-sequencing: 9.4% (3/32)
json-parse-with-source: 0% (0/22)
uint8array-base64: 36.2% (25/69)
upsert: 31.9% (23/72)
</pre></li>
<li>Next: 5.1% (404/7895)<pre>
Atomics.pause: 50% (3/6)
ShadowRealm: 0% (0/64)
Temporal: 0% (0/6671)
await-dictionary: 5.4% (2/37)
canonical-tz: 15.8% (3/19)
decorators: 18.5% (5/27)
explicit-resource-management: 67.1% (320/477)
immutable-arraybuffer: 0% (0/20)
import-bytes: 0% (0/5)
import-defer: 17.9% (41/229)
import-text: 0% (0/6)
joint-iteration: 6.4% (5/78)
legacy-regexp: 0% (0/26)
nonextensible-applies-to-private: 0% (0/4)
regexp-duplicate-named-groups: 21.1% (4/19)
source-phase-imports: 9.2% (21/228)
source-phase-imports-module-source: 23.8% (20/84)
</pre></li>
<li>N/A: 55% (4796/8718)</li>
</ul>
</details>
