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
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>models</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.bigquery.models</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `description` | `string` | Optional. A user-friendly description of this model. |
| `optimalTrialIds` | `array` | Output only. For single-objective [hyperparameter tuning](/bigquery-ml/docs/reference/standard-sql/bigqueryml-syntax-hp-tuning-overview) models, it only contains the best trial. For multi-objective [hyperparameter tuning](/bigquery-ml/docs/reference/standard-sql/bigqueryml-syntax-hp-tuning-overview) models, it contains all Pareto optimal trials sorted by trial_id. |
| `labelColumns` | `array` | Output only. Label columns that were used to train this model. The output of the model will have a "predicted_" prefix to these columns. |
| `hparamTrials` | `array` | Output only. Trials of a [hyperparameter tuning](/bigquery-ml/docs/reference/standard-sql/bigqueryml-syntax-hp-tuning-overview) model sorted by trial_id. |
| `creationTime` | `string` | Output only. The time when this model was created, in millisecs since the epoch. |
| `friendlyName` | `string` | Optional. A descriptive name for this model. |
| `lastModifiedTime` | `string` | Output only. The time when this model was last modified, in millisecs since the epoch. |
| `bestTrialId` | `string` | The best trial_id across all training runs. |
| `etag` | `string` | Output only. A hash of this resource. |
| `trainingRuns` | `array` | Information for all training runs in increasing order of start_time. |
| `encryptionConfiguration` | `object` |  |
| `expirationTime` | `string` | Optional. The time when this model expires, in milliseconds since the epoch. If not present, the model will persist indefinitely. Expired models will be deleted and their storage reclaimed. The defaultTableExpirationMs property of the encapsulating dataset can be used to set a default expirationTime on newly created models. |
| `hparamSearchSpaces` | `object` | Hyperparameter search spaces. These should be a subset of training_options. |
| `modelType` | `string` | Output only. Type of the model resource. |
| `location` | `string` | Output only. The geographic location where the model resides. This value is inherited from the dataset. |
| `featureColumns` | `array` | Output only. Input feature columns that were used to train this model. |
| `defaultTrialId` | `string` | Output only. The default trial_id to use in TVFs when the trial_id is not passed in. For single-objective [hyperparameter tuning](/bigquery-ml/docs/reference/standard-sql/bigqueryml-syntax-hp-tuning-overview) models, this is the best trial ID. For multi-objective [hyperparameter tuning](/bigquery-ml/docs/reference/standard-sql/bigqueryml-syntax-hp-tuning-overview) models, this is the smallest trial ID among all Pareto optimal trials. |
| `modelReference` | `object` |  |
| `labels` | `object` | The labels associated with this model. You can use these to organize and group your models. Label keys and values can be no longer than 63 characters, can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed. Label values are optional. Label keys must start with a letter and each label in the list must have a different key. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `+datasetId, +modelId, projectId` | Gets the specified model resource by model ID. |
| `list` | `SELECT` | `+datasetId, projectId` | Lists all models in the specified dataset. Requires the READER dataset role. After retrieving the list of models, you can get information about a particular model by calling the models.get method. |
| `delete` | `DELETE` | `+datasetId, +modelId, projectId` | Deletes the model specified by modelId from the dataset. |
| `patch` | `EXEC` | `+datasetId, +modelId, projectId` | Patch specific fields in the specified model. |
