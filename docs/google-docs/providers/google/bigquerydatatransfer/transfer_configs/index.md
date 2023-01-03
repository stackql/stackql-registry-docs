---
title: transfer_configs
hide_title: false
hide_table_of_contents: false
keywords:
  - transfer_configs
  - bigquerydatatransfer
  - google    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>transfer_configs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.bigquerydatatransfer.transfer_configs</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | The resource name of the transfer config. Transfer config names have the form `projects/{project_id}/locations/{region}/transferConfigs/{config_id}`. Where `config_id` is usually a uuid, even though it is not guaranteed or required. The name is ignored when creating a transfer config. |
| `nextRunTime` | `string` | Output only. Next time when data transfer will run. |
| `dataSourceId` | `string` | Data source id. Cannot be changed once data transfer is created. |
| `params` | `object` | Parameters specific to each data source. For more information see the bq tab in the 'Setting up a data transfer' section for each data source. For example the parameters for Cloud Storage transfers are listed here: https://cloud.google.com/bigquery-transfer/docs/cloud-storage-transfer#bq |
| `userId` | `string` | Deprecated. Unique ID of the user on whose behalf transfer is done. |
| `state` | `string` | Output only. State of the most recently updated transfer run. |
| `schedule` | `string` | Data transfer schedule. If the data source does not support a custom schedule, this should be empty. If it is empty, the default value for the data source will be used. The specified times are in UTC. Examples of valid format: `1st,3rd monday of month 15:30`, `every wed,fri of jan,jun 13:15`, and `first sunday of quarter 00:00`. See more explanation about the format here: https://cloud.google.com/appengine/docs/flexible/python/scheduling-jobs-with-cron-yaml#the_schedule_format NOTE: The minimum interval time between recurring transfers depends on the data source; refer to the documentation for your data source. |
| `displayName` | `string` | User specified display name for the data transfer. |
| `dataRefreshWindowDays` | `integer` | The number of days to look back to automatically refresh the data. For example, if `data_refresh_window_days = 10`, then every day BigQuery reingests data for [today-10, today-1], rather than ingesting data for just [today-1]. Only valid if the data source supports the feature. Set the value to 0 to use the default value. |
| `emailPreferences` | `object` | Represents preferences for sending email notifications for transfer run events. |
| `updateTime` | `string` | Output only. Data transfer modification time. Ignored by server on input. |
| `datasetRegion` | `string` | Output only. Region in which BigQuery dataset is located. |
| `notificationPubsubTopic` | `string` | Pub/Sub topic where notifications will be sent after transfer runs associated with this transfer config finish. The format for specifying a pubsub topic is: `projects/{project}/topics/{topic}` |
| `scheduleOptions` | `object` | Options customizing the data transfer schedule. |
| `disabled` | `boolean` | Is this config disabled. When set to true, no runs are scheduled for a given transfer. |
| `ownerInfo` | `object` | Information about a user. |
| `destinationDatasetId` | `string` | The BigQuery target dataset id. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_transferConfigs_get` | `SELECT` | `locationsId, projectsId, transferConfigsId` | Returns information about a data transfer config. |
| `projects_locations_transferConfigs_list` | `SELECT` | `locationsId, projectsId` | Returns information about all transfer configs owned by a project in the specified location. |
| `projects_transferConfigs_get` | `SELECT` | `projectsId, transferConfigsId` | Returns information about a data transfer config. |
| `projects_transferConfigs_list` | `SELECT` | `projectsId` | Returns information about all transfer configs owned by a project in the specified location. |
| `projects_locations_transferConfigs_create` | `INSERT` | `locationsId, projectsId` | Creates a new data transfer configuration. |
| `projects_transferConfigs_create` | `INSERT` | `projectsId` | Creates a new data transfer configuration. |
| `projects_locations_transferConfigs_delete` | `DELETE` | `locationsId, projectsId, transferConfigsId` | Deletes a data transfer configuration, including any associated transfer runs and logs. |
| `projects_transferConfigs_delete` | `DELETE` | `projectsId, transferConfigsId` | Deletes a data transfer configuration, including any associated transfer runs and logs. |
| `projects_locations_transferConfigs_patch` | `EXEC` | `locationsId, projectsId, transferConfigsId` | Updates a data transfer configuration. All fields must be set, even if they are not updated. |
| `projects_locations_transferConfigs_scheduleRuns` | `EXEC` | `locationsId, projectsId, transferConfigsId` | Creates transfer runs for a time range [start_time, end_time]. For each date - or whatever granularity the data source supports - in the range, one transfer run is created. Note that runs are created per UTC time in the time range. DEPRECATED: use StartManualTransferRuns instead. |
| `projects_locations_transferConfigs_startManualRuns` | `EXEC` | `locationsId, projectsId, transferConfigsId` | Start manual transfer runs to be executed now with schedule_time equal to current time. The transfer runs can be created for a time range where the run_time is between start_time (inclusive) and end_time (exclusive), or for a specific run_time. |
| `projects_transferConfigs_patch` | `EXEC` | `projectsId, transferConfigsId` | Updates a data transfer configuration. All fields must be set, even if they are not updated. |
| `projects_transferConfigs_scheduleRuns` | `EXEC` | `projectsId, transferConfigsId` | Creates transfer runs for a time range [start_time, end_time]. For each date - or whatever granularity the data source supports - in the range, one transfer run is created. Note that runs are created per UTC time in the time range. DEPRECATED: use StartManualTransferRuns instead. |
| `projects_transferConfigs_startManualRuns` | `EXEC` | `projectsId, transferConfigsId` | Start manual transfer runs to be executed now with schedule_time equal to current time. The transfer runs can be created for a time range where the run_time is between start_time (inclusive) and end_time (exclusive), or for a specific run_time. |
