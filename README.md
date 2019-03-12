# Pigeons
This is a simulation of an experimental desing by Richard Herrstein.
    
    HERRNSTEIN R. J. (1961).
    Relative and absolute strength of response as a function of frequency of reinforcement.
    Journal of the experimental analysis of behavior, 4(3), 267-72. 

The paper rest on the early theory of choice in the realm of Behaviour Analysis.

It hypothesizes the relative frequency of response as a dependent variable to the frequency of reinforcement. It is usually taken as the beginning for the develop of what is call the Matching Law. And it is in turn a precursor work for the Delay Reduction Theory by Edmund Fantino.

    Fantino, E., & Romanowich, P. (2007).
    The effect of conditioned reinforcement rate on choice: A review.
    Journal of the Experimental Analysis of Behavior, 87, 409–421.


## Experimental Desing
![game caption](https://github.com/mesielepush/Pigeons/blob/master/img/for_readmd.png)

1.- This simulation begins with four possible ![concurrent >](https://en.wikipedia.org/wiki/Reinforcement#Concurrent_schedules) ![variable interval (VI) schedules](https://dictionary.apa.org/variable-interval-schedule), all of wich have a constant mean of 1.5 min per reinforcement, as in the original paper.

* VI(3)----- VI(3)
* VI(2.25)-- VI(4.5)
* VI(1.8)--- VI(9)
* VI(1.5)--- VI(0)

##### However, since a mean of 90 seconds per reinforcement could be too much for humans, there are three alternative options with means of: 60, 45 and 23 seconds. Naturally the proportion between the VIs of each schedule is held constant for all alternatives.

2.- The program selects a schedule at random, and assigns each VI to the left and right keys.

![game caption example](https://github.com/mesielepush/Pigeons/blob/master/img/for_readmd2.png)

3.- During the Session:
* Once the time for next reinforcer has been reach, the second response to that key will be reinforced.
* The programs for each key are independent, an action on one does not produce any change on the other.
* The Session ends when the subject has earn 60 reinforcers.

4.- Hypothesis

#### The relation between absolute rate of responding and the absolute rate of reinforcement is a linear function that passes trough the origin.

That implies a result like this.

[![graph](https://github.com/mesielepush/Pigeons/blob/master/img/matching_graph1.png)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1404074/?page=2)

5.- Outputs.

This simulation saves tha data for each subject as a list with a dictionary for every session.

    session = {
        'total_time' : 0,
        'total_reinf_left' : 0,
        'total_reinf_right': 0,
        'left' : left_VI,
        'right': right_VI,
        'left_click' : [],
        'right_click': [],
        'earn_left' : [],
        'earn_right': []
        }

It also returns trhee plots:
* Ratio of key responses.

![graph](https://github.com/mesielepush/Pigeons/blob/master/img/for_readmd_5.jpg)

* Frequency of response.

![graph](https://github.com/mesielepush/Pigeons/blob/master/img/for_readmd_4.jpg)

* Frequency ratio by reinforcer.

![graph](https://github.com/mesielepush/Pigeons/blob/master/img/for_readmd_3.jpg)

