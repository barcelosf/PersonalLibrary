let password = document.getElementById('password')
let confirmPassword = document.getElementById('confirm_password')
let formulario = document.getElementById('formulario')

let senha = password.value 
let confirmaSenha = confirmPassword.value

formulario.addEventListener('submit', function(evento){
    if(senha != confirmaSenha){
      evento.preventDefault()
      alert('As senhas não coincidem')
    }
})
