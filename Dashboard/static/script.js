// Gestión de contador de sesión con sessionStorage
function inicializarContador() {
  const hoy = new Date().toDateString();
  const ultimoContador = sessionStorage.getItem("ultimo-contador-fecha");
  const contadorActual =
    parseInt(sessionStorage.getItem("contador-sesion")) || 0;

  // Si el día cambió, resetear contador
  if (ultimoContador !== hoy) {
    sessionStorage.setItem("contador-anterior", contadorActual);
    sessionStorage.setItem("contador-sesion", "0");
    sessionStorage.setItem("ultimo-contador-fecha", hoy);
  }

  actualizarVistaContador();
}

function incrementarContador() {
  const contador = parseInt(sessionStorage.getItem("contador-sesion")) || 0;
  sessionStorage.setItem("contador-sesion", contador + 1);
  actualizarVistaContador();
}

function actualizarVistaContador() {
  const contador = parseInt(sessionStorage.getItem("contador-sesion")) || 0;
  const anterior = parseInt(sessionStorage.getItem("contador-anterior")) || 0;

  document.getElementById("contador-sesion").textContent =
    contador + " procesadas";

  // Opcional: mostrar contador anterior si existe
  if (anterior > 0) {
    document.getElementById("contador-sesion").title = "Anterior: " + anterior;
  }
}

function submitForm(accion) {
  const form = document.getElementById("form-herramienta");
  if (!form) return;

  // Si es aprobar, incrementar contador
  if (accion === "aprobar") {
    incrementarContador();
  }

  form.action = "/" + accion + "/{{ herramienta.id if herramienta else 0 }}";
  form.method = "POST";
  form.submit();
}

// Inicializar al cargar
document.addEventListener("DOMContentLoaded", inicializarContador);
