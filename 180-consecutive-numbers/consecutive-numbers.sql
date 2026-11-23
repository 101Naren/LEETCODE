# Write your MySQL query statement below
SELECT DISTINCT a.Num AS ConsecutiveNums FROM Logs a
JOIN Logs B ON a.Id = b.Id + 1 AND a.Num = b.Num
JOIN Logs C ON a.Id = c.Id + 2 AND a.Num = c.Num