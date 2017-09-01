function filters() {
  var i;
  var td;
  var input = $('#select_filter').val();
  var filter = input.toUpperCase();
  var table = document.getElementById('main_member_list');
  var tr = table.getElementsByTagName('tr');

  for (i = 0; i < tr.length; i++) {
    td = tr[i].getElementsByTagName('td')[4];
    if (filter === 'ALL') {
      tr[i].style.display = '';
    } else {
        if (td.innerHTML.toUpperCase().indexOf(filter) > -1) {
          tr[i].style.display = '';
        } else {
          tr[i].style.display = 'none';
        }
    }
  }
}