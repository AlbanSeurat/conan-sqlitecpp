# Try to find SQLiteCpp
# Once done, this will define
#
# SQLiteCpp_FOUND        - system has SQLiteCpp
# SQLiteCpp_INCLUDE_DIRS - SQLiteCpp include directories
# SQLiteCpp_LIBRARIES    - libraries needed to use SQLiteCpp

find_path(
	SQLiteCpp_INCLUDE_DIR
	NAMES SQLiteCpp/SQLiteCpp.h
	PATHS ${CONAN_INCLUDE_DIRS_SQLiteCpp}
)

find_library(
	SQLiteCpp_LIBRARY
	NAMES SQLiteCpp
	PATHS ${CONAN_LIB_DIRS_SQLiteCpp}
)

find_library(
    SQLITE3_LIBRARY
    NAMES sqlite3
    PATHS ${CONAN_LIB_DIRS_SQLiteCpp}
)

set(SQLiteCpp_FOUND TRUE)
set(SQLiteCpp_INCLUDE_DIRS ${SQLiteCpp_INCLUDE_DIR})
set(SQLiteCpp_LIBRARIES ${SQLiteCpp_LIBRARY} ${SQLITE3_LIBRARY})

mark_as_advanced(SQLiteCpp_LIBRARY SQLiteCpp_INCLUDE_DIR SQLITE3_LIBRARY)
