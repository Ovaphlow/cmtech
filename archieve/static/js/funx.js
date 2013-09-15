function AddElement(){
  var mytype, TemO=document.getElementById("file");
  var newInput = document.createElement("input");
  newInput.type="file";
  newInput.name="file";
  TemO.appendChild(newInput);
  var newline = document.createElement("br");
  TemO.appendChild(newline);
}
