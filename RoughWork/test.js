consoleLog();
function consoleLog(){
    x = textReader('Airport');
    console.log(x + "hi");
}

function textReader(name){
    const fs = require('fs');
    let text = fs.readFileSync(name + '.txt', 'utf8');
    let res = text.split("/(],)/");
    return res;
}
/*let res = text.split("],");
for(let i=0; i<res.length; i++){
    res[i] = res[i] + ']';
};*/



