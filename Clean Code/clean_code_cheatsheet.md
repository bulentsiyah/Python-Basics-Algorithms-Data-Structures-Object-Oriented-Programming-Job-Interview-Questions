# Clean Code Cheatsheet

Clean code:

- High ratio of reading to writing code
- Leave code cleaner then when you found it

Names:

- Reveal intention
- Avoid disinformation
- Make meaningful distinctions
- Use pronounceable names
- Use searchable names
- Avoid encodings and mental mappings
- One work per concept
- Appropriate context

Functions:

- Single responsibility
- Single abstraction level
- Step down rule
- Switch statements
- Descriptive names
- Minimise arguments
- No flag arguments
- Dyadic functions:
  - Natural ordering of arguments
- Monadic -> Dyadic -> Triadic functions:
  - Argument objects and lists
- Verb and keyword naming
- No side effects
- Command query separation
- Exceptions instead of error codes
- Extract try-catch blocks

Objects and Data Structures:

- Abstract data
- Data object anti-symmetry
- Law of demeter
- Data transfer object

Classes:

- Encapsulated
- Small - single responsibility
- Cohesive
- Organise for change (subclass, interface)

Boundaries:

- Wrap 3rd party interfaces
- Use tests to learn

Error-handling:

- Exceptions over return codes
- Use try-catch-finally
- Use unchecked exceptions (Java)
- Have informative error messages
- Define exception classes according to caller's needs
- Special case pattern
- Don't return or pass null

Testing:

- Test-driven development (TDD) can lead to a lot of test code
- Test code:
  - is as important as production code (PC)
  - keeps PC maintainable
  - changes with PC
  - readability is more important than in PC
  - does not have to be very efficient
  - good to have domain-specific testing APIs
- One concept/assert per test
- FIRST:
  - Fast
  - Independent
  - Repeatable
  - Self-validating
  - Timely

Emergence

- Design rules:
  - Runs all tests
  - Refactoring
  - No duplication
  - Expressive
  - Minimal classes and methods

Code Smells:

- [https://moderatemisbehaviour.github.io/clean-code-smells-and-heuristics/](https://moderatemisbehaviour.github.io/clean-code-smells-and-heuristics/)