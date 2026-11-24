# TOFIX

Findings from a code scan on 2026-10-04.

## High

- `LICENSE:1` vs `fcmp.c:8-12`, `fcmp.h:8-12`, `README:8-12`, `README.md:13` - the repo ships the fleet-wide MIT `LICENSE`, but all of the code is Theodore Belding's LGPL-2+ work, which cannot be relicensed as MIT. The LGPL text the sources point at (`COPYING`, cited at `fcmp.c:11`, `fcmp.h:11`, `fcmp.3:11`, `fcmp.3:65`) is not in the repo, and the LGPL requires shipping it. Fix: add `COPYING` with the LGPL-2 text, and give this repo a deliberate, commented exception for `LICENSE` in `~/.config/rsmultigit/config.toml` (third-party code), not a quietly divergent copy.

## Medium

- `rsconstruct.toml` - there is no `[processor.tera]`, so nothing renders `tera.templates/.github/dependabot.yml.tera`. The committed `.github/dependabot.yml` is a stale hand-made copy: it lacks the blank line between ecosystem blocks that the template emits (compare `pysigfd/.github/dependabot.yml`). Fix: add a `[processor.tera]` block with `src_dirs = ["tera.templates"]`, as in the other tera repos. `dep_auto` must list only config files that exist; this repo has `config/project.lua` but no `personal.lua` or `version.lua`.
- `fcmp.c:26` - no test exercises the library. Fix: add a small C test (equal, greater, less, zero-vs-tiny, and the sign/exponent cases from the comments at `fcmp.c:31-42`) and wire it in as an `explicit` processor that links against `out/libfcmp.so`.
- `README.txt:4` - points readers to `README.old`, which does not exist (the upstream text is in `README`). Fix: merge `README.txt` into `README.md` and delete it, which also closes the open items in `doc/TODO.txt:2-3`.

## Low

- `fcmp.c:19-21` - `#ifdef HAVE_CONFIG_H` / `#include <config.h>` is left over from the autotools build that `scripts/build_fcmp.py` replaced. Nothing defines it now, so remove it.
- `fcmp.c:59-64` - if either input is NaN, both comparisons are false and `fcmp` returns `0` ("equal"). Document this in `fcmp.h` and `fcmp.3`, or return a distinct result, and cover it in the test above.
- `README:48-95` - the INSTALLATION section describes `configure`, `INSTALL` and `--disable-shared`, none of which exist any more. Add a note in `README.md` that the build is now `scripts/build_fcmp.py` via rsconstruct, so readers don't follow the dead instructions.
- `doc/TODO.txt:1` - "create a debian package" contradicts `rsconstruct.toml:22-24`, which says the debian-packaging step was deliberately dropped. Remove the item.
