# RJ45 (Ethernet) hardware tap

This module is for creating a "tap" for a physical network connection.
A tap is capable of listening to traffic between two points without injecting or broadcasting its own signal.

The RJ45 spec allows a physical circuit to be created which is incapable of sending packets.
These could be useful for snooping, but also for diagnosing network traffic without interfering with it.
There are a number of different ways to create these wires/circuits, each with their own tradeoff.
