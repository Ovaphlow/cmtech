function AddElement(id, name){
  var mytype, TemO = document.getElementById(id);
  var newInput = document.createElement("input");
  newInput.type="file";
  newInput.name=name;
  TemO.appendChild(newInput);
  var newline = document.createElement("br");
  TemO.appendChild(newline);
}
