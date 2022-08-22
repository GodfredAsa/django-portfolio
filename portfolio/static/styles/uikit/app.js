

let alertwrapper = document.getElementsByClassName('alert');
let alertClose = document.querySelector('.alert__close');

if(alertwrapper){
  console.log("Something")
  alertClose.addEventListener('click', 
  ()=> alertwrapper.getElementsByClassName.display = 'none')
}
