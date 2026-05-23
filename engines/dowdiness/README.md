# dowdiness/js_engine

Vibe-coded JavaScript engine written in MoonBit.

* Repository:  [dowdiness/js_engine](https://github.com/dowdiness/js_engine) <span class="shields"><img src="https://img.shields.io/github/stars/dowdiness/js_engine?label=&style=flat-square" alt="Stars" title="Stars"><img src="https://img.shields.io/github/last-commit/dowdiness/js_engine?label=&style=flat-square" alt="Last commit" title="Last commit"></span>
* LOC:         [62588](# "cloc --exclude-ext=md .")
* Language:    MoonBit
* License:     Apache-2.0
* Years:       2026-
* Interpreter: tree walker

## Conformance

<details><summary>ES1-ES5: 0%</summary><ul>
<li>Tested version: 0.2.3-72-gefa3301 (<a href="https://github.com/dowdiness/js_engine/commit/efa3301c04c34b5383a278e28476a827de4658ac">2026-05-21</a>, <a href="https://github.com/ivankra/javascript-zoo-data/blob/data/es1-5/dowdiness.json">json</a>)</li>
<li>ES1: 0% (0/198)</li>
<li>ES3: 0% (0/148)</li>
<li>ES5: 0% (0/74)</li>
</ul></details>

<details><summary>compat-table: ES6 0%, ES2016+ 0%, Next 0%, Intl 0%</summary><ul>
<li>Tested version: 0.2.3-72-gefa3301 (<a href="https://github.com/dowdiness/js_engine/commit/efa3301c04c34b5383a278e28476a827de4658ac">2026-05-21</a>, <a href="https://github.com/ivankra/javascript-zoo-data/blob/data/compat-table/dowdiness.json">json</a>)</li>
<li>ES5: 0%</li>
<li>ES6: 0%</li>
<li>ES2016: 0%</li>
<li>ES2017: 0%</li>
<li>ES2018: 0%</li>
<li>ES2019: 0%</li>
<li>ES2020: 0%</li>
<li>ES2021: 0%</li>
<li>ES2022: 0%</li>
<li>ES2023: 0%</li>
<li>ES2024: 0%</li>
<li>ES2025: 0%</li>
<li>Next: 0%</li>
<li>Intl: 0%</li>
</ul></details>

<details><summary>test262: 55.9%, main 67.2%, staging 42.3%, annexB 80.1%, Next 3.6%, Intl 0.5%</summary>
<ul>
<li>Tested version: 0.2.3-72-gefa3301 (<a href="https://github.com/dowdiness/js_engine/commit/efa3301c04c34b5383a278e28476a827de4658ac">2026-05-21</a>, <a href="https://github.com/ivankra/javascript-zoo-data/blob/data/test262/dowdiness.json">json</a>)</li>
<li>Overall: 55.9% (29704/53167)</li>
<li>Excluding staging, annexB, Next and Intl: 67.2% (27911/41549)</li>
<li>Results per edition/feature (note: figure for each feature is across tests for all editions, not just the introducing one):</li>
<li>ES5: 94.1% (7712/8197)<pre>
caller: 0% (0/23)
</pre></li>
<li>ES6: 83% (9179/11054)<pre>
__proto__: 16.7% (3/18)
Array.prototype.values: 75% (3/4)
ArrayBuffer: 14.9% (40/268)
DataView: 26.3% (50/190)
DataView.prototype.getFloat32: 71.4% (5/7)
DataView.prototype.getFloat64: 60% (3/5)
DataView.prototype.getInt16: 85.7% (6/7)
DataView.prototype.getInt32: 85.7% (6/7)
DataView.prototype.getInt8: 80% (4/5)
DataView.prototype.getUint16: 85.7% (6/7)
DataView.prototype.getUint32: 85.7% (6/7)
DataView.prototype.setUint8: 50% (28/56)
Float32Array: 28.6% (2/7)
Float64Array: 28.6% (2/7)
Int16Array: 100% (2/2)
Int32Array: 75% (3/4)
Int8Array: 77.1% (27/35)
Map: 85% (34/40)
Object.is: 100% (2/2)
Promise: 25% (1/4)
Proxy: 66% (309/468)
Reflect: 48.3% (226/468)
Reflect.construct: 61.1% (425/696)
Reflect.set: 76.1% (35/46)
Reflect.setPrototypeOf: 69.6% (16/23)
Set: 92.1% (35/38)
String.fromCodePoint: 45.5% (10/22)
String.prototype.endsWith: 96.3% (26/27)
String.prototype.includes: 96.2% (25/26)
Symbol: 44.4% (663/1494)
Symbol.hasInstance: 94.1% (16/17)
Symbol.isConcatSpreadable: 70.6% (24/34)
Symbol.iterator: 42% (784/1865)
Symbol.match: 37.5% (33/88)
Symbol.replace: 39.8% (39/98)
Symbol.search: 48.6% (18/37)
Symbol.species: 50% (138/276)
Symbol.split: 39.7% (23/58)
Symbol.toPrimitive: 59.7% (139/233)
Symbol.toStringTag: 34.4% (45/131)
Symbol.unscopables: 81.8% (36/44)
TypedArray: 42.4% (1065/2513)
Uint16Array: 33.3% (2/6)
Uint32Array: 100% (2/2)
Uint8Array: 54.5% (6/11)
Uint8ClampedArray: 33.3% (2/6)
WeakMap: 92.4% (73/79)
WeakSet: 88.2% (30/34)
arrow-function: 58.6% (556/949)
class: 28% (1334/4768)
computed-property-names: 84.5% (404/478)
const: 86.7% (13/15)
cross-realm: 33.3% (67/201)
default-parameters: 71.8% (1630/2269)
destructuring-assignment: 44.7% (63/141)
destructuring-binding: 64.5% (4282/6637)
for-of: 60% (3/5)
generators: 63.9% (2609/4085)
let: 53.2% (41/77)
new.target: 59% (36/61)
proxy-missing-checks: 100% (3/3)
rest-parameters: 0% (0/96)
super: 73.7% (14/19)
tail-call-optimization: 0% (0/35)
template: 100% (1/1)
</pre></li>
<li>ES2016: 70.8% (92/130)<pre>
Array.prototype.includes: 31.9% (22/69)
exponentiation: 67% (69/103)
u180e: 84% (21/25)
</pre></li>
<li>ES2017: 31.2% (238/763)<pre>
__getter__: 63% (17/27)
__setter__: 63% (17/27)
Atomics: 0% (0/378)
Intl.DateTimeFormat-dayPeriod: 0% (0/12)
SharedArrayBuffer: 0% (0/464)
async-functions: 48.7% (343/705)
intl-normative-optional: 0% (0/4)
</pre></li>
<li>ES2018: 46.4% (2254/4855)<pre>
IsHTMLDDA: 26.2% (11/42)
Promise.prototype.finally: 89.7% (26/29)
Symbol.asyncIterator: 4.8% (26/538)
async-iteration: 43% (2135/4968)
object-rest: 61.4% (218/355)
object-spread: 71.1% (96/135)
regexp-dotall: 41.2% (7/17)
regexp-lookbehind: 0% (0/19)
regexp-named-groups: 22% (22/100)
regexp-unicode-property-escapes: 0% (0/681)
</pre></li>
<li>ES2019: 81% (111/137)<pre>
Array.prototype.flat: 80% (12/15)
Array.prototype.flatMap: 71.4% (15/21)
Object.fromEntries: 56% (14/25)
String.prototype.trimEnd: 100% (24/24)
String.prototype.trimStart: 100% (23/23)
Symbol.prototype.description: 87.5% (7/8)
json-superset: 100% (4/4)
optional-catch-binding: 60% (3/5)
stable-array-sort: 50% (2/4)
stable-typedarray-sort: 0% (0/1)
string-trimming: 100% (54/54)
well-formed-json-stringify: 0% (0/1)
</pre></li>
<li>ES2020: 25.2% (543/2156)<pre>
BigInt: 10.7% (161/1501)
Intl.NumberFormat-unified: 0% (0/67)
Intl.RelativeTimeFormat: 0% (0/79)
Promise.allSettled: 96.1% (98/102)
String.prototype.matchAll: 93.8% (15/16)
Symbol.matchAll: 55.6% (35/63)
coalesce-expression: 88.5% (23/26)
dynamic-import: 33% (312/946)
export-star-as-namespace-from-module: 15.8% (3/19)
for-in-order: 66.7% (6/9)
globalThis: 54.1% (80/148)
import.meta: 69.6% (16/23)
optional-chaining: 71.4% (40/56)
</pre></li>
<li>ES2021: 41.8% (385/920)<pre>
AggregateError: 67.7% (21/31)
FinalizationRegistry: 0% (0/49)
Intl.DateTimeFormat-datetimestyle: 0% (0/16)
Intl.DateTimeFormat-formatRange: 0% (0/37)
Intl.DateTimeFormat-fractionalSecondDigits: 0% (0/10)
Intl.DisplayNames: 0% (0/47)
Intl.ListFormat: 0% (0/81)
Intl.Locale: 0% (0/156)
Promise.any: 95.7% (88/92)
String.prototype.replaceAll: 58.5% (24/41)
WeakRef: 0% (0/37)
align-detached-buffer-semantics-with-web-reality: 34.8% (55/158)
logical-assignment-operators: 65.7% (71/108)
numeric-separator-literal: 89.3% (142/159)
</pre></li>
<li>ES2022: 26.4% (1441/5465)<pre>
Array.prototype.at: 100% (11/11)
Intl.DateTimeFormat-extend-timezonename: 0% (0/2)
Intl.DisplayNames-v2: 0% (0/12)
Intl.Segmenter: 0% (0/79)
Object.hasOwn: 95.2% (59/62)
String.prototype.at: 100% (11/11)
TypedArray.prototype.at: 84.6% (11/13)
arbitrary-module-namespace-names: 43.8% (7/16)
class-fields-private: 34.4% (390/1134)
class-fields-private-in: 42.1% (8/19)
class-fields-public: 34.5% (711/2058)
class-methods-private: 20.1% (344/1709)
class-static-block: 43.1% (28/65)
class-static-fields-private: 4.9% (17/345)
class-static-fields-public: 68.5% (146/213)
class-static-methods-private: 10.7% (162/1513)
error-cause: 60% (3/5)
regexp-match-indices: 19.4% (6/31)
top-level-await: 2.6% (7/271)
</pre></li>
<li>ES2023: 52.7% (216/410)<pre>
Intl-enumeration: 0% (0/35)
Intl.NumberFormat-v3: 0% (0/102)
array-find-from-last: 70.6% (77/109)
change-array-by-copy: 78.8% (104/132)
hashbang: 69% (20/29)
symbols-as-weakmap-keys: 82.8% (24/29)
</pre></li>
<li>ES2024: 6.5% (55/840)<pre>
Atomics.waitAsync: 0% (0/101)
String.prototype.isWellFormed: 75% (6/8)
String.prototype.toWellFormed: 75% (6/8)
array-grouping: 78.6% (22/28)
arraybuffer-transfer: 0% (0/59)
promise-with-resolvers: 44.4% (4/9)
regexp-v-flag: 3.2% (6/187)
resizable-arraybuffer: 2.4% (11/463)
</pre></li>
<li>ES2025: 12.8% (162/1266)<pre>
Float16Array: 21.6% (11/51)
Intl.DurationFormat: 0% (0/112)
RegExp.escape: 0% (0/21)
import-attributes: 15% (15/100)
iterator-helpers: 2.3% (13/567)
json-modules: 15.4% (2/13)
promise-try: 91.7% (11/12)
regexp-modifiers: 33.5% (77/230)
set-methods: 18.2% (35/192)
</pre></li>
<li>ES2026: 26% (94/361)<pre>
Array.fromAsync: 1.1% (1/95)
Error.isError: 84.6% (11/13)
Intl.Era-monthcode: 0% (0/1543)
Intl.Locale-info: 0% (0/43)
Math.sumPrecise: 60% (6/10)
iterator-sequencing: 0% (0/32)
json-parse-with-source: 0% (0/22)
uint8array-base64: 11.6% (8/69)
upsert: 94.4% (68/72)
</pre></li>
<li>Next: 3.6% (285/7895)<pre>
Atomics.pause: 0% (0/6)
ShadowRealm: 0% (0/64)
Temporal: 0.1% (6/6671)
await-dictionary: 5.4% (2/37)
canonical-tz: 0% (0/19)
decorators: 7.4% (2/27)
explicit-resource-management: 15.5% (74/477)
immutable-arraybuffer: 0% (0/20)
import-bytes: 0% (0/5)
import-defer: 31.9% (73/229)
import-text: 0% (0/6)
joint-iteration: 0% (0/78)
legacy-regexp: 0% (0/26)
nonextensible-applies-to-private: 0% (0/4)
regexp-duplicate-named-groups: 0% (0/19)
source-phase-imports: 56.1% (128/228)
source-phase-imports-module-source: 50% (42/84)
</pre></li>
<li>N/A: 79.6% (6937/8718)</li>
</ul>
</details>
