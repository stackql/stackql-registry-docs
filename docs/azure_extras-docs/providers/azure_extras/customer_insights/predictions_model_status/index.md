---
title: predictions_model_status
hide_title: false
hide_table_of_contents: false
keywords:
  - predictions_model_status
  - customer_insights
  - azure_extras    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Azure resources using SQL
custom_edit_url: null
image: /img/providers/azure/stackql-azure-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>predictions_model_status</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.customer_insights.predictions_model_status</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `message` | `string` | The model status message. |
| `modelVersion` | `string` | Version of the model. |
| `predictionGuidId` | `string` | The prediction GUID ID. |
| `predictionName` | `string` | The prediction name. |
| `signalsUsed` | `integer` | The signals used. |
| `status` | `string` | Prediction model life cycle.  When prediction is in PendingModelConfirmation status, it is allowed to update the status to PendingFeaturing or Active through API. |
| `tenantId` | `string` | The hub name. |
| `testSetCount` | `integer` | Count of the test set. |
| `trainingAccuracy` | `integer` | The training accuracy. |
| `trainingSetCount` | `integer` | Count of the training set. |
| `validationSetCount` | `integer` | Count of the validation set. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get` | `SELECT` | `hubName, predictionName, resourceGroupName, subscriptionId` |
