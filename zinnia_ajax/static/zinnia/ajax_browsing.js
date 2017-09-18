function followLink(e) {
    e.preventDefault();
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            dropAJAXBrowsing();
            document.getElementById('restZinniaContent').innerHTML = this.responseText;
            initAJAXBrowsing();
        }
    };
    xhttp.open('GET', e.target.getAttribute('href'), true);
    xhttp.setRequestHeader('Accept', 'text/ajax-content');
    xhttp.send();
}

function initAJAXBrowsing(follow_selector) {
    if (follow_selector === undefined) {
        var follow_selector = false;
    }
    if (ajaxLinkPattern === undefined) {
        ajaxLinkPattern = false;
    }
    if (ajaxLinkAntiPattern === undefined) {
        ajaxLinkAntiPattern = false;
    }
    var content = document.getElementById('restZinniaContent');
    content.querySelectorAll('a:not(.feeds)').forEach(function (item) {
        var href = item.getAttribute('href');
        if (ajaxLinkPattern && href) {
            if (ajaxLinkAntiPattern && href.split(ajaxLinkAntiPattern).length > 1) {
                return
            }
            if (ajaxLinkPattern && href.split(ajaxLinkPattern).length === 2) {
                item.addEventListener('click', followLink, true);
            }
        }
    });
    if (follow_selector) {
        content.querySelector(follow_selector).click()
    }
}

function dropAJAXBrowsing() {
    document.getElementById('restZinniaContent')
        .querySelectorAll('a').forEach(function (item) {
        item.removeEventListener('click', followLink);
    })
}

