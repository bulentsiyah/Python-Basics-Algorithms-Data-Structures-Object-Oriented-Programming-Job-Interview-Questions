# Clean architecture

### Part 1

##### Goal

Goal of architecture: to minimize human resources required to build and maintain the required system

A good indication of a badly designed system: look at the cost of each line of code, and the productivity of each engineer over time

"And yet, despite all their heroics, overtime, and dedication, they simply aren’t getting much of anything done anymore. All their effort has been diverted away from features and is now consumed with managing the mess. Their job, such as it is, has changed into moving the mess from one place to the next, and the next, and the next, so that they can add one more meager little feature."

"And so the developers never switch modes. They can’t go back and clean things up because they’ve got to get the next feature done, and the next, and the next, and the next. And so the mess builds, and productivity continues its asymptotic approach toward zero."

##### The only way to go fast is to go well

* The misconception of going faster by spending less time in design
"The bigger lie that developers buy into is the notion that writing messy code makes them go fast in the short term, and just slows them down in the long term. Developers who accept this lie exhibit the hare’s overconfidence in their ability to switch modes from making messes to cleaning up messes sometime in the future, but they also make a simple error of fact. The fact is that making messes is always slower than staying clean, no matter which time scale you are using."

"The only way to go fast, is to go well."

And making matters worse

"Their overconfidence will drive the redesign into the same mess as the original project."

##### Two values of a program: behavior and architecture

Behavior: programmers are hired to make machines behave in a way that makes or saves money for the stakeholders.

"To fulfill its purpose, software must be soft—that is, it must be easy to change. When the stakeholders change their minds about a feature, that change should be simple and easy to make. The difficulty in making such a change should be proportional only to the scope of the change, and not to the shape of the change."

"From the stakeholders’ point of view, they are simply providing a stream of changes of roughly similar scope. From the developers’ point of view, the stakeholders are giving them a stream of jigsaw puzzle pieces that they must fit into a puzzle of ever-increasing complexity. Each new request is harder to fit than the last, because the shape of the system does not match the shape of the request."

"The problem, of course, is the architecture of the system. The more this architecture prefers one shape over another, the more likely new features will be harder and harder to fit into that structure. Therefore architectures should be as shape agnostic are practical."

Argument: architecture is the more important value. Consider the two extremes, something that works but cannot be changed is useless facing changing requirements; while something that doesn't work but can be easily changed can be changed.

"You may not find this argument convincing. After all, there’s no such thing as a program that is impossible to change. However, there are systems that are practically impossible to change, because the cost of change exceeds the benefit of change. Many systems reach that point in some of their features or configurations."

"I have two kinds of problems, the urgent and the important. The urgent are not important, and the important are never urgent." --Eisenhower

"The dilemma for software developers is that business managers are not equipped to evaluate the importance of architecture. That’s what software developers were hired to do. Therefore it is the responsibility of the software development team to assert the importance of architecture over the urgency of features."

"Fulfilling this responsibility means wading into a fight—or perhaps a better word is “struggle.” Frankly, that’s always the way these things are done. The development team has to struggle for what they believe to be best for the company, and so do the management team, and the marketing team, and the sales team, and the operations team. It’s always a struggle."

"Just remember: If architecture comes last, then the system will become ever more costly to develop, and eventually change will become practically impossible for part or all of the system. If that is allowed to happen, it means the software development team did not fight hard enough for what they knew was necessary."

### Part 2

Paradigms of programming

**Structured programming**: impose discipline on direct transfer of control

**OOP**: impose discipline on indirect transfer of control

**Functional**: impose discipline upon assignment

Each of these paradigms takes something away from us

Note how well the three aligns with the big concerns of architecture: function, separation of components, data management

##### Structured programming

Goto not in the context of if / while makes a program hard to decompose into smaller units, making proof by divide and conquer hard

Structured programming allows modules to be recursively decomposed into provable units

"Tests can prove a program incorrect, but not correct. Software is like scientific laws, we show correctness by failing to prove incorrectness, despite our best efforts."

falsifiable (testable)

##### OOP

What's really the point?

Encapsulation? C's forward declaration (where data members of a struct need not be declared in header) can achieve hiding members and implementation from clients; C++ breaks this kind of encapsulation

Inheritance? In C if one struct A is a pure superset of another B, A can masquerade as B (C-style cast of A\* to B\*). Such trickery is how C++ implements single inheritance as well.

