# Summary of Clean Code
## By Section Headers

The following are the chapter and section headers of the book _Clean Code: A Handbook of Agile Software Craftsmanship_ by Robert C. Martin, et. al..

### Chapter 1: Clean Code
by Robert C. Martin

#### There will be code

#### Bad Code

#### The Total Cost of Owning a Mess

#### The Grand Redesign in the Sky

#### Attitude

#### The Primal Conundrum

#### The Art of Clean Code?

#### What is Clean Code?
* Bjarne Stroustrup
* Grady Booch
* "Big" Dave Thomas
* Michael Feathers
* Ron Jeffries
* Ward Cunningham

#### Schools of Thought

#### We Are Authors

#### The Boy Scout Rule

#### Prequel and Principles

#### Conclusion

#### Bibliography



### Chapter 2: Meaningful Names
by Tim Ottinger

#### Introduction

#### Use Intention-Revealing Names

#### Avoid Disinformation

#### Make Meaningful Distinctions

#### Use Pronounceable Names

#### Use Searchable Names

#### Avoid Encodings
* Hungarian Notation
* Member Prefixes
* Interfaces and Implementations

#### Avoid Mental Mapping

#### Class Names

#### Method Names

#### Don't Be Cute

#### Pick One Word per Concept

#### Don't Pun

#### Use Solution Domain Names

#### Use Problem Domain Names

#### Add Meaningful Context

#### Don't Add Gratuitous Context

#### Final Words



### Chapter 3: Functions
by Robert C. Martin

#### Small!
* Blocks and Indenting

#### Do One Thing
* Sections within Functions

#### One Level of Abstraction per Function
* Reading Code from Top to Bottom: _The Stepdown Rule_

#### Switch Statements

#### Use Descriptive Names

#### Function Arguments
* Common Monadic Forms
* Flag Arguments
* Dyadic Functions
* Triads
* Argument Objects
* Argument Lists
* Verbs and Keywords

#### Have No Side Effects
* Output Arguments

#### Command Query Separation

#### Prefer Exceptions to Returning Error COdes
* Extract Try/Catch Blocks
* Error Handling is One Thing
* The Error.java Dependency Magnet

#### Don't Repeat Yourself

#### Structured Programming

#### How Do You Write Functions Like This?

#### Conclusion



### Chapter 4: Comments
by Robert C. Martin

#### Comments Do Not Make Up for Bad Code

#### Explain Yourself in Code

#### Good Comments
* Legal Comments
* Informative Comments
* Explanation of Intent
* Clarification
* Warning of Consequences
* TODO Comments
* Amplification
* Javadocs in Public APIs

#### Bad Comments
* Mumbling
* Redundant Comments
* Misleading Comments
* Mandated Comments
* Journal Comments
* Noise Comments
* Scary Noise
* Don't Use a Comment When You Can Use a Function or a Variable
* Position Markers
* Closing Brace Comments

#### Attributions and Bylines

#### Commented-Out Code

#### HTML Comments
* Nonlocal Information
* Too Much Information
* Inobvious Connection
* Function Headers
* Javadocs in Nonpublic Code



### Chapter 5: Formatting
by Robert C. Martin

#### The Purpose of Formatting

#### Vertical Formatting
* The Newspaper Metaphor
* Vertical Openness Between Concepts
* Vertical Density
* Vertical Distance
* Variable Declarations
* Instance Variables
* Dependent Functions
* Conceptual Affinity
* Vertical Ordering

#### Horizontal Formatting
* Horizontal Openness and Density
* Horizontal Alignment
* Indentation
* Breaking Indentation

#### Dummy Scopes

#### Team Rules

#### Uncle Bob's Formatting Rules

### Chapter 6: Objects and Data Structures
by Robert C. Martin

#### Data Abstraction

#### Data/Object Anti-Symmetry

#### The Law of Demeter
* Train Wrecks
* Hybrids
* Hiding Structure

#### Data Transfer Objects
* Active Record

#### Conclusion



### Chapter 7: Error Handling
by Michael Feathers

#### Use Exceptions Rather Than Return Codes

#### Write Your Try-Catch-Finally Statement First

#### Use Unchecked Exceptions

#### Provide Context with Exceptions

#### Define Exception Classes in Terms of a Caller's Needs

#### Define the Normal Flow

#### Don't Return Null

#### Don't Pass Null

#### Conclusion



### Chapter 8. Boundaries
by James Grenning

#### Using Third-Party Code

#### Exploring and Learning Boundaries

#### Learning log4j

#### Learning Tests Are Better Than Free

#### Using Code That Does Not Yet Exist

#### Clean Boundaries



### Chapter 9: Unit Tests
by Robert C. Martin

#### The Three Laws of TDD
* First Law
* Second Law
* Third Law

#### Keeping Tests Clean
* Tests Enable the -ilities

#### Clean Tests
* Domain-Specific Testing Language
* A Dual Standard

#### One Assert per Test
* Single Concept per Test

#### F.I.R.S.T.
* Fast
* Independent
* Repeatable
* Self-Validating
* Timely

#### Conclusion



### Chapter 10: Classes
by Robert C. Martin with Jeff Langr

#### Class Organization
* Encapsulation

#### Classes Should Be Small

#### The Single Responsibility Principle

#### Cohesion

#### Maintaining Cohesion Results in Many Small Classes

#### Organizing for Change
* Isolating from Change

### Chapter 11: Systems
by Dr. Kevin Dean Wampler

