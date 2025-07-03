function addUser() {
    fetch('/add_user')
        .then(response => response.json())
        .then(data => {
            const uid = data.user_id;
            createUserDisplay(uid);
        })
        .catch(error => console.error('Error:', error));
}

function createUserDisplay(uid) {
    const container = document.getElementById("user-containers");

    const div = document.createElement("div");
    div.innerHTML = `
        <h3>User ${uid}</h3>
        <canvas id="chart-${uid}" width="400" height="200"></canvas>
        <p id="bpm-${uid}">Live BPM: Loading...</p>
        <button id="anomaly-${uid}">Anomaly</button>
    `;
    container.appendChild(div);

    const ctx = document.getElementById(`chart-${uid}`).getContext('2d');
    const anomalyButton = document.getElementById(`anomaly-${uid}`);
    anomalyButton.addEventListener("click", bpmAnomalySimulation); //Simulate different bpm anomolies
    const bpmChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: [],
            datasets: [{
                label: `User ${uid} BPM`,
                data: [],
                borderColor: 'green',
                borderWidth: 2,
                fill: false,
                tension: 0.2
            }]
        },
        options: {
            scales: {
                y: {
                    title: { display: true, text: 'BPM' },
                    min: 0, max: 200
                }
            }
        }
    });

    let count = 0;
    let ts, ts_old, ts_new = "";
    let bpm = 0;
    let flag = false;
    setInterval(() => {
        fetch(`/data/${uid}`)
            .then(res => res.json())
            .then(data => {
                const bpmText = document.getElementById(`bpm-${uid}`);
                for (let i = count; i < data.length; i++) {
                    bpmChart.data.labels.push(i);
                    ts = data[i][0];
                    bpm =  data[i][1];
                    bpmChart.data.datasets[0].data.push(bpm);
                }
                count = data.length;
                bpmChart.update();

                // Check for duplicate entries
                ts_old = ts_new;
                ts_new = ts;

                if (data.length == 0) {
                    bpmText.innerText = "Live BPM: Loading..." // The array is empty initially, to ensure that "undefined" doesn't get displayed.
                }
                else if (bpm < 80){
                    if (data.length == 1 && flag == false){
                        bpmText.innerText = "Live BPM: ";
                        flag = true;
                    }
                    if (ts_old != ts_new ){
                        bpmText.innerHTML += `<span style="color:red">${bpm}</span>, `;
                    }
                }
                else if (bpm > 120){
                    if (data.length == 1 && flag == false){
                        bpmText.innerText = "Live BPM: ";
                        flag = true;
                    }
                    if (ts_old != ts_new){
                        bpmText.innerHTML += `<span style="color:orange">${bpm}</span>, `;
                    }
                }
                else{
                    if (data.length == 1 && flag == false){
                        bpmText.innerText = "Live BPM: ";
                        flag = true;
                    }
                    if (ts_old != ts_new){
                        bpmText.innerHTML += bpm + ", ";
                    }
                }
                
            });
    }, 200);

    function bpmAnomalySimulation() {

        console.log(`Working...for ${uid}`);
    };
};

