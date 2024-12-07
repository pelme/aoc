{
  description = "AoC 2024";
  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs?ref=nixos-unstable";
  };
  outputs =
    {
      self,
      nixpkgs,
    }:
    {
      day-1 = (import ./day-1.nix) { inherit nixpkgs; };
      day-2 = (import ./day-2.nix) {
        inherit nixpkgs;
        file = ./day-2.txt;
      };
      day-2-example = (import ./day-2.nix) {
        inherit nixpkgs;
        file = ./day-2-example.txt;
      };
      day-3 = (import ./day-3.nix) {
        inherit nixpkgs;
        file = ./day-3.txt;
      };
      day-3-part2 = (import ./day-3-part2.nix) {
        inherit nixpkgs;
        file = ./day-3.txt;
      };
      day-7 = (import ./day-7.nix) {
        inherit nixpkgs;
        file = ./day-7.txt;
      };
      day-7-example = (import ./day-7.nix) {
        inherit nixpkgs;
        file = ./day-7-example.txt;
      };

    };
}
