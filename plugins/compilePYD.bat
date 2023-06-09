@echo off

g++ -shared -o file_man.pyd file_manipulator.cpp -IC:\Users\AsyaSavelieva\python\include -LC:\Users\AsyaSavelieva\python\libs -lpython311
g++ -shared -o dam_lev.pyd dameru_levenstein.cxx -IC:\Users\AsyaSavelieva\python\include -LC:\Users\AsyaSavelieva\python\libs -lpython311