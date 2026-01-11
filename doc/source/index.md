# DummyPyPi2 Documentation

This is some text

## Main selling points!

The package is easy to use and makes extensive use of the operators `+`, `*`, `in`, `@`, etc.:

```python
import dummypypi2 as dp
...
```

This below should be a note. This is something more. This is one more comment.

!!! note

    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et euismod
    nulla. Curabitur feugiat, tortor non consequat finibus, justo purus auctor
    massa, nec semper lorem quam in massa.

Also check how Python code is rendered.

``` py title="bubble_sort.py"
@property
def vol(self) -> float:
    """Compute the volume of the ellipsoid"""
    if self._vol is None:
        # FROM: https://math.stackexchange.com/questions/226094/measure-of-an-ellipsoid
        if self.is_degen and np.any(self.P == np.inf):
            self._vol = 0
        elif self.is_degen and np.linalg.matrix_rank(self.P) < self.n:
            self._vol = np.inf
        else:
            self._vol = (np.pi ** (self.n / 2) / np.math.gamma(self.n / 2 + 1)) / np.sqrt(np.linalg.det(self.P))
    return self._vol
```
