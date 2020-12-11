# Clean Code

Code is clean if it can be understood easily – by everyone on the team. Clean code can be read and enhanced by a developer other than its original author. With understandability comes readability, changeability, extensibility and maintainability.

- High ratio of reading to writing code
- Leave code cleaner then when you found it
_____________________________________

## General rules

1. Follow standard conventions.
2. Keep it simple stupid. Simpler is always better. Reduce complexity as much as possible.
3. Boy scout rule. Leave the campground cleaner than you found it.
4. Always find root cause. Always look for the root cause of a problem.

## Design rules

1. Keep configurable data at high levels.
2. Prefer polymorphism to if/else or switch/case.
3. Separate multi-threading code.
4. Prevent over-configurability.
5. Use dependency injection.
6. Follow Law of Demeter. A class should know only its direct dependencies.

## Understandability tips

1. Be consistent. If you do something a certain way, do all similar things in the same way.
2. Use explanatory variables.
3. Encapsulate boundary conditions. Boundary conditions are hard to keep track of. Put the processing for them in one place.
4. Prefer dedicated value objects to primitive type.
5. Avoid logical dependency. Don't write methods which works correctly depending on something else in the same class.
6. Avoid negative conditionals.

## Names rules

- Choose descriptive and unambiguous names.
- Make meaningful distinction.
- Use pronounceable names.
- Use searchable names.
- Replace magic numbers with named constants.
- Avoid encodings. Don't append prefixes or type information.
- Reveal intention
- Avoid disinformation
- One work per concept
- Appropriate context


## Functions rules

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
- Small (at least 20 lines)


## Comments rules

- Comments are always a failure because they means the author haven't been able to explain himself enough with the code
- Do not comment bad code, rewrite it
- Accepted comments:
  - Legals
  - Test examples
  - Warning
  - TODO (but not for leaving bad code)
  - Public API documentation generators (like javadoc)


## Classes:

- Encapsulated
- Cohesive
- Organise for change (subclass, interface)
- Before public and after private stuff
- They should be small
- They should do one thing (SRP)
- Keep cohesion as high as possible
- It should be easy to extend a class but hard to modify it (OCP)

## Source code structure

1. Separate concepts vertically.
2. Related code should appear vertically dense.
3. Declare variables close to their usage.
4. Dependent functions should be close.
5. Similar functions should be close.
6. Place functions in the downward direction.
7. Keep lines short.
8. Don't use horizontal alignment.
9. Use white space to associate related things and disassociate weakly related.
10. Don't break indentation.

## Objects and data structures

1. Hide internal structure.
2. Prefer data structures.
3. Avoid hybrids structures (half object and half data).
4. Should be small.
5. Do one thing.
6. Small number of instance variables.
7. Base class should know nothing about their derivatives.
8. Better to have many functions than to pass some code into a function to select a behavior.
9. Prefer non-static methods to static methods.
10. Abstract data
11. Data object anti-symmetry
12. Law of demeter
13. Data transfer object

## Tests

- Testing is always worth
- Test will save your life
- Write before the test and after the production code
- Uncovered code should not exist
- Test code is important as production code
- Keep the test suite clean
- Keep your test suite fast
- Refactor your test if needed
- One assert per test is a good practice
- One concept per test is common sense
- The F.I.R.S.T. Principle
  - **F** ast
  - **I** ndipendent
  - **R** epeatable
  - **S** elf-validating (which means a boolean output)
  - **T** imely (just before the production code)


## Code smells

1. Rigidity. The software is difficult to change. A small change causes a cascade of subsequent changes.
2. Fragility. The software breaks in many places due to a single change.
3. Immobility. You cannot reuse parts of the code in other projects because of involved risks and high effort.
4. Needless Complexity.
5. Needless Repetition.
6. Opacity. The code is hard to understand.


## Boundaries

- Write learning tests
  - to explore third-party APIs
  - to be aware of their changes
  - to use code that does not already exists or is not yet known
- Use the _Adapter_ pattern
- Is better depend on something under the devloper control than on something which is not.


## Error-handling:

- Exceptions over return codes
- Use try-catch-finally
- Use unchecked exceptions (Java)
- Have informative error messages
- Define exception classes according to caller's needs
- Special case pattern
- Don't return or pass null


## Emergent design

- The four rules of *Simple Design*
  - Run (and pass) all the tests
  - No duplication
  - Express the developer intent
  - Minimize the number of classes and methods
- The clearer the code the cheaper is the long-term maintenance
- Classes following the SRP are easier to test
- Tests are the best help for refactoring because they eliminate the fear of breaking stuff
- Test are documentation by examples


## Formatting

#### Vertical formatting

- The newspaper metaphor: the most significant stuff stays on the top
- Concepts closely related should be written closer than unrelated ones
- Variables should be declared as close as possible to their first usage
- Instance variables should be declared on the top of the class

#### Horizontal formatting

- Indentation is order
- Follow the language conventions has a doble value. For searches with regexps and to avoid menta pammpings between structures


## Datas

- The law of Demeter says: _Don't talk with the strangers_  A class should know only her related classes.
- For that low chain calls should be avoided. 
- Use DTO (Datas Transfer Objects)

## Systems

- Use Dependecy Injection
- Keep concerns separates to be able to grow continuously 

## Concurrency 

- Keep the concurrent code separated
- If a test fails randomly but not always is a smell of concurrency problems


## Successive Refinements

- First make it work, then make it right, and last make it better
- Never let the rot get started (the broken window theory)
- Refactoring is an iterative process of trial and error