(doccument).ready(function(){
  let formData{ 
    "movienName": $('#in_mov').val();
    "tickets": $('#in_tick').val();
  }
    $('#form').submit(function(Event) {
      event.preventDefault()
      $.ajax({
        type: "POST"
        url: "/v1/bookings"
        data: JSON.stringify(formData)
        dataType: 'json'
      })

    }