#### How Would You Build a City?

#### Separate Constructing a System from Using It
* Separation of Main
* Factories
* Dependency Injection

#### Scaling Up
* Cross-Cutting Concerns

#### Java Proxies

#### Pure Java AOP Frameworks
* AspectJ Aspects

#### Test Drive the System Architecture

#### Optimize Decision Making

#### Use Standards Wisely, When They Add _Demonstrable_ Value

#### Systems Need Domain-Specific Languages

#### Conclusion

### Chapter 12: Emergence
by Jeff Langr

#### Getting Clean via Emergent Design

#### Simple Design Rule 1: Runs All the Tests

#### Simple Design Rules 2-4: Refactoring

#### No Duplication

#### Expressive

#### Minimal Classes and Methods

#### Conclusion

### Chapter 13: Concurrency
by Brett L. Schuchert

#### Why Concurrency?

#### Myths and Misconceptions

#### Challenges

#### Concurrency Defense Principles
* Single Responsibility Principle
* Corollary: Limit the Scope of Data
* Corollary: Use Copies of Data
* Corollary: Threads Should Be as Independent as Possible

#### Know Your Library
* Thread-Safe Collections

#### Know Your Execution Models
* Producer-Consumer
* Readers-Writers
* Dining Philosophers

#### Beware Dependencies Between Synchronized Methods

#### Keep Synchronized Sections Small

#### Writing Correct Shut-Down Code Is Hard

#### Testing Threaded Code
* Treat Spurious Failures as Candidate Threading Issues
* Get Your Nonthreaded Code Working First
* Make Your Threaded Code Pluggable
* Make Your Threaded Code Tunable
* Run with More Threads Than Processors
* Run on Different Platforms
* Instrument Your Code to Try and Force Failures
* Hand-Coded
* Automated

#### Conclusion



### Chapter 14: Successive Refinement
by Robert C. Martin

#### Args Implementation
* How Did I Do This?

#### Args: The Rough Draft
* So I Stopped
* On Incrementalism

#### String Arguments

#### Conclusion



### Chapter 15: JUnit Internals
by Robert C. Martin

#### The JUnit Framework

#### Conclusion



### Chapter 16: Refactoring SerialDate
by Robert C. Martin

#### First, Make It Work

#### Then Make It Right

#### Conclusion



### Chapter 17: Smells and Heuristics
by Robert C. Martin

#### Comments

* C1: _Inappropriate Information_
* C2: _Obsolete Comment_
* C3: _Redundant Comment_
* C4: _Poorly Written Comment_
* C5: _Commented-Out Code_

#### Environment
* E1: _Build Requires More Than One Step_
* E2: _Tests Require More Than One Step_

#### Functions
* F1: _Too Many Arguments_
* F2: _Output Arguments_
* F3: _Flag Arguments_
* F4: _Dead Function_

#### General
* G1: _Multiple Languages in One Source File_
* G2: _Obvious Behavior is Unimplemented_
* G3: _Incorrect Behavior at the Boundaries_
* G4: _Overridden Safeties_
* G5: _Duplication_
* G6: _Code at Wrong Level of Abstraction_
* G7: _Base Classes Depending on Their Derivatives_
* G8: _Too Much Information_
* G9: _Dead Code_
* G10: _Vertical Separation_
* G11: _Inconsistency_
* G12: _Clutter_
* G13: _Artificial Coupling_
* G14: _Feature Envy_
* G15: _Selector Arguments_
* G16: _Obscured Intent_
* G17: _Misplaced Responsibility_
* G18: _Inappropriate Static_
* G19: _Use Explanatory Variables_
* G20: _Function Names Should Say What They Do_
* G21: _Understand the Algorithm_
* G22: _Make Logical Dependencies Physical_
* G23: _Prefer Polymorphism to If/Else or Switch/Case_
* G24: _Follow Standard Conventions_
* G25: _Replace Magic Numbers with Named Constants_
* G26: _Be Precise_
* G27: _Structure over Convention_
* G28: _Encapsulate Conditionals_
* G29: _Avoid Negative Conditionals_
* G30: _Functions Should Do One Thing_
* G31: _Hidden Temporal Couplings_
* G32: _Don't Be Arbitrary_
* G33: _Encapsulate Boundary Conditions_
* G34: _Functions Should Descend Only One Level of Abstraction_
* G35: _Keep Configurable Data at High Levels_
* G36: _Avoid Transitive Navigation_

#### Java
* J1: _Avoid Long Import Lists by Using Wildcards_
* J2: _Don't Inherit Constants_
* J3: _Constants versus Enums_

#### Names
* N1: _Choose Descriptive Names_
* N2: _Choose Names at the Appropriate Level of Abstraction_
* N3: _Use Standard Nomenclature Where Possible_
* N4: _Unambiguous Names_
* N5: _Use Long Names for Long Scopes_
* N6: _Avoid Encodings_
* N7: _Names Should Describe Side-Effects_

#### Tests
* T1: _Insufficient Tests_
* T2: _Use a Coverage Tool!_
* T3: _Don't Skip Trivial Tests_
* T4: _An Ignored Test Is a Question about an Ambiguity_
* T5: _Test Boundary Conditions_
* T6: _Exhaustively Test Near Bugs_
* T7: _Patterns of Failure Are Revealing_
* T8: _Test Coverage Patterns Can Be Revealing_
* T9: _Tests Should Be Fast_

#### Conclusion
