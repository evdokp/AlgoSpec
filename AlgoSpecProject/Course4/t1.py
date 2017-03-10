vector<int> test(vector<string>& patterns, string& text){
    vector<int> pos;
    for (int i=0; i< text.size();i++){
        for (int j=0; j< patterns.size();j++){
            if ((patterns[j].size()+i-1)< text.size()){
                string sub=text.substr(i,patterns[j].size());
                if (sub.compare(patterns[j])==0){
                    pos.push_back(i);
                    break;
                }
            }
        }
    }
    sort(pos.begin(),pos.end());
    return pos;
}