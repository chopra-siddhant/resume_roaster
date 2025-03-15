// Define the AngularJS app and a custom directive for file uploads.
var app = angular.module('resumeRoasterApp', []);

app.directive('fileModel', ['$parse', function ($parse) {
  return {
    restrict: 'A',
    link: function(scope, element, attrs) {
      var model = $parse(attrs.fileModel);
      element.bind('change', function(){
        scope.$apply(function(){
          model.assign(scope, element[0].files[0]);
        });
      });
    }
  };
}]);

app.controller('MainController', ['$scope', '$http', function($scope, $http) {
  $scope.mode = 'humorous'; // default mode

  $scope.uploadResume = function() {
    var formData = new FormData();
    formData.append('resume', $scope.resumeFile);
    formData.append('mode', $scope.mode);
    if ($scope.email) {  // optional: if you want to collect email info
      formData.append('email', $scope.email);
    }
    
    $("#loading").fadeIn();
    
    $http.post('http://localhost:8000/api/upload_resume/', formData, {
      transformRequest: angular.identity,
      headers: {'Content-Type': undefined}
    }).then(function(response) {
      $("#loading").fadeOut();
      $scope.results = response.data;
    }, function(error) {
      $("#loading").fadeOut();
      alert("Error uploading resume!");
    });
  };
  
  $scope.simulateHR = function() {
    $http.post('http://localhost:8000/api/hr_simulator/', { resume_id: $scope.results.id })
      .then(function(response) {
        $scope.hrResult = response.data.hr_feedback;
      });
  };
  
  $scope.generateLinkedInFlex = function() {
    $http.post('http://localhost:8000/api/linkedin_flex/', { resume_id: $scope.results.id })
      .then(function(response) {
        $scope.linkedinResult = response.data.generated_post;
      });
  };
}]);
