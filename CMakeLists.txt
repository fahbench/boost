add_library(boost INTERFACE)
target_include_directories(boost
	INTERFACE
	.
	)
target_compile_definitions(boost
	INTERFACE
	BOOST_ALL_NO_LIB # Disable "autolink" on msvs
	)


file(GLOB SOURCE_FILES
	libs/system/src/*.cpp
	)
add_library(boost-system ${SOURCE_FILES})
target_link_libraries(boost-system boost)
set_property(TARGET boost-system PROPERTY POSITION_INDEPENDENT_CODE ON)


file(GLOB SOURCE_FILES
	libs/filesystem/src/*.cpp
	)
add_library(boost-filesystem ${SOURCE_FILES})
target_link_libraries(boost-filesystem boost boost-system)
set_property(TARGET boost-filesystem PROPERTY POSITION_INDEPENDENT_CODE ON)

file(GLOB SOURCE_FILES
	libs/program_options/src/*.cpp
	)
add_library(boost-program_options ${SOURCE_FILES})
target_link_libraries(boost-program_options boost)
set_property(TARGET boost-program_options PROPERTY POSITION_INDEPENDENT_CODE ON)
