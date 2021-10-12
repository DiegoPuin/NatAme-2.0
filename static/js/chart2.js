let myChart = document.getElementById('myChart').getContext('2d');
var myInfo = document.getElementById('info_stadistics').textContent;
myInfo = myInfo.replace(/'/g, '"');
var myInfo2 = JSON.parse(myInfo);
var regions = [];
var data = [];
var labels = [];

for (let i=0; i<myInfo2.length; i++){
    regions.push(myInfo2[i].region);
    labels.push(myInfo2[i].product);
    data.push(myInfo2[i].quantity);
}

// Global Options
Chart.defaults.global.defaultFontFamily = 'Lato';
Chart.defaults.global.defaultFontSize = 18;
Chart.defaults.global.defaultFontColor = '#777';

let massPopChart = new Chart(myChart, {
type:'bar', // bar, horizontalBar, pie, line, doughnut, radar, polarArea
data:{
    labels: [labels[0]],
    datasets:[{
    label: [regions[0]],
    data: [data[0]],
    backgroundColor: ['rgba(255, 99, 132, 0.6)'],
    borderWidth:1,
    borderColor:'#777',
    hoverBorderWidth:3,
    hoverBorderColor:'#000'
    },
    {
    label: [regions[1]],
    data: [data[1]],
    backgroundColor: ['rgba(54, 162, 235, 0.6)'],
    borderWidth:1,
    borderColor:'#777',
    hoverBorderWidth:3,
    hoverBorderColor:'#000'
    },
    {
    label: [regions[2]],
    data: [data[2]],
    backgroundColor: ['rgba(255, 206, 86, 0.6)'],
    borderWidth:1,
    borderColor:'#777',
    hoverBorderWidth:3,
    hoverBorderColor:'#000'
    }]
},
options:{
    title:{
    display:true,
    text:'Producto mas vendido por regional',
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
        top:200
    }
    },
    tooltips:{
    enabled:true
    }
}
});