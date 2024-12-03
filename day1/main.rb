puts File.readlines("a").map{
|l|l.split.map(&:to_i)
}.transpose.then{
|l,r|[l.sort.zip(r.sort).sum{
|a,b|(a-b).abs
},l.sum{
|n|n*r.count(n)
}]}