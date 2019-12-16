# Restarting Threads

A simple repo showing an example of how an individual or group of threads can be restarted.
For this implementation the *restart condition* is left ambiguous to be implemented by anyone. Idealy it would be a function
that returns a Bool.

This type of thing has been used before with a condition function that checked the most recent entry in a database, restarting
if the most recent entry was created longer than 10 minutes ago.
