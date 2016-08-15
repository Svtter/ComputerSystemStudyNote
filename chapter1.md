Programs that perform the four phases
---

1. preprocessor
2. compiler
3. assembler
4. linker

- preprocessing phase
For example, the `#include <stdio.h>` command in line 1 of `hello.c` tells preprocessor to read the contents
of the system header file `stdio.h` and insert it directly into the program text.

The result is another C program, typically with the .i suffix.

- Complication phase
The compiler(cc1) translates the text file `hello.i` into text file `hello.s` which contains an *assembly-language
program*. 

- Assembly phase
The assembler (as) translates `hello.s` into machine-language instructions, packages them in a form known as a
*relocatable object program*, and stores the result in the object file `hello.o.`

- Linking phase
The `printf` function resides in a separate precompiled object file called `printf.o`, which must somehow be
merged with `hello.o`. The linker(ld) handles this merging.

The result is the hello file, which is an executable object file.


Storage Devices Form a Hierarchy
---

The main idea of a memory hierarchy is that storage at one level serves as a cache for storage at the next lower
level. Thus, the register file is a cache for the L1 cache. Caches L1 and L2 are caches for L2 and L3, respectively.
The L3 cache is a cache for the disk. 

On some networked systems with distributed file systems, the local disk serves as a cache for data stored on the 
disks of other systems.

读罢感想
---

英文原版书籍的质量的确要高于翻译版本，具体表现在对问题的深刻讲解，以及通俗程度。
在某些教材版本中，省略了许多尚未入门的人士所不知道的名词解释，这是经常出现的。
如果刚刚进入这个领域，最好不要从中文课本入手，直接读英文原版书籍，提升的会更快。

并且，此书在一定程度上指导了Unix系系统的使用。
