# Match Case

## (Structural pattern matching in Python 3.10)

### Ad Hoc Exercise

Take the name of a kitchen appliance from the user and assign it to a variable.

Take a numerical energy rating, grade 1 - 5, also from the user and assign it to a variable.

Using `match` and `case` keywords and the sample code provided, construct a Python script that assigns a _VERBAL_ Energy rating grade from the range "Excellent, Good, Fair, Poor, Ungraded" to a _NUMERICAL_ grade 1-5.

You should display the result for each case in a formatted string with the words "Your <appliance_name> is rated..." and the verbal grade, together with the numerical grade used to derive the result.

Example output:

```python
print(f'Your {appliance_name} is rated Excellent based on a score of {energy_grade}.')
```

You may wish to refactor your initial working code to reduce duplication.
