{ nixpkgs, file }:
let
  input = s.trim (b.readFile file);
  b = builtins;
  s = nixpkgs.lib.strings;

  rawLines = s.splitString "\n" input;
  parseLine = line: map s.toInt (s.splitString " " line);
  lines = map parseLine rawLines;
  isSortedBy = cmp: line: (b.sort cmp line) == line;
  isIncrOrDecr = line: (isSortedBy (x: y: x < y) line || isSortedBy (x: y: x > y) line);
in
{
  # part1 = input;
  # out = map parseLine rawLines;
  out = lines;
  goodie = map isIncrOrDecr lines;
}
