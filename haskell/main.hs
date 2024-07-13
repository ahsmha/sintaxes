-- haskell
{-
    purely functional pl
    famous for its monads and typesystem
-}

-- ---------------------------------
-- primitive datatypes and operators
-- numbers
3
-- and maths
1+1 -- 1
8-1 -- 7
1*1 -- 1
1/1 -- 1.0
5 `mod` 3 == 2
5 `rem` 3 == 2

5 `mod` (-3) == -1
5 `rem` (-3) == 2

(-5) `mod` 3 == 1 -- towards negative infinity
(-5) `rem` 3 == -2 -- towards zero

(-5) `mod` (-3) == -2
(-5) `rem` (-3) == -2
-- mod uses div - which is towards negative infinity
-- rem uses quot - which is towards zero

-- division is not integer division by default
1/2 -- 0.5
-- integer division
1 `div` 2 -- 0

-- boolean values
True
False

-- boolean operators
True && False
True || False
not True -- not is a function that takes one value and returns a boolean
1 == 1 -- true
1 /= 1 -- false
1 < 10 -- true

-- no need of parenthesis for function calls
-- all args are just listed after function
-- general pattern: 
-- func arg1 arg2 arg3
--

-- strings and characters
" this is a string "
'a' -- character
-- can't use single quotes for strings
--
-- string concatenation
"hello  " ++ "world"
-- string is a list of characters
['w', 'o', 'r', 'l', 'd']   -- "world"
-- string length
length "hello world" -- 11
-- string indexing
"hello world" !! 6 -- 'w'

-- ---------------------------------
-- lists and tuples
[1, 2, 3] -- [1, 2, 3]
[1..3] -- [1, 2, 3]
-- ranges
['A'..'F'] -- "ABCDEF"
-- list concatenation
[1, 2, 3] ++ [4, 5, 6] -- [1, 2, 3, 4, 5, 6]
-- list indexing
[1, 2, 3] !! 1 -- 2
-- can create a step in a range
[0,2..10] -- [0,2,4,6,8,10]
-- reverse
[5..1] -- []
[5,4..1] -- [5,4,3,2,1]
-- infinte lists in haskell
[1..] -- all natural numbers
-- infinite lists work because haskell has
-- lazy evaluation
-- lazy evaluation means that the list is not computed
-- until it is needed
-- more list ops
head [1..5] -- 1
tail [1..5] -- [2, 3, 4, 5]
init [1..5] -- [1, 2, 3, 4]
last [1..5] -- 5
-- list comprehensions
[x*2 | x <- [1..5]] -- [2, 4, 6, 8, 10]
-- with conditional
[x*2 | x <- [1..5], x*2 > 4] -- [6, 8, 10]
-- every eleemnt in a tuple can be a different
-- type, but a tuple has a fixed length
-- a tuple:
("haskell", 1)
-- accessing elements of a pair (tupel len 2)
fst ("haskell", 1) -- "haskell"
snd ("haskell", 1) -- 1
-- fst, snd only owwrk on tupel len 2
-- tuple length
length ("haskell", 1) -- 2
-- list of tuples
zip [1, 2, 3] ["haskell", "is", "great"] -- [(1, "haskell"), (2, "is"), (3, "great")]

-------------------------------------
    -- functions

