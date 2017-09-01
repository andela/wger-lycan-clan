function filters() {
  var input;
  var filter;
  var table;
  var tr;
  var td;
  var i;

  input = $('#select_filter').val();
  filter = input.toUpperCase();
  table = document.getElementById('main_member_list');
  tr = table.getElementsByTagName('tr');

  for (i = 0; i < tr.length; i++) {
    td = tr[i].getElementsByTagName('td')[4];
    if (filter === 'ALL') {
      $('.Inactive').css('background', 'beige');
      tr[i].style.display = '';
    } else if (td && (td.innerHTML.toUpperCase().indexOf(filter) > -1)) {
      tr[i].style.display = '';
    } else {
      tr[i].style.display = 'none';
    }
  }
}
console.log(filters());
