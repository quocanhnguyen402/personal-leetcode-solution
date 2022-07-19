class Solution {
public:
    vector<vector<string>> ans;
    vector<string> v;
    bool isSafe(int r,int i,int n)
    {
        for(int j=0;j<n;j++) //checking for the coloumn
            if(i!=j and v[r][j]=='Q')
                return false;
        for(int j=0;j<n;j++) //checking for the row
            if(r!=j and v[j][i]=='Q')
                return false;
        int a = r+1;
        int b = i+1;
        while(a<n and b<n) //checking for right lower diagonal
        {
            if(v[a][b]=='Q')
                return false;
            a++;
            b++;
        }
        a = r-1;
        b = i-1;
        while(a>=0 and b>=0) //checking for left upper diagonal
        {
            if(v[a][b]=='Q')
                return false;
            a--;
            b--;
        }
        a = r-1;
        b = i+1;
        while(a>=0 and b<n) //checking for right upper diagonal
        {
            if(v[a][b]=='Q')
                return false;
            a--;
            b++;
        }
        a = r+1;
        b = i-1;
        while(a<n and b>=0) //checking for left lower diagonal
        {
            if(v[a][b]=='Q')
                return false;
            a++;
            b--;
        }
        return true;
    }
    void helper(int r,int n)
    {
        if(r==n) //if all rows visited then we have found a valid board arrangement
        {
            ans.push_back(v);
            return;
        }
        for(int i=0;i<n;i++) //placing only one queen in a row
        {
            if(isSafe(r,i,n))
            {
                v[r][i] = 'Q';
                helper(r+1,n);
                v[r][i] = '.'; //backtrack
            }
        }
    }
    int totalNQueens(int n) 
    {
        for(int i=0;i<n;i++) //making a blank board
        {
            string s="";
            for(int j=0;j<n;j++)
            {
                s+='.';
            }
            v.push_back(s);
        }
                
        helper(0,n);    //calling for 0th row
        return ans.size();    
    }
};