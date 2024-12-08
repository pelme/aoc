{ nixpkgs, file }:
with builtins;
with nixpkgs.lib.trivial;
with nixpkgs.lib.strings;
with nixpkgs.lib.lists;
let
  shiftRight = n: steps: div n (pow 2 steps);
  pow = (base: exp: if exp == 0 then 1 else base * (pow base (exp - 1)));
  makeOps =
    numOps: n: builtins.genList (idx: if (bitAnd (shiftRight n idx) 1) == 0 then add else mul) numOps;
  makeAllOps = numOps: builtins.genList (makeOps numOps) ((pow 2 numOps));
  calculate =
    nums: ops:
    if length nums == 1 then
      (head nums)
    else
      ((head ops) (head nums) (calculate (tail nums) (tail ops)));
  isValid =
    testValue: numbers:
    (any (ops: (calculate numbers ops) == testValue) (makeAllOps ((length numbers) - 1)));
in
pipe file [
  builtins.readFile
  trim
  (splitString "\n")
  (map (splitString ": "))
  (map (x: [
    (toInt (head x))
    (map toInt (splitString " " (head (tail x))))
  ]))
  (filter (line: isValid (head line) (reverseList (head (tail line)))))
  (map head)
  (foldl' add 0)
]
