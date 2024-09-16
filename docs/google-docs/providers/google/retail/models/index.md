---
title: models
hide_title: false
hide_table_of_contents: false
keywords:
  - models
  - retail
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
<tr><td><b>Id</b></td><td><CopyableCode code="google.retail.models" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Required. The fully qualified resource name of the model. Format: `projects/{project_number}/locations/{location_id}/catalogs/{catalog_id}/models/{model_id}` catalog_id has char limit of 50. recommendation_model_id has char limit of 40. |
| <CopyableCode code="createTime" /> | `string` | Output only. Timestamp the Recommendation Model was created at. |
| <CopyableCode code="dataState" /> | `string` | Output only. The state of data requirements for this model: `DATA_OK` and `DATA_ERROR`. Recommendation model cannot be trained if the data is in `DATA_ERROR` state. Recommendation model can have `DATA_ERROR` state even if serving state is `ACTIVE`: models were trained successfully before, but cannot be refreshed because model no longer has sufficient data for training. |
| <CopyableCode code="displayName" /> | `string` | Required. The display name of the model. Should be human readable, used to display Recommendation Models in the Retail Cloud Console Dashboard. UTF-8 encoded string with limit of 1024 characters. |
| <CopyableCode code="filteringOption" /> | `string` | Optional. If `RECOMMENDATIONS_FILTERING_ENABLED`, recommendation filtering by attributes is enabled for the model. |
| <CopyableCode code="lastTuneTime" /> | `string` | Output only. The timestamp when the latest successful tune finished. |
| <CopyableCode code="modelFeaturesConfig" /> | `object` | Additional model features config. |
| <CopyableCode code="optimizationObjective" /> | `string` | Optional. The optimization objective e.g. `cvr`. Currently supported values: `ctr`, `cvr`, `revenue-per-order`. If not specified, we choose default based on model type. Default depends on type of recommendation: `recommended-for-you` => `ctr` `others-you-may-like` => `ctr` `frequently-bought-together` => `revenue_per_order` This field together with optimization_objective describe model metadata to use to control model training and serving. See https://cloud.google.com/retail/docs/models for more details on what the model metadata control and which combination of parameters are valid. For invalid combinations of parameters (e.g. type = `frequently-bought-together` and optimization_objective = `ctr`), you receive an error 400 if you try to create/update a recommendation with this set of knobs. |
| <CopyableCode code="periodicTuningState" /> | `string` | Optional. The state of periodic tuning. The period we use is 3 months - to do a one-off tune earlier use the `TuneModel` method. Default value is `PERIODIC_TUNING_ENABLED`. |
| <CopyableCode code="servingConfigLists" /> | `array` | Output only. The list of valid serving configs associated with the PageOptimizationConfig. |
| <CopyableCode code="servingState" /> | `string` | Output only. The serving state of the model: `ACTIVE`, `NOT_ACTIVE`. |
| <CopyableCode code="trainingState" /> | `string` | Optional. The training state that the model is in (e.g. `TRAINING` or `PAUSED`). Since part of the cost of running the service is frequency of training - this can be used to determine when to train model in order to control cost. If not specified: the default value for `CreateModel` method is `TRAINING`. The default value for `UpdateModel` method is to keep the state the same as before. |
| <CopyableCode code="tuningOperation" /> | `string` | Output only. The tune operation associated with the model. Can be used to determine if there is an ongoing tune for this recommendation. Empty field implies no tune is goig on. |
| <CopyableCode code="type" /> | `string` | Required. The type of model e.g. `home-page`. Currently supported values: `recommended-for-you`, `others-you-may-like`, `frequently-bought-together`, `page-optimization`, `similar-items`, `buy-it-again`, `on-sale-items`, and `recently-viewed`(readonly value). This field together with optimization_objective describe model metadata to use to control model training and serving. See https://cloud.google.com/retail/docs/models for more details on what the model metadata control and which combination of parameters are valid. For invalid combinations of parameters (e.g. type = `frequently-bought-together` and optimization_objective = `ctr`), you receive an error 400 if you try to create/update a recommendation with this set of knobs. |
| <CopyableCode code="updateTime" /> | `string` | Output only. Timestamp the Recommendation Model was last updated. E.g. if a Recommendation Model was paused - this would be the time the pause was initiated. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_locations_catalogs_models_get" /> | `SELECT` | <CopyableCode code="catalogsId, locationsId, modelsId, projectsId" /> | Gets a model. |
| <CopyableCode code="projects_locations_catalogs_models_list" /> | `SELECT` | <CopyableCode code="catalogsId, locationsId, projectsId" /> | Lists all the models linked to this event store. |
| <CopyableCode code="projects_locations_catalogs_models_create" /> | `INSERT` | <CopyableCode code="catalogsId, locationsId, projectsId" /> | Creates a new model. |
| <CopyableCode code="projects_locations_catalogs_models_delete" /> | `DELETE` | <CopyableCode code="catalogsId, locationsId, modelsId, projectsId" /> | Deletes an existing model. |
| <CopyableCode code="projects_locations_catalogs_models_patch" /> | `UPDATE` | <CopyableCode code="catalogsId, locationsId, modelsId, projectsId" /> | Update of model metadata. Only fields that currently can be updated are: `filtering_option` and `periodic_tuning_state`. If other values are provided, this API method ignores them. |
| <CopyableCode code="projects_locations_catalogs_models_pause" /> | `EXEC` | <CopyableCode code="catalogsId, locationsId, modelsId, projectsId" /> | Pauses the training of an existing model. |
| <CopyableCode code="projects_locations_catalogs_models_resume" /> | `EXEC` | <CopyableCode code="catalogsId, locationsId, modelsId, projectsId" /> | Resumes the training of an existing model. |
| <CopyableCode code="projects_locations_catalogs_models_tune" /> | `EXEC` | <CopyableCode code="catalogsId, locationsId, modelsId, projectsId" /> | Tunes an existing model. |

