# Object-Oriented-Programming
A couple examples of using Class Oriented Programming
There are 3 examples in this repository:
  
## 1. bomb_calc1:

* This module I have been updating occasionally. This is meant to simulate an ESO bomber attacking a defending player. The first version of it was function based program. I was able to compare builds against the meta. I used this module to determine that medium armor would deal more damage than the light armor builds. I gave my friend this build and he used it to become the 2nd highest score per campaign for two straight campaigns and the highest on his alliance (3 alliances in a campaign).
*  The meta changed this past patch so it was a good time to give it an update. I formatted it more into a Class oriented format so most functions became methods. There are two classes in this module: Bomber and Zergling. Bomber represents the bombing player and zergling represents a defending player. I added multiple functationality to the code: healing per second, health, vicious death procs, attacking a group of defending players, and doing subsequent attacks.

## 2. Simpy:

* This was a class project where we simulated the Numpy modules. The joke is Simpy simps for Numpy. It was a great tutorial that taught me many features of classes: attributes, methods, and responsible use of operator overloads.

## 3. Sample:

* This was a module that will help me deal with statistical analysis of population distributions. This is the module that needs the most work. As of right now it can only solve p-values with z scores. 
* Before my exam, I plan to add more functionality to this module. It is limited to z scores but in the future I want it to determine, by the attributes saved to the sample class, if it should use a T hypothesis or not to solve for the p-value. This would be determined by if it has a population standard deviation or a sample standard deviation attached to it.
