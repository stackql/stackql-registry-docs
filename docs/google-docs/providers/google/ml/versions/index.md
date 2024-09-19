---
title: versions
hide_title: false
hide_table_of_contents: false
keywords:
  - versions
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

Creates, updates, deletes, gets or lists a <code>versions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>versions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.ml.versions" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Required. The name specified for the version when it was created. The version name must be unique within the model it is created in. |
| <CopyableCode code="description" /> | `string` | Optional. The description specified for the version when it was created. |
| <CopyableCode code="acceleratorConfig" /> | `object` | Represents a hardware accelerator request config. Note that the AcceleratorConfig can be used in both Jobs and Versions. Learn more about [accelerators for training](/ml-engine/docs/using-gpus) and [accelerators for online prediction](/ml-engine/docs/machine-types-online-prediction#gpus). |
| <CopyableCode code="autoScaling" /> | `object` | Options for automatically scaling a model. |
| <CopyableCode code="container" /> | `object` | Specification of a custom container for serving predictions. This message is a subset of the [Kubernetes Container v1 core specification](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.18/#container-v1-core). |
| <CopyableCode code="createTime" /> | `string` | Output only. The time the version was created. |
| <CopyableCode code="deploymentUri" /> | `string` | The Cloud Storage URI of a directory containing trained model artifacts to be used to create the model version. See the [guide to deploying models](/ai-platform/prediction/docs/deploying-models) for more information. The total number of files under this directory must not exceed 1000. During projects.models.versions.create, AI Platform Prediction copies all files from the specified directory to a location managed by the service. From then on, AI Platform Prediction uses these copies of the model artifacts to serve predictions, not the original files in Cloud Storage, so this location is useful only as a historical record. If you specify container, then this field is optional. Otherwise, it is required. Learn [how to use this field with a custom container](/ai-platform/prediction/docs/custom-container-requirements#artifacts). |
| <CopyableCode code="errorMessage" /> | `string` | Output only. The details of a failure or a cancellation. |
| <CopyableCode code="etag" /> | `string` | `etag` is used for optimistic concurrency control as a way to help prevent simultaneous updates of a model from overwriting each other. It is strongly suggested that systems make use of the `etag` in the read-modify-write cycle to perform model updates in order to avoid race conditions: An `etag` is returned in the response to `GetVersion`, and systems are expected to put that etag in the request to `UpdateVersion` to ensure that their change will be applied to the model as intended. |
| <CopyableCode code="explanationConfig" /> | `object` | Message holding configuration options for explaining model predictions. There are three feature attribution methods supported for TensorFlow models: integrated gradients, sampled Shapley, and XRAI. [Learn more about feature attributions.](/ai-platform/prediction/docs/ai-explanations/overview) |
| <CopyableCode code="framework" /> | `string` | Optional. The machine learning framework AI Platform uses to train this version of the model. Valid values are `TENSORFLOW`, `SCIKIT_LEARN`, `XGBOOST`. If you do not specify a framework, AI Platform will analyze files in the deployment_uri to determine a framework. If you choose `SCIKIT_LEARN` or `XGBOOST`, you must also set the runtime version of the model to 1.4 or greater. Do **not** specify a framework if you're deploying a [custom prediction routine](/ai-platform/prediction/docs/custom-prediction-routines) or if you're using a [custom container](/ai-platform/prediction/docs/use-custom-container). |
| <CopyableCode code="isDefault" /> | `boolean` | Output only. If true, this version will be used to handle prediction requests that do not specify a version. You can change the default version by calling projects.methods.versions.setDefault. |
| <CopyableCode code="labels" /> | `object` | Optional. One or more labels that you can add, to organize your model versions. Each label is a key-value pair, where both the key and the value are arbitrary strings that you supply. For more information, see the documentation on using labels. Note that this field is not updatable for mls1* models. |
| <CopyableCode code="lastMigrationModelId" /> | `string` | Output only. The [AI Platform (Unified) `Model`](https://cloud.google.com/ai-platform-unified/docs/reference/rest/v1beta1/projects.locations.models) ID for the last [model migration](https://cloud.google.com/ai-platform-unified/docs/start/migrating-to-ai-platform-unified). |
| <CopyableCode code="lastMigrationTime" /> | `string` | Output only. The last time this version was successfully [migrated to AI Platform (Unified)](https://cloud.google.com/ai-platform-unified/docs/start/migrating-to-ai-platform-unified). |
| <CopyableCode code="lastUseTime" /> | `string` | Output only. The time the version was last used for prediction. |
| <CopyableCode code="machineType" /> | `string` | Optional. The type of machine on which to serve the model. Currently only applies to online prediction service. To learn about valid values for this field, read [Choosing a machine type for online prediction](/ai-platform/prediction/docs/machine-types-online-prediction). If this field is not specified and you are using a [regional endpoint](/ai-platform/prediction/docs/regional-endpoints), then the machine type defaults to `n1-standard-2`. If this field is not specified and you are using the global endpoint (`ml.googleapis.com`), then the machine type defaults to `mls1-c1-m2`. |
| <CopyableCode code="manualScaling" /> | `object` | Options for manually scaling a model. |
| <CopyableCode code="packageUris" /> | `array` | Optional. Cloud Storage paths (`gs://…`) of packages for [custom prediction routines](/ml-engine/docs/tensorflow/custom-prediction-routines) or [scikit-learn pipelines with custom code](/ml-engine/docs/scikit/exporting-for-prediction#custom-pipeline-code). For a custom prediction routine, one of these packages must contain your Predictor class (see [`predictionClass`](#Version.FIELDS.prediction_class)). Additionally, include any dependencies used by your Predictor or scikit-learn pipeline uses that are not already included in your selected [runtime version](/ml-engine/docs/tensorflow/runtime-version-list). If you specify this field, you must also set [`runtimeVersion`](#Version.FIELDS.runtime_version) to 1.4 or greater. |
| <CopyableCode code="predictionClass" /> | `string` | Optional. The fully qualified name (module_name.class_name) of a class that implements the Predictor interface described in this reference field. The module containing this class should be included in a package provided to the [`packageUris` field](#Version.FIELDS.package_uris). Specify this field if and only if you are deploying a [custom prediction routine (beta)](/ml-engine/docs/tensorflow/custom-prediction-routines). If you specify this field, you must set [`runtimeVersion`](#Version.FIELDS.runtime_version) to 1.4 or greater and you must set `machineType` to a [legacy (MLS1) machine type](/ml-engine/docs/machine-types-online-prediction). The following code sample provides the Predictor interface: class Predictor(object): """Interface for constructing custom predictors.""" def predict(self, instances, **kwargs): """Performs custom prediction. Instances are the decoded values from the request. They have already been deserialized from JSON. Args: instances: A list of prediction input instances. **kwargs: A dictionary of keyword args provided as additional fields on the predict request body. Returns: A list of outputs containing the prediction results. This list must be JSON serializable. """ raise NotImplementedError() @classmethod def from_path(cls, model_dir): """Creates an instance of Predictor using the given path. Loading of the predictor should be done in this method. Args: model_dir: The local directory that contains the exported model file along with any additional files uploaded when creating the version resource. Returns: An instance implementing this Predictor class. """ raise NotImplementedError() Learn more about [the Predictor interface and custom prediction routines](/ml-engine/docs/tensorflow/custom-prediction-routines). |
| <CopyableCode code="pythonVersion" /> | `string` | Required. The version of Python used in prediction. The following Python versions are available: * Python '3.7' is available when `runtime_version` is set to '1.15' or later. * Python '3.5' is available when `runtime_version` is set to a version from '1.4' to '1.14'. * Python '2.7' is available when `runtime_version` is set to '1.15' or earlier. Read more about the Python versions available for [each runtime version](/ml-engine/docs/runtime-version-list). |
| <CopyableCode code="requestLoggingConfig" /> | `object` | Configuration for logging request-response pairs to a BigQuery table. Online prediction requests to a model version and the responses to these requests are converted to raw strings and saved to the specified BigQuery table. Logging is constrained by [BigQuery quotas and limits](/bigquery/quotas). If your project exceeds BigQuery quotas or limits, AI Platform Prediction does not log request-response pairs, but it continues to serve predictions. If you are using [continuous evaluation](/ml-engine/docs/continuous-evaluation/), you do not need to specify this configuration manually. Setting up continuous evaluation automatically enables logging of request-response pairs. |
| <CopyableCode code="routes" /> | `object` | Specifies HTTP paths served by a custom container. AI Platform Prediction sends requests to these paths on the container; the custom container must run an HTTP server that responds to these requests with appropriate responses. Read [Custom container requirements](/ai-platform/prediction/docs/custom-container-requirements) for details on how to create your container image to meet these requirements. |
| <CopyableCode code="runtimeVersion" /> | `string` | Required. The AI Platform runtime version to use for this deployment. For more information, see the [runtime version list](/ml-engine/docs/runtime-version-list) and [how to manage runtime versions](/ml-engine/docs/versioning). |
| <CopyableCode code="serviceAccount" /> | `string` | Optional. Specifies the service account for resource access control. If you specify this field, then you must also specify either the `containerSpec` or the `predictionClass` field. Learn more about [using a custom service account](/ai-platform/prediction/docs/custom-service-account). |
| <CopyableCode code="state" /> | `string` | Output only. The state of a version. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_models_versions_get" /> | `SELECT` | <CopyableCode code="modelsId, projectsId, versionsId" /> | Gets information about a model version. Models can have multiple versions. You can call projects.models.versions.list to get the same information that this method returns for all of the versions of a model. |
| <CopyableCode code="projects_models_versions_list" /> | `SELECT` | <CopyableCode code="modelsId, projectsId" /> | Gets basic information about all the versions of a model. If you expect that a model has many versions, or if you need to handle only a limited number of results at a time, you can request that the list be retrieved in batches (called pages). If there are no versions that match the request parameters, the list request returns an empty response body: {}. |
| <CopyableCode code="projects_models_versions_create" /> | `INSERT` | <CopyableCode code="modelsId, projectsId" /> | Creates a new version of a model from a trained TensorFlow model. If the version created in the cloud by this call is the first deployed version of the specified model, it will be made the default version of the model. When you add a version to a model that already has one or more versions, the default version does not automatically change. If you want a new version to be the default, you must call projects.models.versions.setDefault. |
| <CopyableCode code="projects_models_versions_delete" /> | `DELETE` | <CopyableCode code="modelsId, projectsId, versionsId" /> | Deletes a model version. Each model can have multiple versions deployed and in use at any given time. Use this method to remove a single version. Note: You cannot delete the version that is set as the default version of the model unless it is the only remaining version. |
| <CopyableCode code="projects_models_versions_patch" /> | `UPDATE` | <CopyableCode code="modelsId, projectsId, versionsId" /> | Updates the specified Version resource. Currently the only update-able fields are `description`, `requestLoggingConfig`, `autoScaling.minNodes`, and `manualScaling.nodes`. |
| <CopyableCode code="projects_models_versions_set_default" /> | `EXEC` | <CopyableCode code="modelsId, projectsId, versionsId" /> | Designates a version to be the default for the model. The default version is used for prediction requests made against the model that don't specify a version. The first version to be created for a model is automatically set as the default. You must make any subsequent changes to the default version setting manually using this method. |

## `SELECT` examples

Gets basic information about all the versions of a model. If you expect that a model has many versions, or if you need to handle only a limited number of results at a time, you can request that the list be retrieved in batches (called pages). If there are no versions that match the request parameters, the list request returns an empty response body: {}.

```sql
SELECT
name,
description,
acceleratorConfig,
autoScaling,
container,
createTime,
deploymentUri,
errorMessage,
etag,
explanationConfig,
framework,
isDefault,
labels,
lastMigrationModelId,
lastMigrationTime,
lastUseTime,
machineType,
manualScaling,
packageUris,
predictionClass,
pythonVersion,
requestLoggingConfig,
routes,
runtimeVersion,
serviceAccount,
state
FROM google.ml.versions
WHERE modelsId = '{{ modelsId }}'
AND projectsId = '{{ projectsId }}';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>versions</code> resource.

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
INSERT INTO google.ml.versions (
modelsId,
projectsId,
name,
description,
isDefault,
deploymentUri,
lastUseTime,
runtimeVersion,
machineType,
autoScaling,
manualScaling,
state,
errorMessage,
predictionClass,
packageUris,
labels,
etag,
framework,
pythonVersion,
acceleratorConfig,
serviceAccount,
requestLoggingConfig,
explanationConfig,
container,
routes
)
SELECT 
'{{ modelsId }}',
'{{ projectsId }}',
'{{ name }}',
'{{ description }}',
{{ isDefault }},
'{{ deploymentUri }}',
'{{ lastUseTime }}',
'{{ runtimeVersion }}',
'{{ machineType }}',
'{{ autoScaling }}',
'{{ manualScaling }}',
'{{ state }}',
'{{ errorMessage }}',
'{{ predictionClass }}',
'{{ packageUris }}',
'{{ labels }}',
'{{ etag }}',
'{{ framework }}',
'{{ pythonVersion }}',
'{{ acceleratorConfig }}',
'{{ serviceAccount }}',
'{{ requestLoggingConfig }}',
'{{ explanationConfig }}',
'{{ container }}',
'{{ routes }}'
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

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>versions</code> resource.

```sql
/*+ update */
UPDATE google.ml.versions
SET 
name = '{{ name }}',
description = '{{ description }}',
isDefault = true|false,
deploymentUri = '{{ deploymentUri }}',
lastUseTime = '{{ lastUseTime }}',
runtimeVersion = '{{ runtimeVersion }}',
machineType = '{{ machineType }}',
autoScaling = '{{ autoScaling }}',
manualScaling = '{{ manualScaling }}',
state = '{{ state }}',
errorMessage = '{{ errorMessage }}',
predictionClass = '{{ predictionClass }}',
packageUris = '{{ packageUris }}',
labels = '{{ labels }}',
etag = '{{ etag }}',
framework = '{{ framework }}',
pythonVersion = '{{ pythonVersion }}',
acceleratorConfig = '{{ acceleratorConfig }}',
serviceAccount = '{{ serviceAccount }}',
requestLoggingConfig = '{{ requestLoggingConfig }}',
explanationConfig = '{{ explanationConfig }}',
container = '{{ container }}',
routes = '{{ routes }}'
WHERE 
modelsId = '{{ modelsId }}'
AND projectsId = '{{ projectsId }}'
AND versionsId = '{{ versionsId }}';
```

## `DELETE` example

Deletes the specified <code>versions</code> resource.

```sql
/*+ delete */
DELETE FROM google.ml.versions
WHERE modelsId = '{{ modelsId }}'
AND projectsId = '{{ projectsId }}'
AND versionsId = '{{ versionsId }}';
```
