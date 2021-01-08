@echo off

set problemname=%1
set testdir=python\test\%problemname%
set baseurl=%problemname:~0,-2%
set baseurlreplaced=%baseurl:_=-%

rem # log in
oj login -u nanjaro -p haruking4503 "https://atcoder.jp/"
oj login --check "https://atcoder.jp/"

rem # make test directory
if not exist %testdir% (
  oj dl -d python/test/%problemname%/ https://atcoder.jp/contests/%baseurlreplaced%/tasks/%problemname%
)

oj test -c "python python/src/%problemname%.py" -d python/test/%problemname%/