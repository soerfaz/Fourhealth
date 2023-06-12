$(document).ready(function() {
    var daftarGejala = [
        "batuk", "gatal", "demam", "nyeri"
    ];
    $('#gejala1').select2({
        data:daftarGejala,
        theme: "classic",
    });
  });
