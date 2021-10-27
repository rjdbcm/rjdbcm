
<p align="center">
  <img align="center" src="https://raw.githubusercontent.com/rjdbcm/rjdbcm/main/github-metrics.svg" />
</p>

## Projects Below

### Woma Programming Language
  
  When developing C extensions for Python it is common to struggle with debugging. Being written in C, there is no memory safety which makes failures common. These failures tend to take the form of segmentation faults which can be especially difficult to debug. This is especially true of remote builds where you may not even have access to the proper system resources to find the source of a bug. There are tools like Cython that can help to reduce the chances of a encountering an error due to memory violations. These tools, however, are not 100% effective and you can still be left with particularly hard to debug errors. Woma aims to improve this by using contract-based constraints on function parameters and return values. This is combined with syntax that encourages writing and composing short functions. Additionally error messages are highly informative and Woma only allows procured access to Python internals.

### Aspidites

  The reference implementation of the Woma Programming Language compiler that contains everything you need to build CPython extensions written in Woma.
