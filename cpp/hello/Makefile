CC = g++
EXEC = hello
OBJS = $(patsubst %.cc,%.o,$(wildcard *.cc))

CFLAGS = 
LIBS = 

.PHONY : all clean init

all : $(EXEC)

%.o : %.cc
	$(CC) $(CFLAGS) -o $@ -c $<

$(EXEC) : $(OBJS)
	$(CC) -o $@ $^ $(LIBS)

clean :
	rm *.o

init : clean
	rm $(EXEC)
