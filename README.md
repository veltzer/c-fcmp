# c-fcmp

fcmp is a C library for comparing two floating point numbers safely.

Comparing floats with `==` is unreliable. fcmp implements Knuth's
suggestions for safer floating-point comparison as a C function.

This repo revives the original fcmp library by Theodore C. Belding
(University of Michigan Center for the Study of Complex Systems). The
upstream documentation is kept in `README`, and the manual page is
`fcmp.3`.

The library is LGPL, version 2 or later.
