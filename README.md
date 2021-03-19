# madness
tournament simulator / bracket generator.
picks winners using simple seed-weighted probability.

usage: `./madness.py [-h] [-q] JSON`  *ex:* `./madness.py ../data/2021/womens.json`

sample output:
```
* Alamo *

(1)Stanford  |  
--------------------------------------------------------------------------------
(1)Stanford  |  (2)Louisville  |  
--------------------------------------------------------------------------------
(1)Stanford  |  (12)UC Davis  |  (6)Oregon  |  (2)Louisville  |  
--------------------------------------------------------------------------------
(1)Stanford  |  (9)Wake Forest  |  (12)UC Davis  |  (4)Arkansas  |  (6)Oregon  |  (3)Georgia  |  (10)UCF  |  (2)Louisville  |  
--------------------------------------------------------------------------------
(1)Stanford  |  (16)Utah Valley  |  (8)Oklahoma St.  |  (9)Wake Forest  |  (5)Missouri St.  |  (12)UC Davis  |  (4)Arkansas  |  (13)Wright St.  |  (6)Oregon  |  (11)South Dakota  |  (3)Georgia  |  (14)Drexel  |  (7)Northwestern  |  (10)UCF  |  (2)Louisville  |  (15)Marist  |  
--------------------------------------------------------------------------------

* Hemisfair *

(3)UCLA  |  
--------------------------------------------------------------------------------
(1)South Carolina  |  (3)UCLA  |  
--------------------------------------------------------------------------------
(1)South Carolina  |  (5)Georgia Tech  |  (3)UCLA  |  (10)North Carolina  |  
--------------------------------------------------------------------------------
(1)South Carolina  |  (9)Florida St.  |  (5)Georgia Tech  |  (4)West Virginia  |  (6)Texas  |  (3)UCLA  |  (10)North Carolina  |  (15)Mount St. Mary's  |  
--------------------------------------------------------------------------------
(1)South Carolina  |  (16)Mercer  |  (8)Oregon St.  |  (9)Florida St.  |  (5)Georgia Tech  |  (12)SFA  |  (4)West Virginia  |  (13)Lehigh  |  (6)Texas  |  (11)Bradley  |  (3)UCLA  |  (14)Wyoming  |  (7)Alabama  |  (10)North Carolina  |  (2)Maryland  |  (15)Mount St. Mary's  |  
--------------------------------------------------------------------------------

* River Walk *

(1)UConn  |  
--------------------------------------------------------------------------------
(1)UConn  |  (6)Michigan  |  
--------------------------------------------------------------------------------
(1)UConn  |  (4)Kentucky  |  (6)Michigan  |  (7)Virginia Tech  |  
--------------------------------------------------------------------------------
(1)UConn  |  (8)Syracuse  |  (12)Central Mich.  |  (4)Kentucky  |  (6)Michigan  |  (3)Tennessee  |  (7)Virginia Tech  |  (2)Baylor  |  
--------------------------------------------------------------------------------
(1)UConn  |  (16)High Point  |  (8)Syracuse  |  (9)South Dakota St.  |  (5)Iowa  |  (12)Central Mich.  |  (4)Kentucky  |  (13)Idaho St.  |  (6)Michigan  |  (11)FGCU  |  (3)Tennessee  |  (14)Middle Tenn.  |  (7)Virginia Tech  |  (10)Marquette  |  (2)Baylor  |  (15)Jackson St.  |  
--------------------------------------------------------------------------------

* Mercado *

(2)Texas A&M  |  
--------------------------------------------------------------------------------
(1)NC State  |  (2)Texas A&M  |  
--------------------------------------------------------------------------------
(1)NC State  |  (4)Indiana  |  (3)Arizona  |  (2)Texas A&M  |  
--------------------------------------------------------------------------------
(1)NC State  |  (8)South Fla.  |  (12)Belmont  |  (4)Indiana  |  (6)Rutgers  |  (3)Arizona  |  (7)Iowa St.  |  (2)Texas A&M  |  
--------------------------------------------------------------------------------
(1)NC State  |  (16)N.C. A&T  |  (8)South Fla.  |  (9)Washington St.  |  (5)Gonzaga  |  (12)Belmont  |  (4)Indiana  |  (13)VCU  |  (6)Rutgers  |  (11)BYU  |  (3)Arizona  |  (14)Stony Brook  |  (7)Iowa St.  |  (10)Michigan St.  |  (2)Texas A&M  |  (15)Troy  |  
--------------------------------------------------------------------------------

* Finals *

(1)UConn  |  
--------------------------------------------------------------------------------
(1)Stanford  |  (1)UConn  |  
--------------------------------------------------------------------------------
(1)Stanford  |  (3)UCLA  |  (1)UConn  |  (2)Texas A&M  |  
--------------------------------------------------------------------------------
Winner: (1)UConn
```


### to do
* infer initial ordering from seed numbers
* support more winner picking strategies
* prettify output
