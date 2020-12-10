# My learnings from Clean Code book by Martin fowler


## General

* You know you are working on clean code when each routine you read turns out to be pretty much what you expected.

* The next time you write a line of code, remember you are an author, writing for readers who will judge your effort. The ratio of time spent reading vs. writing is well over 10:1. We are constantly reading old code as part of the effort to write new code. Because this ratio is so high, we want the reading of code to be easy, even if it makes the writing harder. 

* Leave the campground cleaner than you found it. -Boy scout rule
 If we all checked-in our code a little cleaner than when we checked it out, the code simply could not rot. The cleanup doesn’t have to be something big. Change one variable name for the better, break up one function that’s a little too large, eliminate one small bit of duplication, clean up one composite if statement.

## Naming

* It is easy to say that names should reveal intent. Choosing good names takes time but saves more than it takes. So take care with your names and change them when you find better ones. Everyone who reads your code (including you) will be happier if you do.

* Beware of using names which vary in small ways. How long does it take to spot the subtle difference between a `XYZControllerForEfficientHandlingOfStrings` in one module and, somewhere a little more distant, `XYZControllerForEfficientStorageOfStrings` The words have frightfully similar shapes.

* Noise words are another meaningless distinction. Imagine that you have a Product class. If you have another called ProductInfo or ProductData, you have made the names different without making them mean anything different. Info and Data are indistinct noise words like a, an, and the.

* In the absence of specific conventions, the variable moneyAmount is indistinguishable from money, customerInfo is indistinguishable from customer, accountData is indistinguishable from account, and theMessage is indistinguishable from message. Distinguish names in such a way that the reader knows what the differences offer.

* Use Pronounceable Names: A company I know has genymdhms (generation date, year, month, day, hour, minute, and second) so they walked around saying “gen why emm dee aich emm ess”. Change
```
private Date genymdhms;
to
private Date generationTimestamp; 
```
Intelligent conversation is now possible: "Hey, Mikey, take a look at this record! The generation timestamp is set to  tomorrow’s date! How can that be?"

* Class Names: Classes and objects should have noun or noun phrase names like Customer, WikiPage, Account, and AddressParser. Avoid words like Manager, Processor, Data, or Info in the name of a class. A class name should not be a verb.
   Noun: a word that refers to a person, place, thing, event, substance or quality.

* Method Names: Methods should have verb or verb phrase names like postPayment, deletePage, or save. Accessors, mutators, and predicates should be named for their value and prefixed with get, set, and is according to the javabean standard.
   Verb: a word or phrase that describes an action, condition or experience e.g. 'run', 'look' and 'feel’.

* In an imaginary application called “Gas Station Deluxe,” it is a bad idea to prefix every class with GSD. Frankly, you are working against your tools. You type G and press the completion key and are rewarded with a mile-long list of every class in the system. Is that wise? Why make it hard for the IDE to help you?

## Functions

* The first rule of functions is that they should be small. The second rule of functions is that they should be smaller than that.

* Ward’s principle: “You know you are working on clean code when each routine turns out to be pretty much what you expected.” Half the battle to achieving that principle is choosing good names for small functions that do one thing. The smaller and more focused a function is, the easier it is to choose a descriptive name.

* The ideal number of arguments for a function is zero (niladic). Next comes one (monadic), followed closely by two (dyadic). Three arguments (triadic) should be avoided where possible. More than three (polyadic) requires very special justification—and then shouldn’t be used anyway.

* Using an output argument instead of a return value for a transformation is confusing. If a function is going to transform its input argument, the transformation should appear as the return value.

* Flag arguments are ugly. It immediately complicates the signature of the method, loudly proclaiming that this function does more than one thing. It does one thing if the flag is true and another if the flag is false! But if the code is being duplicated you can create a private method to avoid duplicacy. 
https://martinfowler.com/bliki/FlagArgument.html

* Reducing the number of arguments by creating objects out of them may seem like cheating, but it’s not. When groups of variables are passed together, the way x and y are in the example above, they are likely part of a concept that deserves a name of its own.

* Prefer Exceptions to Returning Error Codes:  
`if(delete(id) == CODE_OK)`
This does not suffer from verb/adjective confusion but does lead to deeply nested structures. When you return an error code, you create the problem that the caller must deal with the error immediately often by nested if else checks.

* When writing functions the first draft might be clumsy and disorganized, so you wordsmith it and restructure it and refine it until it reads the way you want it to read.

