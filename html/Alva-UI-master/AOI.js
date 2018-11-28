function postGo(bookid) {
    $.ajax({
        type: 'POST',
        url: 'http://nginx/ACSinfo',
        data: {
            "bookid": bookid
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

function postSubmit(bookid) {
    $.ajax({
        type: 'POST',
        url: 'http://nginx/ACS_command-manager',
        data: {
            "bookid": bookid
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

function postSearch(keyword) {
    $.ajax({
        type: 'POST',
        url: 'http://alva2018.com',
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

function DropDownMenu() {
    var select1 = document.forms.formName.series; //変数select1を宣言
    var select2 = document.forms.formName.number; //変数select2を宣言

    select2.options.length = 0; // 選択肢の数がそれぞれに異なる場合、これが重要

    if (select1.options[select1.selectedIndex].value == "garupan") {
        select2.options[0] = new Option("1", "1");
        select2.options[1] = new Option("2", "2");
        select2.options[2] = new Option("3", "3");
        select2.options[3] = new Option("4", "4");
    } else if (select1.options[select1.selectedIndex].value == "gansuri") {
        select2.options[0] = new Option("1", "5");
        select2.options[1] = new Option("2", "6");
        select2.options[2] = new Option("3", "7");
        select2.options[3] = new Option("4", "8");
        select2.options[4] = new Option("5", "9");
        select2.options[5] = new Option("6", "10");
        select2.options[6] = new Option("7", "11");
        select2.options[7] = new Option("8", "12");
        select2.options[8] = new Option("9", "13");
        select2.options[9] = new Option("10", "14");
        select2.options[10] = new Option("11", "15");
        select2.options[11] = new Option("12", "16");
        select2.options[12] = new Option("13", "17");
        select2.options[13] = new Option("14", "18");
    } else if (select1.options[select1.selectedIndex].value == "haru") {
        select2.options[0] = new Option("1", "19");
        select2.options[1] = new Option("2", "20");
        select2.options[2] = new Option("3", "21");
        select2.options[3] = new Option("4", "22");
    }
}