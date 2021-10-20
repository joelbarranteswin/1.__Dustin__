**Command lines for PyTest**

1. test any file in a folder

> pytest

2. watch function and class in a list

> pytest --collect-only

3. watch function naming in a test

> pytest -k

buscar funciones por nombre, usando "or, and , and not"

recordar que se debe usar or en un name_testing para cada script

> pytest -v -k "name_part_script or function_name"
>
> pytest -v -k "name_part_script or function_name" --tb=no
>
> pytest -v -k "name_part_script or function_name" --tb=no -x
>
> pytest -v -k "name_part_script or function_name" --tb=no --lf
>
> pytest -v -k "name_part_script or function_name" --tb=no -ff

4. run mark test in from your scripts

remember set :

> import pytest
>
> @pytest.mack.run_first

then run test in terminal

> pytest -v -m run_first

5. watch just the first error

> pytest -x

6. watch number of errors

> pytest --maxfail=2

7. to get all the fail test in our folder

> pytest --lf

8. to get all the fail test first and then the pass test

> pytest --ff

9. fail test and pass test in a line

> pytest -q

10. to watch local variables

> pytest -l

11. to remove advices in a test (trace backs)

> pytest --tb=no

12. test just a function naming it

> pytest -v name_script.py :: name_of_function.py

13. test in each function or class

> pytest -v  name_script.py --setup-show -s
