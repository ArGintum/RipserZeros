# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.12

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/local/lib/python2.7/dist-packages/cmake/data/bin/cmake

# The command to remove a file.
RM = /usr/local/lib/python2.7/dist-packages/cmake/data/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = "/content/drive/My Drive/Хлам/1/RipserZeros/ripserplusplus"

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = "/content/drive/My Drive/Хлам/1/RipserZeros/ripserplusplus/build"

# Utility rule file for tests.

# Include the progress variables for this target.
include CMakeFiles/tests.dir/progress.make

CMakeFiles/tests: functional_tests


functional_tests:
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold --progress-dir="/content/drive/My Drive/Хлам/1/RipserZeros/ripserplusplus/build/CMakeFiles" --progress-num=$(CMAKE_PROGRESS_1) "Generating functional_tests"
	/bin/sh /content/drive/My\ Drive/Хлам/1/RipserZeros/ripserplusplus/testing/tests.sh

tests: CMakeFiles/tests
tests: functional_tests
tests: CMakeFiles/tests.dir/build.make

.PHONY : tests

# Rule to build all files generated by this target.
CMakeFiles/tests.dir/build: tests

.PHONY : CMakeFiles/tests.dir/build

CMakeFiles/tests.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/tests.dir/cmake_clean.cmake
.PHONY : CMakeFiles/tests.dir/clean

CMakeFiles/tests.dir/depend:
	cd "/content/drive/My Drive/Хлам/1/RipserZeros/ripserplusplus/build" && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" "/content/drive/My Drive/Хлам/1/RipserZeros/ripserplusplus" "/content/drive/My Drive/Хлам/1/RipserZeros/ripserplusplus" "/content/drive/My Drive/Хлам/1/RipserZeros/ripserplusplus/build" "/content/drive/My Drive/Хлам/1/RipserZeros/ripserplusplus/build" "/content/drive/My Drive/Хлам/1/RipserZeros/ripserplusplus/build/CMakeFiles/tests.dir/DependInfo.cmake" --color=$(COLOR)
.PHONY : CMakeFiles/tests.dir/depend
