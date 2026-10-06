set UnixPath to POSIX path of (path to me)
set JdkPath to UnixPath & "Contents/Resources/jdk/Contents/Home/bin"
set GhidraRun to UnixPath & "Contents/Resources/ghidra/ghidraRun"
set SupportPath to POSIX path of (path to application support from user domain) & "Ghidra"
do shell script "mkdir -p " & quoted form of SupportPath & "; cd " & quoted form of SupportPath & "; export PATH=" & quoted form of JdkPath & ":$PATH; exec " & quoted form of GhidraRun
