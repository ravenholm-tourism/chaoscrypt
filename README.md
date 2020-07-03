# Stream Cipher using [Chaotic Cryptography](https://en.wikipedia.org/wiki/Chaotic_cryptology)

Implementation of a stream cipher described by baptista [in this paper](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.476.9974&rep=rep1&type=pdf).
Note this is not a secure cryptosystem and is vulnerable to many attacks.  The primary purpose of this project is to understand and investigate properties of cryptography using chaotic maps.  Current implementation uses the Logistic Map, but hope to include other well-known one dimensional chaotic maps (Tent Map, Dyadic Map, Circle Map) and higher dimensional ones (Complex Quadratic Map, Arnold's Cat Map, Rössler system, Lorentz Equations).

## encryption parameters
* initial value x_0
* logistic map control parameter r - from equation x_n+1 = r * x_n * (1 - x_n)
* alphabet A = {a_1,a_2, ..., a_n} - uses ASCII 256 by default
* map of chars in A to intervals in [.2,.8]   a_i -> [s_i, s_i+1)
* transient time N_0 - basically lyapunov time to ensure sufficient divergence of paths with close initial values
* eta - controls stochastic transmission; it determines which orbit in chars's interval to use.  Each iteration as a prob of 1 - normaldistcdf(eta) to be chosen as ciphertext (note if eta=0 then 1st iteration that enters interval is used)
* plaintext stream with chars in A

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