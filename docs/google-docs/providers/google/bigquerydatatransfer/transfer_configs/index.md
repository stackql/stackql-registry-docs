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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>transfer_configs</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>transfer_configs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.bigquerydatatransfer.transfer_configs" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Identifier. The resource name of the transfer config. Transfer config names have the form either `projects/{project_id}/locations/{region}/transferConfigs/{config_id}` or `projects/{project_id}/transferConfigs/{config_id}`, where `config_id` is usually a UUID, even though it is not guaranteed or required. The name is ignored when creating a transfer config. |
| <CopyableCode code="dataRefreshWindowDays" /> | `integer` | The number of days to look back to automatically refresh the data. For example, if `data_refresh_window_days = 10`, then every day BigQuery reingests data for [today-10, today-1], rather than ingesting data for just [today-1]. Only valid if the data source supports the feature. Set the value to 0 to use the default value. |
| <CopyableCode code="dataSourceId" /> | `string` | Data source ID. This cannot be changed once data transfer is created. The full list of available data source IDs can be returned through an API call: https://cloud.google.com/bigquery-transfer/docs/reference/datatransfer/rest/v1/projects.locations.dataSources/list |
| <CopyableCode code="datasetRegion" /> | `string` | Output only. Region in which BigQuery dataset is located. |
| <CopyableCode code="destinationDatasetId" /> | `string` | The BigQuery target dataset id. |
| <CopyableCode code="disabled" /> | `boolean` | Is this config disabled. When set to true, no runs will be scheduled for this transfer config. |
| <CopyableCode code="displayName" /> | `string` | User specified display name for the data transfer. |
| <CopyableCode code="emailPreferences" /> | `object` | Represents preferences for sending email notifications for transfer run events. |
| <CopyableCode code="encryptionConfiguration" /> | `object` | Represents the encryption configuration for a transfer. |
| <CopyableCode code="nextRunTime" /> | `string` | Output only. Next time when data transfer will run. |
| <CopyableCode code="notificationPubsubTopic" /> | `string` | Pub/Sub topic where notifications will be sent after transfer runs associated with this transfer config finish. The format for specifying a pubsub topic is: `projects/{project_id}/topics/{topic_id}` |
| <CopyableCode code="ownerInfo" /> | `object` | Information about a user. |
| <CopyableCode code="params" /> | `object` | Parameters specific to each data source. For more information see the bq tab in the 'Setting up a data transfer' section for each data source. For example the parameters for Cloud Storage transfers are listed here: https://cloud.google.com/bigquery-transfer/docs/cloud-storage-transfer#bq |
| <CopyableCode code="schedule" /> | `string` | Data transfer schedule. If the data source does not support a custom schedule, this should be empty. If it is empty, the default value for the data source will be used. The specified times are in UTC. Examples of valid format: `1st,3rd monday of month 15:30`, `every wed,fri of jan,jun 13:15`, and `first sunday of quarter 00:00`. See more explanation about the format here: https://cloud.google.com/appengine/docs/flexible/python/scheduling-jobs-with-cron-yaml#the_schedule_format NOTE: The minimum interval time between recurring transfers depends on the data source; refer to the documentation for your data source. |
| <CopyableCode code="scheduleOptions" /> | `object` | Options customizing the data transfer schedule. |
| <CopyableCode code="state" /> | `string` | Output only. State of the most recently updated transfer run. |
| <CopyableCode code="updateTime" /> | `string` | Output only. Data transfer modification time. Ignored by server on input. |
| <CopyableCode code="userId" /> | `string` | Deprecated. Unique ID of the user on whose behalf transfer is done. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_locations_transfer_configs_get" /> | `SELECT` | <CopyableCode code="locationsId, projectsId, transferConfigsId" /> | Returns information about a data transfer config. |
| <CopyableCode code="projects_locations_transfer_configs_list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Returns information about all transfer configs owned by a project in the specified location. |
| <CopyableCode code="projects_transfer_configs_get" /> | `SELECT` | <CopyableCode code="projectsId, transferConfigsId" /> | Returns information about a data transfer config. |
| <CopyableCode code="projects_transfer_configs_list" /> | `SELECT` | <CopyableCode code="projectsId" /> | Returns information about all transfer configs owned by a project in the specified location. |
| <CopyableCode code="projects_locations_transfer_configs_create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates a new data transfer configuration. |
| <CopyableCode code="projects_transfer_configs_create" /> | `INSERT` | <CopyableCode code="projectsId" /> | Creates a new data transfer configuration. |
| <CopyableCode code="projects_locations_transfer_configs_delete" /> | `DELETE` | <CopyableCode code="locationsId, projectsId, transferConfigsId" /> | Deletes a data transfer configuration, including any associated transfer runs and logs. |
| <CopyableCode code="projects_transfer_configs_delete" /> | `DELETE` | <CopyableCode code="projectsId, transferConfigsId" /> | Deletes a data transfer configuration, including any associated transfer runs and logs. |
| <CopyableCode code="projects_locations_transfer_configs_patch" /> | `UPDATE` | <CopyableCode code="locationsId, projectsId, transferConfigsId" /> | Updates a data transfer configuration. All fields must be set, even if they are not updated. |
| <CopyableCode code="projects_transfer_configs_patch" /> | `UPDATE` | <CopyableCode code="projectsId, transferConfigsId" /> | Updates a data transfer configuration. All fields must be set, even if they are not updated. |
| <CopyableCode code="projects_locations_transfer_configs_schedule_runs" /> | `EXEC` | <CopyableCode code="locationsId, projectsId, transferConfigsId" /> | Creates transfer runs for a time range [start_time, end_time]. For each date - or whatever granularity the data source supports - in the range, one transfer run is created. Note that runs are created per UTC time in the time range. DEPRECATED: use StartManualTransferRuns instead. |
| <CopyableCode code="projects_locations_transfer_configs_start_manual_runs" /> | `EXEC` | <CopyableCode code="locationsId, projectsId, transferConfigsId" /> | Start manual transfer runs to be executed now with schedule_time equal to current time. The transfer runs can be created for a time range where the run_time is between start_time (inclusive) and end_time (exclusive), or for a specific run_time. |
| <CopyableCode code="projects_transfer_configs_schedule_runs" /> | `EXEC` | <CopyableCode code="projectsId, transferConfigsId" /> | Creates transfer runs for a time range [start_time, end_time]. For each date - or whatever granularity the data source supports - in the range, one transfer run is created. Note that runs are created per UTC time in the time range. DEPRECATED: use StartManualTransferRuns instead. |
| <CopyableCode code="projects_transfer_configs_start_manual_runs" /> | `EXEC` | <CopyableCode code="projectsId, transferConfigsId" /> | Start manual transfer runs to be executed now with schedule_time equal to current time. The transfer runs can be created for a time range where the run_time is between start_time (inclusive) and end_time (exclusive), or for a specific run_time. |

