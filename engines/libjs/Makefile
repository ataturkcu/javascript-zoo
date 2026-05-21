# SPDX-FileCopyrightText: 2026 Ivan Krasilnikov
# SPDX-License-Identifier: MIT

include ../../build/build.mk

SUPPORTED_ARCHS = amd64 arm64 riscv64  # see Meta/host_platform.py

$(eval $(call build_engine,libjs,Dockerfile))
$(eval $(call build_engine,libjs_gcc,Dockerfile,--build-arg BASE=jsz-gcc))
