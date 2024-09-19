---
title: models
hide_title: false
hide_table_of_contents: false
keywords:
  - models
  - ml
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
<tr><td><b>Id</b></td><td><CopyableCode code="google.ml.models" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Required. The name specified for the model when it was created. The model name must be unique within the project it is created in. |
| <CopyableCode code="description" /> | `string` | Optional. The description specified for the model when it was created. |
| <CopyableCode code="defaultVersion" /> | `object` | Represents a version of the model. Each version is a trained model deployed in the cloud, ready to handle prediction requests. A model can have multiple versions. You can get information about all of the versions of a given model by calling projects.models.versions.list. |
| <CopyableCode code="etag" /> | `string` | `etag` is used for optimistic concurrency control as a way to help prevent simultaneous updates of a model from overwriting each other. It is strongly suggested that systems make use of the `etag` in the read-modify-write cycle to perform model updates in order to avoid race conditions: An `etag` is returned in the response to `GetModel`, and systems are expected to put that etag in the request to `UpdateModel` to ensure that their change will be applied to the model as intended. |
| <CopyableCode code="labels" /> | `object` | Optional. One or more labels that you can add, to organize your models. Each label is a key-value pair, where both the key and the value are arbitrary strings that you supply. For more information, see the documentation on using labels. Note that this field is not updatable for mls1* models. |
| <CopyableCode code="onlinePredictionConsoleLogging" /> | `boolean` | Optional. If true, online prediction nodes send `stderr` and `stdout` streams to Cloud Logging. These can be more verbose than the standard access logs (see `onlinePredictionLogging`) and can incur higher cost. However, they are helpful for debugging. Note that [logs may incur a cost](/stackdriver/pricing), especially if your project receives prediction requests at a high QPS. Estimate your costs before enabling this option. Default is false. |
| <CopyableCode code="onlinePredictionLogging" /> | `boolean` | Optional. If true, online prediction access logs are sent to Cloud Logging. These logs are like standard server access logs, containing information like timestamp and latency for each request. Note that [logs may incur a cost](/stackdriver/pricing), especially if your project receives prediction requests at a high queries per second rate (QPS). Estimate your costs before enabling this option. Default is false. |
| <CopyableCode code="regions" /> | `array` | Optional. The list of regions where the model is going to be deployed. Only one region per model is supported. Defaults to 'us-central1' if nothing is set. See the available regions for AI Platform services. Note: * No matter where a model is deployed, it can always be accessed by users from anywhere, both for online and batch prediction. * The region for a batch prediction job is set by the region field when submitting the batch prediction job and does not take its value from this field. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_models_get" /> | `SELECT` | <CopyableCode code="modelsId, projectsId" /> | Gets information about a model, including its name, the description (if set), and the default version (if at least one version of the model has been deployed). |
| <CopyableCode code="projects_models_list" /> | `SELECT` | <CopyableCode code="projectsId" /> | Lists the models in a project. Each project can contain multiple models, and each model can have multiple versions. If there are no models that match the request parameters, the list request returns an empty response body: {}. |
| <CopyableCode code="projects_models_create" /> | `INSERT` | <CopyableCode code="projectsId" /> | Creates a model which will later contain one or more versions. You must add at least one version before you can request predictions from the model. Add versions by calling projects.models.versions.create. |
| <CopyableCode code="projects_models_delete" /> | `DELETE` | <CopyableCode code="modelsId, projectsId" /> | Deletes a model. You can only delete a model if there are no versions in it. You can delete versions by calling projects.models.versions.delete. |
| <CopyableCode code="projects_models_patch" /> | `UPDATE` | <CopyableCode code="modelsId, projectsId" /> | Updates a specific model resource. Currently the only supported fields to update are `description` and `default_version.name`. |

## `SELECT` examples

Lists the models in a project. Each project can contain multiple models, and each model can have multiple versions. If there are no models that match the request parameters, the list request returns an empty response body: {}.

```sql
SELECT
name,
description,
defaultVersion,
etag,
labels,
onlinePredictionConsoleLogging,
onlinePredictionLogging,
regions
FROM google.ml.models
WHERE projectsId = '{{ projectsId }}';
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
INSERT INTO google.ml.models (
projectsId,
name,
description,
defaultVersion,
regions,
onlinePredictionLogging,
onlinePredictionConsoleLogging,
labels,
etag
)
SELECT 
'{{ projectsId }}',
'{{ name }}',
'{{ description }}',
'{{ defaultVersion }}',
'{{ regions }}',
{{ onlinePredictionLogging }},
{{ onlinePredictionConsoleLogging }},
'{{ labels }}',
'{{ etag }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: name
      value: string
    - name: description
      value: string
    - name: defaultVersion
      value:
        - name: name
          value: string
        - name: description
          value: string
        - name: isDefault
          value: boolean
        - name: deploymentUri
          value: string
        - name: createTime
          value: string
        - name: lastUseTime
          value: string
        - name: runtimeVersion
          value: string
        - name: machineType
          value: string
        - name: autoScaling
          value:
            - name: minNodes
              value: integer
            - name: maxNodes
              value: integer
            - name: metrics
              value:
                - - name: name
                    value: string
                  - name: target
                    value: integer
        - name: manualScaling
          value:
            - name: nodes
              value: integer
        - name: state
          value: string
        - name: errorMessage
          value: string
        - name: predictionClass
          value: string
        - name: packageUris
          value:
            - string
        - name: labels
          value: object
        - name: etag
          value: string
        - name: framework
          value: string
        - name: pythonVersion
          value: string
        - name: acceleratorConfig
          value:
            - name: count
              value: string
            - name: type
              value: string
        - name: serviceAccount
          value: string
        - name: requestLoggingConfig
          value:
            - name: samplingPercentage
              value: number
            - name: bigqueryTableName
              value: string
        - name: explanationConfig
          value:
            - name: integratedGradientsAttribution
              value:
                - name: numIntegralSteps
                  value: integer
            - name: sampledShapleyAttribution
              value:
                - name: numPaths
                  value: integer
            - name: xraiAttribution
              value:
                - name: numIntegralSteps
                  value: integer
        - name: container
          value:
            - name: image
              value: string
            - name: command
              value:
                - string
            - name: args
              value:
                - string
            - name: ports
              value:
                - - name: containerPort
                    value: integer
            - name: env
              value:
                - - name: name
                    value: string
                  - name: value
                    value: string
        - name: routes
          value:
            - name: predict
              value: string
            - name: health
              value: string
        - name: lastMigrationTime
          value: string
        - name: lastMigrationModelId
          value: string
    - name: regions
      value:
        - string
    - name: onlinePredictionLogging
      value: boolean
    - name: onlinePredictionConsoleLogging
      value: boolean
    - name: labels
      value: object
    - name: etag
      value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>models</code> resource.

```sql
/*+ update */
UPDATE google.ml.models
SET 
name = '{{ name }}',
description = '{{ description }}',
defaultVersion = '{{ defaultVersion }}',
regions = '{{ regions }}',
onlinePredictionLogging = true|false,
onlinePredictionConsoleLogging = true|false,
labels = '{{ labels }}',
etag = '{{ etag }}'
WHERE 
modelsId = '{{ modelsId }}'
AND projectsId = '{{ projectsId }}';
```

## `DELETE` example

Deletes the specified <code>models</code> resource.

```sql
/*+ delete */
DELETE FROM google.ml.models
WHERE modelsId = '{{ modelsId }}'
AND projectsId = '{{ projectsId }}';
```
