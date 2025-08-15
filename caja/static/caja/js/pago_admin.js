document.addEventListener("DOMContentLoaded", function () {
    const socioField = document.getElementById("id_socio");
    const montoField = document.getElementById("id_monto_formateado");

    if (!socioField || !montoField) {
        console.error("No se encontró socioField o montoField en el DOM");
        return;
    }

    console.log("🎯 Select2 detectado, escuchando con jQuery...");

    // Usamos jQuery para Select2
    $('#id_socio').on('change', function () {
        const socioId = $(this).val();

        if (!socioId) {
            montoField.value = '';
            return;
        }
    ['change', 'input', 'select2:select'].forEach(eventType => {
    $('#id_socio').on(eventType, () => {
        console.log(`Evento detectado: ${eventType}`);
    });
});
    

        fetch(`/admin/api/socio/${socioId}/precio/`)
            .then(response => response.json())
            .then(data => {
                if (data.precio) {
                    montoField.value = `$${parseFloat(data.precio).toLocaleString("es-AR")}`;
                } else {
                    montoField.value = "Sin membresía";
                }
            })
            .catch(error => {
                console.error("Error al obtener el precio:", error);
                montoField.value = "Error";
            });
    });
});
