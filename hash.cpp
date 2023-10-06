#include<iostream>
#include<map>
#include<unordered_map>
using namespace std;

int main(){

    map<string,int> m ;


    /// there can  be 3 ways to insert in unordered map //

    pair<string , int > p = make_pair("saurabh",4);
    m.insert(p);
    
    // 2 ways
    pair<string , int> pair2("aniket",2);
    m.insert(pair2);

    //3 ways;

    m["good boh"] = 3;
    

    cout << m["good boh"] << endl;
    cout << m.at("saurabh") << endl;

    cout << m["india"] << endl;
    cout << m.at("india") << endl;


    cout << "Count whether it presentn or not  "<< endl;
    cout  << m.count("india") << endl;


    cout  << "Erase" << endl;

    cout << m.erase("saurabh") << endl;
    
    cout << "Size after Erase" << endl;

    cout << m.size() << endl;

    map<string , int > :: iterator it = m.begin();
    while(it != m.end()){
        cout << it->first << " " << it->second << endl;
        it++;
    }





    return 0 ;
}