-- add two numbers
add :: Int -> Int -> Int
add x y = x + y
-- note if using ghci (haskell interpreter)
-- will need to use `let` i.e, 
-- let add x y = x + y
-- using function
add 2 3 -- 5
-- function with multiple arguments
add3 :: Int -> Int -> Int -> Int
add3 x y z = x + y + z
add3 1 2 3 -- 6
-- alternatively
1 `add` 2 -- 3
-- can also define functions that have no
-- letters.
-- this lets you define own operators!
(//) a b = a `div` b
1 // 3 -- 0
--
-- guards - easy way to do branching in functions
fib x
    | x < 2 = 1
    | otherwise = fib (x-1) + fib (x-2)
-- pattern matching on tuples
sndOfTriple (_, y, _) = y 
-- y -- use a wildcard (_) to bypass naming unused value
-- pattern matching on lists. here `x` is first element
-- in the list and `xs` is thre 
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
-- --------------------------------
-- type signatures
-- haskell has a very strong type system
-- every valid expression has a type
--
-- some basic types:
5 :: Integer
"hello" :: String
True :: Bool
True :: Bool
-- functions have types too
-- `not` takes a boolean and returns a bool:
-- not :: Bool -> Bool
--
-- add function
add :: Integer -> Integer -> Integer
add x y = x + y

----------------------------------------
-- control flows
--
-- if expressions
haskell = if 1 == 1 then "awesome" else "awful"
-- haskell == "awesome"
--
-- if - expressions can be on multiple lines too,
-- indentation is important
haskell = if 1 == 1
             then "awesome"
             else "awful"
-- case expressions: example parsing cmd line args
case args of
  "help" -> printHelp
  "start" -> startProgram
  _ -> putStrLn "unknown command"

-- haskell doesn't have loops
-- uses recursion instead
-- map applies a function over every element in a 
-- list
map (+1) [1..3] -- [2, 3, 4]
-- you can make a for function using map
for array func = map func array

-- and then use it
for [0..5] $ \i -> show i
-- another way of writing the same thing
for [0..5] show

-- you can use foldl or foldr to reduce a list
-- foldl <fn> <initialValue> <list>
foldl (\x y -> 2*x + y) 4 [1,2,3] -- 43
-- same as
(2 * 
    (2 * 
        (2 * 4 + 1) 
    + 2) 
+ 3)

-- foldl is left handed
-- foldr is right handed
foldr (\x y -> 2*x + y) 4 [1,2,3] -- 16 
-- same as 
(2 * 1 + 
    (2 * 2 + 
        (2 * 3 + 4)
    )
)

--
-- ----------------------------------------
-- data types
--
-- declared with a 'type constructor' on left
-- and one or more 'data constructors' on right
-- separated by pipe symbol.
--
-- essentailly an enum
data Color = Red | Green | Blue
-- Red, Green, Blue are functions (possibly nullary)
-- which create object of type named by type constructor i.e, color
-- now you can use it in a function
say :: Color -> String
say Red = "you're red"
say Green = "you're green"
say Blue = "you're blue"

-- -------------------------------------------
-- type classes
-- one way haskell does polymorphism
-- similar to interfaces in other langs
--
-- typeclass defines a set of functions
-- that must work on any type that is in that 
-- typeclass
--
-- the Eq typeclass is for types whose instances
-- can be compared for equality
--
class Eq a where
    (==) :: a -> a -> Bool
    (/=) :: a -> a -> Bool
    x == y = not (x /= y)
    x /= y = not (x == y)

-- this defines a typeclass that requires two 
-- functions (==) and (/=)
-- 
-- creating instance of this class
instance Eq Ball where
    Red == Red = True
    Green == Green = True
    Blue == Blue = True
    _ == _ = False
-- following won't work
-- instance Eq Ball where
--     Color == Color = True
--     _ == _ = False
-- you cannot create an instance definition
-- for a type synonym
--
-- now we can use (==) and (/=) with Ball objects
isRedBall :: Ball -> Bool
isRedBall t = t == Red
-- or
isBlueBall :: Ball -> Bool
isBlueBall t = t == Blue

-- functions can be written to take typeclasses
-- with type parameters
-- rather than types, assuming that funciton only
-- relies on features of typeclass
--
isEqual (Eq a) => a -> a -> Bool
isEqual x y = x == y
-- note that x and y must be same type,as 
-- they are both defined.
-- as being of type parameter 'a'.
-- A typeclass does not state that different
-- types in the typeclass can be mixed together.
-- So `isEqual Red 2` is invalid. even though 2
-- is an Integer, which is an instance of Eq,
-- and Red is a Ball which which is also an
-- instance of Eq.
--
-- other common typeclasses are:
-- Ord for types that can be ordered, allowing
-- to use >, <=, etc.
-- Read for types that can be created from a 
-- string representation.
-- Show for types that can be converted to a
-- string representation.
-- Enum for types that can be enumerated
-- Bounded for types that have a min and max
-- value
-- Num, Read, Integral, Fractional for types 
-- that can be added, subtracted, multiplied, etc.
--
-- Haskell can automatically make types part
-- of Eq, Ord, Read, Show, Enum, Bounded
-- with the `deriving` keyword at the end of
-- type declaration.
--
data Point = Point Float Float 
    deriving (Eq, Read, Show)

-- in this case it's not necessary to create an
-- 'instance' definition
--
--------------------------------------------
    -- IO
-- also read monads to better understand IO in haskell.
--
-- when a haskell program is executed. `main` is
-- called. it must return a value of type `IO a`
-- for some type `a`. example:
main :: IO ()
main = putStrLn $ "Hello, world!" ++ (say Blue)
-- putStrLn has type String -> IO ()
-- easiest to do IO if you can implement your 
-- program as a function from String to String.
-- the function
-- interact :: (String -> String) -> IO ()
-- inputs some text, runs a function on it, and
-- prints the result.
--
countLines :: String -> String
countLines = show . length . lines

main' = interact countLines
-- 
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
--
-- -----------------------------------
-- haskell REPL
--
-- start the repl by typing `ghci`.
-- any new values need to be created with `let`:
let x = 5
let foo = 6
> :t foo
foo :: Integer

-- operators, such as `+`, `:`, and `$`, are 
-- functions.
-- their type can be inspected by putting the 
-- operator in paranthesis.
> :t (:)
(:) :: a => [a] -> [a]

-- can get additional information on any `name`
-- using `:i`:
> :i (+)
class Num a where
    (+) :: a -> a -> a
    (-) :: a -> a -> a
    (*) :: a -> a -> a
    negate :: a -> a
    abs :: a -> a
    signum :: a -> a
    fromInteger :: Integer -> a
    -- defined in `GHC.Num`
infixl 6 +
-- you can also run any action of type `IO ()`
> sayHello
what is your name?
Friend!
Hello, Friend!

-- quicksort in haskell, using recursion
qsort [] = []
qsort (p:xs) = qsort lesser ++ [p] ++ qsort greater
    where lesser = filter (< p) xs
          greater = filter (>= p) xs



