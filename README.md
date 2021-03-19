# Stream Cipher using [Chaotic Cryptography](https://en.wikipedia.org/wiki/Chaotic_cryptology)

## __Note this is <ins>*not*</ins> a secure cryptosystem and is vulnerable to [several](https://arxiv.org/abs/cs/0402004) [attacks](http://hdl.handle.net/20.500.11929/sdsu:2476)__

This project is an implementation of the stream cipher introduced by baptista [in this paper](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.476.9974&rep=rep1&type=pdf).  The primary purpose of this project is to explore the properties of cryptosystems that use chaotic maps.  The current version uses the Logistic Map, but I hope to include other well-known one dimensional maps (Tent Map, Dyadic Map, Circle Map) and higher dimensional ones (Complex Quadratic Map, Arnold's Cat Map, Rössler system, Lorentz Equations).

## Encryption Parameters
* initial position to begin iterating from __x<sub>0</sub>__
* the logistic map's control parameter __b__
  * From the logistic map equation x<sub>n+1</sub> = __b__ * x<sub>n</sub> * (1 - x<sub>n</sub>)
  * This controls whether or not the function is chaotic (defaults to known chaotic value 3.8)
* A set of characters __A__ that your message is written with (its alphabet)
  * uses ASCII 256 by default
* A mapping __S__ that maps each character in __A__ to a sub-interval of [.2, .8]
  * For example "h" &rightarrow; (0.44375000000000, 0.44609375000000]
* Transient time __N<sub>0</sub>__ - the number of initial iterations to ignore so that close initial positions have sufficient time to  diverge
  * This is essentially the Lyapunov Time of the chaotic system
  * For the Logistic Map, default value is 250
* __&eta;__ determines which iteration in an orbit that lands in a character's sub-interval to use.  Each iteration that lands in the interval has a probability of __P__ = 1 - normaldistcdf(&eta;) to be chosen as the interation number for that character's ciphertext.  If a given iteration is not chosen, then the map continues iterating until it lands in the sub-interval again and has a chance to be chosen.
  * note: if &eta;=0 then the first iteration to enter the interval is used
* __msg__ plaintext message with characters in __A__

## ciphertext
* sequence of 16-bit unsigned ints - each is number of iterations to get to interval mapped to the next plaintext char

## key
* char-to-interval mapping __A__ &rightarrow; __S__ = {[s<sub>0</sub>, s<sub>1</sub>), ..., [s<sub>n</sub>, s<sub>n+1</sub>)}
  * can modify this by permuting the order that chars are stored in the alphabet array
* initial condition __x<sub>0</sub>__
* control parameter __b__

## notes
* choose __b__ to make map chaotic, e.g. 3.8
  * other values work as well, like 3.78.  See [here](https://en.wikipedia.org/wiki/Logistic_map#Behavior_dependent_on_r)
* choose a transient time high enough to allow for divergence, N<sub>0</sub> >> map's lyapunov time, ~250