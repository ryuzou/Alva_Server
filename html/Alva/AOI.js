function postGo() {
    var bookid = document.formName.number.value
    var CMD = "MOV " + "bookid " + bookid + " TO " + "bookshelf " + "0000"
    var Data = {
        cmd: CMD
    } 
    $.ajax({
        type: 'POST',
        url: document.location.protocol + "//" + document.location.hostname + ":8182",
        data: JSON.stringify(Data),
        contentType: 'application/json',
        dataType: "json",
        success: function (json_data) {
            if (!json_data[0]) {
                //dosomething when nothing had been returned
                return;
            } else {
                alert(json_data)
            }
        },
        error: function () {
            alert("Server Error. Pleasy try again later.");
        }
    }).then(function (response) {
        console.log(response)
    })
}

function postSubmit() {
    var json = {
        Idf: "bookid",
        name: document.formName.number.value,
        img: "YES"
    }
    $.ajax({
        type: 'POST',
        url: document.location.protocol + "//" + document.location.hostname + ":8182" + "/ACSinfo/",
        data: JSON.stringify(json),
        contentType: 'application/json',
        dataType: "json",
        success: function (json_data) {
            var sb = document.getElementById("sendbotton")
            sb.innerHTML = "<input class=\"pure-button\" onClick=\"postGo(this)\"\n" +
                "                       style=\"background: #7E7E7E; border-radius: 20px; color: white; margin: 0 auto; font-size: 2em\"\n" +
                "                       type=\"button\"\n" +
                "                       value=\"取り出す\" >"
            var dt = document.getElementById("datatable")
            dt.innerHTML = "<div class=\"pure-table\">\n" +
                "                        <h3>Title:</h3>\n" + json_data["bookname"] +
                "                        <h3>Author:</h3>\n" + json_data["author"] +
                "                        <h3>Bookshelf Number:</h3>\n" + "X:" + json_data["X"] + "Y:" + json_data["Y"] +
                "                        <h3>State:</h3>\n" +
                "                    </div>"
            document.getElementById("img1").src = json_data["img"]
        },
        error: function () {
            alert("Server Error. Pleasy try again later.");
        }
    }).then(function (response) {
        console.log(response)
    })
}

function postSearch(keyword) {
    $.ajax({
        type: 'POST',
        url: document.location.protocol + "//" + document.location.hostname + ":8182",
        data: {
            "keyword": keyword
        },
        headers: {
            'API-Token': 'AAAAAAAAAAAAAAA',
            'Authorization': 'BBBBBBBBBBBBBB',
            'Content-Type': 'application/json',
        },
    }).then(function (response) {
        console.log(response)
    })
}

function DropDownMenu() {   //todo
    var select1 = document.forms.formName.series; //変数select1を宣言
    var select2 = document.forms.formName.number; //変数select2を宣言

    select2.options.length = 0; // 選択肢の数がそれぞれに異なる場合、これが重要

    if (select1.options[select1.selectedIndex].value == "garupan") {
        select2.options[0] = new Option("1", "16");
        select2.options[1] = new Option("2", "17");
        select2.options[2] = new Option("3", "18");
        select2.options[3] = new Option("4", "19");
    } else if (select1.options[select1.selectedIndex].value == "gansuri") {
        select2.options[0] = new Option("1", "1");
        select2.options[1] = new Option("2", "2");
        select2.options[2] = new Option("3", "3");
        select2.options[3] = new Option("4", "4");
        select2.options[4] = new Option("5", "5");
        select2.options[5] = new Option("6", "6");
        select2.options[6] = new Option("7", "7");
        select2.options[7] = new Option("8", "8");
        select2.options[8] = new Option("9", "9");
        select2.options[9] = new Option("10", "10");
        select2.options[10] = new Option("11", "11");
        select2.options[11] = new Option("12", "12");
        select2.options[12] = new Option("13", "13");
        select2.options[13] = new Option("14", "14");
        select2.options[14] = new Option("15", "15");
    } else if (select1.options[select1.selectedIndex].value == "haru") {
        select2.options[0] = new Option("1", "20");
        select2.options[1] = new Option("2", "21");
        select2.options[2] = new Option("3", "22");
        select2.options[3] = new Option("4", "23");
    } else if (select1.options[select1.selectedIndex].value == "humetsu") {
        select2.options[0] = new Option("1", "24");
        select2.options[1] = new Option("2", "25");
        select2.options[2] = new Option("3", "26");
        select2.options[3] = new Option("4", "27");
        select2.options[4] = new Option("5", "28");
    }
}