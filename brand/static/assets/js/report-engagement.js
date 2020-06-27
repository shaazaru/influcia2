


var chartrer1 = new CanvasJS.Chart("Replies-rer1", {
	animationEnabled: true,  
	title:{
		text: ""
	},
	axisY: {
		title: "",
		valueFormatString: "#0,,.",
		suffix: "	",
		prefix: ""
	},
	data: [{
		type: "splineArea",
		color: "rgba(54,158,173,.7)",
		markerSize: 5,
		xValueFormatString: "YYYY",
		yValueFormatString: "##0.##",
		dataPoints: [
			{ x: new Date(2000, 0), y: 3289000 },
			{ x: new Date(2001, 0), y: 3830000 },
			{ x: new Date(2002, 0), y: 2009000 },
			{ x: new Date(2003, 0), y: 2840000 },
			{ x: new Date(2004, 0), y: 2396000 },
			{ x: new Date(2005, 0), y: 1613000 },
			{ x: new Date(2006, 0), y: 2821000 },
			{ x: new Date(2007, 0), y: 2000000 },
			{ x: new Date(2008, 0), y: 1397000 },
			{ x: new Date(2009, 0), y: 2506000 },
			{ x: new Date(2010, 0), y: 2798000 },
			{ x: new Date(2011, 0), y: 3386000 },
			{ x: new Date(2012, 0), y: 6704000},
			{ x: new Date(2013, 0), y: 6026000 },
			{ x: new Date(2014, 0), y: 2394000 },
			{ x: new Date(2015, 0), y: 1872000 },
			{ x: new Date(2016, 0), y: 2140000 }
		]
	}]
	});



var chartrer2 = new CanvasJS.Chart("Response-rer2", {
	exportEnabled: true,
	animationEnabled: true,
	title:{
		text: ""
	},
	subtitles: [{
		text: ""
	}], 
	axisX: {
		title: ""
	},
	axisY: {
		title: "",
		titleFontColor: "#4F81BC",
		lineColor: "#4F81BC",
		labelFontColor: "#4F81BC",
		tickColor: "#4F81BC"
	},
	axisY2: {
		title: "",
		titleFontColor: "#C0504E",
		lineColor: "#C0504E",
		labelFontColor: "#C0504E",
		tickColor: "#C0504E"
	},
	toolTip: {
		shared: true
	},
	legend: {
		cursor: "pointer",
		itemclick: toggleDataSeries
	},
	data: [{
		type: "column",
		name: "",
		showInLegend: true,      
		yValueFormatString: "##0.# %",
		dataPoints: [
			{ label: "July 31",  y: 19034.5 },
			{ label: "Aug 13", y: 20015 },
			{ label: "Aug 27", y: 25342 },
			{ label: "Sep 9",  y: 20088 },
			{ label: "Sep 23",  y: 28234 }
		]
	},
	{
		type: "column",
		name: "",
		axisYType: "secondary",
		showInLegend: true,
		yValueFormatString: "##0.# %",
		dataPoints: [
			{ label: "July 31", y: 210.5 },
			{ label: "Aug 13", y: 135 },
			{ label: "Aug 27", y: 425 },
			{ label: "Sep 9", y: 130 },
			{ label: "Sep 23", y: 528 }
		]
	}]
});
chartrer1.render();
chartrer2.render();

function toggleDataSeries(e) {
	if (typeof (e.dataSeries.visible) === "undefined" || e.dataSeries.visible) {
		e.dataSeries.visible = false;
	} else {
		e.dataSeries.visible = true;
	}
	e.chartrer1.render();
}

var chartrer3 = new CanvasJS.Chart("Time-rer3", {
	animationEnabled: true,
	theme: "light2",
	title:{
		text: ""
	},
	axisX:{
		valueFormatString: "DD MMM",
		crosshair: {
			enabled: true,
			snapToDataPoint: true
		}
	},
	axisY: {
		title: "",
		crosshair: {
			enabled: true
		}
	},
	toolTip:{
		shared:true
	},  
	legend:{
		cursor:"pointer",
		verticalAlign: "bottom",
		horizontalAlign: "left",
		dockInsidePlotArea: true,
		itemclick: toogleDataSeries
	},
	data: [{
		type: "line",
		showInLegend: false,
		name: "Total Visit",
		markerType: "square",
		xValueFormatString: "DD MMM, YYYY",
		color: "#F08080",
		dataPoints: [
			{ x: new Date(2017, 0, 3), y: 650 },
			{ x: new Date(2017, 0, 4), y: 700 },
			{ x: new Date(2017, 0, 5), y: 710 },
			{ x: new Date(2017, 0, 6), y: 658 },
			{ x: new Date(2017, 0, 7), y: 734 },
			{ x: new Date(2017, 0, 8), y: 963 },
			{ x: new Date(2017, 0, 9), y: 847 },
			{ x: new Date(2017, 0, 10), y: 853 },
			{ x: new Date(2017, 0, 11), y: 869 },
			{ x: new Date(2017, 0, 12), y: 943 },
			{ x: new Date(2017, 0, 13), y: 970 },
			{ x: new Date(2017, 0, 14), y: 869 },
			{ x: new Date(2017, 0, 15), y: 890 },
			{ x: new Date(2017, 0, 16), y: 930 }
		]
	},
	{
		type: "line",
		showInLegend: false,
		name: "Unique Visit",
		lineDashType: "dash",
		dataPoints: [
			{ x: new Date(2017, 0, 3), y: 510 },
			{ x: new Date(2017, 0, 4), y: 560 },
			{ x: new Date(2017, 0, 5), y: 540 },
			{ x: new Date(2017, 0, 6), y: 558 },
			{ x: new Date(2017, 0, 7), y: 544 },
			{ x: new Date(2017, 0, 8), y: 693 },
			{ x: new Date(2017, 0, 9), y: 657 },
			{ x: new Date(2017, 0, 10), y: 663 },
			{ x: new Date(2017, 0, 11), y: 639 },
			{ x: new Date(2017, 0, 12), y: 673 },
			{ x: new Date(2017, 0, 13), y: 660 },
			{ x: new Date(2017, 0, 14), y: 562 },
			{ x: new Date(2017, 0, 15), y: 643 },
			{ x: new Date(2017, 0, 16), y: 570 }
		]
	}]
});
chartrer3.render();

function toogleDataSeries(e){
	if (typeof(e.dataSeries.visible) === "undefined" || e.dataSeries.visible) {
		e.dataSeries.visible = false;
	} else{
		e.dataSeries.visible = true;
	}
	chartrer1.render();
}

