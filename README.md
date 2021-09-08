# pipeline

Some transforms utilities based on `Arrows` from Haskell.

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

