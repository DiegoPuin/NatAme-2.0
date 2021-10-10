let myChart = document.getElementById('myChart').getContext('2d');
// var myvar = '{{info}}'
// myvar = myvar.replace(/'/g, '"');
// var newInfo = JSON.parse('{{ myvar | tojson }}');
// console.log(myvar);
// Global Options
Chart.defaults.global.defaultFontFamily = 'Lato';
Chart.defaults.global.defaultFontSize = 18;
Chart.defaults.global.defaultFontColor = '#777';

let massPopChart = new Chart(myChart, {
type:'bar', // bar, horizontalBar, pie, line, doughnut, radar, polarArea
data:{
    labels:['Andina', 'Caribe', 'Pacifica'],
    datasets:[{
    label:'Ventas',
    data:[
        14600,
        34600,
        14600
    ],
    //backgroundColor:'green',
    backgroundColor:[
        'rgba(255, 99, 132, 0.6)',
        'rgba(54, 162, 235, 0.6)',
        'rgba(255, 206, 86, 0.6)',
        'rgba(75, 192, 192, 0.6)',
        // 'rgba(153, 102, 255, 0.6)',
        // 'rgba(255, 159, 64, 0.6)',
        // 'rgba(255, 99, 132, 0.6)'
    ],
    borderWidth:1,
    borderColor:'#777',
    hoverBorderWidth:3,
    hoverBorderColor:'#000'
    }]
},
options:{
    title:{
    display:true,
    text:'Ventas por regional',
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