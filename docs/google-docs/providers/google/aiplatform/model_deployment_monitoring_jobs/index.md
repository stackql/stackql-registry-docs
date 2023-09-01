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
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>model_deployment_monitoring_jobs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.aiplatform.model_deployment_monitoring_jobs</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. Resource name of a ModelDeploymentMonitoringJob. |
| `loggingSamplingStrategy` | `object` | Sampling Strategy for logging, can be for both training and prediction dataset. |
| `modelMonitoringAlertConfig` | `object` |  |
| `scheduleState` | `string` | Output only. Schedule state when the monitoring job is in Running state. |
| `displayName` | `string` | Required. The user-defined name of the ModelDeploymentMonitoringJob. The name can be up to 128 characters long and can consist of any UTF-8 characters. Display name of a ModelDeploymentMonitoringJob. |
| `samplePredictInstance` | `any` | Sample Predict instance, same format as PredictRequest.instances, this can be set as a replacement of ModelDeploymentMonitoringJob.predict_instance_schema_uri. If not set, we will generate predict schema from collected predict requests. |
| `latestMonitoringPipelineMetadata` | `object` | All metadata of most recent monitoring pipelines. |
| `labels` | `object` | The labels with user-defined metadata to organize your ModelDeploymentMonitoringJob. Label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed. See https://goo.gl/xmQnxf for more information and examples of labels. |
| `createTime` | `string` | Output only. Timestamp when this ModelDeploymentMonitoringJob was created. |
| `state` | `string` | Output only. The detailed state of the monitoring job. When the job is still creating, the state will be 'PENDING'. Once the job is successfully created, the state will be 'RUNNING'. Pause the job, the state will be 'PAUSED'. Resume the job, the state will return to 'RUNNING'. |
| `bigqueryTables` | `array` | Output only. The created bigquery tables for the job under customer project. Customer could do their own query & analysis. There could be 4 log tables in maximum: 1. Training data logging predict request/response 2. Serving data logging predict request/response |
| `endpoint` | `string` | Required. Endpoint resource name. Format: `projects/&#123;project&#125;/locations/&#123;location&#125;/endpoints/&#123;endpoint&#125;` |
| `nextScheduleTime` | `string` | Output only. Timestamp when this monitoring pipeline will be scheduled to run for the next round. |
| `modelDeploymentMonitoringObjectiveConfigs` | `array` | Required. The config for monitoring objectives. This is a per DeployedModel config. Each DeployedModel needs to be configured separately. |
| `modelDeploymentMonitoringScheduleConfig` | `object` | The config for scheduling monitoring job. |
| `error` | `object` | The `Status` type defines a logical error model that is suitable for different programming environments, including REST APIs and RPC APIs. It is used by [gRPC](https://github.com/grpc). Each `Status` message contains three pieces of data: error code, error message, and error details. You can find out more about this error model and how to work with it in the [API Design Guide](https://cloud.google.com/apis/design/errors). |
| `logTtl` | `string` | The TTL of BigQuery tables in user projects which stores logs. A day is the basic unit of the TTL and we take the ceil of TTL/86400(a day). e.g. &#123; second: 3600&#125; indicates ttl = 1 day. |
| `analysisInstanceSchemaUri` | `string` | YAML schema file uri describing the format of a single instance that you want Tensorflow Data Validation (TFDV) to analyze. If this field is empty, all the feature data types are inferred from predict_instance_schema_uri, meaning that TFDV will use the data in the exact format(data type) as prediction request/response. If there are any data type differences between predict instance and TFDV instance, this field can be used to override the schema. For models trained with Vertex AI, this field must be set as all the fields in predict instance formatted as string. |
| `predictInstanceSchemaUri` | `string` | YAML schema file uri describing the format of a single instance, which are given to format this Endpoint's prediction (and explanation). If not set, we will generate predict schema from collected predict requests. |
| `statsAnomaliesBaseDirectory` | `object` | The Google Cloud Storage location where the output is to be written to. |
| `encryptionSpec` | `object` | Represents a customer-managed encryption key spec that can be applied to a top-level resource. |
| `updateTime` | `string` | Output only. Timestamp when this ModelDeploymentMonitoringJob was updated most recently. |
| `enableMonitoringPipelineLogs` | `boolean` | If true, the scheduled monitoring pipeline logs are sent to Google Cloud Logging, including pipeline status and anomalies detected. Please note the logs incur cost, which are subject to [Cloud Logging pricing](https://cloud.google.com/logging#pricing). |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `locationsId, modelDeploymentMonitoringJobsId, projectsId` | Gets a ModelDeploymentMonitoringJob. |
| `list` | `SELECT` | `locationsId, projectsId` | Lists ModelDeploymentMonitoringJobs in a Location. |
| `create` | `INSERT` | `locationsId, projectsId` | Creates a ModelDeploymentMonitoringJob. It will run periodically on a configured interval. |
| `delete` | `DELETE` | `locationsId, modelDeploymentMonitoringJobsId, projectsId` | Deletes a ModelDeploymentMonitoringJob. |
| `_list` | `EXEC` | `locationsId, projectsId` | Lists ModelDeploymentMonitoringJobs in a Location. |
| `patch` | `EXEC` | `locationsId, modelDeploymentMonitoringJobsId, projectsId` | Updates a ModelDeploymentMonitoringJob. |
| `pause` | `EXEC` | `locationsId, modelDeploymentMonitoringJobsId, projectsId` | Pauses a ModelDeploymentMonitoringJob. If the job is running, the server makes a best effort to cancel the job. Will mark ModelDeploymentMonitoringJob.state to 'PAUSED'. |
| `resume` | `EXEC` | `locationsId, modelDeploymentMonitoringJobsId, projectsId` | Resumes a paused ModelDeploymentMonitoringJob. It will start to run from next scheduled time. A deleted ModelDeploymentMonitoringJob can't be resumed. |
| `search_model_deployment_monitoring_stats_anomalies` | `EXEC` | `locationsId, modelDeploymentMonitoringJobsId, projectsId` | Searches Model Monitoring Statistics generated within a given time window. |
