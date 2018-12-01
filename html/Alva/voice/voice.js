window.SpeechRecognition = window.SpeechRecognition || webkitSpeechRecognition;
var recognition = new webkitSpeechRecognition();
recognition.lang = 'ja';
recognition.interimResults = true;

recognition.onsoundstart = function () {
    document.getElementById('status').innerHTML = "認識中";
};
recognition.onnomatch = function () {
    document.getElementById('status').innerHTML = "もう一度試してください";
};
recognition.onerror = function () {
    document.getElementById('status').innerHTML = "エラー";
};
recognition.onsoundend = function () {
    document.getElementById('status').innerHTML = "停止中";
};

recognition.onresult = function (event) {
    var results = event.results;
    for (var i = event.resultIndex; i < results.length; i++) {
        if (results[i].isFinal) {
            document.getElementById('result_text').innerHTML = results[i][0].transcript;
            document.getElementById('status').innerHTML = "終了";
            recognition.ecd();
        } else
            document.getElementById('result_text').innerHTML = "[途中経過] " + results[i][0].transcript;
    }
}