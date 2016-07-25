"use strict"
function sortObjectKeys(obj) {
  var tmp = {};
  Object.keys(obj).sort().forEach(function(k) { tmp[k] = obj[k] });
  return tmp;
}

Date.prototype.Format = function(fmt) //author: meizz
  {
    var o = {
      "M+": this.getMonth() + 1, //月份
      "d+": this.getDate(), //日
      "h+": this.getHours(), //小时
      "m+": this.getMinutes(), //分
      "s+": this.getSeconds(), //秒
      "q+": Math.floor((this.getMonth() + 3) / 3), //季度
      "S": this.getMilliseconds() //毫秒
    };
    if (/(y+)/.test(fmt))
      fmt = fmt.replace(RegExp.$1, (this.getFullYear() + "").substr(4 - RegExp.$1.length));
    for (var k in o)
      if (new RegExp("(" + k + ")").test(fmt))
        fmt = fmt.replace(RegExp.$1, (RegExp.$1.length == 1) ? (o[k]) : (("00" + o[k]).substr(("" + o[k]).length)));
    return fmt;
  }

var serialize = function(obj) {
  var str = [];
  for (var p in obj)
    if (obj.hasOwnProperty(p)) {
      str.push(encodeURIComponent(p) + "=" + encodeURIComponent(obj[p]));
    }
  return str.join("&");
}


var addEvent = (function() {
  if (document.addEventListener) {
    return function(el, type, fn) {
      if (el.length) {
        for (var i = 0; i < el.length; i++) {
          addEvent(el[i], type, fn);
        }
      } else {
        el.addEventListener(type, fn, false);
      }
    };
  } else {
    return function(el, type, fn) {
      if (el.length) {
        for (var i = 0; i < el.length; i++) {
          addEvent(el[i], type, fn);
        }
      } else {
        el.attachEvent('on' + type, function() {
          return fn.call(el, window.event);
        });
      }
    };
  }
})();


$(document).ajaxSend(function(event, xhr, settings) {
  if (!/^(GET|HEAD|OPTIONS|TRACE)$/.test(settings.type) && !settings.crossDomain) {
    xhr.setRequestHeader("X-CSRFToken", Cookies.get('csrftoken'));
  }
})

$(function() {
    var $table = $('#table').bootstrapTable({
      url: API_URL
    }),
    $modal = $('#modal'),
    $alert = $('.alert').hide();
});