* [Command query separation](https://en.wikipedia.org/wiki/Command%E2%80%93query_separation): Functions should either do something or answer something. That’s practical and clear advice.

## Classes

* The name of a class should describe what responsibilities it fulfills. In fact, naming is probably the first way of helping determine class size. If we cannot derive a concise name for a class, then it’s likely too large. The more ambiguous the class name, the more likely it has too many responsibilities. For example, class names including weasel words like Processor or Manager or Super often hint at unfortunate aggregation of responsibilities.

* SRP is one of the more important concept in OO design. It’s also one of the simpler concepts to understand and adhere to. Yet oddly, SRP is often the most abused class design principle. We regularly encounter classes that do far too many things. Why? Getting software to work and making software clean are two very different activities. Most of us have limited room in our heads, so we focus on getting our code to work more than organization and cleanliness. This is wholly appropriate. Maintaining a separation of concerns is just as important in our programming activities as it is in our programs. The problem is that too many of us think that we are done once the program works. We fail to switch to the other concern of organization and cleanliness. We move on to the next problem rather than going back and breaking the overstuffed classes into decoupled units with single responsibilities.

* Cohesion refers to the degree to which the elements inside a class belong together. Thus, cohesion measures the strength of relationship between pieces of functionality within a given module. Classes should have a small number of instance variables. Each of the methods of a class should manipulate one or more of those variables. In general the more variables a method manipulates the more cohesive that method is to its class. When cohesion is high, it means that the methods and variables of the class are co-dependent and hang together as a logical whole. 

## Good Design
* According to Kent, a design is “simple” if it follows these rules: 
     1. Runs all the tests (Highest priority. Create systems which can be tested and verified)
     2. Contains no duplication 
     3. Expresses the intent of the programmer 
     4. Minimizes the number of classes and methods

* All too often we get our code working and then move on to the next problem without giving sufficient thought to making that code easy for the next person to read. Remember, the most likely next person to read the code will be you. So take a little pride in your workmanship. Spend a little time with each of your functions and classes. Choose better names, split large functions into smaller functions, and generally just take care of what you’ve created. Care is a precious resource.

## Smells and Heurestics 
* It makes me crazy to see stretches of code that are commented out. Who knows how old it is? Who knows whether or not it’s meaningful? Yet no one will delete it because everyone assumes someone else needs it or has plans for it. That code sits there and rots, getting less and less relevant with every passing day. It calls functions that no longer exist. It uses variables whose names have changed. It follows conventions that are long obsolete. It pollutes the modules that contain it and distracts the people who try to read it. Commented-out code is an abomination. When you see commented-out code, delete it! Don’t worry, the source code control system still remembers it. If anyone really needs it, he or she can go back and check out a previous version. Don’t suffer commented-out code to survive.

* Variables and function should be defined close to where they are used. Local variables should be declared just above their first usage and should have a small vertical scope. We don’t want local variables declared hundreds of lines distant from their usages. Private functions should be defined just below their first usage. Private functions belong to the scope of the whole class, but we’d still like to limit the vertical distance between the invocations and definitions. Finding a private function should just be a matter of scanning downward from the first usage.

* The most common reason for partitioning concepts into base and derivative classes is so that the higher level base class concepts can be independent of the lower level derivative class concepts. Therefore, when we see base classes mentioning the names of their derivatives, we suspect a problem. In general, base classes should know nothing about their derivatives. There are exceptions to this rule, of course. Sometimes the number of derivatives is strictly fixed, and the base class has code that selects between the derivatives. We see this a lot in finite state machine implementations.

* This is one of Martin Fowler’s code smells.6 The methods of a class should be interested in the variables and functions of the class they belong to, and not the variables and functions of other classes. When a method uses accessors and mutators of some other object to manipulate the data within that object, then it envies the scope of the class of that other object. It wishes that it were inside that other class so that it could have direct access to the variables it is manipulating.

* Misplaced Responsibility: One of the most important decisions a software developer can make is where to put code. For example, where should the PI constant go? Should it be in the Math class? Perhaps it belongs in the Trigonometry class? Or maybe in the Circle class? The principle of least surprise comes into play here. Code should be placed where a reader would naturally expect it to be. The PI constant should go where the trig functions are declared.

* Static methods: Math.max(double a, double b) is a good static method. It does not operate on a single instance; indeed, it would be silly to have to say new Math().max(a,b) or even a.max(b). All the data that max uses comes from its two arguments, and not from any “owning” object. More to the point, there is almost no chance that we’d want Math.max to be polymorphic. In general you should prefer nonstatic methods to static methods. When in doubt, make the function nonstatic. If you really want a function to be static, make sure that there is no chance that you’ll want it to behave polymorphically.

* Replace Magic Numbers with Named Constants

* Encapsulate Conditionals: Boolean logic is hard enough to understand without having to see it in the context of an if or while statement. Extract functions that explain the intent of the conditional. For example: if (shouldBeDeleted(timer)) is preferable to if (timer.hasExpired() && !timer.isRecurrent())
