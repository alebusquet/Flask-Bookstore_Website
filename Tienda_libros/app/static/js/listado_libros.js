
(function () {

    const btnsComprarLibro = document.querySelectorAll('.btnComprarLibro');

    let isbnLibroSeleccionado = null;
    const csrf_token = document.querySelector("[name='csrf-token']").value;

    btnsComprarLibro.forEach((btn) => {
        btn.addEventListener('click', function() {
            isbnLibroSeleccionado = this.id;
            confirmarComprar();
        })
    });

    const confirmarComprar = async() => {

        Swal.fire({
            title: 'Confirma la compra del libro seleccionado?',
            inputAttributes: {
                autocapitalize: 'off'
            },
            showCancelButton: true,
            confirmButtonText: 'Comprar',
            showLoaderOnConfirm: true,
            preConfirm: async () => {
                return await fetch(`${window.origin}/comprarLibro`, {
                    method: 'POST',
                    mode: 'same-origin',
                    credentials: 'same-origin',
                    headers: {
                        'Content-Type': 'application/json',
                        'X-CSRF-TOKEN': csrf_token
                    },
                    body: JSON.stringify({
                        'isbn': isbnLibroSeleccionado
                    })
                }).then(response => {
                    if (!response.ok) {
                        notificacionSwal('Error', response.statusText, 'error','Cerrar');
                    }
                    return response.json();
                }).then(data => {
                    if(data.exito) {
                        notificacionSwal('Exito!!', 'Libro Comprado', 'success','Ok!');
                    } else {
                        notificacionSwal('Alerta!!', data.mensaje, 'warning','Ok');
                    }
                }).catch(error => {
                    notificacionSwal('Error', error, 'error','Cerrar');
                });
            },
            allowOutsideClick: () => false,
            allowEscapeKey: () => false
        });


    };
})();


