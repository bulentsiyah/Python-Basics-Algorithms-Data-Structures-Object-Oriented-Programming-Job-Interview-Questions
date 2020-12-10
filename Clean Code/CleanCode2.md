# Clean Code

## The boy scout rule
_Leave the campground cleaner than you found it_

## Naming

- If a name requires a comment, then the name doesn't reveal its intent
- Use searchable, meaningful and pronounceable names
- Avoid mental mapping
- A class name should not be a verb
- Methods should be verbs or contain one in the name
- Use one word per concept

## Functions

- Small (at least 20 lines)
- Do one thing and do it well
- Only one level of abstraction
- Ordered top down
- The smaller and more focused a function is, the easier it is to choose a descriptive name
- The ideal number of arguments is 0
- More than 3 arguments is a smell of a bad design
- Flag arguments are ugly, is better to have 2 functions
- Arguments should be ordered naturally
- Avoid side effects because they are unexpected
- Prefer throwing exceptions instead of returning error codes
- Extract try/catch blocks when possible
- **Don't repeat yourself**
- They should have a single entry and a single exit. (avoid multiple returns)

## Comments

- Comments are always a failure because they means the author haven't been able to explain himself enough with the code
- Do not comment bad code, rewrite it
- Accepted comments:
  - Legals
  - Test examples
  - Warning
  - TODO (but not for leaving bad code)
  - Public API documentation generators (like javadoc)
- **Don't use a comment when you can use a function**

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

## Error handling
- Use exceptions rather than return codes
- Write the try-catch-finally statement first
- Is a good practice provide the context of the error (and not only the stack)
- Don't pass or return null

## Boundaries
- Write learning tests
  - to explore third-party APIs
  - to be aware of their changes
  - to use code that does not already exists or is not yet known
- Use the _Adapter_ pattern
- Is better depend on something under the devloper control than on something which is not.

## Testing
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

## Classes
- Before public and after private stuff
- They should be small
- They should do one thing (SRP)
- Keep cohesion as high as possible
- It should be easy to extend a class but hard to modify it (OCP)

## Systems
- Use Dependecy Injection
- Keep concerns separates to be able to grow continuously 

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

## Concurrency 
- Keep the concurrent code separated
- If a test fails randomly but not always is a smell of concurrency problems

## Successive Refinements
- First make it work, then make it right, and last make it better
- Never let the rot get started (the broken window theory)
- Refactoring is an iterative process of trial and error

## Code smells

#### Comments
- Inappropriate 
- Useless 
- Obsolete
- Redundant
- Obvious or poor
- **Commented code**

#### Environment
- Multiple step buildings
- Multiple step tests

#### Naming
- Meaningless or ambiguous names
- Lack of standard nomenclature
- Hungarian notation 
- Names not describing side effects 

#### Functions and Classes
- Too many arguments
- Output arguments
- Flag in/out arguments
- Dead code

#### Testing
- Insufficient coverage
- Boundaries not tested
- Bugs not covered
- Slow suite
- Test with duplicated code
- Trivial tests aren't written

#### General
- Multiple languages in the same file (spaghetti code)
- Obvious behavior is unimplemented
- Safeties overridden (to skip them)
- Incorrect boundary behaviors
- Duplication
- Abstraction at wrong level 
- Too much information exposed
- Dead code
- Inconsistency (the same concept implemented in different ways)
- Useless clutter
- Violation of the Demeter's law
- Selector arguments (values used to choose the behavior of a function or a class)
- Obscured code (magic numbers, hungarian notation, unexpressive code...)
- Misplaced responsibility
- Lack of explanatory variables
- Switch and if/else chains instead of polymorphism
- Lack of standard and precision
- Conditional chains instead of encapsulated ones
- Functions doing more than one thing

#### Java 
- Long list of imports instead of using wildcards
- Inheriting constants instead of import them statically
- Constants instead of enums
