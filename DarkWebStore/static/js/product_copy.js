function myFunction1() {
    /* Get the text field */
    var copyText = "bc1qk47h64v4lk2ltvxqphpq6kq3r90wqxaqklea6w";
  
    /* Select the text field */
    copyText.select();
  
    /* Copy the text inside the text field */
    document.execCommand("copy");
  
    /* Alert the copied text */
    alert("Copied the text: " + copyText.value);
  }

function myFunction2() {
    /* Get the text field */
    var copyText = "0x8F5e571FA46002B62FB73dC1A0F3560dDd3CFEdE";
  
    /* Select the text field */
    copyText.select();
  
    /* Copy the text inside the text field */
    document.execCommand("copy");
  
    /* Alert the copied text */
    alert("Copied the text: " + copyText.value);
  }