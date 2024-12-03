{ nixpkgs, file }:
let
  b = builtins;
  s = nixpkgs.lib.strings;
  t = nixpkgs.lib.trivial;
  calculate = (
    enabled: list:
    let
      h = b.head list;
      t = b.tail list;
    in
    if list == [ ] then
      0
    else if h == true then
      calculate true t
    else if h == false then
      calculate false t
    else if enabled then
      h + (calculate enabled t)
    else
      calculate enabled t
  );
in
t.pipe (b.readFile file) [
  (b.split "(do\\(\\))|(don't\\(\\))|mul\\(([0-9]{1,3}),([0-9]{1,3})\\)")
  (b.filter b.isList)
  (map (b.filter (x: x != null)))
  (map (
    x:
    if b.head x == "do()" then
      true
    else if b.head x == "don't()" then
      false
    else
      b.foldl' b.mul 1 (map s.toInt x)
  ))
  (calculate true)
]
