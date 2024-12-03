{ nixpkgs, file }:
let
  b = builtins;
  s = nixpkgs.lib.strings;
  t = nixpkgs.lib.trivial;
in
t.pipe (b.readFile file) [
  (b.split "mul\\(([0-9]{1,3}),([0-9]{1,3})\\)")
  (b.filter b.isList)
  (map (map s.toInt))
  (map (b.foldl' b.mul 1))
  (b.foldl' b.add 0)
]
