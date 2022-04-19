var whHtml5QrCode = null;
var whProductQrcodePrefix = "PRODUCT";
var whProductIDs = [];

var audioError = new Audio('/wayhouse/static/src/sound/error.mp3');
var audioBeep = new Audio('/wayhouse/static/src/sound/beep.mp3');
var audioSent = new Audio('/wayhouse/static/src/sound/sent.mp3');


function PrintElem(elem) {
    var mywindow = window.open('', 'PRINT', 'height=400,width=600');

    mywindow.document.write('<html><head><title></title>');
    mywindow.document.write('</head><body >');
    mywindow.document.write(elem.innerHTML);
    mywindow.document.write('</body></html>');

    mywindow.document.close(); // necessary for IE >= 10
    mywindow.focus(); // necessary for IE >= 10*/

    mywindow.print();
    mywindow.close();

    return true;
}

function wh_create_product_qrcode() {

    let reference = $(".wh-product-reference")[0][$(".wh-product-reference")[0].selectedIndex].text;
    let caliber = $(".wh-product-caliber")[0].value;
    let choice = $(".wh-product-choice")[0][$(".wh-product-choice")[0].selectedIndex].text;
    let shade = $(".wh-product-shade")[0].value;
    let format = $(".wh-product-format")[0][$(".wh-product-format")[0].selectedIndex].text;
    let metrage = $(".wh-product-metrage")[0].value;
    let production_line = $(".wh-product-production_line")[0].value;
    let manufacturing_date = $(".wh-product-manufacturing_date")[0].value;

    let reference_val = $(".wh-product-reference-val")[0];
    let caliber_val = $(".wh-product-caliber-val")[0];
    let choice_val = $(".wh-product-choice-val")[0];
    let shade_val = $(".wh-product-shade-val")[0];
    let format_val = $(".wh-product-format-val")[0];
    let metrage_val = $(".wh-product-metrage-val")[0];
    let production_line_val = $(".wh-product-production_line-val")[0];
    let manufacturing_date_val = $(".wh-product-manufacturing_date-val")[0];

    reference_val.innerText = "";
    caliber_val.innerText = "";
    choice_val.innerText = "";
    shade_val.innerText = "";
    format_val.innerText = "";
    metrage_val.innerText = 0.00;
    production_line_val.innerText = "";
    manufacturing_date_val.innerText = "";

    document.getElementById("wh-qrcode-place").innerHTML = "";

    if (
        reference == "false" ||
        caliber == "false" ||
        choice == "false" ||
        shade == "false" ||
        format == "false" ||
        metrage <= 0 ||
        production_line == "false" ||
        manufacturing_date == "false") {
        alert("error");
        return false;
    }

    let qrcode_data = {
        reference: reference,
        caliber: parseInt(caliber),
        choice: choice,
        shade: shade,
        format: format,
        metrage: parseFloat(metrage),
        production_line: production_line,
        manufacturing_date: manufacturing_date.substring(1, manufacturing_date.length - 1)
    };

    reference_val.innerText = qrcode_data.reference;
    caliber_val.innerText = qrcode_data.caliber;
    choice_val.innerText = qrcode_data.choice;
    shade_val.innerText = qrcode_data.shade;
    format_val.innerText = qrcode_data.format;
    metrage_val.innerText = qrcode_data.metrage;
    production_line_val.innerText = qrcode_data.production_line;
    manufacturing_date_val.innerText = qrcode_data.manufacturing_date;

    let qrcode = new QRCode(document.getElementById("wh-qrcode-place"), {
        text: whProductQrcodePrefix + JSON.stringify(qrcode_data)
    });

    let product_qrcode_result = document.getElementById("wh-product-qrcode-result");
    PrintElem(product_qrcode_result);

    qrcode.clear();

    return false;
}

function whAssignProduct(qrcodeData) {

    data = {
        "params": {
            "reference": qrcodeData.reference,
            "caliber": qrcodeData.caliber,
            "choice": qrcodeData.choice,
            "shade": qrcodeData.shade,
            "format": qrcodeData.format,
            "metrage": qrcodeData.metrage,
            "production_line": qrcodeData.production_line,
            "manufacturing_date": qrcodeData.manufacturing_date,
            "tag": qrcodeData.tag
        }
    };

    $.ajax({
        type: "POST",
        url: "/wayhouse/product/assign",
        data: JSON.stringify(data),
        contentType: "application/json; charset=utf-8",
        dataType: "json",
        success: function (data) {
            console.log(data);
            audioSent.play();

            whProductIDs.push(data["result"]["data"]["product_id"]);
        },
        failure: function (err) {
            console.log(err);
            audioError.play();
        }
    });

}

function whOnScanSuccess(decodedText, decodedResult) {

    // only QrCode format
    if (decodedResult.result.format.format != 0) {
        return 0;
    }

    //PRODUCT{"A":1}
    let decodedTextPrefix = decodedText.substring(0, whProductQrcodePrefix.length);

    // product qrcode
    if (decodedTextPrefix == whProductQrcodePrefix) {
        let product_qrcodeData = decodedText.substring(whProductQrcodePrefix.length);

        $(".wh-product-qrcode")[0].value = product_qrcodeData;
    } else {
        $(".wh-product-tag")[0].value = decodedText;
    }

    audioBeep.play();

    let productQrcode = $(".wh-product-qrcode")[0].value
    let productTag = $(".wh-product-tag")[0].value

    if (productQrcode.length > 0 && productTag.length > 0) {
        let qrcodeData = JSON.parse(productQrcode);
        qrcodeData["tag"] = productTag;

        $(".wh-product-qrcode")[0].value = "";
        $(".wh-product-tag")[0].value = "";

        whAssignProduct(qrcodeData);
    }
}

function whOnScanFailure(error) {
    //audioError.play();
    console.warn(`Code scan error = ${error}`);
}

function whStopScanQrcode() {
    whHtml5QrCode.stop().then((ignore) => {
        console.log("QR Code scanning is stopped");
        whHtml5QrCode = null;
    }).catch((err) => {
        console.warn(`Code scan error = ${err}`);
        whHtml5QrCode = null;
    });

}

function whScanQrcode() {
    if (whHtml5QrCode && whHtml5QrCode.isScanning) {
        whStopScanQrcode();
        return false;
    }

    whHtml5QrCode = new Html5Qrcode("wh-qrcode-reader");
    let config = { fps: 20, qrbox: { width: 600, height: 600 } };
    whHtml5QrCode.start({ facingMode: "environment" }, config, whOnScanSuccess, whOnScanFailure);

    return false;
}

function whReceiveProducts() {
    data = {
        "params": {
            "product_ids": whProductIDs,
            "location_dest_id": 4
        }
    };

    $.ajax({
        type: "POST",
        url: "/wayhouse/product/receive",
        data: JSON.stringify(data),
        contentType: "application/json; charset=utf-8",
        dataType: "json",
        success: function (data) {
            console.log(data);
            audioSent.play();

            whProductIDs = [];
        },
        failure: function (err) {
            console.log(err);
            audioError.play();
        }
    });
}