## `SELECT` examples

Returns information about all transfer configs owned by a project in the specified location.

```sql
SELECT
name,
dataRefreshWindowDays,
dataSourceId,
datasetRegion,
destinationDatasetId,
disabled,
displayName,
emailPreferences,
encryptionConfiguration,
nextRunTime,
notificationPubsubTopic,
ownerInfo,
params,
schedule,
scheduleOptions,
state,
updateTime,
userId
FROM google.bigquerydatatransfer.transfer_configs
WHERE projectsId = '{{ projectsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>transfer_configs</code> resource.

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
INSERT INTO google.bigquerydatatransfer.transfer_configs (
projectsId,
name,
destinationDatasetId,
displayName,
dataSourceId,
params,
schedule,
scheduleOptions,
dataRefreshWindowDays,
disabled,
userId,
notificationPubsubTopic,
emailPreferences,
encryptionConfiguration
)
SELECT 
'{{ projectsId }}',
'{{ name }}',
'{{ destinationDatasetId }}',
'{{ displayName }}',
'{{ dataSourceId }}',
'{{ params }}',
'{{ schedule }}',
'{{ scheduleOptions }}',
'{{ dataRefreshWindowDays }}',
true|false,
'{{ userId }}',
'{{ notificationPubsubTopic }}',
'{{ emailPreferences }}',
'{{ encryptionConfiguration }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
name: string
destinationDatasetId: string
displayName: string
dataSourceId: string
params: object
schedule: string
scheduleOptions:
  disableAutoScheduling: boolean
  startTime: string
  endTime: string
dataRefreshWindowDays: integer
disabled: boolean
updateTime: string
nextRunTime: string
state: string
userId: string
datasetRegion: string
notificationPubsubTopic: string
emailPreferences:
  enableFailureEmail: boolean
ownerInfo:
  email: string
encryptionConfiguration:
  kmsKeyName: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>transfer_configs</code> resource.

```sql
/*+ update */
UPDATE google.bigquerydatatransfer.transfer_configs
SET 
name = '{{ name }}',
destinationDatasetId = '{{ destinationDatasetId }}',
displayName = '{{ displayName }}',
dataSourceId = '{{ dataSourceId }}',
params = '{{ params }}',
schedule = '{{ schedule }}',
scheduleOptions = '{{ scheduleOptions }}',
dataRefreshWindowDays = '{{ dataRefreshWindowDays }}',
disabled = true|false,
userId = '{{ userId }}',
notificationPubsubTopic = '{{ notificationPubsubTopic }}',
emailPreferences = '{{ emailPreferences }}',
encryptionConfiguration = '{{ encryptionConfiguration }}'
WHERE 
projectsId = '{{ projectsId }}'
AND transferConfigsId = '{{ transferConfigsId }}';
```

## `DELETE` example

Deletes the specified <code>transfer_configs</code> resource.

```sql
/*+ delete */
DELETE FROM google.bigquerydatatransfer.transfer_configs
WHERE projectsId = '{{ projectsId }}'
AND transferConfigsId = '{{ transferConfigsId }}';
```
