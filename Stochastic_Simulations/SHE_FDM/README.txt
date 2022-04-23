The scripts in this directory give simulations to the heat question with either deterministic or random source term. In either case, we use the finite difference method to generate a simulation.

The he.py script has a deterministic source term.

The she.py script has the randm forcing term. The noise is white in time and space. We use the theory of Walsh to generate the noise. More specfically, we create a grid use the fact that

W(t + dt, x + dx) - W(t + dt, x) - W(t, x + dx) + W(t, x) ~ normal(0,dt * dx).

Some animations and pictures can be found in the GIFsAndPics file.

Note that the finite difference method requires are very fine time partition. Doing so increases the computation time drastically on my computer which can't really handle the computations. Becasue of this, I am not able to simulation longer gifs or increase the time or space intervals by much.  
