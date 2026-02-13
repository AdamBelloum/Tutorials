
CFLAGS = -fopenmp -O2

# --- Beginner Targets ---
# Get a list of all C files in the beginner directory
SOURCES_BEGINNER = $(wildcard solution_beginner/*.c)

# Define the corresponding executables (without the .c extension and in the CURRENT directory)
TARGETS_BEGINNER = $(patsubst solution_beginner/%.c, %, $(SOURCES_BEGINNER))

# --- Intermediate Targets ---
# Get a list of all C files in the intermediate directory
SOURCES_INTERMEDIATE = $(wildcard solution_intermediate/*.c)

# Define the corresponding executables (without the .c extension and in the CURRENT directory)
TARGETS_INTERMEDIATE = $(patsubst solution_intermediate/%.c, %, $(SOURCES_INTERMEDIATE))

# Combined list of all executable targets
ALL_TARGETS = $(TARGETS_BEGINNER) $(TARGETS_INTERMEDIATE)

.PHONY: all clean

## Compiles all targets
all: $(ALL_TARGETS)

## Compilation Rule for Beginner Files
# Target is the executable name (e.g., 01_hello_par)
# Prerequisites is the source file (e.g., solution_beginner/01_hello_par.c)
$(TARGETS_BEGINNER): %: solution_beginner/%.c
	$(CC) $(CFLAGS) $< -o $@

## Compilation Rule for Intermediate Files
# Target is the executable name
# Prerequisites is the source file
$(TARGETS_INTERMEDIATE): %: solution_intermediate/%.c
	$(CC) $(CFLAGS) $< -o $@

## Cleans all executable targets
clean:
	rm -f $(ALL_TARGETS)

