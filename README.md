### Otus python basic course homework (Ivan Lysogor)
#### Homework 1
Code output
```
Executing function list power with following argc ([1, 2, 3, 4, 5], 2)
[1, 4, 9, 16, 25]

Execuring function select numbers with following argc ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3)
Function select_numbers execution time is 0.0000069141
[1, 2, 3, 5, 7]

Execuring function select numbers with following argc ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 1)
Function select_numbers execution time is 0.0000028610
[2, 4, 6, 8, 10]

Execuring function select numbers with following argc ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 2)
Function select_numbers execution time is 0.0000030994
[1, 3, 5, 7, 9]

Executing function fib to get Fibonacchi numbers with following argc (50,)
--->fib_loop(0)
-------->fib_loop(1)
------------->fib_loop(2)
------------------>fib_loop(3)
----------------------->fib_loop(4)
---------------------------->fib_loop(5)
--------------------------------->fib_loop(6)
<---------------------------------fib_loop(6)
<----------------------------fib_loop(5)
<-----------------------fib_loop(4)
<------------------fib_loop(3)
<-------------fib_loop(2)
<--------fib_loop(1)
<---fib_loop(0)
[1, 2, 3, 5, 8, 13, 21, 34]
```

#### Homework 2
Code output
```
Please check debug output at hw2.log

This is a car object with the following attributes:
{capacity : '500', weight : '2000', number_of_wheels : '4', engine : 'number_of_cylinders=4 engine_type=<EngineTypeEnum.gazoline: 'gazoline'> engine_capacity=2000'}
Car Beeeeeep
Car engine started
Car engine stopped

This is a boat object with the following attributes:
{capacity : '500', weight : '2500', number_of_passengers : '2', }
Boat doesn't have a signal
Boat doesn't have an engine
Boat doesn't have an engine

This is a wherry object with the following attributes:
{capacity : '50000', weight : '60000', number_of_passengers : '4', engine : 'number_of_cylinders=12 engine_type=<EngineTypeEnum.diesel: 'diesel'> engine_capacity=20000'}
Wherry Tuuuuuu-Tuuuuu
Wherry engine started
Wherry engine stopped
Setting fuel to 0 and trying to start engine.
Exception - ("Vehicle doesn't have enough fuel. Current fuel level - 0",)

2021-01-05 00:04:24,970 - hw2 - DEBUG - Car method with name __init__ at <function Car.__init__ at 0x10777bf70> invoked
2021-01-05 00:04:24,970 - hw2 - DEBUG - Car method with name init_engine at <function MixinEngine.init_engine at 0x1078174c0> invoked
2021-01-05 00:04:24,971 - hw2 - DEBUG - Car method with name fuel at <function MixinEngine.fuel at 0x1082c3af0> invoked
2021-01-05 00:04:24,971 - hw2 - DEBUG - Car method with name __init__ at <function Carriage.__init__ at 0x10780f8b0> invoked
2021-01-05 00:04:24,971 - hw2 - DEBUG - Car method with name __init__ at <function Vehicle.__init__ at 0x10780f940> invoked
2021-01-05 00:04:24,971 - hw2 - DEBUG - Car method with name weight at <function Vehicle.weight at 0x10780ff70> invoked
2021-01-05 00:04:24,971 - hw2 - DEBUG - Car method with name capacity at <function Vehicle.capacity at 0x10780fd30> invoked
2021-01-05 00:04:24,971 - hw2 - DEBUG - Car method with name __str__ at <function Car.__str__ at 0x1082c3ca0> invoked
2021-01-05 00:04:24,971 - hw2 - DEBUG - Car method with name capacity at <function Vehicle.capacity at 0x10780fc10> invoked
2021-01-05 00:04:24,971 - hw2 - DEBUG - Car method with name weight at <function Vehicle.weight at 0x10780fe50> invoked
2021-01-05 00:04:24,971 - hw2 - DEBUG - Car method with name make_beep at <function Car.make_beep at 0x1082c3dc0> invoked
2021-01-05 00:04:24,971 - hw2 - DEBUG - Car method with name start at <function MixinEngine.start at 0x108200ca0> invoked
2021-01-05 00:04:24,971 - hw2 - DEBUG - Car method with name stop at <function MixinEngine.stop at 0x1082c38b0> invoked
2021-01-05 00:04:24,971 - hw2 - DEBUG - Boat method with name __init__ at <function Boat.__init__ at 0x1082c6040> invoked
2021-01-05 00:04:24,971 - hw2 - DEBUG - Boat method with name __init__ at <function Vehicle.__init__ at 0x10780f940> invoked
2021-01-05 00:04:24,971 - hw2 - DEBUG - Boat method with name weight at <function Vehicle.weight at 0x10780ff70> invoked
2021-01-05 00:04:24,972 - hw2 - DEBUG - Boat method with name capacity at <function Vehicle.capacity at 0x10780fd30> invoked
2021-01-05 00:04:24,972 - hw2 - DEBUG - Boat method with name __str__ at <function Boat.__str__ at 0x1082c6160> invoked
2021-01-05 00:04:24,972 - hw2 - DEBUG - Boat method with name capacity at <function Vehicle.capacity at 0x10780fc10> invoked
2021-01-05 00:04:24,972 - hw2 - DEBUG - Boat method with name weight at <function Vehicle.weight at 0x10780fe50> invoked
2021-01-05 00:04:24,972 - hw2 - DEBUG - Boat method with name make_beep at <function Boat.make_beep at 0x1082c6280> invoked
2021-01-05 00:04:24,972 - hw2 - DEBUG - Boat method with name start at <function Boat.start at 0x1082c63a0> invoked
2021-01-05 00:04:24,972 - hw2 - DEBUG - Boat method with name stop at <function Boat.stop at 0x1082c64c0> invoked
2021-01-05 00:04:24,972 - hw2 - DEBUG - Wherry method with name __init__ at <function Wherry.__init__ at 0x1082c3f70> invoked
2021-01-05 00:04:24,972 - hw2 - DEBUG - Wherry method with name init_engine at <function MixinEngine.init_engine at 0x1078174c0> invoked
2021-01-05 00:04:24,972 - hw2 - DEBUG - Wherry method with name fuel at <function MixinEngine.fuel at 0x1082c3af0> invoked
2021-01-05 00:04:24,972 - hw2 - DEBUG - Wherry method with name __init__ at <function Boat.__init__ at 0x1082c6040> invoked
2021-01-05 00:04:24,972 - hw2 - DEBUG - Wherry method with name __init__ at <function Vehicle.__init__ at 0x10780f940> invoked
2021-01-05 00:04:24,972 - hw2 - DEBUG - Wherry method with name weight at <function Vehicle.weight at 0x10780ff70> invoked
2021-01-05 00:04:24,973 - hw2 - DEBUG - Wherry method with name capacity at <function Vehicle.capacity at 0x10780fd30> invoked
2021-01-05 00:04:24,973 - hw2 - DEBUG - Wherry method with name __str__ at <function Wherry.__str__ at 0x1082c6670> invoked
2021-01-05 00:04:24,973 - hw2 - DEBUG - Wherry method with name capacity at <function Vehicle.capacity at 0x10780fc10> invoked
2021-01-05 00:04:24,973 - hw2 - DEBUG - Wherry method with name weight at <function Vehicle.weight at 0x10780fe50> invoked
2021-01-05 00:04:24,973 - hw2 - DEBUG - Wherry method with name make_beep at <function Wherry.make_beep at 0x1082c6790> invoked
2021-01-05 00:04:24,973 - hw2 - DEBUG - Wherry method with name start at <function MixinEngine.start at 0x108200ca0> invoked
2021-01-05 00:04:24,973 - hw2 - DEBUG - Wherry method with name stop at <function MixinEngine.stop at 0x1082c38b0> invoked
2021-01-05 00:04:24,973 - hw2 - DEBUG - Wherry method with name fuel at <function MixinEngine.fuel at 0x1082c3af0> invoked


Process finished with exit code 0
```

