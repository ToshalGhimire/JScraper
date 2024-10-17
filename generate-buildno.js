var fs = require('fs');
fs.readFile('./metadata.json',function(err,content) {
    if (err) throw err;
    var metadata = JSON.parse(content);
    metadata.buildRevision = metadata.buildRevision + 1;
    fs.writeFile('./metadata.json',JSON.stringify(metadata),function(err){
        if (err) throw err;
    })
});