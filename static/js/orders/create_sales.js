
    document.addEventListener('DOMContentLoaded', function () {
        const radioButtons = document.querySelectorAll('#measurement_type');
        const radioButtons2 = document.querySelectorAll('#payment_type');
        const totalNewForms = document.getElementById('id_items-TOTAL_FORMS')
        const submitButton = document.querySelector('#submits');
        const addMoreBtn = document.getElementById('add-more');
        const priceFields = document.querySelectorAll('price');
        const totalPriceField = $('#total-price');
        const totalVatField = $('#total-vat');
        const quantityFields = $('.quantity');

        addMoreBtn.addEventListener('click', add_new_form);
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

        const formsets = $('.item-list');
        const total_price_fields = document.querySelectorAll('.total_price');
        const total_vat_fields = document.querySelectorAll('.before_vat');
        //const discountApplied = discount_checkbox.checked;
        
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
           
            univ_total = total;
            univ_vat = total_vat;
            totalPriceField.val(total.toFixed(2));  // Update the 'value' of the field
            totalPriceField.text('Total Price: $' + total.toFixed(2)); 
            totalVatField.val(total_vat.toFixed(2));  // Update the 'value' of the field
            totalVatField.text('Total Price: $' + total_vat.toFixed(2));  // Update the displayed text
        });
    }
    calculateTotalPrice();
        
    submitButton.addEventListener('click', function (event) {
            event.preventDefault(); // Prevent the default form submission

            // Serialize form data
            const formData1 = new FormData(form1);
            const formData2 = new FormData(form2);

            const prNoValue = formData1.get('order_no');

            //formData1.set('PR_total_price', univ_total);
            formData1.set('PR_before_vat', univ_vat);
            
          
            const amount = 1
           
            console.log(prNoValue)
            formData2.append('order_no', prNoValue)

            // Use fetch to submit both forms asynchronously
            fetch(form1.action, {
    method: 'POST',
    body: formData1
})
.then(response => {
    if (!response.ok) {
        // console.log(form_errors)
        return response.json().then(data => {
            // Display form 1 errors in the error container
            const errorContainer = document.getElementById('error-container');
            // errorContainer.innerHTML = ''; // Clear previous errors
            if (data.form_errors) {
                const errorList = document.createElement('ul');
                for (const key in data.form_errors) {
                    if (Object.prototype.hasOwnProperty.call(data.form_errors, key)) {
                        const errorItem = document.createElement('li');
                        errorItem.textContent = `${key}: ${data.form_errors[key]}`;
                        errorList.appendChild(errorItem);
                    }
                }
                // errorContainer.appendChild(errorList);
            }
        });
    }else {
        // If the response is successful, proceed to the next form submission
        return fetch(form2.action, {
            method: 'POST',
            body: formData2
        });
    }
})
.then(response => {
    if (response && !response.ok) {
        // Handle errors from the second form submission, if any
        return response.json().then(data => {
            // 'data' will contain the form errors returned from the server
            // Update the UI to display these errors to the user
            console.log('Form 2 errors:', data.form_errors);
            // Display the errors in the UI
        });
    } else {
        // Handle success or no error from the second form submission
        // Reload the page or do any other necessary action
        document.getElementById('form1').reset();
        document.getElementById('form2').reset();

        window.location.reload();
    }
})
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
        function add_new_form(args) {
            // Your code to add a new form here
            const currentForms = document.getElementsByClassName('item-list')
            let currentFormsCount = currentForms.length + 1
            console.log(currentForms.length)
            console.log(totalNewForms);
            const copyFormTarget = document.getElementById('form-lists')
            const copyEmptyForm = document.getElementById('empty-form').cloneNode(true);
            copyEmptyForm.setAttribute('class', 'item-list form-group col-md-5 text-dark')
            copyEmptyForm.setAttribute('id', `form-${currentFormsCount}`)
            // Clear input values in the cloned form
            const regex = new RegExp('__prefix__', 'g')
            copyEmptyForm.querySelectorAll('input').forEach(function (input) {
                input.value = '';
            });
            copyEmptyForm.innerHTML = copyEmptyForm.innerHTML.replace(regex, currentFormsCount)
            // Append the cloned form to the form list
            totalNewForms.value = currentFormsCount + 1;
            copyFormTarget.appendChild(copyEmptyForm);
        }
    
});
        
