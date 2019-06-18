function tijiao() {

    let yewu = $("#yewu").val();
    let canshu1 = $("#canshu1").val();
    let canshu2 = $("#canshu2").val();
    let data = {"A":yewu,"B":2,"C":canshu2};
    // 异步请求后台数据
    $.ajax({
        url: site_url+'tijiao/',
        type: 'POST',
        data:JSON.stringify(data),
        success: function (res) {
            alert(res['DATA']);
        }
    });
}