#### Homework 3 (Async work with DB)

```
2021-04-20 00:19:48,618 INFO sqlalchemy.engine.Engine select version()
2021-04-20 00:19:48,618 INFO sqlalchemy.engine.Engine [raw sql] ()
2021-04-20 00:19:48,625 INFO sqlalchemy.engine.Engine select current_schema()
2021-04-20 00:19:48,625 INFO sqlalchemy.engine.Engine [raw sql] ()
2021-04-20 00:19:48,631 INFO sqlalchemy.engine.Engine show standard_conforming_strings
2021-04-20 00:19:48,631 INFO sqlalchemy.engine.Engine [raw sql] ()
2021-04-20 00:19:48,635 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2021-04-20 00:19:48,636 INFO sqlalchemy.engine.Engine select relname from pg_class c join pg_namespace n on n.oid=c.relnamespace where pg_catalog.pg_table_is_visible(c.oid) and relname=%s
2021-04-20 00:19:48,636 INFO sqlalchemy.engine.Engine [generated in 0.00013s] ('posts',)
2021-04-20 00:19:48,641 INFO sqlalchemy.engine.Engine select relname from pg_class c join pg_namespace n on n.oid=c.relnamespace where pg_catalog.pg_table_is_visible(c.oid) and relname=%s
2021-04-20 00:19:48,641 INFO sqlalchemy.engine.Engine [cached since 0.005106s ago] ('comments',)
2021-04-20 00:19:48,643 INFO sqlalchemy.engine.Engine select relname from pg_class c join pg_namespace n on n.oid=c.relnamespace where pg_catalog.pg_table_is_visible(c.oid) and relname=%s
2021-04-20 00:19:48,643 INFO sqlalchemy.engine.Engine [cached since 0.00707s ago] ('posts',)
2021-04-20 00:19:48,645 INFO sqlalchemy.engine.Engine select relname from pg_class c join pg_namespace n on n.oid=c.relnamespace where pg_catalog.pg_table_is_visible(c.oid) and relname=%s
2021-04-20 00:19:48,645 INFO sqlalchemy.engine.Engine [cached since 0.009195s ago] ('comments',)
2021-04-20 00:19:48,648 INFO sqlalchemy.engine.Engine 
CREATE TABLE posts (
	id SERIAL NOT NULL, 
	data VARCHAR, 
	create_date TIMESTAMP WITHOUT TIME ZONE DEFAULT now(), 
	PRIMARY KEY (id)
)


2021-04-20 00:19:48,649 INFO sqlalchemy.engine.Engine [no key 0.00011s] ()
2021-04-20 00:19:48,660 INFO sqlalchemy.engine.Engine 
CREATE TABLE comments (
	id SERIAL NOT NULL, 
	post_id INTEGER, 
	data VARCHAR, 
	PRIMARY KEY (id), 
	FOREIGN KEY(post_id) REFERENCES posts (id)
)


2021-04-20 00:19:48,660 INFO sqlalchemy.engine.Engine [no key 0.00011s] ()
2021-04-20 00:19:48,670 INFO sqlalchemy.engine.Engine COMMIT
2021-04-20 00:19:49,444 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2021-04-20 00:19:49,445 INFO sqlalchemy.engine.Engine INSERT INTO posts (id, data) VALUES (%s, %s) RETURNING posts.create_date
2021-04-20 00:19:49,445 INFO sqlalchemy.engine.Engine [generated in 0.00017s] (1, 'Post 1')
2021-04-20 00:19:49,451 INFO sqlalchemy.engine.Engine INSERT INTO posts (id, data) VALUES (%s, %s) RETURNING posts.create_date
2021-04-20 00:19:49,451 INFO sqlalchemy.engine.Engine [cached since 0.006544s ago] (2, 'Post 2')
2021-04-20 00:19:49,453 INFO sqlalchemy.engine.Engine INSERT INTO posts (id, data) VALUES (%s, %s) RETURNING posts.create_date
2021-04-20 00:19:49,454 INFO sqlalchemy.engine.Engine [cached since 0.008923s ago] (3, 'Post 3')
2021-04-20 00:19:49,456 INFO sqlalchemy.engine.Engine INSERT INTO comments (id, post_id, data) VALUES (%s, %s, %s)
2021-04-20 00:19:49,456 INFO sqlalchemy.engine.Engine [generated in 0.00019s] ((1, 1, 'some comment'), (2, 1, 'some comment'))
2021-04-20 00:19:49,462 INFO sqlalchemy.engine.Engine COMMIT

```

