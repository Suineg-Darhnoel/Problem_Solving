-- Print Pascal Triangle
pascal n
    | n == 1 = [1]
    | n == 2 = [1,1]
    | otherwise = [1] ++ (map f xs) ++ [1]
    where
        f n = fst n + snd n
        xs = zip pascal_l (tail pascal_l)
        pascal_l = pascal (n-1)

lst2str [] = ""
lst2str (x:xs) = show x ++ " " ++ lst2str xs

main :: IO ()
main = do
    let xs = map pascal [1..20]
    mapM_ (putStrLn . lst2str) xs
