#!/usr/bin/env python3
# Add a non-x86_64 stub for try_emit_int32_mod_by_constant so arm64 builds
# compile — the stub returns false, letting callers fall through to the slow path.
import sys

path = sys.argv[1]
with open(path) as f:
    text = f.read()

stub = (
    '    #[cfg(not(any(\n'
    '        stator_maglev_jit_x86_64,\n'
    '        all(target_arch = "x86_64", any(unix, windows))\n'
    '    )))]\n'
    '    fn try_emit_int32_mod_by_constant(&mut self, _id: NodeId, _left: NodeId, _d: i32) -> bool { false }\n\n'
)
marker = (
    '    #[cfg(any(\n'
    '        stator_maglev_jit_x86_64,\n'
    '        all(target_arch = "x86_64", any(unix, windows))\n'
    '    ))]\n'
    '    fn try_emit_int32_mod_by_constant'
)

assert marker in text, f"marker not found in {path}"
assert text.count(marker) == 1, f"marker not unique in {path}"
text = text.replace(marker, stub + marker, 1)

with open(path, 'w') as f:
    f.write(text)
