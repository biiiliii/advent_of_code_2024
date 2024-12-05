puts File.readlines("a").map{
_1.split.map(&:to_i)
}.transpose.then{
|l,r|[l.sort.zip(r.sort).sum{
(_1-_2).abs
},l.sum{
_1*r.count(_1)
}]}