<mark>review, implement</mark>
Polymorphism? C can achieve polymorphism as well. E.g. the definition of STDIN, how does a console getchar() call know which device is STDIN?
Unix require that every IO device driver provide five standard functions with same function signatures. open, close, read, write, seek
FILE is a struct with members that are pointers to the above function signatures. STDIN can then be pointer to FILE, who was populated with console's implementation of the above five functions.
This approach is not that different from C++'d vtable polymorphism. While polymorphism is achievable in C, C++ makes it more convenient and safer.

This "plugin" architecture of device drivers makes programs device independent.

**Dependency inversion**: the source code dependency (of an inheritance relationship) points in the opposite direction compared to the flow of control (where a high-level function needs to know the source of a lower-level function in order to call it).
This means any source code dependency, no matter where it is, can be inverted. And one is not constrained to organizing dependencies aligned to the flow of control.
With the dependencies organized via an interface and plugged in, one also achieves independent deployability and independent developability.
(_Having compile dependency being opposite to runtime dependency is dependency inversion_)

What is OO to an architect: "OO is the ability, through the use of polymorphism, to gain absolute control over every source code dependency in the system. It allows the architect to create a plugin architecture, in which modules that contain high-level policies are independent of modules that contain low-level details. The low-level details are relegated to plugin modules that can be deployed and developed independently from the modules that contain high-level policies."

##### Functional programming

* Immutability:

Variables in functional languages do not vary.
Why would immutability be a concern: race conditions, deadlocks, concurrent update problems are all due to mutable variables.
Mutability in Clojure: functional languages like Clojure can allow mutable variables, but only mutated under very strict conditions that are enforced by swap!, which uses a traditional compare and swap (?) algorithm.
Thus, a well-structured program can be modeled in a functional language by segregating its variables into mutable and immutable ones. And it'd be wise to push as much as possible into immutable area.

* Event sourcing:

"The limits of storage and processing power have been rapidly receding from view. Nowadays it is common for processors to execute billions of instructions per second and to have billions of bytes of RAM. The more memory we have, and the faster our machines are, the less we need mutable state."

"As a simple example, imagine a banking application that maintains the account balances of its customers. It mutates those balances when deposit and withdrawal transactions are executed."

"Now imagine that instead of storing the account balances, we store only the transactions. Whenever anyone wants to know the balance of an account, we simply add up all the transactions for that account, from the beginning of time. This scheme requires no mutable variables."

"If this still sounds absurd, it might help if you remembered that this is precisely the way your source code control system works." (that, and also BigTable, those that are based on log structured merge trees)

### Part 3

The principle of SOLID for module (mid) level software design (component, in BDE terms).
Goal: tolerate change, easy to understand, create basis of components that can be used in many software systems.
Not confined in OOP: general enough for any paradigm that groups functions and data into (general) classes

* Single responsibility principle: so that each module has only one reason to change: being responsible only to one 'actor' (group of stakeholders)
Cohesion => SRP
Symptoms   (e.g.): putting functions that support different parties in one class
Resolution (e.g.): putting them in different classes, and if required, have them share the same underlying data. Now more classes needs to be instantiated and kept track of. Consider Facade pattern if needed.
Similarly: common closure principle, and at architecture level: axis of change.

* Open closed principle: software system should allow change of its behavior by adding new code, rather than changing existing code
A software artifact should be open for extension but closed for modification. Or, the behavior of a software artifact ought to be extendible, without having to modify that artifact.
Architecture separates functionality into a **hierarchy** of components (no bidirectional dependencies crossing package group boundaries). Higher-level components are protected from the changes made to lower-level components (depend on an interface, not an implementation; dependency inversion).

* Liskov substituion principle: build software from interchangeable components, and have them conform to a contract so that they are substitutable
We want this substitution property: if for each object o1 of type S there is an object o2 of type T such that for all programs P defined in terms of T, the behavior of P is unchanged when o1 is substituted for o2 then S is a subtype of T. (input type contravariant)
(Remind yourself of this especially when you start to see a lot of special case handling in the code. It might be that we have the wrong generalization. _Can Colombian quasi-IL, Chinese dimsum, Italian tax rate be justified_?)

* Interface segregation principle: avoid depending on things you don't use. This includes transitive dependencies (consider using an interface for information hiding in that case)
In general, it is harmful to depend on modules that contain more than you need.
(_Achieving flexibility in dynamically typed languages like Python may be different in this sense from, say, C++_? Consider the current sfgs architecture? Or by DI, the same principle should hold: high-level policy should not depend on low-level details)

