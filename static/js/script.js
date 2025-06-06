function fetchData() {
            fetch('/data')
                .then(response => response.json())
                .then(data => {
                    console.log("Fetched data:", data); // For debugging on console
                    
                    let bpmDisplay = document.getElementById('bpm-data'); // Get html element with id 'bpm-data'

                    for (let i = count_chart; i < data.length; i++) {
                        bpmChart.data.labels.push(i); // x-axis
                        bpmChart.data.datasets[0].data.push(data[i]); // y-axis
                    }
                    count_chart = data.length;
                    

                    if (count == 0) {
                        bpmDisplay.innerHTML = " ";
                    } // Erase "Loading..." text in element

                    let displayValue = check_value(data);
                    bpmDisplay.innerHTML += displayValue; // Update the live data text
                    bpmChart.update(); // Refresh the chart with new data

                })
                .catch(error => console.error('Error fetching data:', error));
        }

function check_value(data) {

    let return_text = "";

    // Append only the new data
    for (let i = count; i < data.length; i++) {               
    // document.getElementById('bpm-data').innerText = data.join(', ');
        if (count == 0) {
            return_text +=  `ID: ${data[i]}</br>`
            return_text += "Live BPM Data: "; // Display ID on first line and bpm feed on next line
        }
        else {
            
            if(data[i] > 120) {
                //return_text +=  ' ' + data[i].fontcolor("red") + ','; // Display bpm list data
                return_text +=   `<span style="color:red">${data[i]}</span>, `;
            }
            else if (data[i] < 80) {
                // return_text +=  ' ' + data[i].fontcolor("orange") + ','; // Display bpm list data
                return_text +=   `<span style="color:orange">${data[i]}</span>, `;
            }
            else {
                return_text +=  ' ' + data[i] + ','; // Display bpm list data
            }
        }
    }

    count = data.length; // Ensure new data is appended
    return return_text
}

function plot_chart() {

}

let count = 0;
let count_chart = 0;

let chart = document.getElementById('bpm-chart');
let bpmChart = new Chart(chart, {
    type: 'line',
    data: {
        labels: [], // Time or sample index
        datasets: [{
            label: 'Live BPM',
            data: [],
            borderColor: 'blue',
            borderWidth: 2,
            fill: false,
            tension: 0.2
        }]
    },
    options: {
        scales: {
            x: { title: { display: true, text: 'Sample' } },
            y: { title: { display: true, text: 'BPM' }, min: 0, max: 200 }
        }
    }
}
)
setInterval(fetchData, 1000);  // Fetch every 1 second
fetchData();  // Run immediately, otherwise we would have to wait 1 second before first data fetch happens
