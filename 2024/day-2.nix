{ nixpkgs, file }:
let
  pipe = nixpkgs.lib.trivial.pipe;
  trim = nixpkgs.lib.strings.trim;
  readFile = builtins.readFile;
  splitString = nixpkgs.lib.strings.splitString;
  toInt = nixpkgs.lib.strings.toInt;
  head = builtins.head;
  tail = builtins.tail;
  length = builtins.length;
  concatLists = builtins.concatLists;
  filter = builtins.filter;
  sort = builtins.sort;
  all = builtins.all;

  isSortedBy = cmp: line: (sort cmp line) == line;
  isIncrOrDecr = line: (isSortedBy (x: y: x < y) line || isSortedBy (x: y: x > y) line);
  abs = x: if x > 0 then x else -x;
  isGoodDiff =
    pair:
    let
      diff = (abs ((head pair) - (head (tail pair))));
    in
    diff > 0 && diff <= 3;

  pairs =
    xs:
    (
      if (length xs) < 2 then
        [ ]
      else
        (concatLists [
          [
            [
              (head xs)
              (head (tail xs))
            ]
          ]
          (pairs (tail xs))
        ])
    );
in
(pipe file [
  readFile
  trim
  (splitString "\n")
  (map (line: map toInt (splitString " " line)))
  (filter isIncrOrDecr)
  (map pairs)
  (filter (all isGoodDiff))
  length
])
