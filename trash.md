# TRASH

Here is the information, that I'm too greedy too throw it out yet.

medium online assessment involving intersection of polygons
web development including cookies, user authentication, data hashing, security etc.
Minimum number of characters to delete from a string so that each character appears unique number of times. Note: You can delete all occurances of characters.
eg: "aaaabbbb" -> 1 "a" or 1"b" would make "a" and "b" appear unique number of times.
Given number in binary form, if its even -> you can divide it by 2; if its odd -> you can substract 1 from it. You can repeat above steps as many times as you want to reach 0. How many steps it took to reach zero?
CPU task

Take home challenge by Tesla

Question #1
Log Processor Outline: You are developing a log processing  system, which is made up of many different "steps" that process the logs in different ways. Each step is declared in advance, and the system is built up by feeding the output of one step into the inputs of other steps. Each step has a python function (stored in the "action" attribute) that gets evaluated to produce the output for that step. The user interacts with the system by telling the system they want the output of a particular step, and the system will call the action for that step (and any other actions that the desired step depends on) to return the processed log. Each step is given an "output_name" attribute, which the user can use to get the output of that step. The "input_names" attribute stores a list of strings that match the output_name from other steps, so that the output value from one step can be used as an input parameter to other steps. Read further to see examples of the system in action, and begin with Questions 1-4.


QUESTION 1:In example_system_1, the step for "output3" takes inputs from the steps for "output1" and "output2".Thus, if the user requests "output3", we must first evaluate the actions for "output2" and "output1"    to get the values of these outputs, so the values can be used as inputs to the action of "output3".To determine the correct ordering of step dependencies, complete the action_evaluation_order()    function below, so that it will return a list of "output_name"s needed for the "order_for_output_name" parameter.    Each "output_name" item in the list should appear *after* any of its dependencies.    The ordering should not contain any duplicates.You may assume every list of "StepDeclarations" is valid and solvable, eg: - each "StepDeclaration" will only have one output - each "StepDeclaration" can have any number of dependencies (including 0) - a list of StepDeclarations will not contain duplicate "output_name"s - a "StepDeclaration" cannot depend on its own output (directly or indirectly)For this and the following questions, assume in real life the system is running at a large scale, so efficiency is important.That said, correct slow solutions will get more marks than incorrect fast ones.You may also leave notes explaining where you further optimize if you had the time.  


QUESTION 2:Now that we know the order in which the actions have to be evaluated, complete the  get_output_value() function below so that it calls each "action" in  the correct order with the right input(s), and returns the output value of  the "action" function for the StepDeclaration where the output_name attribute  matches the "output_name" parameter.You can use your previous working if desired.for example_system_1, the get_output_value(example_system_1, "output3") function will do the following1) call action_get_logs1(), and store the output2) call action_get_logs2(), and store the output3) call action_combine_logs(), with the output from 1) and 2) as the input4) return the result of 3), as the "value_for_output_name" parameter matches the StepDeclaration.output_name for that step.# note that as in Q1, step 1) and 2) could happen in the reverser order.  


QUESTION 3:We expect the "get_output_value()" function to be called multiple times with varying "step_declarations" and "value_for_output_name"s.As some of the "actions" might be expensive to call, we should cache the output of "action" calls.That way, if an "action" is called multiple times with the same input values, the output value can be reused without recomputing.An "action" function may be re-used multiple in many "StepDeclarations" within one system, or within different systems sharing a cache.Implement get_output_value_with_caching() below to use the global "cache" variable."actions" are pure functions, where the output value of each function only depends on the values of the inputs. Ina real system, some inputs are accessing external data (eg, reading logs off a filesystem) rather than just fixedstrings like the examples given. We can simulate this by having one of the steps that takes no inputs return a variable result. 

QUESTION 4:Another performance upgrade would be to add concurrency/parallelism where possible to increase the performance of the system.One example of this, in example_system_1, is that a single-threaded system will wait for the result of action_get_logs1() before calling action_get_logs2() (or vice versa).However these functions are independent of eachother and could be executed in parallel, speeding up the system.Complete the "get_output_value_with_caching_and_parallelism" below, using concurrency/parallelism anywhere possible to increase the performance of the system.Your selection of parallelization primitive or library does not affect your score (eg, you may use multithreading, multiprocessing, asyncio, etc)You can assume that there is no performance overhead for additional workers(eg, you have unlimited CPUs), and that all action functions are IO-bound.Extra for experts: limit the number of CPU cores you have to N, and assume each action can utilize a fixed number of CPUs from 1 to N. Then schedule parallel actions such that CPU cores are optimally utilized (but not oversaturated). 

Question #2
find shortest path between tesla chargers
https://pathcompression.com/sinya/articles/9


￼

Question
Given a phone number, write an algorithm to print all possible alpha-codes that correspond to it.
Given two classes and an interface, implement the interface.


Given a bunch of redis instance design a service to perform following operations
a) Connection to redis instance
b) access the data within that connection
c) create and update the entry in redis.
d) flush an entry (using time bound constraints)


Some advices:
- ДА вздрогнет FAANG* или [практическое руководство] по поиску работы в США/Европе для айтишника
- Работа не волк, часть 1. Поиск работы: 9 кругов HR-a
- Улучшаем профиль в LinkedIn перед поиском работы
- https://habr.com/ru/post/421595/
- приоткрыл завесу процесса найма на работу
- https://leetcode.com, www.crackingthecodinginterview.com - тренировка

https://app.codility.com
https://www.slideshare.net/emilyjessica893/tesla-motors-interview-questions-and-answers
http://steve-yegge.blogspot.com/2008/03/get-that-job-at-google.html
https://www.geeksforgeeks.org/interview-preparation-for-software-developer/
https://onlinejudge.org
www.programminginterviewprep.com
https://leetcode.com/problemset/top-interview-questions/
$35 https://practice.geeksforgeeks.org/courses/dsa-self-paced?utm_source=geeksforgeeks&utm_medium=article&utm_campaign=gfg_article_dsa_content_bottom

	10 - https://www.youtube.com/watch?v=NdF1QDTRkck

	11 - https://www.youtube.com/watch?v=p-gpaIGRCQI



