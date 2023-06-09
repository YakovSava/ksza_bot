g++ -shared -o file_man.pyd file_manipulator.cpp \
-I/usr/bin/python/include \
-L/usr/bin/python/lib \
-lpython311

g++ -shared -o dam_lev.pyd dameru_levenstein.cxx \
-I/usr/bin/python/include \
-L/usr/bin/python/lib \
-lpython311
