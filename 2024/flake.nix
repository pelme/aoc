{
  description = "AoC 2024";
  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs?ref=nixos-unstable";
  };
  outputs = {
    self,
    nixpkgs,
  }: {
    day-1 = (import ./day-1.nix) {inherit nixpkgs;};
  };
}