## `SELECT` examples

Lists all the models linked to this event store.

```sql
SELECT
name,
createTime,
dataState,
displayName,
filteringOption,
lastTuneTime,
modelFeaturesConfig,
optimizationObjective,
periodicTuningState,
servingConfigLists,
servingState,
trainingState,
tuningOperation,
type,
updateTime
FROM google.retail.models
WHERE catalogsId = '{{ catalogsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>models</code> resource.

<Tabs
    defaultValue="all"
    values={[
        { label: 'All Properties', value: 'all', },
        { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO google.retail.models (
catalogsId,
locationsId,
projectsId,
name,
displayName,
trainingState,
type,
optimizationObjective,
periodicTuningState,
filteringOption,
modelFeaturesConfig
)
SELECT 
'{{ catalogsId }}',
'{{ locationsId }}',
'{{ projectsId }}',
'{{ name }}',
'{{ displayName }}',
'{{ trainingState }}',
'{{ type }}',
'{{ optimizationObjective }}',
'{{ periodicTuningState }}',
'{{ filteringOption }}',
'{{ modelFeaturesConfig }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: name
      value: '{{ name }}'
    - name: displayName
      value: '{{ displayName }}'
    - name: trainingState
      value: '{{ trainingState }}'
    - name: type
      value: '{{ type }}'
    - name: optimizationObjective
      value: '{{ optimizationObjective }}'
    - name: periodicTuningState
      value: '{{ periodicTuningState }}'
    - name: filteringOption
      value: '{{ filteringOption }}'
    - name: modelFeaturesConfig
      value:
        - name: frequentlyBoughtTogetherConfig
          value:
            - name: contextProductsType
              value: '{{ contextProductsType }}'

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>models</code> resource.

```sql
/*+ update */
UPDATE google.retail.models
SET 
name = '{{ name }}',
displayName = '{{ displayName }}',
trainingState = '{{ trainingState }}',
type = '{{ type }}',
optimizationObjective = '{{ optimizationObjective }}',
periodicTuningState = '{{ periodicTuningState }}',
filteringOption = '{{ filteringOption }}',
modelFeaturesConfig = '{{ modelFeaturesConfig }}'
WHERE 
catalogsId = '{{ catalogsId }}'
AND locationsId = '{{ locationsId }}'
AND modelsId = '{{ modelsId }}'
AND projectsId = '{{ projectsId }}';
```

## `DELETE` example

Deletes the specified <code>models</code> resource.

```sql
/*+ delete */
DELETE FROM google.retail.models
WHERE catalogsId = '{{ catalogsId }}'
AND locationsId = '{{ locationsId }}'
AND modelsId = '{{ modelsId }}'
AND projectsId = '{{ projectsId }}';
```