* Dependency inversion principle: high-level policy should not depend on low-level details, should be the other way round.
The most flexible systems are those in which source code dependencies refer only to abstractions not to concretions.
Reduce the volatility of interfaces.
Don't refer to volatile concrete classes. (_The relationship between this and the usage of abstract factory?_)
Don't derive from volatile concrete classes.
Don't override concrete functions.
Don't mention the name of anything concrete and volatile.
(Main will often times be a concrete component that relies on concrete components, as ultimately one needs to specify which concrete implementation should be used.)

(_Rethinking our question on TCPClient in client side business objects.
Say, main creates a client side business logic object. One should consider using abstract factory to abstract away a transport mechanism from client side business logic object (assume this object needs to **instantiate** (thus one of the differences between taking in an interface and an abstract factory, other consideration being fully isolated unit tests) / acquire (which might make transport layer client not such a great example) a transport mechanism), which should be transport mechanism independent.
So it looks like, when you instantiate the client side business object in main, give it a (could be global) concrete factory._)

(_Think about architectural boundaries, and dependency / inheritance lines that cross them, more in dependency rule_)

### Part 4: package (group) rules

package: a unit of release that retains the ability to be independently deployable and developable

Early days of programming and non-relocatable code; linking loader (external reference, U symbols, and external definitions (definitions exposed to external callers), T symbols)
Then linking and loading were split: linking is a one time job after compilation and loading happens at runtime.
(_claim: shared object is re-exploring the idea of a linker loader_)

* Package cohesion: which components go into which packages?

REP: reuse / release equivalence principle
The granule of reuse is the granule of release (the package must have some overarching theme or purpose that components in it all share; and components grouped into a package should be releasable together) (weak rule)

CCP: 

Gather into packages those components that change for the same reason and at the same times. Separate into different packages those components that change at different times and for different reasons.
It's similar with Single Responsibility Principle in that the latter discusses what to put in one component, and this discusses what to put in a package.

CRP: common reuse principle
Don't force users of a package to depend on things they don't need.
Classes and modules that tend to be reused together belong in the same package.
We want to make sure that the classes we put into a package are inseparable: it is not possible for a client to depend on some and not on others.
It's similar with Interface Segregation Principle (package level vs component level)

The first two rules are inclusive and third is exclusive, and an architect strikes the right balance, and expect the balance to change over time.

* Package coupling: the dependency between packages?

ADP: acyclic dependencies principle
Break down dependency cycles so that when one package changes, the affected parties are only its clients, and their change should not propagate back to this changed package, and the release of each packge can go from bottom to up
Cycles essentially make the packages one large piece, and difficult to isolate packages and unit test.
Common ways to break down cycles include separating a smaller piece out that both packages depend on, and applying DIP

The logical design of the system can go top-down, with whom the packages dependency design grows and evolves.

(The weekly build (similar as ADP, also introduced to combat multiple contributors to the same project changing things others depend on and project being unable to build), four days independent dev and one day integration, not exactly robo cycle)

SDP: stable dependency principle
Depend in the direction of stability
There are packages that are developed knowing they'd be volatile and subject to change. Any volatile package should not be depended by a package that is difficult to change.
Stability does not necessarily mean frequent changes, but rather, the effort required to change the package (size, clarity, complexity, amount of clients, e.g. as denoted by NumberOfDependencies / (NumberOfDependencies + NumberOfClients), and the lower the more stable the package is)
Typically abstract interfaces (in statically typed languages) should be very stable.

SAP: stable abstraction principle
A package should be as abstract as it is stable
Stable - abstract (or consists of interfaces), unstable - concrete implementation
This echos with OCP, where stable interfaces are closed for modification but open to extention

SAP + SDP => DIP for packages (If something is widely depended on, it better be abstract and do not change often)
With packages there can be a shade a grey (partially abstract and stable; a measure of abstractness can be number of interfaces divided by total number of classes in package)

Consider a plane of (Stableness, Abstractness) per calculations above.
Packages grouping around (0, 0) likely introduce pain, since these are concrete and stable. Some packages do fall into this zone, e.g. a DB schema or a concrete utility such as String class, which is concrete and highly depended on.
Packages grouping around (1, 1) are likely useless: abstractions that few uses.
The most desirable position for components is at the two ends of the diagonal, aka the main sequence. Thus a design can be analyzed for the overall distance to the main sequence. The quantization of this metric, though, is arbitrary and imperfect.

### Part 5: architecture

##### Architecture

What is a software architect? He is a programmer first and foremost.

The purpose of an architecture is to facilitate development, deployment, operation, and maintenance of the software system contained within.
The strategy behind this facilitation is to leave as many options open as possible, for as long as possible.
Note that it is not architecture's primary focus to make sure the system works correctly (sure it helps, but) many existing systems work fine but have poor architecture, for these systems the pain is in development, maintenance, and deployment.

