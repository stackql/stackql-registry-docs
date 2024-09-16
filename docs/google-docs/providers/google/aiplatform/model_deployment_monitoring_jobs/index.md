---
title: model_deployment_monitoring_jobs
hide_title: false
hide_table_of_contents: false
keywords:
  - model_deployment_monitoring_jobs
  - aiplatform
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

Creates, updates, deletes, gets or lists a <code>model_deployment_monitoring_jobs</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>model_deployment_monitoring_jobs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.aiplatform.model_deployment_monitoring_jobs" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. Resource name of a ModelDeploymentMonitoringJob. |
| <CopyableCode code="analysisInstanceSchemaUri" /> | `string` | YAML schema file uri describing the format of a single instance that you want Tensorflow Data Validation (TFDV) to analyze. If this field is empty, all the feature data types are inferred from predict_instance_schema_uri, meaning that TFDV will use the data in the exact format(data type) as prediction request/response. If there are any data type differences between predict instance and TFDV instance, this field can be used to override the schema. For models trained with Vertex AI, this field must be set as all the fields in predict instance formatted as string. |
| <CopyableCode code="bigqueryTables" /> | `array` | Output only. The created bigquery tables for the job under customer project. Customer could do their own query & analysis. There could be 4 log tables in maximum: 1. Training data logging predict request/response 2. Serving data logging predict request/response |
| <CopyableCode code="createTime" /> | `string` | Output only. Timestamp when this ModelDeploymentMonitoringJob was created. |
| <CopyableCode code="displayName" /> | `string` | Required. The user-defined name of the ModelDeploymentMonitoringJob. The name can be up to 128 characters long and can consist of any UTF-8 characters. Display name of a ModelDeploymentMonitoringJob. |
| <CopyableCode code="enableMonitoringPipelineLogs" /> | `boolean` | If true, the scheduled monitoring pipeline logs are sent to Google Cloud Logging, including pipeline status and anomalies detected. Please note the logs incur cost, which are subject to [Cloud Logging pricing](https://cloud.google.com/logging#pricing). |
| <CopyableCode code="encryptionSpec" /> | `object` | Represents a customer-managed encryption key spec that can be applied to a top-level resource. |
| <CopyableCode code="endpoint" /> | `string` | Required. Endpoint resource name. Format: `projects/{project}/locations/{location}/endpoints/{endpoint}` |
| <CopyableCode code="error" /> | `object` | The `Status` type defines a logical error model that is suitable for different programming environments, including REST APIs and RPC APIs. It is used by [gRPC](https://github.com/grpc). Each `Status` message contains three pieces of data: error code, error message, and error details. You can find out more about this error model and how to work with it in the [API Design Guide](https://cloud.google.com/apis/design/errors). |
| <CopyableCode code="labels" /> | `object` | The labels with user-defined metadata to organize your ModelDeploymentMonitoringJob. Label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed. See https://goo.gl/xmQnxf for more information and examples of labels. |
| <CopyableCode code="latestMonitoringPipelineMetadata" /> | `object` | All metadata of most recent monitoring pipelines. |
| <CopyableCode code="logTtl" /> | `string` | The TTL of BigQuery tables in user projects which stores logs. A day is the basic unit of the TTL and we take the ceil of TTL/86400(a day). e.g. { second: 3600} indicates ttl = 1 day. |
| <CopyableCode code="loggingSamplingStrategy" /> | `object` | Sampling Strategy for logging, can be for both training and prediction dataset. |
| <CopyableCode code="modelDeploymentMonitoringObjectiveConfigs" /> | `array` | Required. The config for monitoring objectives. This is a per DeployedModel config. Each DeployedModel needs to be configured separately. |
| <CopyableCode code="modelDeploymentMonitoringScheduleConfig" /> | `object` | The config for scheduling monitoring job. |
| <CopyableCode code="modelMonitoringAlertConfig" /> | `object` | The alert config for model monitoring. |
| <CopyableCode code="nextScheduleTime" /> | `string` | Output only. Timestamp when this monitoring pipeline will be scheduled to run for the next round. |
| <CopyableCode code="predictInstanceSchemaUri" /> | `string` | YAML schema file uri describing the format of a single instance, which are given to format this Endpoint's prediction (and explanation). If not set, we will generate predict schema from collected predict requests. |
| <CopyableCode code="samplePredictInstance" /> | `any` | Sample Predict instance, same format as PredictRequest.instances, this can be set as a replacement of ModelDeploymentMonitoringJob.predict_instance_schema_uri. If not set, we will generate predict schema from collected predict requests. |
| <CopyableCode code="satisfiesPzi" /> | `boolean` | Output only. Reserved for future use. |
| <CopyableCode code="satisfiesPzs" /> | `boolean` | Output only. Reserved for future use. |
| <CopyableCode code="scheduleState" /> | `string` | Output only. Schedule state when the monitoring job is in Running state. |
| <CopyableCode code="state" /> | `string` | Output only. The detailed state of the monitoring job. When the job is still creating, the state will be 'PENDING'. Once the job is successfully created, the state will be 'RUNNING'. Pause the job, the state will be 'PAUSED'. Resume the job, the state will return to 'RUNNING'. |
| <CopyableCode code="statsAnomaliesBaseDirectory" /> | `object` | The Google Cloud Storage location where the output is to be written to. |
| <CopyableCode code="updateTime" /> | `string` | Output only. Timestamp when this ModelDeploymentMonitoringJob was updated most recently. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="locationsId, modelDeploymentMonitoringJobsId, projectsId" /> | Gets a ModelDeploymentMonitoringJob. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists ModelDeploymentMonitoringJobs in a Location. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates a ModelDeploymentMonitoringJob. It will run periodically on a configured interval. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="locationsId, modelDeploymentMonitoringJobsId, projectsId" /> | Deletes a ModelDeploymentMonitoringJob. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="locationsId, modelDeploymentMonitoringJobsId, projectsId" /> | Updates a ModelDeploymentMonitoringJob. |
| <CopyableCode code="pause" /> | `EXEC` | <CopyableCode code="locationsId, modelDeploymentMonitoringJobsId, projectsId" /> | Pauses a ModelDeploymentMonitoringJob. If the job is running, the server makes a best effort to cancel the job. Will mark ModelDeploymentMonitoringJob.state to 'PAUSED'. |
| <CopyableCode code="resume" /> | `EXEC` | <CopyableCode code="locationsId, modelDeploymentMonitoringJobsId, projectsId" /> | Resumes a paused ModelDeploymentMonitoringJob. It will start to run from next scheduled time. A deleted ModelDeploymentMonitoringJob can't be resumed. |
| <CopyableCode code="search_model_deployment_monitoring_stats_anomalies" /> | `EXEC` | <CopyableCode code="locationsId, modelDeploymentMonitoringJobsId, projectsId" /> | Searches Model Monitoring Statistics generated within a given time window. |

## `SELECT` examples

Lists ModelDeploymentMonitoringJobs in a Location.

```sql
SELECT
name,
analysisInstanceSchemaUri,
bigqueryTables,
createTime,
displayName,
enableMonitoringPipelineLogs,
encryptionSpec,
endpoint,
error,
labels,
latestMonitoringPipelineMetadata,
logTtl,
loggingSamplingStrategy,
modelDeploymentMonitoringObjectiveConfigs,
modelDeploymentMonitoringScheduleConfig,
modelMonitoringAlertConfig,
nextScheduleTime,
predictInstanceSchemaUri,
samplePredictInstance,
satisfiesPzi,
satisfiesPzs,
scheduleState,
state,
statsAnomaliesBaseDirectory,
updateTime
FROM google.aiplatform.model_deployment_monitoring_jobs
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>model_deployment_monitoring_jobs</code> resource.

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
INSERT INTO google.aiplatform.model_deployment_monitoring_jobs (
locationsId,
projectsId,
displayName,
samplePredictInstance,
predictInstanceSchemaUri,
logTtl,
statsAnomaliesBaseDirectory,
modelDeploymentMonitoringScheduleConfig,
endpoint,
modelMonitoringAlertConfig,
encryptionSpec,
labels,
analysisInstanceSchemaUri,
loggingSamplingStrategy,
enableMonitoringPipelineLogs,
modelDeploymentMonitoringObjectiveConfigs
)
SELECT 
'{{ locationsId }}',
'{{ projectsId }}',
'{{ displayName }}',
'{{ samplePredictInstance }}',
'{{ predictInstanceSchemaUri }}',
'{{ logTtl }}',
'{{ statsAnomaliesBaseDirectory }}',
'{{ modelDeploymentMonitoringScheduleConfig }}',
'{{ endpoint }}',
'{{ modelMonitoringAlertConfig }}',
'{{ encryptionSpec }}',
'{{ labels }}',
'{{ analysisInstanceSchemaUri }}',
'{{ loggingSamplingStrategy }}',
true|false,
'{{ modelDeploymentMonitoringObjectiveConfigs }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: displayName
      value: '{{ displayName }}'
    - name: samplePredictInstance
      value: '{{ samplePredictInstance }}'
    - name: predictInstanceSchemaUri
      value: '{{ predictInstanceSchemaUri }}'
    - name: logTtl
      value: '{{ logTtl }}'
    - name: statsAnomaliesBaseDirectory
      value:
        - name: outputUriPrefix
          value: '{{ outputUriPrefix }}'
    - name: modelDeploymentMonitoringScheduleConfig
      value:
        - name: monitorWindow
          value: '{{ monitorWindow }}'
        - name: monitorInterval
          value: '{{ monitorInterval }}'
    - name: endpoint
      value: '{{ endpoint }}'
    - name: modelMonitoringAlertConfig
      value:
        - name: enableLogging
          value: '{{ enableLogging }}'
        - name: emailAlertConfig
          value:
            - name: userEmails
              value:
                - name: type
                  value: '{{ type }}'
        - name: notificationChannels
          value:
            - name: type
              value: '{{ type }}'
    - name: encryptionSpec
      value:
        - name: kmsKeyName
          value: '{{ kmsKeyName }}'
    - name: labels
      value: '{{ labels }}'
    - name: analysisInstanceSchemaUri
      value: '{{ analysisInstanceSchemaUri }}'
    - name: loggingSamplingStrategy
      value:
        - name: randomSampleConfig
          value:
            - name: sampleRate
              value: '{{ sampleRate }}'
    - name: enableMonitoringPipelineLogs
      value: '{{ enableMonitoringPipelineLogs }}'
    - name: modelDeploymentMonitoringObjectiveConfigs
      value:
        - name: $ref
          value: '{{ $ref }}'

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>model_deployment_monitoring_jobs</code> resource.

```sql
/*+ update */
UPDATE google.aiplatform.model_deployment_monitoring_jobs
SET 
displayName = '{{ displayName }}',
samplePredictInstance = '{{ samplePredictInstance }}',
predictInstanceSchemaUri = '{{ predictInstanceSchemaUri }}',
logTtl = '{{ logTtl }}',
statsAnomaliesBaseDirectory = '{{ statsAnomaliesBaseDirectory }}',
modelDeploymentMonitoringScheduleConfig = '{{ modelDeploymentMonitoringScheduleConfig }}',
endpoint = '{{ endpoint }}',
modelMonitoringAlertConfig = '{{ modelMonitoringAlertConfig }}',
encryptionSpec = '{{ encryptionSpec }}',
labels = '{{ labels }}',
analysisInstanceSchemaUri = '{{ analysisInstanceSchemaUri }}',
loggingSamplingStrategy = '{{ loggingSamplingStrategy }}',
enableMonitoringPipelineLogs = true|false,
modelDeploymentMonitoringObjectiveConfigs = '{{ modelDeploymentMonitoringObjectiveConfigs }}'
WHERE 
locationsId = '{{ locationsId }}'
AND modelDeploymentMonitoringJobsId = '{{ modelDeploymentMonitoringJobsId }}'
AND projectsId = '{{ projectsId }}';
```

## `DELETE` example

Deletes the specified <code>model_deployment_monitoring_jobs</code> resource.

```sql
/*+ delete */
DELETE FROM google.aiplatform.model_deployment_monitoring_jobs
WHERE locationsId = '{{ locationsId }}'
AND modelDeploymentMonitoringJobsId = '{{ modelDeploymentMonitoringJobsId }}'
AND projectsId = '{{ projectsId }}';
```
