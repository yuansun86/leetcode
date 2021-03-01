class Solution {
    public List<String> findWords(char[][] board, String[] words) {
        Trie wordsList = new Trie();
        boolean[][] visited = new boolean[board.length][board[0].length];
        for (String s:words){
            wordsList.insert(s);
        }
        List<String> results = new ArrayList<>();
        for (int i = 0; i < board.length; i++){
            for (int j = 0; j < board[0].length; j++){
                this.dfs(i, j, board, visited, wordsList, "", results);
            }
        }
        return results;
    }
    
    public void dfs(int i, int j, char[][] board, boolean[][] visited, Trie wordsList, String path, List results){
        if (i < 0 || i >= board.length || j < 0 || j >= board[0].length){
            return;
        }
        if (visited[i][j]){
            return;
        }
        path = path + board[i][j];
        if (!wordsList.startsWith(path)){
            return;
        }
        if (wordsList.search(path)){
            if (!results.contains(path)){
                results.add(path);
            }
        }
        visited[i][j] = true;
        this.dfs(i + 1, j, board, visited, wordsList, path, results);
        this.dfs(i - 1, j, board, visited, wordsList, path, results);
        this.dfs(i, j + 1, board, visited, wordsList, path, results);
        this.dfs(i, j - 1, board, visited, wordsList, path, results);
        visited[i][j] = false;
    }
}

class Trie {
    private TrieNode root;
    /** Initialize your data structure here. */
    public Trie() {
        root = new TrieNode();
        
    }
    
    /** Inserts a word into the trie. */
    public void insert(String word) {
        TrieNode node = root;
        for (int i = 0; i < word.length(); i++){
            char curChar = word.charAt(i);
            if (! node.containsKey(curChar)){
                node.put(curChar, new TrieNode());
            }
            node = node.get(curChar);
        }
        node.setEnd();
    }
    
    /** Returns if the word is in the trie. */
    public boolean search(String word) {
        TrieNode node = root;
        for (int i = 0;i < word.length();i++){
            char curChar = word.charAt(i);
            if (node.containsKey(curChar)){
                node = node.get(curChar);
            }else{
                return false;
            }
        }
        return node.isEnd();
        
    }
    
    /** Returns if there is any word in the trie that starts with the given prefix. */
    public boolean startsWith(String prefix) {
        TrieNode node = root;
        for (int i = 0;i < prefix.length();i++){
            char curChar = prefix.charAt(i);
            if (node.containsKey(curChar)){
                node = node.get(curChar);
            }else{
                return false;
            }
        }
        return true;
    }
}


class TrieNode{
    private TrieNode[] links;
    private final int R = 26;
    private boolean isEnd;
    
    public TrieNode(){
        links = new TrieNode[R];
    }
    
    public boolean containsKey(char c){
        return links[c - 'a'] != null;
    }
    
    public TrieNode get(char ch){
        return links[ch - 'a'];
    }
    
    public void put(char c, TrieNode node){
        links[c - 'a'] = node;
    }
    
    public void setEnd(){
        isEnd = true;
    }
    
    
    public boolean isEnd(){
        return isEnd;
    }
}