"Different team structures imply different architectural decisions. On the one hand, a small team of five developers can quite effectively work together to develop a monolithic system without well-defined components or interfaces. In fact, such a team would likely find the strictures of an architecture something of an impediment during the early days of development. This is likely the reason why so many systems lack good architecture: They were begun with none, because the team was small and did not want the impediment of a superstructure.
On the other hand, a system being developed by five different teams, each of which includes seven developers, cannot make progress unless the system is divided into well-defined components with reliably stable interfaces. If no other factors are considered, the architecture of that system will likely evolve into five components—one for each team.
Such a component-per-team architecture is not likely to be the best architecture for deployment, operation, and maintenance of the system. Nevertheless, it is the architecture that a group of teams will gravitate toward if they are driven solely by development schedule."

* Deployable: to be effective, a software system must be deployable, ideally, with one single action.

One potential downside of micro services: "For example, in the early development of a system, the developers may decide to use a “micro-service architecture.” They may find that this approach makes the system very easy to develop since the component boundaries are very firm and the interfaces relatively stable. However, when it comes time to deploy the system, they may discover that the number of micro-services has become daunting; configuring the connections between them, and the timing of their initiation, may also turn out to be a huge source of errors.

Had the architects considered deployment issues early on, they might have decided on fewer services, a hybrid of services and in-process components, and a more integrated means of managing the interconnections."

* Operation: architecture tends to be a less dramatic effect, as almost any operational difficulties can be resolved by throwing more hardware at the system.
Yet, architecture should reveal operation: elevate use cases, features, and the required behaviors of the system to first class entities that are visible landmarks for the developers.

* Maintenance: of all the aspects of a software system, maintenance is the most costly, whose primary costs come from spelunking (cost of digging through existing software to decide the best place and strategy to add a new feature or repair a defect) and risk (changing existing behavior and introducing bugs)

* Keep options open: recall the two values of a software with the greater value being structure as that's what makes software soft: it does so by leaving choices open. Choices that are left open are details that don't matter.
All software systems can be decomposed into two major elements: policy and details. Policy embodies business rules and procedures, which is where the true value of the system lives. Details are things that are necessary to enable humans, other systems and programmeres to communicate with the policy, but that do not impacting the policy at all. (IO devices, DBs, web systems, communication protocols, etc)
The goal of the architect is to create a shape for the system that recognizes policy as the most essential element of the system while making the details irrelevant to that policy. This allows decisions about those details to be delayed and deferred. And the longer you wait to make those decisions, the more information you have to make them properly, and this leaves you open to trying different experiments / flavors of details.

"What if the decisions have already been made by someone else? What if your company has made a commitment to a certain database, or a certain web server, or a certain framework? A good architect pretends that the decision has not been made, and shapes the system such that those decisions can still be deferred or changed for as long as possible.
A good architect maximizes the number of decisions not made."

* Device independence: detail vs policy we learnt from the early days

"Good architects carefully separate details from policy, and then decouple the policy from the details so thoroughly that the policy has no knowledge of the details and does not depend on the details in any way. Good architects design the policy so that decisions about the details can be delayed and deferred for as long as possible."

##### Independence

A good architecture must support: use cases (in making them obvious) and operation, maintenance, development, deployment.
A good architecture makes the system easy to change, in all the ways that it must change, by leaving options open.

Conway's law
"Any organization that designs a system will produce a design whose structure is a copy of the organization’s communication structure."

"A good architecture does not rely on dozens of little configuration scripts and property file tweaks. It does not require manual creation of directories or files that must be arranged just so. A good architecture helps the system to be immediately deployable after build."

In the real world, the difficulty is that most of the time we don’t know what all the use cases are, nor do we know the operational constraints, the team structure, or the deployment requirements. Worse, even if we did know them, they will inevitably change as the system moves through its life cycle.
Meanwhile, some principles of architecture are relatively inexpensive to implement and can help balance those concerns, even when you don’t have a clear picture of the targets you have to hit. Those principles help us partition our systems into well-isolated components that allow us to leave as many options open as possible, for as long as possible.

* Decoupling layers

Consider the use cases, an architect may not know all of them, but knowing the intent of the system, an architect can use Single Responsiblity Principle and Open Closed Principle to gather things that change for the same reason.

