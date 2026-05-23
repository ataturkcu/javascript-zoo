# Asynkron

Vibe-coded JavaScript interpreter for .NET.

* Repository:       [asynkron/Asynkron.JsEngine](https://github.com/asynkron/Asynkron.JsEngine.git) <span class="shields"><img src="https://img.shields.io/github/stars/asynkron/Asynkron.JsEngine?label=&style=flat-square" alt="Stars" title="Stars"><img src="https://img.shields.io/github/last-commit/asynkron/Asynkron.JsEngine?label=&style=flat-square" alt="Last commit" title="Last commit"></span>
* LOC:              [137782](# "cloc src")
* Language:         C#
* License:          MIT
* Standard:         ESnext
* Runtime platform: .NET

## Conformance

<details><summary>ES1-ES5: 99%</summary><ul>
<li>Tested version: <a href="https://github.com/asynkron/Asynkron.JsEngine/commit/d37c1fe0860b4a00a242db6733229406f4852401">2026-05-22</a> (<a href="https://github.com/ivankra/javascript-zoo-data/blob/data/es1-5/asynkron.json">json</a>)</li>
<li>ES1: 99.5% (197/198)<pre>
<a href="../../conformance/es1/annex-b.literals.octal.js">annex-b.literals.octal.js</a>: SyntaxError: Legacy octal literals are not allowed. Use 0o prefix for octal literals on line 14 column 10.
</pre></li>
<li>ES3: 100% (148/148)</li>
<li>ES5: 95.9% (71/74)<pre>
<a href="../../conformance/es5/debugger.js">debugger.js</a>: ReferenceError: debugger is not defined
<a href="../../conformance/es5/strict.no-delete-bindings.js">strict.no-delete-bindings.js</a>: FAIL
<a href="../../conformance/es5/strict.no-eval-or-arguments-assignment.js">strict.no-eval-or-arguments-assignment.js</a>: FAIL
</pre></li>
</ul></details>

<details><summary>compat-table: ES6 92%, ES2016+ 98%, Next 36%, Intl 100%</summary><ul>
<li>Tested version: <a href="https://github.com/asynkron/Asynkron.JsEngine/commit/d37c1fe0860b4a00a242db6733229406f4852401">2026-05-22</a> (<a href="https://github.com/ivankra/javascript-zoo-data/blob/data/compat-table/asynkron.json">json</a>)</li>
<li>ES5: 99.1%<pre>
<a href="../../conformance/compat-table/es5/strict.assignment-eval-arguments-error.js">strict.assignment-eval-arguments-error.js</a>: FAIL
</pre></li>
<li>ES6: 92.1%<pre>
<a href="../../conformance/compat-table/es6/Promise.all.iterable.js">Promise.all.iterable.js</a>: FAIL: [JsEngine] setTimeout firing timerId=2 delay=1000; [JsEngine] setTimeout firing timerId=4 delay=1000; [JsEngine] setTimeout firing timerId=1 delay=2000; [JsEngine] setTimeout firing timerId=3 delay=20...
<a href="../../conformance/compat-table/es6/Promise.all.js">Promise.all.js</a>: FAIL: [JsEngine] setTimeout firing timerId=2 delay=1000; [JsEngine] setTimeout firing timerId=4 delay=1000; [JsEngine] setTimeout firing timerId=1 delay=2000; [JsEngine] setTimeout firing timerId=3 delay=20...
<a href="../../conformance/compat-table/es6/Promise.race.iterable.js">Promise.race.iterable.js</a>: FAIL: [JsEngine] setTimeout firing timerId=1 delay=1000; [JsEngine] setTimeout firing timerId=3 delay=1000; [JsEngine] setTimeout firing timerId=2 delay=2000; [JsEngine] setTimeout firing timerId=4 delay=20...
<a href="../../conformance/compat-table/es6/Promise.race.js">Promise.race.js</a>: FAIL: [JsEngine] setTimeout firing timerId=1 delay=1000; [JsEngine] setTimeout firing timerId=3 delay=1000; [JsEngine] setTimeout firing timerId=2 delay=2000; [JsEngine] setTimeout firing timerId=4 delay=20...
<a href="../../conformance/compat-table/es6/annex-b.regex.invalid-char-escapes.js">annex-b.regex.invalid-char-escapes.js</a>: SyntaxError: Invalid pattern '[\z]' at offset 3. Unrecognized escape sequence \z.
<a href="../../conformance/compat-table/es6/annex-b.regex.invalid-hex-escapes.js">annex-b.regex.invalid-hex-escapes.js</a>: SyntaxError: Invalid pattern '[\x1]' at offset 5. Insufficient or invalid hexadecimal digits.
<a href="../../conformance/compat-table/es6/annex-b.regex.invalid-unicode-escapes.js">annex-b.regex.invalid-unicode-escapes.js</a>: SyntaxError: Invalid pattern '[\u1]' at offset 3. Insufficient or invalid hexadecimal digits.
<a href="../../conformance/compat-table/es6/annex-b.__proto__.literals.multiple-error.js">annex-b.__proto__.literals.multiple-error.js</a>: FAIL
<a href="../../conformance/compat-table/es6/arrow.no-line-break.js">arrow.no-line-break.js</a>: FAIL
<a href="../../conformance/compat-table/es6/destructuring-assign.parenthesised-error.js">destructuring-assign.parenthesised-error.js</a>: FAIL
<a href="../../conformance/compat-table/es6/destructuring-params.duplicate-identifier.js">destructuring-params.duplicate-identifier.js</a>: FAIL
<a href="../../conformance/compat-table/es6/misc.Object.isExtensible.primitives.js">misc.Object.isExtensible.primitives.js</a>: FAIL
<a href="../../conformance/compat-table/es6/misc.Proxy.get.Array.from.js">misc.Proxy.get.Array.from.js</a>: FAIL
<a href="../../conformance/compat-table/es6/misc.Proxy.get.Array.pop.js">misc.Proxy.get.Array.pop.js</a>: FAIL
<a href="../../conformance/compat-table/es6/misc.Proxy.get.Array.shift.js">misc.Proxy.get.Array.shift.js</a>: FAIL
<a href="../../conformance/compat-table/es6/misc.Proxy.get.ClassDefinitionEvaluation.js">misc.Proxy.get.ClassDefinitionEvaluation.js</a>: TypeError: Class extends value is not a constructor or null
<a href="../../conformance/compat-table/es6/misc.Proxy.get.CreateDynamicFunction.js">misc.Proxy.get.CreateDynamicFunction.js</a>: FAIL
<a href="../../conformance/compat-table/es6/misc.Proxy.get.Function.bind.js">misc.Proxy.get.Function.bind.js</a>: FAIL
<a href="../../conformance/compat-table/es6/misc.Proxy.get.HasBinding.js">misc.Proxy.get.HasBinding.js</a>: FAIL
<a href="../../conformance/compat-table/es6/misc.Proxy.get.RegExp-constructor.js">misc.Proxy.get.RegExp-constructor.js</a>: FAIL: Unable to cast object of type 'Asynkron.JsEngine.JsTypes.JsProxy' to type 'Asynkron.JsEngine.JsTypes.JsObject'.
...
</pre></li>
<li>ES2016: 84.8%<pre>
<a href="../../conformance/compat-table/es2016/exponentiation.unary-negation-error.js">exponentiation.unary-negation-error.js</a>: FAIL
<a href="../../conformance/compat-table/es2016/misc.strict-fn-non-simple-params-error.js">misc.strict-fn-non-simple-params-error.js</a>: FAIL
</pre></li>
<li>ES2017: 94%<pre>
<a href="../../conformance/compat-table/es2017/async.await-rejection.js">async.await-rejection.js</a>: FAIL: [JsEngine] setTimeout firing timerId=1 delay=800
<a href="../../conformance/compat-table/es2017/async.await.js">async.await.js</a>: FAIL: [JsEngine] setTimeout firing timerId=1 delay=800; [JsEngine] setTimeout firing timerId=2 delay=800
<a href="../../conformance/compat-table/es2017/async.no-await-in-params.js">async.no-await-in-params.js</a>: FAIL
</pre></li>
<li>ES2018: 98.9%<pre>
<a href="../../conformance/compat-table/es2018/regex.unicode-property-escapes.unicode-17.0.js">regex.unicode-property-escapes.unicode-17.0.js</a>: SyntaxError: Invalid regular expression: invalid unicode property escape \p{Script=Sidetic}.
</pre></li>
<li>ES2019: 98.2%<pre>
<a href="../../conformance/compat-table/es2019/misc.Function-toString.native-code.js">misc.Function-toString.native-code.js</a>: FAIL
</pre></li>
<li>ES2020: 100%</li>
<li>ES2021: 100%</li>
<li>ES2022: 100%</li>
<li>ES2023: 100%</li>
<li>ES2024: 100%</li>
<li>ES2025: 100%</li>
<li>Next: 36.4%</li>
<li>Intl: 100%</li>
</ul></details>

<details><summary>test262: 89.1%, main 91.5%, staging 77%, annexB 98.5%, Next 75.8%, Intl 57.6%</summary>
<ul>
<li>Tested version: <a href="https://github.com/asynkron/Asynkron.JsEngine/commit/d37c1fe0860b4a00a242db6733229406f4852401">2026-05-22</a> (<a href="https://github.com/ivankra/javascript-zoo-data/blob/data/test262/asynkron.json">json</a>)</li>
<li>Overall: 89.1% (47382/53167)</li>
<li>Excluding staging, annexB, Next and Intl: 91.5% (38024/41549)</li>
<li>Results per edition/feature (note: figure for each feature is across tests for all editions, not just the introducing one):</li>
<li>ES5: 98.4% (8065/8197)<pre>
caller: 100% (23/23)
</pre></li>
<li>ES6: 93.9% (10377/11054)<pre>
__proto__: 100% (18/18)
Array.prototype.values: 100% (4/4)
ArrayBuffer: 98.9% (265/268)
DataView: 94.2% (179/190)
DataView.prototype.getFloat32: 100% (7/7)
DataView.prototype.getFloat64: 100% (5/5)
DataView.prototype.getInt16: 100% (7/7)
DataView.prototype.getInt32: 100% (7/7)
DataView.prototype.getInt8: 100% (5/5)
DataView.prototype.getUint16: 100% (7/7)
DataView.prototype.getUint32: 100% (7/7)
DataView.prototype.setUint8: 100% (56/56)
Float32Array: 85.7% (6/7)
Float64Array: 85.7% (6/7)
Int16Array: 100% (2/2)
Int32Array: 100% (4/4)
Int8Array: 100% (35/35)
Map: 100% (40/40)
Object.is: 100% (2/2)
Promise: 100% (4/4)
Proxy: 99.1% (464/468)
Reflect: 99.1% (464/468)
Reflect.construct: 98.3% (684/696)
Reflect.set: 100% (46/46)
Reflect.setPrototypeOf: 100% (23/23)
Set: 100% (38/38)
String.fromCodePoint: 100% (22/22)
String.prototype.endsWith: 100% (27/27)
String.prototype.includes: 100% (26/26)
Symbol: 97.9% (1463/1494)
Symbol.hasInstance: 100% (17/17)
Symbol.isConcatSpreadable: 100% (34/34)
Symbol.iterator: 94.8% (1768/1865)
Symbol.match: 100% (88/88)
Symbol.replace: 100% (98/98)
Symbol.search: 100% (37/37)
Symbol.species: 100% (276/276)
Symbol.split: 100% (58/58)
Symbol.toPrimitive: 100% (233/233)
Symbol.toStringTag: 84.7% (111/131)
Symbol.unscopables: 100% (44/44)
TypedArray: 99.8% (2507/2513)
Uint16Array: 100% (6/6)
Uint32Array: 100% (2/2)
Uint8Array: 100% (11/11)
Uint8ClampedArray: 100% (6/6)
WeakMap: 98.7% (78/79)
WeakSet: 100% (34/34)
arrow-function: 92% (873/949)
class: 88.8% (4233/4768)
computed-property-names: 97.5% (466/478)
const: 86.7% (13/15)
cross-realm: 100% (201/201)
default-parameters: 97.7% (2216/2269)
destructuring-assignment: 33.3% (47/141)
destructuring-binding: 96.8% (6425/6637)
for-of: 100% (5/5)
generators: 94.8% (3873/4085)
let: 94.8% (73/77)
new.target: 77% (47/61)
proxy-missing-checks: 100% (3/3)
rest-parameters: 0% (0/96)
super: 78.9% (15/19)
tail-call-optimization: 0% (0/35)
template: 100% (1/1)
</pre></li>
<li>ES2016: 89.2% (116/130)<pre>
Array.prototype.includes: 97.1% (67/69)
exponentiation: 86.4% (89/103)
u180e: 100% (25/25)
</pre></li>
<li>ES2017: 86.4% (659/763)<pre>
__getter__: 100% (27/27)
__setter__: 100% (27/27)
Atomics: 98.1% (371/378)
Intl.DateTimeFormat-dayPeriod: 100% (12/12)
SharedArrayBuffer: 98.1% (455/464)
async-functions: 77% (543/705)
intl-normative-optional: 100% (4/4)
</pre></li>
<li>ES2018: 85.4% (4146/4855)<pre>
IsHTMLDDA: 97.6% (41/42)
Promise.prototype.finally: 93.1% (27/29)
Symbol.asyncIterator: 84.2% (453/538)
async-iteration: 88.2% (4381/4968)
object-rest: 98.9% (351/355)
object-spread: 100% (135/135)
regexp-dotall: 100% (17/17)
regexp-lookbehind: 100% (19/19)
regexp-named-groups: 46% (46/100)
regexp-unicode-property-escapes: 64% (436/681)
</pre></li>
<li>ES2019: 99.3% (136/137)<pre>
Array.prototype.flat: 93.3% (14/15)
Array.prototype.flatMap: 100% (21/21)
Object.fromEntries: 100% (25/25)
String.prototype.trimEnd: 100% (24/24)
String.prototype.trimStart: 100% (23/23)
Symbol.prototype.description: 100% (8/8)
json-superset: 100% (4/4)
optional-catch-binding: 100% (5/5)
stable-array-sort: 100% (4/4)
stable-typedarray-sort: 100% (1/1)
string-trimming: 100% (54/54)
well-formed-json-stringify: 100% (1/1)
</pre></li>
<li>ES2020: 83.6% (1803/2156)<pre>
BigInt: 98.2% (1474/1501)
Intl.NumberFormat-unified: 100% (67/67)
Intl.RelativeTimeFormat: 100% (79/79)
Promise.allSettled: 100% (102/102)
String.prototype.matchAll: 100% (16/16)
Symbol.matchAll: 100% (63/63)
coalesce-expression: 76.9% (20/26)
dynamic-import: 45.7% (432/946)
export-star-as-namespace-from-module: 68.4% (13/19)
for-in-order: 100% (9/9)
globalThis: 98.6% (146/148)
import.meta: 47.8% (11/23)
optional-chaining: 57.1% (32/56)
</pre></li>
<li>ES2021: 96.5% (888/920)<pre>
AggregateError: 100% (31/31)
FinalizationRegistry: 100% (49/49)
Intl.DateTimeFormat-datetimestyle: 100% (16/16)
Intl.DateTimeFormat-formatRange: 100% (37/37)
Intl.DateTimeFormat-fractionalSecondDigits: 100% (10/10)
Intl.DisplayNames: 100% (47/47)
Intl.ListFormat: 100% (81/81)
Intl.Locale: 99.4% (155/156)
Promise.any: 100% (92/92)
String.prototype.replaceAll: 100% (41/41)
WeakRef: 100% (37/37)
align-detached-buffer-semantics-with-web-reality: 100% (158/158)
logical-assignment-operators: 88.9% (96/108)
numeric-separator-literal: 87.4% (139/159)
</pre></li>
<li>ES2022: 88% (4808/5465)<pre>
Array.prototype.at: 100% (11/11)
Intl.DateTimeFormat-extend-timezonename: 100% (2/2)
Intl.DisplayNames-v2: 100% (12/12)
Intl.Segmenter: 100% (79/79)
Object.hasOwn: 100% (62/62)
String.prototype.at: 100% (11/11)
TypedArray.prototype.at: 100% (13/13)
arbitrary-module-namespace-names: 75% (12/16)
class-fields-private: 68.1% (772/1134)
class-fields-private-in: 73.7% (14/19)
class-fields-public: 86.4% (1779/2058)
class-methods-private: 85.5% (1461/1709)
class-static-block: 58.5% (38/65)
class-static-fields-private: 96.2% (332/345)
class-static-fields-public: 86.9% (185/213)
class-static-methods-private: 95.1% (1439/1513)
error-cause: 100% (5/5)
regexp-match-indices: 100% (31/31)
top-level-await: 94.5% (256/271)
</pre></li>
<li>ES2023: 99.8% (409/410)<pre>
Intl-enumeration: 94.3% (33/35)
Intl.NumberFormat-v3: 100% (102/102)
array-find-from-last: 100% (109/109)
change-array-by-copy: 100% (132/132)
hashbang: 100% (29/29)
symbols-as-weakmap-keys: 100% (29/29)
</pre></li>
<li>ES2024: 92.7% (779/840)<pre>
Atomics.waitAsync: 96% (97/101)
String.prototype.isWellFormed: 100% (8/8)
String.prototype.toWellFormed: 100% (8/8)
array-grouping: 100% (28/28)
arraybuffer-transfer: 96.6% (57/59)
promise-with-resolvers: 88.9% (8/9)
regexp-v-flag: 72.2% (135/187)
resizable-arraybuffer: 98.9% (458/463)
</pre></li>
<li>ES2025: 86.6% (1096/1266)<pre>
Float16Array: 96.1% (49/51)
Intl.DurationFormat: 100% (112/112)
RegExp.escape: 95.2% (20/21)
import-attributes: 24% (24/100)
iterator-helpers: 96.6% (548/567)
json-modules: 84.6% (11/13)
promise-try: 100% (12/12)
regexp-modifiers: 63.9% (147/230)
set-methods: 100% (192/192)
</pre></li>
<li>ES2026: 93.1% (336/361)<pre>
Array.fromAsync: 84.2% (80/95)
Error.isError: 100% (13/13)
Intl.Era-monthcode: 19.4% (299/1543)
Intl.Locale-info: 97.7% (42/43)
Math.sumPrecise: 100% (10/10)
iterator-sequencing: 93.8% (30/32)
json-parse-with-source: 95.5% (21/22)
uint8array-base64: 100% (69/69)
upsert: 98.6% (71/72)
</pre></li>
<li>Next: 75.8% (5987/7895)<pre>
Atomics.pause: 100% (6/6)
ShadowRealm: 98.4% (63/64)
Temporal: 77.5% (5167/6671)
await-dictionary: 5.4% (2/37)
canonical-tz: 94.7% (18/19)
decorators: 92.6% (25/27)
explicit-resource-management: 82.4% (393/477)
immutable-arraybuffer: 5% (1/20)
import-bytes: 0% (0/5)
import-defer: 62.9% (144/229)
import-text: 0% (0/6)
joint-iteration: 6.4% (5/78)
legacy-regexp: 100% (26/26)
nonextensible-applies-to-private: 0% (0/4)
regexp-duplicate-named-groups: 94.7% (18/19)
source-phase-imports: 58.3% (133/228)
source-phase-imports-module-source: 50% (42/84)
</pre></li>
<li>N/A: 89.2% (7777/8718)</li>
</ul>
</details>
