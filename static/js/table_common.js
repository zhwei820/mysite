"use strict"

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

var $table = $('#table').bootstrapTable({
    url: API_URL
  }),
  $modal = $('#modal'),
  $alert = $('.alert').hide();

$(function() {
  // create event
  $('.create').click(function() {
    showModal($(this).text());
  });

  $modal.validator().on('submit', function(e) {
    if ($modal.data('bs.validator').hasErrors()) {
      e.preventDefault();
    } else {
      e.preventDefault();

      var row = {};

      $modal.find('input[type!="radio"][name]').each(function() {
        row[$(this).attr('name')] = $(this).val();
      });

      $modal.find('select[name] option[title]:selected').each(function() {
        row[$(this).parent("select").attr('name')] = $(this).val();
      });

      $modal.find('input[type="radio"][name][title]:checked').each(function() {
        row[$(this).attr('name')] = $(this).val();
      });

      $.ajax({
        url: API_URL + ($modal.data('id') || ''),
        type: $modal.data('id') ? 'put' : 'post',
        contentType: 'application/json',
        data: JSON.stringify(row),
        success: function(data) {
          $modal.modal('hide');
          $table.bootstrapTable('refresh');
          if (data.status == 0) {
            showAlert(data.message, 'success');
          } else {
            showAlert(data.message, 'danger');
          }
        },
        error: function() {
          $modal.modal('hide');
          showAlert(($modal.data('id') ? 'Update' : 'Create') + ' item error!', 'danger');
        }
      });
    }
  });
});

function showModal(title, row) {

  row = row || {
    id: 0
  }; // default row value

  $modal.data('id', row.id);
  $modal.find('.modal-title').text(title);
  for (var name in row) {
    $modal.find('input[type!="radio"][name="' + name + '"]').val(row[name]);
    $modal.find('select[name="' + name + '"] option[title="' + row[name] + '"]').attr("selected", true);
    $modal.find('input[type="radio"][name="' + name + '"][title="' + row[name] + '"]').attr("checked", true);
  }
  $modal.modal('show');
}