Some obviousness exists in identifying these things: UI, business rules and DB (query language, schema, accessor, etc) usually change for different reasons, thus keeping them independently evolvable is a good practice.
Business rules may serve different goals, e.g. input validation and calculation of interest on an account. These rules will change at different times for different reasons, so they should be separated and kept independently changeable.

* Decoupling use cases

Use cases can be grouped as well based on when and why they change, thus making use cases a natural way to divide the system. While the components (UI, business rules, DB) are horizontal layers, use cases are vertical slices through the horizontal layers
Thus we divide the system both horizontally and vertically.
Advantage of decoupling use cases (dividing vertically) being each use case uses a different aspect of UI / business rule / DB, and adding new cases won't affect existing ones.

(_The division by functions, YASN, SWPM, OVME, CDSW, etc, is an example of this vertical decoupling. We do find awkwardness in this decoupling. This could be a case where the general guideline applies, but making the right decision is case by case and requires knowledge and observation of the system_)

* Decoupling mode (e.g., into services)

The decoupling we did for layers / use cases also helps with operations: different parts of the system can run on different machines, cater to different performance / throughput requirement, scale differently.
To take advantage of the operational benefit, the decoupling must have the appropriate mode, e.g. not depending on addressing in the same machine.
Many architects call such components services, and architecture based on services is a "service-oriented architecture"

Modes can be decoupled at
  * Source level: changing one module does not force the recompilation of one that is independent from it,
  * Binary (deployment) level: changing one module (like, changing a shared object) do not force others to rebuilt and redeployed.
  * Execution unit (service) level: reduce dependency between components down to the level of data structures. And each execution unit is independent from others

SoA may not be the best architecture for everything. The best changes as the project evolves.
Although the general solution is SoA, it may be expensive (development time and system resources) and encourage coarse-grained decoupling.

Rather, a good architect leaves the options open for as long as possible, with decoupling mode being one of those options, and protects majority of the code from potential changes: foresees these changes and _appropriately_ facilitates them.

* Independent developability

The horizontal and vertical decoupling helps with team organization and focus.

* Independent deployability

If done right, the decoupling should help each component deploy and roll out separately.

* Duplication

Architect often fall into a trap that hinges on their fear of duplication.

Duplication is generally a bad thing in software.
But there are different kinds of duplication: two seemingly duplicated code blocks may evolve along different paths and for different reasons.

When you separate vertically, you will be tempted to think two use cases are similar because of similar algorithm, UI screens, or DB accesses. Be careful. Make sure the duplication is real before committing into coupling them.
Similarly, when separate horizontally, you may notice the data structure of a particular database record is very similar to the data structure of a screen view. You may be tempted to simply pass the DB record to the UI rather than to create a view model that looks the same and copies the elements across. Be careful, this duplication is most likely fake, better keep them decoupled.
(_The discussion with Fei about DPQA using an individual DBRecord class client structure or generated message type may reflect consideration for this coupling_)
 
##### Boundaries: drawing lines

Separate software elements from one another, with those side A knowing little about side B (side B may know about side A).
Some are drawn early on, some later. Those early on are drawn for the purpose of deferring decisions: avoid having decisions about details pollute business logic.

Coupling because of premature decisions saps a system's maintainability.
A good system avoids premature decisions made on details such as frameworks, databases, web servers, util libraries, dependency injection, and defer them to the latest possible without significant impact.

_what might go wrong in the design of an SoA? they are not panacea_

Which lines to draw: between things that matter and things that don't. Contrary to common misconception, usually business rule doesn't need to know database schema, thus the layer of (abstract) database accessor. (_which fortunately is in dpqa design_)

E.g. business rule and accessor interface belong to one element, accessor impl belongs to another. 
Direction of lines crossing the line we draw: business rules element doesn't know about DB impl, DB impl knows about business rules (as db can't exist without business rules: query languages in accessor impl reflects business logic, not vice versa, business rule only needs to know about an accessor interface, what underlying storage is does not matter)

Similarly, I/O, GUI is irrelevant to business rules.

With this we form a **plugin architecture**: DB / GUI are plugins to business rules. This deeply asymmetric relationship is what we want in our systems, for certain modules (business rules) to be immune to others (DB / GUI).
Touching back on earlier content, elements on different sides of the line change at different times, for different reasons. Single Responsibility Principle tells us where to draw the boundaries.

##### Boundary anatomy

Architecture of a system is defined by a set of components with boundaries separating them.
At runtime, a boundary crossing is a function on one side calling one on the other side.
Trick to creating appropriate boundary crossing is to manage source code dependencies.

