let myChart = document.getElementById('myChart').getContext('2d');
var myInfo = document.getElementById('info_stadistics').textContent;
myInfo = myInfo.replace(/'/g, '"');
var myInfo2 = JSON.parse(myInfo);
var products = [];

for (let i=0; i<myInfo2.length; i++){
    var x = false;
    if (products.length == 0){
        products.push(myInfo2[i].product);
    }
    for (let j=0; j<products.length; j++){
        if (myInfo2[i].product == products[j]){
            x = true;
        }   
    }
    if (!x){
        products.push(myInfo2[i].product);
    }
}

var labelsAndina = [];
var labelsCaribe = [];
var labelsPacifica = [];
var labelsOrinoquia = [];
var labelsAmazonia = [];
var dataAndina  = [];
var dataCaribe  = [];
var dataPacifica  = [];
var dataOrinoquia  = []; 
var dataAmazonia = [];
var color = ['rgba(255, 99, 132, 0.6)', 'rgba(54, 162, 235, 0.6)', 'rgba(255, 206, 86, 0.6)',
'rgba(75, 192, 192, 0.6)', 'rgba(153, 102, 255, 0.6)'];

for (let i=0; i<myInfo2.length; i++){
    if (myInfo2[i].region.toUpperCase() == "ANDINA"){
        labelsAndina.push(myInfo2[i].product);
        dataAndina.push(myInfo2[i].quantity);
    } 
    if (myInfo2[i].region.toUpperCase() == "CARIBE"){
        labelsCaribe.push(myInfo2[i].product);
        dataCaribe.push(myInfo2[i].quantity);
    }
    if (myInfo2[i].region.toUpperCase() == "PACIFICA"){
        labelsPacifica.push(myInfo2[i].product);
        dataPacifica.push(myInfo2[i].quantity);
    }
    if (myInfo2[i].region.toUpperCase() == "ORINOQUIA"){
        labelsOrinoquia.push(myInfo2[i].product);
        dataOrinoquia.push(myInfo2[i].quantity);
    }
    if (myInfo2[i].region.toUpperCase() == "AMAZONIA"){
        labelsAmazonia.push(myInfo2[i].product);
        dataAmazonia.push(myInfo2[i].quantity);
    }
}

console.log("Regiones");
console.log(products);
console.log("Label Andina");
console.log(labelsAndina);
console.log(dataAndina);
console.log("Label Caribe");
console.log(labelsCaribe);
console.log(dataCaribe);
console.log("Label Pacifica");
console.log(labelsPacifica);
console.log(dataPacifica);

// Global Options
Chart.defaults.global.defaultFontFamily = 'Lato';
Chart.defaults.global.defaultFontSize = 18;
Chart.defaults.global.defaultFontColor = '#777';

let massPopChart = new Chart(myChart, {
type:'bar', // bar, horizontalBar, pie, line, doughnut, radar, polarArea
data:{
    labels: products,
    datasets:[{
    label:'Andina',
    data: dataAndina,
    //backgroundColor:'green',
    backgroundColor: color[0],
    borderWidth:1,
    borderColor:'#777',
    hoverBorderWidth:3,
    hoverBorderColor:'#000'
    }, {
    label:'Caribe',
    data: labelsCaribe,
    //backgroundColor:'green',
    backgroundColor: color[1],
    borderWidth:1,
    borderColor:'#777',
    hoverBorderWidth:3,
    hoverBorderColor:'#000'
    }, {
    label:'Pacifica',
    data: dataPacifica,
    //backgroundColor:'green',
    backgroundColor: color[2],
    borderWidth:1,
    borderColor:'#777',
    hoverBorderWidth:3,
    hoverBorderColor:'#000'
    }

    ]
},
options:{
    title:{
    display:true,
    text:'Productos mas vendidos',
    fontSize:25
    },
    legend:{
    display:true,
    position:'right',
    labels:{
        fontColor:'#000'
    }
    },
    layout:{
    padding:{
        left:50,
        right:0,
        bottom:0,
        top:120
    }
    },
    tooltips:{
    enabled:true
    }
}
});