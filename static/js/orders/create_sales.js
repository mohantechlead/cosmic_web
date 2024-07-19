document.addEventListener('DOMContentLoaded', function () {
    const totalNewForms = document.getElementById('id_items-TOTAL_FORMS')
    const submitButton = document.querySelector('#submits');
    const priceFields = document.querySelectorAll('.price');
    const totalPriceField = $('#total-price');
    const totalVatField = $('#total-vat');
    const quantityFields = $('.quantity');
    const dropdowns = document.querySelectorAll('.item_name');
    
    

    $('.item-list').each(function () {
        var form = $(this);
        updateTotalPrice(form);
        fetchCodes(form);
    });

    $(document).on('change', '.item-list .item_name', function () {
        var form = $(this).closest('.item-list');
        var itemId = form.find('.item_name').val();
       
            // Make AJAX request to Django view
            fetch(`get_item_data/${itemId}/`)
                .then(response => response.json())
                .then(data => {
                    console.log(data.code, "code");
                    // Update corresponding output div with fetched data
                    var codes= form.find('.hs_codes').val(data.code); 
                     
                })
                .catch(error => console.error('Error:', error));
        
    });
    function fetchCodes(form){
    
dropdowns.forEach(function(dropdown) {

dropdown.addEventListener("change", function() {
    var form = $(this).closest('.item-list');
    //updateCode(form);
    const formsets = $('.item-list');
    const itemId = dropdown.value;
    const codes = document.querySelectorAll('.hs_code');
    console.log(itemId, "id");
    $('.item-list').each(function() {
        // Within each formset, select the 'total_price' fields
        const itemId = $(this).find('.item_name');
        const code = $(this).find('.hs_codes');
        
        console.log(itemId, "id2");
        itemId.each(function() {
            const name = $(this).val();
            console.log(name, "name");
            // Make AJAX request to Django view
            fetch(`get_item_data/${name}/`)
                .then(response => response.json())
                .then(data => {
                    console.log(data.code, "code");
                    // Update corresponding output div with fetched data
                    code.val(data.code); 
                     
                })
                .catch(error => console.error('Error:', error));
        });
        
        const codeInput = $(this).find('.hs_codes');
        //codeInput.val("is");
    });
});
});
    };

    // addMoreBtn.addEventListener('click', add_new_form);
    submitButton.addEventListener('click', function (event) {
        event.preventDefault();
        calculateTotalPrice();
    });

    var univ_total = 0
    var univ_vat = 0
    
function calculateTotalPrice() {
    var total = 0
    var total_vat = 0
    var originalTotal = 0;
    var originalVat = 0;
    var freight = document.getElementById('freight_price');
    
    const formsets = $('.item-list');
    const total_price_fields = document.querySelectorAll('.total_price');
    const total_vat_fields = document.querySelectorAll('.before_vat');
    //const discountApplied = discount_checkbox.checked;
    var freightElement = document.getElementById('freight_price');

    var freight = 0;
    if (freightElement) {
        freight = parseFloat(freightElement.value) || 0;
    }
    $('.item-list').each(function() {
        
    
        // Within each formset, select the 'total_price' fields
        const totalFields = $(this).find('.total_price');
        const vatFields = $(this).find('.before_vat');
        totalFields.each(function() {
        const price = parseFloat($(this).val()) || 0;
     
        total += price;
        originalTotal += price; 
        });
        vatFields.each(function() {
        const vat_price = parseFloat($(this).val()) || 0;
        total_vat += vat_price;
        originalVat += vat_price;
      
        });
        
        console.log(total)
        var total_with_freight = total_vat + freight;
        univ_total = total;
        univ_vat = total_vat;
        totalVatField.val(total_with_freight.toFixed(2));  // Update the 'value' of the field
        totalVatField.text('Total Price: $' + total_with_freight.toFixed(2));  // Update the displayed text
    });
}
calculateTotalPrice();
    
submitButton.addEventListener('click', function (event) {
        event.preventDefault(); // Prevent the default form submission

        // Serialize form data
        const formData1 = new FormData(form1);
        const prNoValue = formData1.get('order_no');

        formData1.set('PR_before_vat', univ_vat);
        const amount = 1
       
        console.log(prNoValue)

        // Use fetch to submit both forms asynchronously
        fetch(form1.action, {
            method: 'POST',
            body: formData1
            }).then(
                response => {
                    if (response && response.ok){
                        // document.getElementById('form1').reset();

                        // window.location.reload();
                    }
                }
            )

    });


function updateTotalPrice(form) {
        var quantity = parseFloat(form.find('.quantity').val());
        var price = parseFloat(form.find('.price').val());
        var total = quantity * price || 0;
        var total_price = total + (total * 0.15)
        form.find('.before_vat').val(total.toFixed(2));
        form.find('.total_price').val(total_price.toFixed(2));
}

    $(document).on('input', '.item-list .quantity, .item-list .price', function () {
        var form = $(this).closest('.item-list');
        updateTotalPrice(form);
    });

    // Apply initial calculation for existing forms
    $('.item-list').each(function () {
        var form = $(this);
        updateTotalPrice(form);
    });

});
