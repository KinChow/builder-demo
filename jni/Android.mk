LOCAL_PATH := $(call my-dir)

include $(CLEAR_VARS)

# 定义模块名称
LOCAL_MODULE := example

# 添加源文件
LOCAL_SRC_FILES := hello_world.cpp

LOCAL_LDLIBS := -lc++_shared

include $(BUILD_EXECUTABLE)
