CC = gcc

EXEC = write_video
OBJS = $(patsubst %.c,%.o,$(wildcard *.c))

CFLAGS = `pkg-config --cflags opencv`
LIBS = `pkg-config --libs opencv`

.PHONY : all clean init

all : $(EXEC)

%.o : %.c
	$(CC) $(CFLAGS) -o $@ -c $<

$(EXEC) : $(OBJS)
	$(CC) -o $@ $^ $(LIBS)

clean :
	@rm *.o 2> /dev/null

init : clean
	rm $(EXEC) 2> /dev/null

