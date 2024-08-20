const submitBtn = document.getElementById('submit-btn');
const warning = document.getElementById('warning');
const nameInput = document.getElementById('name');
const macAddressInput = document.getElementById('mac-address');
const serialNumberInput = document.getElementById('serial-number');
const manufacturerInput = document.getElementById('manufacturer');
const descriptionInput = document.getElementById('description');
const priceInput = document.getElementById('price');

const checkForm = () => {
    if (nameInput.value === "" ||
        macAddressInput.value === "" ||
        serialNumberInput.value === "" ||
        manufacturerInput.value === "" ||
        descriptionInput.value === "" ||
        priceInput.value === "") {
        warning.innerHTML = "<h5>Please fill out all the fields on the form.</h5>";
        return false;
    }
}
