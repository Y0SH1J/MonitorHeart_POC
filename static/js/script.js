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
    `;
    container.appendChild(div);

    const ctx = document.getElementById(`chart-${uid}`).getContext('2d');
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
    setInterval(() => {
        fetch(`/data/${uid}`)
            .then(res => res.json())
            .then(data => {
                const bpmText = document.getElementById(`bpm-${uid}`);
                for (let i = count; i < data.length; i++) {
                    bpmChart.data.labels.push(i);
                    bpmChart.data.datasets[0].data.push(data[i]);
                }
                count = data.length;
                bpmChart.update();

                if (data.length == 0) {
                    bpmText.innerText = "Live BPM: Loading..." // The array is empty initially, to ensure that "undefined" doesn't get displayed.
                }
                else if (data[data.length-1] < 80){
                    if (data.length == 1){
                        bpmText.innerText = "Live BPM: ";
                    }
                    bpmText.innerHTML += `<span style="color:red">${data[data.length - 1]}</span>, `;
                }
                else if (data[data.length-1] > 120){
                    if (data.length == 1){
                        bpmText.innerText = "Live BPM: ";
                    }
                    bpmText.innerHTML += `<span style="color:orange">${data[data.length - 1]}</span>, `;
                }
                else{
                    if (data.length == 1){
                        bpmText.innerText = "Live BPM: ";
                    }
                    bpmText.innerHTML += data[data.length - 1] + ", ";
                }
                
            });
    }, 1000);
}