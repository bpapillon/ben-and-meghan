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
		'comments': '',
	};
	$scope.rsvp_code = '';
	$scope.party_size_options = [1];

	$scope.getRsvp = function() {
		var rsvp_code = $scope.rsvp_code.toLowerCase().replace(/[^a-z0-9]/g, '');
		if (!rsvp_code) {
			$scope.setError('Whoops, Ben screwed up the web site somehow. Shoot him an email or call and we\'ll figure it out.');
			return;
		}
		$scope.setError();
		$scope.form_state = 1;
		$http({
			'method': 'GET',
			'url': '/rsvp/' + rsvp_code + '/'
		}).then(function successCallback(response) {
			$scope.rsvp = response.data;
			if (!$scope.rsvp.responded) {
				$scope.rsvp.attending = true;
			}
			$scope.updatePartySizeOptions($scope.rsvp.party_size);
			if (!$scope.rsvp.confirmed_party_size) {
				$scope.rsvp.confirmed_party_size = $scope.rsvp.party_size;
			}
			$scope.form_state = 2;
		}, function errorCallback(response) {
			$scope.setError('Are you sure? We couldn\'t find that RSVP code...');
			$scope.form_state = 0;
		});
	};

	$scope.submitRsvp = function() {
		if ($scope.rsvp.attending && !$scope.rsvp.email) {
			$scope.setError('We\'re gonna need your email address...');
			return;
		}
		$scope.setError();
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
			$scope.setError('Something\'s not right here...');
			$scope.form_state = 2;
		});
	};

	$scope.setError = function(message) {
		if (typeof message === 'undefined') {
			$scope.error_text = '';
		} else {
			$scope.error_text = message;
		}
	};

	$scope.updatePartySizeOptions = function(party_size) {
		var options = [];
		for (var i = 0; i < party_size; i++) {
			options.push(i + 1);
		}
		$scope.party_size_options = options;
	};

}]);
