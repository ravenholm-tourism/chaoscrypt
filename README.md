# Logistic Map Steam Cypher

## encryption parameters
* initial value x_0
* logistic map control parameter r
* alphabet A = {a1,a2, ..., an}
* map of chars in A to intervals in [.2,.8]   ai -> [si, si+1)
* transient time N_0
* eta determines which orbit in letter's interval to use - each one as a prob of 1 - normaldistcdf(eta)   (e.g.if eta=0 then 1st orbit in interval used)
* plaintext stream with chars in A

## cyphertext
* sequence of 16-bit unsigned ints    (each is number of iterations to get to interval mapped to char)

## key
* char-to-interval mapping A -> S = {[s0,s1), ..., [sn,sn+1)},  [si,si+1) in [.2,.8]
* initial condition x_0
* logistic parameter r

## notes
* choose r to make map chaotic, ~3.8+
* choose transient time high enough to allow for divergence, N_0 >> map's lyapunov time, ~250
* make sure sender's and receiver's floating point arithmetic are consistent, use float64 - need at least 14 decimal precision