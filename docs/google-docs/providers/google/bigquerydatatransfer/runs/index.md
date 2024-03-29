---
title: runs
hide_title: false
hide_table_of_contents: false
keywords:
  - runs
  - bigquerydatatransfer
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
<tr><td><b>Name</b></td><td><code>runs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.bigquerydatatransfer.runs</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | The resource name of the transfer run. Transfer run names have the form `projects/&#123;project_id&#125;/locations/&#123;location&#125;/transferConfigs/&#123;config_id&#125;/runs/&#123;run_id&#125;`. The name is ignored when creating a transfer run. |
| `destinationDatasetId` | `string` | Output only. The BigQuery target dataset id. |
| `state` | `string` | Data transfer run state. Ignored for input requests. |
| `startTime` | `string` | Output only. Time when transfer run was started. Parameter ignored by server for input requests. |
| `schedule` | `string` | Output only. Describes the schedule of this transfer run if it was created as part of a regular schedule. For batch transfer runs that are scheduled manually, this is empty. NOTE: the system might choose to delay the schedule depending on the current load, so `schedule_time` doesn't always match this. |
| `params` | `object` | Output only. Parameters specific to each data source. For more information see the bq tab in the 'Setting up a data transfer' section for each data source. For example the parameters for Cloud Storage transfers are listed here: https://cloud.google.com/bigquery-transfer/docs/cloud-storage-transfer#bq |
| `scheduleTime` | `string` | Minimum time after which a transfer run can be started. |
| `userId` | `string` | Deprecated. Unique ID of the user on whose behalf transfer is done. |
| `errorStatus` | `object` | The `Status` type defines a logical error model that is suitable for different programming environments, including REST APIs and RPC APIs. It is used by [gRPC](https://github.com/grpc). Each `Status` message contains three pieces of data: error code, error message, and error details. You can find out more about this error model and how to work with it in the [API Design Guide](https://cloud.google.com/apis/design/errors). |
| `notificationPubsubTopic` | `string` | Output only. Pub/Sub topic where a notification will be sent after this transfer run finishes. The format for specifying a pubsub topic is: `projects/&#123;project&#125;/topics/&#123;topic&#125;` |
| `runTime` | `string` | For batch transfer runs, specifies the date and time of the data should be ingested. |
| `dataSourceId` | `string` | Output only. Data source id. |
| `endTime` | `string` | Output only. Time when transfer run ended. Parameter ignored by server for input requests. |
| `emailPreferences` | `object` | Represents preferences for sending email notifications for transfer run events. |
| `updateTime` | `string` | Output only. Last time the data transfer run state was updated. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_transfer_configs_runs_get` | `SELECT` | `locationsId, projectsId, runsId, transferConfigsId` | Returns information about the particular transfer run. |
| `projects_locations_transfer_configs_runs_list` | `SELECT` | `locationsId, projectsId, transferConfigsId` | Returns information about running and completed transfer runs. |
| `projects_transfer_configs_runs_get` | `SELECT` | `projectsId, runsId, transferConfigsId` | Returns information about the particular transfer run. |
| `projects_transfer_configs_runs_list` | `SELECT` | `projectsId, transferConfigsId` | Returns information about running and completed transfer runs. |
| `projects_locations_transfer_configs_runs_delete` | `DELETE` | `locationsId, projectsId, runsId, transferConfigsId` | Deletes the specified transfer run. |
| `projects_transfer_configs_runs_delete` | `DELETE` | `projectsId, runsId, transferConfigsId` | Deletes the specified transfer run. |
| `_projects_locations_transfer_configs_runs_list` | `EXEC` | `locationsId, projectsId, transferConfigsId` | Returns information about running and completed transfer runs. |
| `_projects_transfer_configs_runs_list` | `EXEC` | `projectsId, transferConfigsId` | Returns information about running and completed transfer runs. |
