# Test Output Expectations

## Running Tests

### Unit Tests

**Command:**
```powershell
pytest unit_tests/test_module2_logic_representation.py -v
```

**Expected Output (All Passing):**
```
============================= test session starts =============================
platform win32 -- Python 3.12.5, pytest-9.0.2, pluggy-1.6.0
cachedir: .pytest_cache
rootdir: C:\Users\...\project-2-ai-system-tori-madigan
collecting ... collected 20 items

unit_tests/test_module2_logic_representation.py::test_generate_proposition_symbol PASSED [  5%]
unit_tests/test_module2_logic_representation.py::test_constraint_equality PASSED [ 10%]
unit_tests/test_module2_logic_representation.py::test_constraint_inequality PASSED [ 15%]
...
[more tests...]

============================= 20 passed in 0.18s =============================
```

**Key Indicators:**
- ✅ `PASSED` for each test
- ✅ Final summary: `20 passed in 0.18s`
- ✅ Exit code: 0 (success)

### Integration Tests

**Command:**
```powershell
pytest integration_tests/test_module1_to_module2.py -v
```

**Expected Output:**
```
============================= test session starts =============================
...
collecting ... collected 5 items

integration_tests/test_module1_to_module2.py::test_module1_to_module2_integration PASSED [ 20%]
integration_tests/test_module1_to_module2.py::test_module1_to_module2_all_difficulties PASSED [ 40%]
...

============================== 5 passed in 0.16s ==============================
```

### Running All Tests

**Command:**
```powershell
pytest unit_tests/ integration_tests/ -v
```

**Expected Output:**
- All tests from both directories
- Summary showing total passed/failed
- Total time taken

## What a Failed Test Looks Like

**Example Failure:**
```
============================= test session starts =============================
...
unit_tests/test_module2_logic_representation.py::test_constraint_equality FAILED [ 10%]

================================== FAILURES ===================================
___________________ test_constraint_equality ___________________

    def test_constraint_equality():
        constraint = {
            "type": "equality",
            "entity": "E1",
            "attribute": "A1",
            "value": "V3"
        }
        attributes = {"A1": ["V1", "V2", "V3", "V4"]}
        
        formula = constraint_to_formula(constraint, attributes)
>       assert formula == "E1_A1_V3"
E       AssertionError: assert 'E1_A1_V2' == 'E1_A1_V3'
E         - E1_A1_V2
E         + E1_A1_V3

unit_tests/test_module2_logic_representation.py:45: AssertionError

=========================== short test summary info ============================
FAILED unit_tests/test_module2_logic_representation.py::test_constraint_equality
======================== 1 failed, 19 passed in 0.18s =========================
```

**Key Indicators:**
- ❌ `FAILED` instead of `PASSED`
- ❌ Shows the assertion that failed
- ❌ Shows expected vs actual values
- ❌ Final summary: `1 failed, 19 passed`
- ❌ Exit code: 1 (failure)

## Knowledge Base Output Format

When Module 2 runs successfully, it produces a knowledge base in this format:

```
=== KNOWLEDGE BASE ===

FACTS (All possible propositions):
E1_A1_V1, E1_A1_V2, E1_A1_V3, E1_A2_V1, E1_A2_V2, E1_A2_V3, ...

RULES (Domain Constraints):
1. (E1_A1_V1 ∨ E1_A1_V2 ∨ E1_A1_V3) ∧ (¬(E1_A1_V1 ∧ E1_A1_V2) ∧ ...)
2. (E1_A2_V1 ∨ E1_A2_V2 ∨ E1_A2_V3) ∧ (¬(E1_A2_V1 ∧ E1_A2_V2) ∧ ...)
...

RULES (Puzzle Constraints):
1. E1_A1_V3
2. ¬E2_A1_V1
3. (E1_A2_V1 ↔ E2_A2_V1) ∨ (E1_A2_V2 ↔ E2_A2_V2) ∨ ...
...
```

**Structure:**
- **Header**: `=== KNOWLEDGE BASE ===`
- **FACTS section**: All possible proposition symbols (E1_A1_V1, etc.)
- **RULES (Domain Constraints)**: Implicit constraints (exactly one value per attribute)
- **RULES (Puzzle Constraints)**: Explicit constraints from Module 1

**Logical Connectives Used:**
- `∧` - Conjunction (AND)
- `∨` - Disjunction (OR)
- `¬` - Negation (NOT)
- `↔` - Biconditional (IFF)
- `→` - Implication (IF-THEN) - may appear in some formulas

## Test Coverage Summary

### Module 2 Unit Tests (20 tests)
- ✅ Proposition symbol generation
- ✅ All 5 constraint types (equality, inequality, different_values, same_value, relative_position)
- ✅ Implicit constraint generation
- ✅ Knowledge base structure
- ✅ Integration with Module 1 (JSON input)
- ✅ Edge cases (negative offsets, invalid types, etc.)
- ✅ Various grid sizes

### Integration Tests (5 tests)
- ✅ Module 1 → Module 2 pipeline
- ✅ All difficulty levels
- ✅ Various grid sizes
- ✅ Constraint type distribution
- ✅ Data consistency

## Quick Test Commands

```powershell
# Run all Module 2 tests
pytest unit_tests/test_module2_logic_representation.py -v

# Run all integration tests
pytest integration_tests/ -v

# Run all tests
pytest -v

# Run with more detail (show print statements)
pytest -v -s

# Run specific test
pytest unit_tests/test_module2_logic_representation.py::test_constraint_equality -v

# Run tests and show coverage
pytest --cov=src/module2_logic_representation unit_tests/test_module2_logic_representation.py
```

## Success Criteria

✅ **All tests passing** means:
- All functions work correctly
- All constraint types convert properly
- Knowledge base format is correct
- Integration with Module 1 works
- Edge cases are handled

✅ **Ready for Module 3** when:
- All 20 unit tests pass
- All 5 integration tests pass
- Knowledge base output is properly formatted
- No syntax or runtime errors
