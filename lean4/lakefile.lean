import Lake
open Lake DSL

package «SymplecticKAM» where

@[default_target]
lean_lib «SymplecticKAM» where

require mathlib from git
  "https://github.com/leanprover-community/mathlib4.git"