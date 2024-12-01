{nixpkgs}: (
  let
    libStrings = nixpkgs.lib.strings;
    libLists = nixpkgs.lib.lists;
    linesWithEmptyStrings = libStrings.splitString "\n" (builtins.readFile ./day-1.txt);
    lines = builtins.filter (line: line != "") linesWithEmptyStrings;
    unsortedLeftStrs = map (line: (builtins.head (builtins.split " " line))) lines;
    unsortedRightStrs = map (line: (libLists.last (builtins.split " " line))) lines;
    sortNums = (xs: builtins.sort builtins.lessThan xs);
    lefts = map libStrings.toInt (sortNums unsortedLeftStrs);
    rights = map libStrings.toInt (sortNums unsortedRightStrs);
    abs = x: if x < 0 then -x else x;
    diffs = libLists.zipListsWith (left: right: abs (left - right)) lefts rights;
    sumList = xs: builtins.foldl' builtins.add 0 xs;
    part2sums = map (left: left * (builtins.length (builtins.filter (right: left == right) rights))) lefts;
  in
    {
        part1 = sumList diffs;
        part2 = sumList part2sums;
    }
)
