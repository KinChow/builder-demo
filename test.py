from builder import Builder, BuilderType, BuilderFactory

if __name__ == "__main__":
    test_cases = [
        # [BuilderType.NDK, "ndk_build", "D://android-ndk-r27c-windows//android-ndk-r27c//"],
        # [BuilderType.CMAKE_ANDROID, "android_build", "D://android-ndk-r27c-windows//android-ndk-r27c//"],
        [BuilderType.CMAKE_WINDOWS_VS_MSVC, "windows_msvc_build", ""],
        # [BuilderType.CMAKE_WINDOWS_MINGW, "windows_mingw_build", "D:\\Program Files\\x86_64-14.2.0-release-win32-seh-msvcrt-rt_v12-rev0\\mingw64\\bin\\"],
        # [BuilderType.CMAKE_CLANG, "windows_clang_msvc_build", "d:\\Program Files\\LLVM\\bin\\"],
    ]
    for test_case in test_cases:
        builder = BuilderFactory.create(test_case[0], test_case[1])
        builder.clean()
        print("Clean finished")
        input()
        builder.build(test_case[2])
        print("Build finished")
        input()
        builder.clean()
        print("Clean finished")
        input()
