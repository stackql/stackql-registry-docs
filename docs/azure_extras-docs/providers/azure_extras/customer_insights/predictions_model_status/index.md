---
title: predictions_model_status
hide_title: false
hide_table_of_contents: false
keywords:
  - predictions_model_status
  - customer_insights
  - google
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/google/stackql-google-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>predictions_model_status</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>predictions_model_status</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.customer_insights.predictions_model_status" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="message" /> | `string` | The model status message. |
| <CopyableCode code="modelVersion" /> | `string` | Version of the model. |
| <CopyableCode code="predictionGuidId" /> | `string` | The prediction GUID ID. |
| <CopyableCode code="predictionName" /> | `string` | The prediction name. |
| <CopyableCode code="signalsUsed" /> | `integer` | The signals used. |
| <CopyableCode code="status" /> | `string` | Prediction model life cycle.  When prediction is in PendingModelConfirmation status, it is allowed to update the status to PendingFeaturing or Active through API. |
| <CopyableCode code="tenantId" /> | `string` | The hub name. |
| <CopyableCode code="testSetCount" /> | `integer` | Count of the test set. |
| <CopyableCode code="trainingAccuracy" /> | `integer` | The training accuracy. |
| <CopyableCode code="trainingSetCount" /> | `integer` | Count of the training set. |
| <CopyableCode code="validationSetCount" /> | `integer` | Count of the validation set. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="hubName, predictionName, resourceGroupName, subscriptionId" /> | Gets model status of the prediction. |

## `SELECT` examples

Gets model status of the prediction.


```sql
SELECT
message,
modelVersion,
predictionGuidId,
predictionName,
signalsUsed,
status,
tenantId,
testSetCount,
trainingAccuracy,
trainingSetCount,
validationSetCount
FROM azure_extras.customer_insights.predictions_model_status
WHERE hubName = '{{ hubName }}'
AND predictionName = '{{ predictionName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```