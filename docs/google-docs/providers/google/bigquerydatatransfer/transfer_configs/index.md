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
image: /img/providers/google/stackql-google-provider-featured-image.png
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
| `name` | `string` | The resource name of the transfer config. Transfer config names have the form `projects/&#123;project_id&#125;/locations/&#123;region&#125;/transferConfigs/&#123;config_id&#125;`. Where `config_id` is usually a uuid, even though it is not guaranteed or required. The name is ignored when creating a transfer config. |
| `dataSourceId` | `string` | Data source ID. This cannot be changed once data transfer is created. The full list of available data source IDs can be returned through an API call: https://cloud.google.com/bigquery-transfer/docs/reference/datatransfer/rest/v1/projects.locations.dataSources/list |
| `datasetRegion` | `string` | Output only. Region in which BigQuery dataset is located. |
| `schedule` | `string` | Data transfer schedule. If the data source does not support a custom schedule, this should be empty. If it is empty, the default value for the data source will be used. The specified times are in UTC. Examples of valid format: `1st,3rd monday of month 15:30`, `every wed,fri of jan,jun 13:15`, and `first sunday of quarter 00:00`. See more explanation about the format here: https://cloud.google.com/appengine/docs/flexible/python/scheduling-jobs-with-cron-yaml#the_schedule_format NOTE: The minimum interval time between recurring transfers depends on the data source; refer to the documentation for your data source. |
| `nextRunTime` | `string` | Output only. Next time when data transfer will run. |
| `dataRefreshWindowDays` | `integer` | The number of days to look back to automatically refresh the data. For example, if `data_refresh_window_days = 10`, then every day BigQuery reingests data for [today-10, today-1], rather than ingesting data for just [today-1]. Only valid if the data source supports the feature. Set the value to 0 to use the default value. |
| `userId` | `string` | Deprecated. Unique ID of the user on whose behalf transfer is done. |
| `emailPreferences` | `object` | Represents preferences for sending email notifications for transfer run events. |
| `notificationPubsubTopic` | `string` | Pub/Sub topic where notifications will be sent after transfer runs associated with this transfer config finish. The format for specifying a pubsub topic is: `projects/&#123;project&#125;/topics/&#123;topic&#125;` |
| `destinationDatasetId` | `string` | The BigQuery target dataset id. |
| `updateTime` | `string` | Output only. Data transfer modification time. Ignored by server on input. |
| `state` | `string` | Output only. State of the most recently updated transfer run. |
| `disabled` | `boolean` | Is this config disabled. When set to true, no runs are scheduled for a given transfer. |
| `ownerInfo` | `object` | Information about a user. |
| `encryptionConfiguration` | `object` | Represents the encryption configuration for a transfer. |
| `displayName` | `string` | User specified display name for the data transfer. |
| `params` | `object` | Parameters specific to each data source. For more information see the bq tab in the 'Setting up a data transfer' section for each data source. For example the parameters for Cloud Storage transfers are listed here: https://cloud.google.com/bigquery-transfer/docs/cloud-storage-transfer#bq |
| `scheduleOptions` | `object` | Options customizing the data transfer schedule. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_transfer_configs_list` | `SELECT` | `locationsId, projectsId` | Returns information about all transfer configs owned by a project in the specified location. |
| `projects_transfer_configs_list` | `SELECT` | `projectsId` | Returns information about all transfer configs owned by a project in the specified location. |
| `projects_locations_transfer_configs_create` | `INSERT` | `locationsId, projectsId` | Creates a new data transfer configuration. |
| `projects_transfer_configs_create` | `INSERT` | `projectsId` | Creates a new data transfer configuration. |
| `projects_locations_transfer_configs_delete` | `DELETE` | `locationsId, projectsId, transferConfigsId` | Deletes a data transfer configuration, including any associated transfer runs and logs. |
| `projects_transfer_configs_delete` | `DELETE` | `projectsId, transferConfigsId` | Deletes a data transfer configuration, including any associated transfer runs and logs. |
| `_projects_locations_transfer_configs_list` | `EXEC` | `locationsId, projectsId` | Returns information about all transfer configs owned by a project in the specified location. |
| `_projects_transfer_configs_list` | `EXEC` | `projectsId` | Returns information about all transfer configs owned by a project in the specified location. |
| `projects_locations_transfer_configs_get` | `EXEC` | `locationsId, projectsId, transferConfigsId` | Returns information about a data transfer config. |
| `projects_locations_transfer_configs_patch` | `EXEC` | `locationsId, projectsId, transferConfigsId` | Updates a data transfer configuration. All fields must be set, even if they are not updated. |
| `projects_locations_transfer_configs_schedule_runs` | `EXEC` | `locationsId, projectsId, transferConfigsId` | Creates transfer runs for a time range [start_time, end_time]. For each date - or whatever granularity the data source supports - in the range, one transfer run is created. Note that runs are created per UTC time in the time range. DEPRECATED: use StartManualTransferRuns instead. |
| `projects_locations_transfer_configs_start_manual_runs` | `EXEC` | `locationsId, projectsId, transferConfigsId` | Start manual transfer runs to be executed now with schedule_time equal to current time. The transfer runs can be created for a time range where the run_time is between start_time (inclusive) and end_time (exclusive), or for a specific run_time. |
| `projects_transfer_configs_get` | `EXEC` | `projectsId, transferConfigsId` | Returns information about a data transfer config. |
| `projects_transfer_configs_patch` | `EXEC` | `projectsId, transferConfigsId` | Updates a data transfer configuration. All fields must be set, even if they are not updated. |
| `projects_transfer_configs_schedule_runs` | `EXEC` | `projectsId, transferConfigsId` | Creates transfer runs for a time range [start_time, end_time]. For each date - or whatever granularity the data source supports - in the range, one transfer run is created. Note that runs are created per UTC time in the time range. DEPRECATED: use StartManualTransferRuns instead. |
| `projects_transfer_configs_start_manual_runs` | `EXEC` | `projectsId, transferConfigsId` | Start manual transfer runs to be executed now with schedule_time equal to current time. The transfer runs can be created for a time range where the run_time is between start_time (inclusive) and end_time (exclusive), or for a specific run_time. |
