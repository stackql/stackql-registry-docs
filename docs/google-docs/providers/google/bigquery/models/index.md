---
title: models
hide_title: false
hide_table_of_contents: false
keywords:
  - models
  - bigquery
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

Creates, updates, deletes, gets or lists a <code>models</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>models</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.bigquery.models" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="description" /> | `string` | Optional. A user-friendly description of this model. |
| <CopyableCode code="bestTrialId" /> | `string` | The best trial_id across all training runs. |
| <CopyableCode code="creationTime" /> | `string` | Output only. The time when this model was created, in millisecs since the epoch. |
| <CopyableCode code="defaultTrialId" /> | `string` | Output only. The default trial_id to use in TVFs when the trial_id is not passed in. For single-objective [hyperparameter tuning](https://cloud.google.com/bigquery-ml/docs/reference/standard-sql/bigqueryml-syntax-hp-tuning-overview) models, this is the best trial ID. For multi-objective [hyperparameter tuning](https://cloud.google.com/bigquery-ml/docs/reference/standard-sql/bigqueryml-syntax-hp-tuning-overview) models, this is the smallest trial ID among all Pareto optimal trials. |
| <CopyableCode code="encryptionConfiguration" /> | `object` | Configuration for Cloud KMS encryption settings. |
| <CopyableCode code="etag" /> | `string` | Output only. A hash of this resource. |
| <CopyableCode code="expirationTime" /> | `string` | Optional. The time when this model expires, in milliseconds since the epoch. If not present, the model will persist indefinitely. Expired models will be deleted and their storage reclaimed. The defaultTableExpirationMs property of the encapsulating dataset can be used to set a default expirationTime on newly created models. |
| <CopyableCode code="featureColumns" /> | `array` | Output only. Input feature columns for the model inference. If the model is trained with TRANSFORM clause, these are the input of the TRANSFORM clause. |
| <CopyableCode code="friendlyName" /> | `string` | Optional. A descriptive name for this model. |
| <CopyableCode code="hparamSearchSpaces" /> | `object` | Hyperparameter search spaces. These should be a subset of training_options. |
| <CopyableCode code="hparamTrials" /> | `array` | Output only. Trials of a [hyperparameter tuning](https://cloud.google.com/bigquery-ml/docs/reference/standard-sql/bigqueryml-syntax-hp-tuning-overview) model sorted by trial_id. |
| <CopyableCode code="labelColumns" /> | `array` | Output only. Label columns that were used to train this model. The output of the model will have a "predicted_" prefix to these columns. |
| <CopyableCode code="labels" /> | `object` | The labels associated with this model. You can use these to organize and group your models. Label keys and values can be no longer than 63 characters, can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed. Label values are optional. Label keys must start with a letter and each label in the list must have a different key. |
| <CopyableCode code="lastModifiedTime" /> | `string` | Output only. The time when this model was last modified, in millisecs since the epoch. |
| <CopyableCode code="location" /> | `string` | Output only. The geographic location where the model resides. This value is inherited from the dataset. |
| <CopyableCode code="modelReference" /> | `object` | Id path of a model. |
| <CopyableCode code="modelType" /> | `string` | Output only. Type of the model resource. |
| <CopyableCode code="optimalTrialIds" /> | `array` | Output only. For single-objective [hyperparameter tuning](https://cloud.google.com/bigquery-ml/docs/reference/standard-sql/bigqueryml-syntax-hp-tuning-overview) models, it only contains the best trial. For multi-objective [hyperparameter tuning](https://cloud.google.com/bigquery-ml/docs/reference/standard-sql/bigqueryml-syntax-hp-tuning-overview) models, it contains all Pareto optimal trials sorted by trial_id. |
| <CopyableCode code="remoteModelInfo" /> | `object` | Remote Model Info |
| <CopyableCode code="trainingRuns" /> | `array` | Information for all training runs in increasing order of start_time. |
| <CopyableCode code="transformColumns" /> | `array` | Output only. This field will be populated if a TRANSFORM clause was used to train a model. TRANSFORM clause (if used) takes feature_columns as input and outputs transform_columns. transform_columns then are used to train the model. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="+datasetId, +modelId, projectId" /> | Gets the specified model resource by model ID. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="+datasetId, projectId" /> | Lists all models in the specified dataset. Requires the READER dataset role. After retrieving the list of models, you can get information about a particular model by calling the models.get method. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="+datasetId, +modelId, projectId" /> | Deletes the model specified by modelId from the dataset. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="+datasetId, +modelId, projectId" /> | Patch specific fields in the specified model. |

## `SELECT` examples

Lists all models in the specified dataset. Requires the READER dataset role. After retrieving the list of models, you can get information about a particular model by calling the models.get method.

```sql
SELECT
description,
bestTrialId,
creationTime,
defaultTrialId,
encryptionConfiguration,
etag,
expirationTime,
featureColumns,
friendlyName,
hparamSearchSpaces,
hparamTrials,
labelColumns,
labels,
lastModifiedTime,
location,
modelReference,
modelType,
optimalTrialIds,
remoteModelInfo,
trainingRuns,
transformColumns
FROM google.bigquery.models
WHERE +datasetId = '{{ +datasetId }}'
AND projectId = '{{ projectId }}'; 
```

## `UPDATE` example

Updates a <code>models</code> resource.

```sql
/*+ update */
UPDATE google.bigquery.models
SET 
bestTrialId = '{{ bestTrialId }}',
description = '{{ description }}',
encryptionConfiguration = '{{ encryptionConfiguration }}',
expirationTime = '{{ expirationTime }}',
friendlyName = '{{ friendlyName }}',
labels = '{{ labels }}',
modelReference = '{{ modelReference }}',
trainingRuns = '{{ trainingRuns }}'
WHERE 
+datasetId = '{{ +datasetId }}'
AND +modelId = '{{ +modelId }}'
AND projectId = '{{ projectId }}';
```

## `DELETE` example

Deletes the specified <code>models</code> resource.

```sql
/*+ delete */
DELETE FROM google.bigquery.models
WHERE +datasetId = '{{ +datasetId }}'
AND +modelId = '{{ +modelId }}'
AND projectId = '{{ projectId }}';
```
