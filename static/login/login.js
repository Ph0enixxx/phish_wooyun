$(function() {
  $(".subbtn").click(function() {
    var user = $('#user').val();
    if ($('#user').val() == '') {
      $('#msg').html('请输入邮箱')
      return false;
    }
    if ($('#pwd').val() == '') {
      $('#msg').html('请输入密码')
      return false;
    }
    var captcha = $('#captcha').val();
    var pwd = hex_md5(hex_md5($('#user').val() + hex_md5(addslashes(htmlspecialchars($('#pwd').val())))) + captcha.toLocaleLowerCase())
    $.ajax({
      type: "post",
      url: "/index.php?do=login&act=ajax",
      data: {
        token: loginToken,
        user: user,
        pwd: pwd,
        captcha: captcha.toLocaleLowerCase()
      },
      dataType: "json",
      success: function(data) {
        if (data.code == 'A0001') {
          $('#msg').html(data.msg)
        } else {
          location.href = '/';
        }
      }
    });
  });
})

function addslashes(str) {
  return str.replace(/(['"\\])/g, "\\$1");
}

function htmlspecialchars(str) {
  var map = {
    "&": "&amp;",
    "\"": "&quot;",
    "'": "&#039;",
    "<": "&lt;",
    ">": "&gt;"
  };
  return str.replace(/([&"'<>])/g, function(match, char) {
    return map[char];
  });
}
