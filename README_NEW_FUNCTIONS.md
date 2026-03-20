# New Calculator Functions Documentation

## CAPS (UPPERCASE) Functions

### LOG_UPPER
- **Purpose**: Calculate base-10 logarithm
- **Usage**: `LOG_UPPER(x)`
- **Example**: `LOG_UPPER(100)` returns `2.0`
- **Error Handling**: Raises ValueError for non-positive values

### LOG_E
- **Purpose**: Calculate natural logarithm (base e)
- **Usage**: `LOG_E(x)`
- **Example**: `LOG_E(math.e)` returns `1.0`
- **Error Handling**: Raises ValueError for non-positive values

### EXPONENT
- **Purpose**: Calculate base raised to power
- **Usage**: `EXPONENT(base, exponent)`
- **Example**: `EXPONENT(2, 3)` returns `8`

## camel (camelCase) Functions

### Sine
- **Purpose**: Calculate sine of angle in radians
- **Usage**: `Sine(angle)`
- **Example**: `Sine(math.pi/2)` returns `1.0`

### Cosine
- **Purpose**: Calculate cosine of angle in radians
- **Usage**: `Cosine(angle)`
- **Example**: `Cosine(0)` returns `1.0`

## snake (snake_case) Functions

### Root
- **Purpose**: Calculate nth root of a number
- **Usage**: `Root(value, degree=2)`
- **Example**: `Root(16)` returns `4.0`, `Root(27, 3)` returns `3.0`
- **Error Handling**: Raises ValueError for even root of negative or non-positive degree

### Cube
- **Purpose**: Calculate cube of a number
- **Usage**: `Cube(value)`
- **Example**: `Cube(3)` returns `27`

## Testing Commands

### Individual Function Tests:
```bash
python -c "from CAPS import LOG_UPPER, LOG_E, EXPONENT; print('LOG_UPPER(100):', LOG_UPPER(100)); print('LOG_E(math.e):', LOG_E(math.e)); print('EXPONENT(2,3):', EXPONENT(2,3))"

python -c "from camel import Sine, Cosine; import math; print('Sine(0):', Sine(0)); print('Cosine(math.pi/2):', Cosine(math.pi/2))"

python -c "from snake import Root, Cube; print('Root(16):', Root(16)); print('Root(27,3):', Root(27,3)); print('Cube(3):', Cube(3))"
```

### Combined Test:
```bash
python -c "
from CAPS import LOG_UPPER, LOG_E, EXPONENT
from camel import Sine, Cosine
from snake import Root, Cube
import math

print('CAPS Functions:')
print('LOG_UPPER(100):', LOG_UPPER(100))
print('LOG_E(math.e):', LOG_E(math.e))
print('EXPONENT(2,3):', EXPONENT(2,3))

print('\ncamel Functions:')
print('Sine(0):', Sine(0))
print('Cosine(math.pi/2):', Cosine(math.pi/2))

print('\nsnake Functions:')
print('Root(16):', Root(16))
print('Root(27,3):', Root(27,3))
print('Cube(3):', Cube(3))
"
```

### Unit Tests:
```bash
python -m unittest tests/test_new_functions.py -v
```

## Expression Parser Integration

All new functions are integrated into the expression parser:
- CAPS: `log(x)`, `log10(x)`, `ln(x)`, `exp(base, exponent)`
- camel: `sin(angle)`, `cos(angle)`
- snake: `root(value, degree)`, `cube(value)`

**Usage Examples:**
```
log(100)           # 2.0
log10(1000)        # 3.0
ln(math.e)         # 1.0
exp(2, 3)          # 8
root(16, 2)        # 4.0
cube(3)            # 27
sin(math.pi/2)     # 1.0
cos(0)             # 1.0
```