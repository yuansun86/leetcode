解题思路是利用递归，在每一轮往下的搜索中记录已经使用的数字index。

每一次dfs中，从左到右iterate，如果遇到使用过的index，则不做任何事情继续。如果遇到没有使用过的，则加入path中，同时标记为used，在这一轮dfs结束后，记得把used[index]重新设置为false，并且将path中加入的元素进行删除。
结束条件是如果结果长度等于初始数组长度则加入结果中并且返回。
