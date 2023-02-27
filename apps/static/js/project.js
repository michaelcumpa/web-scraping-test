function getCryptoCurrencyRate(event) {
    var value = event.target.value;
    setInterval(() => {
        getRate(value);
    }, 10000);
}

function getRate(crytocurrency) {
    fetch(`/${crytocurrency}/`)
    .then(response => response.text())
    .then((html) => {
        var card = document.getElementById(`id_card_${crytocurrency}`);
        if (card) {
            card.outerHTML = html;
        }
        else {
            var contentRates = document.getElementById("id_rates");
            contentRates.innerHTML = html + contentRates.innerHTML;
        }
        drawRate(crytocurrency);
    });
}

function drawRate(crytocurrency) {
    fetch(`/${crytocurrency}/rates/`)
    .then(response => response.json())
    .then((data) => {
        setTimeout(() => {
            var chartCanvas = document.getElementById(`id_rates_timeline${crytocurrency}`);
            var myChart = new Chart(chartCanvas, {
                type: "line",
                data: data
            });
        }, 500);
    });
}

var inputs = document.querySelectorAll('input[name="crytocurrencies"]')
inputs.forEach(e => e.addEventListener("click", getCryptoCurrencyRate));
