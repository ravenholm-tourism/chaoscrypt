# Logistic Map Stream Cipher

Implementation of a stream cipher described by baptista [in this paper](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.476.9974&rep=rep1&type=pdf).
Note this is not a secure cryptosystem and is vulnerable to many attacks.  The primary purpose of this project is to understand and investigate properties of cryptography using chaotic maps.

## encryption parameters
* initial value x_0
* logistic map control parameter r
* alphabet A = {a_1,a_2, ..., a_n} (uses ASCII 256 by default)
* map of chars in A to intervals in [.2,.8]   a_i -> [s_i, s_i+1)
* transient time N_0    (basically lyapunov time to ensure sufficient divergence of paths that start close together)
* eta allows for stochastic transmission; it determines which orbit in letter's interval to use - each one as a prob of 1 - normaldistcdf(eta)   (e.g.if eta=0 then 1st orbit in interval used)
* plaintext stream with chars in A

## cyphertext
* sequence of 16-bit unsigned ints    (each is number of iterations to get to interval mapped to char)

## key
* char-to-interval mapping A -> S = {[s_0,s_1), ..., [s_n,s_n+1)}, change this by permuting the order characters are stored in the alphabet array
* initial condition x_0
* logistic parameter r

## notes
* choose r to make map chaotic, ~3.8+
* choose transient time high enough to allow for divergence, N_0 >> map's lyapunov time, ~250
* make sure sender's and receiver's floating point arithmetic are consistent, use float64 - need at least 14 decimal precision
  * for instance, there is a small difference in values computed for intervals for example message "hi" (in baptista paper) because of different implementations of floating point arithmetic (and possibly different machine epsilons)