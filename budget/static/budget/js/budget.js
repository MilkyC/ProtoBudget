function editCell(cellId) {
  console.log(['cellId', cellId]);
  document.getElementById(cellId).readOnly = '';
}

function finishEditingCell(apiName, valueChanged, cellId, objectId) {
  document.getElementById(cellId).readOnly = true;
  let params = [];
  params['id'] = objectId;
  params[valueChanged] = document.getElementById(cellId).value;
  makeRequestToApi(apiName, 'partial_update', params).then(function(result) {
    // calculate new totals on backend and update UI.
    makeRequestToApi('computedvalue', 'list', {'budget_period_id': getCurrentBudgetPeriod()}).then(function(result) {
      console.log(['totals result', result]);
      updateComputedCells(result);
    });
  });
}

function updateComputedCells(values) {
  values.forEach(function(value) {
      console.log(['value', value]);
    let cellId = value['name'];
    let amount = value['amount'];
    document.getElementById(cellId).innerHTML = amount;
  });

}

function makeGetRequestToApi(type, operation) {
  let auth = new coreapi.auth.SessionAuthentication({
      csrfCookieName: 'csrftoken',
      csrfHeaderName: 'X-CSRFToken'
  })
  let client = new coreapi.Client({auth: auth});

  let action = [type, operation];
  return client.action(schema, action);
}

function makeRequestToApi(type, operation, params) {
  let auth = new coreapi.auth.SessionAuthentication({
      csrfCookieName: 'csrftoken',
      csrfHeaderName: 'X-CSRFToken'
  })
  let client = new coreapi.Client({auth: auth});

  let action = [type, operation];
  return client.action(schema, action, params);
}

function getCurrentBudgetPeriod() {
  return 6;
}
