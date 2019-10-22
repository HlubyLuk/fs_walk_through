# file system walk through
Tool which find all directories which contains **tiff image** file.

## Run
```python
python <path to fs_walk_through>/src/main/main.py <directory where start walk>
```

## Example
Call from bash script:

```bash
#!/usr/bin/env bash

tmp=(\
    $(\
    python \
        <path to fs_walk_through>/src/main/main.py \
        <directory where start walk>\
    )\
)

function run() {
    printf "print from run ${1}\n"
}

for f in ${tmp[*]}; do
    run ${f}
done
```

## TODO
* Custom file extension which search.
* Multiple start directories.
* More examples.