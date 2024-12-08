{ nixpkgs, file }:
with builtins;
with nixpkgs.lib.trivial;
with nixpkgs.lib.strings;
with nixpkgs.lib.lists;
let
  pow = (base: exp: if exp == 0 then 1 else base * (pow base (exp - 1)));
  modulo =
    a: b:
    let
      quotient = div a b;
      multiple = b * quotient;
    in
    a - multiple;
  shiftRight = n: steps: div n (pow 3 steps);
  concat = a: b: toInt "${toString b}${toString a}";
  makeOps =
    numOps: n:
    genList (
      idx:
      let
        x = modulo (shiftRight n idx) 3;
      in
      if x == 0 then
        add
      else if x == 1 then
        mul
      else if x == 2 then
        concat
      else
        throw "bad ${x}"
    ) numOps;
  makeAllOps = numOps: genList (makeOps numOps) ((pow 3 numOps));
  # cache the calls to makeAllOps to improve speed
  allOps = listToAttrs (
    (genList (n: {
      name = "${toString n}";
      value = makeAllOps n;
    }) 12)
  );
  calculate =
    nums: ops:
    if length nums == 1 then
      (head nums)
    else
      ((head ops) (head nums) (calculate (tail nums) (tail ops)));
  isValid =
    testValue: numbers:
    (any (ops: (calculate numbers ops) == testValue) (allOps."${toString ((length numbers) - 1)}"));
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
