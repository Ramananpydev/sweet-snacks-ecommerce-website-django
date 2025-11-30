   let quantity = 1;

    function increase() {
      quantity++;

      document.getElementById('qty').value = quantity;
      document.getElementById('price').innerHTML = quantity * 40;
      
    }

    function decrease() {
      if (quantity > 1) {
        quantity--;
        document.getElementById('qty').value = quantity;
        document.getElementById('price').innerHTML = quantity * 40;
      }
    }

    

    


    

    document.querySelector(".checkout-form").addEventListener("submit", function(e) {
      e.preventDefault();
      window.location.href = "{% url 'onlineproduce:success' %}";
    });