"Without OO, or an equivalent form of polymorphism, architects must fall back on the dangerous practice of using pointers to functions to achieve the appropriate decoupling."
(_Reminder for the argument that high level business logic should not depend on low level mechanism, should be the other way round_)

Threads are not architectural boundaries, but rather a way to organize the schedule and order of execution. They may be contained in one component, or span across multiple.

A local process is a much stronger physical boundary, and a service even stronger. For local processes and services, the same argument of "high level services should not contain specific knowledge of low level services, but rather low level services can serve as plugins to high level services" applies

##### Policy and level

Software systems are statements of policy, that which transforms inputs to outputs.

Policies further break down into smaller ones, e.g. business rules for calcs, input validation, output formatting, etc.
Part of the art of developing an architecture is carefully separating policies from one another, grouping them based on the ways they change, and into separate components, which are formed into an acyclic graph. Meaning, policies, too, should be grouped by Single Responsibility Principle and Common Closure Principle.

"In a good architecture, the direction of those dependencies is based on the level of the components that they connect. In every case, low-level components are designed so that they depend on high-level components."

* Level: "a strict definition of “level” is “the distance from the inputs and outputs.” The farther a policy is from both the inputs and the outputs of the system, the higher its level. The policies that manage input and output are the lowest-level policies in the system."

"The data flows and the source code dependencies do not always point in the same direction. This, again, is part of the art of software architecture. We want source code dependencies to be decoupled from data flow and coupled to level."

"Higher-level policies—those that are farthest from the inputs and outputs—tend to change less frequently, and for more important reasons, than lower-level policies. Lower-level policies—those that are closest to the inputs and outputs—tend to change frequently, and with more urgency, but for less important reasons."

Lower level policies should be plugins to higher level policies.

