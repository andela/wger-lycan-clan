function filters() {
  var input;
  var  filter;
  var  table;
  var  tr;

  input = $('#select_filter').val();
  filter = input.toUpperCase();
  table = document.getElementById('main_member_list');
  tr = table.getElementsByTagName('tr');

  for (var i = 0; i < tr.length; i++) {
    var td = tr[i].getElementsByTagName('td')[4];
    console.log(td);
    if (filter == 'ALL') {
      $('.Inactive').css('background', 'beige');
      tr[i].style.display = '';
      
    } else if (td && (td.innerHTML.toUpperCase().indexOf(filter) > -1)) {
            tr[i].style.display = '';
    } else {
            tr[i].style.display = 'none';
            console.log('No Data Tables');
    }  
  }
}
console.log(filters());
