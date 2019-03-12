# Pigeons
This is a simulation of an experimental desing by Richard Herrstein.
    
    HERRNSTEIN R. J. (1961).
    Relative and absolute strength of response as a function of frequency of reinforcement.
    Journal of the experimental analysis of behavior, 4(3), 267-72. 

The paper rest on the early theory of choice in the realm of Behaviour Analisys.

It hypothesizes the relative frequency of response as a dependent variable to the frequency of reinforcement.
It is ussually taken as the beggining for the development of what is call the Matching Law.
And it is in turn a precursor work for the Delay Reduction Theory by Edmund Fantino.

    Fantino, E., & Romanowich, P. (2007).
    The effect of conditioned reinforcement rate on choice: A review.
    Journal of the Experimental Analysis of Behavior, 87, 409–421.


## Experimental Desing
![game caption](https://github.com/mesielepush/Pigeons/blob/master/img/for_readmd.png)

This simulation begins with four posible ![concurrent](https://en.wikipedia.org/wiki/Reinforcement#Concurrent_schedules) ![variable interval (VI) schedules](https://dictionary.apa.org/variable-interval-schedule), all of wich have a constant mean of 1.5 min per renforcement, as in the original paper.

* VI(3)----- VI(3)
* VI(2.25)-- VI(4.5)
* VI(1.8)--- VI(9)
* VI(1.5)--- VI(0)

###However, since a mean of 90 seconds per reinforcement could be too much for humans, there are three alternative options with means of: 60, 45 and 23 seconds. Naturally the proportion between the VIs of each schedule is held constant for all alternatives.

At the begining of each Session, the user chooses either the original mean or one of the alternatives.
The program selects a schedule at random, and assaings each VI to the left and right keys also at random.


