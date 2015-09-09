/**
 * Created by team on 03.06.2015.
 */
/* sayfaları modal içine basmak sayfa yenilememesi için anasayfa a tagın içindeki href e #koy*/
/* (linuxhtml,icerikhtml)elenamları  anasayfa nın on click te yer alan link ;' onclick="menu('/webcore/linux','sayfa')
 sayfada iceriğin basıldığı elemanın id si bu div olabilir link olabilir.">*/

function menuaa(url, id) {

    $.ajax({
        url: url,
        success: function (linuxhtml) {
            $("#" + id).html(linuxhtml)

        }

    })
}

function icerikgetir(url, id) {

    $.ajax({
        url: url,
        success: function (icerikhtml) {
            $("#" + id).html(icerikhtml)

        }

    })
}


