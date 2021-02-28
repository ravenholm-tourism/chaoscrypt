# Stream Cipher using [Chaotic Cryptography](https://en.wikipedia.org/wiki/Chaotic_cryptology)

## __Note this is *not* a secure cryptosystem and is vulnerable to [several](https://arxiv.org/abs/cs/0402004) [attacks](http://hdl.handle.net/20.500.11929/sdsu:2476)__

Implementation of a stream cipher described by baptista [in this paper](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.476.9974&rep=rep1&type=pdf).  The primary purpose of this project is to explore and investigate the properties of cryptosystems that use chaotic maps.  The current implementation uses the Logistic Map, but I hope to include other well-known one dimensional maps (Tent Map, Dyadic Map, Circle Map) and higher dimensional ones (Complex Quadratic Map, Arnold's Cat Map, Rössler system, Lorentz Equations).

## Encryption Parameters
* initial position to begin iterating from __x<sub>0</sub>__
* the logistic map's control parameter __r__
  * From the logistic map equation x<sub>n+1</sub> = __r__ * x<sub>n</sub> * (1 - x<sub>n</sub>)
  * Controls whether or not the function is chaotic (defaults to known chaotic value 3.8)
* A list of characters __A__ that your message is written with (its alphabet)
  * uses ASCII 256 by default
* A mapping __S__ that maps each character in __A__ to a sub-interval of [.2, .8]
  * For example "h" &rightarrow; (0.44375000000000, 0.44609375000000]
* Transient time __N<sub>0</sub>__ - the number of initial iterations to ignore so that close initial positions have sufficient time to  diverge
  * This is essentially the Lyapunov Time of the chaotic system
* __&eta;__ determines which orbit that lands in a character's interval to use.  Each iteration that lands in the interval has a probability of __P__ = 1 - normaldistcdf(&eta;) to be chosen as the interation number for that character's ciphertext
  * note: if &eta;=0 then the first iteration to enter the interval is used
* __msg__ plaintext message with characters in __A__

## ciphertext
* sequence of 16-bit unsigned ints (number of iterations to get to interval mapped to plaintext char)

## key
* char-to-interval mapping A -> S = {[s_0,s_1), ..., [s_n,s_n+1)}, can modify this by permuting the order that chars are stored in the alphabet array
* initial condition x_0
* control parameter r

## notes
* choose r to make map chaotic, e.g. 3.8
  * note other values work as well, like 3.78.  See [here](https://en.wikipedia.org/wiki/Logistic_map#Behavior_dependent_on_r)
* choose transient time high enough to allow for divergence, N_0 >> map's lyapunov time, ~250
* make sure sender's and receiver's floating point arithmetic are consistent, use float64 - need at least 14 decimal precision
  * for instance, there is a small difference in values computed for intervals for example message "hi" (in baptista paper) because of different implementations of floating point arithmetic (and possibly different machine epsilons)