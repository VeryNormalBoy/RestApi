(doccument).ready(function(){
  const movie = $('#in_mov').val();
  const tickets = $('#in_tick').val();
  const form= $("#form");
  const formData = {
    "movieName": movie,
    "tickets": tickets
  }
    $form.on("submit",function(Event) {
      event.preventDefault()
      $.ajax({
        type: "POST"
        url: "/v1/bookings"
        data: formData
        dataType: 'json'
      });

    };