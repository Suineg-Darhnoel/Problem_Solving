-- Generate fibonacci serie
-- Brute Force Fibonacci

fib_b :: Integer -> Integer
fib_b n
    | n == 1 = 1
    | n == 2 = 1
    | otherwise = fib_b (n-1) + fib_b (n-2)

-- Better Solution for Fibonacci
fib2 :: Integer -> [Integer]
fib2 n
    | n <= 0 = []
    | n == 1 = [0, 1]
    | otherwise = fibl1 : fibl2 : []
    where
        fibl1 = last fibl
        fibl2 = fibl1 + (head fibl)
        fibl = fib2 (n-1)

fib :: Integer -> Integer
fib n
    | n == 1 = 1
    | otherwise = last (fib2 n)

renderline :: Show a => Integer -> a -> String
renderline i a = show i ++ ". " ++ show a

bs :: Show a => [a] -> String
bs = unlines . zipWith renderline [1..]

x :: [Integer]
x = map fib [1..50]

main :: IO ()
main = do
    putStr $ bs x
