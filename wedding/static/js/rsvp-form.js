var app = angular.module('rsvpForm', ['ngCookies']).

config(function($interpolateProvider) {
    $interpolateProvider.startSymbol('{=');
    $interpolateProvider.endSymbol('=}');
}).

run(['$http', '$cookies', function($http, $cookies) {
    $http.defaults.headers.common['X-CSRFToken'] = $cookies.csrftoken;
}]).

controller('rsvpFormCtrl', ['$cookies', '$http', '$scope', function($cookies, $http, $scope) {

	$scope.error_text = '';
	$scope.form_states = [
		'empty',
		'loading',
		'rsvping',
		'rsvped'
	]
	$scope.form_state = 0;

	$scope.rsvp = {
		'name': '',
		'email': '',
		'attending': true,
		'party_size': 2,
		'staying_onsite': true,
		'staying_friday': false,
	};
	$scope.rsvp_code = '';

	$scope.getRsvp = function() {
		var rsvp_code = $scope.rsvp_code.toLowerCase().replace(/[\s\_]+/g, '-').replace(/[^a-z0-9\-]/g, '');
		$scope.error_text = '';
		$scope.form_state = 1;
		$http({
			'method': 'GET',
			'url': '/rsvp/' + rsvp_code + '/'
		}).then(function successCallback(response) {
			$scope.rsvp = response.data;
			$scope.form_state = 2;
		}, function errorCallback(response) {
			$scope.error_text = 'Wups....';
			$scope.form_state = 0;
		});
	};

	$scope.submitRsvp = function() {
		$scope.error_text = '';
		$scope.form_state = 1;
		$scope.rsvp.responded = true;
		$http({
			'method': 'PUT',
			'url': '/rsvp/' + $scope.rsvp.rsvp_code_slug + '/',
			'data': $scope.rsvp,
			'headers': {
			    'X-CSRFToken': document.forms[0].csrfmiddlewaretoken.value
			}
		}).then(function successCallback(response) {
			$scope.rsvp = response.data;
			$scope.form_state = 3;
		}, function errorCallback(response) {
			$scope.error_text = 'Wups....';
			$scope.form_state = 2;
		});
	};

}]);
