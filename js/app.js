//Fuente para el range slider: http://danielcrisp.github.io/angular-rangeslider/

function indexJsonArray(array, id){
  var index = -1;
  for(var i=0; i < array.length; i++){
    if(array[i].id == id){
      index = i;
      break;
    }
  }
  return index;
}

function getFechaActual(){
  var d = new Date();
  var dia = d.getDate();
  var mes = d.getMonth() + 1;
  var ano = d.getFullYear();
  if(mes < 10)
    mes = "0" + mes;
  if(dia < 10)
    dia = "0" + dia;
  var fecha = ano + "-" + mes + "-" + dia;
  return fecha;
}

function getHoraActual(){
  var d = new Date();
  var hora = d.getHours();
  var minuto = d.getMinutes();
  if(hora < 10)
    hora = "0" + hora;
  if(minuto < 10)
    minuto = "0" + minuto;
  var horario = hora + ":" + minuto;

  return horario;
}

var app = angular.module('myApp', ['ui-rangeSlider']);

app.config(['$interpolateProvider', function($interpolateProvider) {
	$interpolateProvider.startSymbol('{[');
    $interpolateProvider.endSymbol(']}');
}]);

app.controller('encuentraCtrl', function($scope, $http, REST, $sce) {

    $scope.filtrarCursoEditar = function(idCurso){
      $scope.cursoEditar = [];
      $scope.cursoEditar = $scope.cursosArray.filter(function(curso) {
        return curso.id == idCurso;
      })
    }

    $scope.enableBtn = function () {
      $scope.rangoPrecio.disabled = !$scope.rangoPrecio.disabled;
    };

    $scope.buscar = function(){
    	$scope.buscador = $scope.inputBuscar;
    }

    $scope.rangoPrecio = {
      limites: {
        min: 0,
        max: 10000
      },
      minPrice: 0,
      maxPrice: 10000,
      disabled: false
    };
    $scope.buscador = {
      str_ciudad : cityGET.myvalue
    }

    var lugaresAPI = new REST("http://encuentra-casa.appspot.com/getLugaresREST");

    $scope.lugaresArray = [];

    lugaresAPI.getElementsOfTable($scope.lugaresArray);

});

app.filter('rangeFilter', function() {
    return function( items, rangeInfo ) {
        var filtered = [];
        var min = parseInt(rangeInfo.minPrice);
        var max = parseInt(rangeInfo.maxPrice);
        // If time is with the range
        angular.forEach(items, function(item) {
            if( item.int_rentaMensual >= min && item.int_rentaMensual <= max ) {
                filtered.push(item);
            }
        });
        return filtered;
    };
});


app.factory('REST', 

  function($http) {
  
    var REST = function(url, tabla, limit) {
      if(limit === undefined || limit < 0 )
        limit = 0;

      this.url = url;
      this.tabla = "xxx";
      this.limit = limit;
      this.clickCounter = 0;
    };

    REST.prototype.getElementsOfTable = function(arreglo){

      if(this.tabla === undefined){
        alert("no se ha definido una tabla");
        return;
      }
      var url = this.url;

      //url = url + "?method=get&table=" + this.tabla ;

      /*if(this.limit != 0)
        url = url + "&limit=" + this.limit + "&offset=" + (this.clickCounter * this.limit);*/

      $http.get(url).success(
        function (data) {
          for (var i = 0; i < data.length; i++) {
              arreglo.push(data[i]);
          }
        }
      );
      
      this.clickCounter = this.clickCounter + 1;

      return arreglo;

    };

    REST.prototype.postData = function(arreglo, idArray, scopeActualizar){
      if(this.tabla === undefined){
        alert("no se ha definido una tabla");
        return;
      }
      var url = this.url;
      url = url + "?method=post&table=" + this.tabla;


      var request = $http({
          method: "post",
          url: url,
          data: arreglo,
          headers: { 'Content-Type': 'application/x-www-form-urlencoded' }
      });

      request.then(function (response) {
          //alert(JSON.stringify(response.data));
          idArray.id = response.data;
          arreglo.id = JSON.parse(idArray.id);
          scopeActualizar.push(arreglo);
      });

    };

    REST.prototype.updateData = function(arreglo){
      if(this.tabla === undefined){
        alert("no se ha definido una tabla");
        return;
      }
      var url = this.url;
      url = url + "?method=update&table=" + this.tabla;


      var request = $http({
          method: "post",
          url: url,
          data: arreglo,
          headers: { 'Content-Type': 'application/x-www-form-urlencoded' }
      });

      request.then(function (response) {
        //alert(JSON.stringify(response.data));
      });

    };

    REST.prototype.deleteAll = function (arreglo){
      if(this.tabla === undefined){
        alert("no se ha definido una tabla");
        return;
      }
      var url = this.url;

      url = url + "?method=delete&table=" + this.tabla;

      var json = JSON.stringify(arreglo);

      var request = $http({
          method: "post",
          url: url,
          data: JSON.parse(json),
          headers: { 'Content-Type': 'application/x-www-form-urlencoded' }
      });

      request.then(function (response) {
          //alert(JSON.stringify(response.data));
      });
    };

    REST.prototype.postObjects = function (arreglo){
      if(this.tabla === undefined){
        alert("no se ha definido una tabla");
        return;
      }
      var url = this.url;

      url = url + "?method=postObjects&table=" + this.tabla;

      var json = JSON.stringify(arreglo);

      var request = $http({
          method: "post",
          url: url,
          data: JSON.parse(json),
          headers: { 'Content-Type': 'application/x-www-form-urlencoded' }
      });

      request.then(function (response) {
        alert(JSON.stringify(response.data));
      });
    };

    return REST;
  }

);