# pipeline

Some transforms utilities based on `Arrows` from Haskell.

# Installation

Add the following line in your `requirements.txt`:

```
git+https://github.com/willGuimont/pipeline
```

# Usage

```python
import pipeline as pp

input_value = 7
transform = pp.Compose([
    pp.Tee(),
    pp.First(lambda x: x + 1),
    pp.Second(lambda x: x - 1),
    pp.Both(lambda x: x * 2),
    pp.Bifunctor(lambda x: x // 3, lambda x: x * 2),
    pp.Both(str),
    pp.Lambda(lambda x: ''.join(x))
])

output = transform(input_value)
print(output)
assert output == "524"
```