(_Think about the sapiwrapper service we recently looked at, retrieving different data from a number of services, carry out some business logic, and serve the requests to it. In this case the services sapiwrapper asks for data should be plugins to sapiwrapper service (imagine, the data source could be a BAS client, or file system, etc), with sapiwrapper service's own business logic being higher level_)

(_Then if we think about plugging in guts to a business logic module, metrics, being low level, should probably also be not a direct dependency of the higher level business logic module? But instead, we have a metrics interface?_)

##### Business rules

If we are to divide our application into business rules and plugins, we need to understand what business rules really are.

Critical business rules: those that will save / make business money, executed on a computer or not.
Critical business rules usually require critical business data to work with.

We model critical business rules and critical business data with an **Entity** (an object, a module, etc), and this entity should exist, unsullied with concerns about databases, UI, or thirdparty software.

Not all business rules are entities: they can be **use cases**, a description of how the automated system is used (application-specific business rules), one that wouldn't exist on paper.

Use cases contain rules that specify when critical business rules within the entities are invoked: they control the dance of entities, while entities should have no knowledge of them. Entities are high level, use cases are low level, in the sense that use cases are application specific rules, while entities are general enough for any applications.
Use case does not describe, say, a concrete user interface, or a data ingestion method; which are at an even lower level: use case takes in input structure, and gives output structure. From what transport mechanism those come is low-level detail.

You might be tempted to contain references to entity objects inside request/response model, because they share so much data. Avoid this temptation as they change for different purposes at different times.

Business rules are the family jewels that should remain pristine, unsullied by baser concerns such as UI or DB, who should be plugged in as lesser concerns.

##### Screaming architecture

Software architectures are structures that support the use cases of the system. Just as the plans for a house or a library scream about the use cases of those buildings, so should the architecture of a software application scream about the use cases of the application (as opposed to a particular framework).

When using a framework, think about hwo you can preserve the use case emphasis of your architecture. Develop a strategy that prevents the framework from taking over the architecture.

If you have kept your frameworks at arm's length, and your architecture is all about the use cases, then you should be able to unit test each particular use case without having frameworks (say, BAS, ComDB2) in place.

##### The clean architecture

An architecture should be independent of frameworks (UI, DB, external agencies) and testable

Figure 22.1 is a good illustration: in a concentric circle entities being the inner most, wrapped by use cases, then by interface adapters and finally by frameworks.
Given this circle, we have **the Dependency Rule**: source code dependency should only point inwards: no changes in the outer circle should cause changes in the high-level business object. Note how the flow of control is the reverse of source code dependency (business object calls something from the outer circle via an interface, flow of control; _but in this calling-a-concrete-implementation-via-an-interface pattern, why do we say source code dependency is inverted? Maybe although the DB accessor does not \#include the business object header, but the queries it makes reflect the usage pattern mandated by the business object? An answer could be that **the interface is considered part of the inner circle's package**, and a concrete implementation includes this interface definition such that it can inherit from this interface. And in terms of what goes in this interface: take DB as an example, recall that we don't allow SQL in use case layer. So the particular query (input/output) would be hidden behind an interface, and implemented by the concrete accessor, as opposed to accessor exposing a SQL execution interface._)

Isolated, simple data structures are passed across boundaries: we don't want data structures to have any kind of dependencies that violate the Dependency Rule (e.g. passing a DB row structure that's particular to a DB)

##### Presenters and humble objects

The humble object pattern was introduced as a way to help unit testers to separate behaviors that are hard to test from those that are easy to test: split the behaviors into two classes, the humble one containing all the hard to test behavoirs (e.g. where an element is in GUI, "the view"), and the other one containing the easy to test behaviors ("the presenter" that formats the data it gets and makes them screen-display ready). Focus on testing the presenter, and keep the view "humble" (does nothing more than load data from View Model into the screen)

Another example would be a DB accessor: the concrete component that wraps around a particular DB query is humble, and the interactors using such accessors via an interface are not: they encapsulate particular business rules and perform things based on the output. Focus the test on the interactor.

(_Then speaking of real examples, is iribsz --> sft mapper humble? I believe yes, one way to think about it is this module packs a plain old data to be carried across boundaries, the mapper itself matters less than the interactor that works with the data, not unlike given a View Model, load data to the screen? If this holds, does it justify not unit testing iribsz --> sft mapper?_)

##### Partial boundary

A full boundary may be expensive: boundary interfaces, input output data structures, and hard to maintain.
A purely anticipatory design may violate YAGNI "you arne't going to need it", in which case architects sometimes propose a partial boundary, in which all the components may be in place but sitting in one group, or a dependency inversion (interface) is in place, or like a Facade pattern where even a dependency inversion is not enforced.

##### Layers and boundaries

Hunt the Wumpus game example: support multiple languages? Different input interfaces? Underlying data storage? Multiplayer? Player status management as a microservice?
The point is, however simple a program, architects need to identify boundaries, when they are needed, and if we don't add them now, how much effort would it be to add them later.
Over engineering is often much worse than under engineering, but on the other hand when you discover you do need boundaries whereas they don't already exist, it's often risky and costly to add them.
As an architect, you make educated guesses, and keep a watchful eye and revisit your decisions as the project progresses.

##### The main component

In every system, there is at least one component that creates, coordinates, and oversees others. We call this component Main.
Main is the ultimate detail, the lowest-level entry. Nothing depends on Main, Main create higher level objects and hand over control to them.
Think of Main as a plugin to the application who sets up the initial conditions and configs, gathers outside resources then hand over control to higher level policy of the application. A different Main / configuration could be plugged in for each scenario.

##### Services: great and small

SOAs.

Are services always architecturally significant? Not necessarily: the architecture of the system is defined by boundaries that separate high-level policy from low-level detail. Services themselves are a form, and they are architecturally significant when they represent architectural boundaries.
Do they offer better decoupling? Not necessarily. They can still be coupled by shared resources on the network, or data they share. E.g. similar to function signature changes, plumbing a new field in a series of microservices needs service schema changes.
Do they offer independent development and deployment? True to some extent, but often times we see operations still needing coordination.
"Architecture is not defined by the physical mechanisms by which elements communicate and execute."

Cross cutting concerns: a system built with functional decomposition are very vulnerable to new features that cut across all functional behaviors, SOA or not. (e.g. Uber to deliver cats. Considering which taxi suppliers / drivers are in, passenger allergies, etc)
The answer is to think in terms of functional components, a taxi supplier component, service or not, could offer an interface where the concrete human / cat rides behavior can derive from. In which case, the boundary may run through services dividing them into components.

To summarize, useful as they are, SOAs are not panaceas, and to account for cross cutting changes, the internals of a service (or a functional component) may need to be designed with Dependency Rule in mind, and allow pluggable concrete implementations.

##### Test boundaries

Tests (of different flavors, unit, integration, etc) are part of the system.
They are very detailed and concrete, nothing depends on the them, and they follow the Dependency Rule pointing inwards.

Fragile test problem: changing common system components breaks tons of tests. Tests that are not well integrated into the design of the system tend to be fragile, and they make the system rigid and difficult to change. 

Design for testability: tests (and others) should not depend on volatile things. E.g. test the business logic without depending on UI.

Structural coupling (_questionable_): if a test suite has a test class for each production class, and a test method for each production method, tests have to be changed as well for each production interface change.
The proposed solution is a test API that allows changes in production which don't affect the tests.
_I find this questionable, and should be analyzed case by case: in unit tests, all public interfaces should be tested. At unit test level, having test API probably means having methods to force the object into a certain state. This would be useful but does not allow not having a test method corresponding with each method in the public interface; what the authors claim to be structural coupling_

##### Clean embedded architecture

Software does not wear out, unlike hardware.
However software can be destroyed from within by unmanaged dependencies on firmware and hardware.

What really is firmware? Code that lives on ROM? Maybe another way of seeing it is code that is heavily dependent on hardware.
(In a sense we write firmware too if our software is coupled with particular hardware "details")
Don't write "firmware" if you want your code to have a long useful life.

First make it work. Then make it right. Then make it fast.

The hardware is a detail. Split your software from your firmware, and make those that don't need to depend on hardware hardware-independent. Software should allow off target testing.
Introduce a Hardware Abstraction Layer between firmware and software if needed, and HAL exposes application-semantic interfaces.

Similarly, you should insulate your software from OS dependencies. An OSAL should be introduced.
(_Similarly for us, pricing code should be testable off target as well._)

Don't repeat yourself

### Part 6: details

##### The database is a detail

The particulars of a database is of little architectural importance, while the data model is. (_How would one define a data model?_)
Business entity should not know the detail of the underlying data stored in a relational way, represented as tabular rows of records, etc.

Why are database systems so prevalent? They work with disks: file system does and offers a document abstraction, databases are content based, and provide a natural and convenient way to find records based on their content.

Relational database used to be a buzzword, nowadays, are "SoA"s such words as well?

##### The web is a detail

The endless pendulum: client-side execution, server-side execution; superhosts and dumb terminals, or vice versa; cloud or edge; centralizing, distributing; _the spiraling up_
These oscillations will continue for some time to come.

The story of the UI of company Q.

The upshot is simple: the GUI is a detail, and the web is a GUI, as an architect, keep such stuff away from your business logic.

Alternatively, does it make sense to provide abstractions over different technologies like the web and the desktop (or over RabbitMQ and Kafka?)

"The argument can be made that a GUI, like the web, is so unique and rich that it is absurd to pursue a device-independent architecture. When you think about the intricacies of JavaScript validation or drag-and-drop AJAX calls, or any of the plethora of other widgets and gadgets you can put on a web page, it’s easy to argue that device independence is impractical.

To some extent, this is true. The interaction between the application and the GUI is “chatty” in ways that are quite specific to the kind of GUI you have. The dance between a browser and a web application is different from the dance between a desktop GUI and its application. Trying to abstract out that dance, the way devices are abstracted out of UNIX, seems unlikely to be possible."

The argument is that it's still possible to provide such abstractions, especially isolating business logic from the underlying details.
"This kind of abstraction is not easy, and it will likely take several iterations to get just right. But it is possible. And since the world is full of marketing geniuses, it’s not hard to make the case that it’s often very necessary."

##### Frameworks are details

Frameworks are not architectures.

Framework authors do not know your problems, although your problems may overlap.

The framework author is asking you to couple with their framework, your commitment to the framework is huge, while the framework makes no commitment to you. 
Risks with a framework: the framework may help you with early features, but your product may outgrow the framework; the framework may evolve in a direction you don't want; a better framework may come along the way.

The solution is that you can use a framework, but don't "marry" it: don't let it in the inner circle.

"If the framework wants you to derive your business objects from its base classes, say no! Derive proxies instead, and keep those proxies in components that are plugins to your business rules."

### Use case

Video serving website; roles and use cases; division of components;

### The missing advice

"Your best design intentions can be destroyed in a flash if you don’t consider the intricacies of the implementation strategy. Think about how to map your desired design on to code structures, how to organize that code, and which decoupling modes to apply during runtime and compile-time. Leave options open where applicable, but be pragmatic, and take into consideration the size of your team, their skill level, and the complexity of the solution in conjunction with your time and budgetary constraints. Also think about using your compiler to help you enforce your chosen architectural style, and watch out for coupling in other areas, such as data models. The devil is in the implementation details."

### Afterword

The evolution from Big architectures and engineering practices to Agile.

"Now you’ve seen how it’s possible to write code that delivers value today without blocking future value tomorrow; the onus is on you to put in the practice so you can apply these principles to your own code.
Like riding a bicycle, you can’t master software design just by reading about it. To get the best from a book like this, you need to get practical. Analyze your code and look for the kinds of problems Bob highlights, then practice refactoring the code to fix these problems. If you’re new to the refactoring discipline, then this will be a doubly valuable experience."
