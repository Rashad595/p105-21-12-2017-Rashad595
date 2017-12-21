var n1 = int(input("Birinci reqem: ")); 
var n2 = int(input("Ikinci reqem: ")); 
var n3 = int(input("Ucuncu reqem: "));

if(n1 > n2){
    if(n1 > n3){
        print(n1 + " en boyukdur");
    }else{
        print(n3 + " en boyukdur");
    }
}else{
    if(n2 > n3){
        print(n2 + " en boyukdur");
    }else{
        print(n3 + " en boyukdur");
    }
}