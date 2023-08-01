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
| `nextPageToken` | `string` | Output only. The next-pagination token. For multiple-page list results, this token can be used as the `ListTransferConfigsRequest.page_token` to request the next page of list results. |
| `transferConfigs` | `array` | Output only. The stored pipeline transfer configurations. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_transfer_configs_list` | `SELECT` | `locationsId, projectsId` | Returns information about all transfer configs owned by a project in the specified location. |
| `projects_transfer_configs_list` | `SELECT` | `projectsId` | Returns information about all transfer configs owned by a project in the specified location. |
| `projects_locations_transfer_configs_create` | `INSERT` | `locationsId, projectsId` | Creates a new data transfer configuration. |
| `projects_transfer_configs_create` | `INSERT` | `projectsId` | Creates a new data transfer configuration. |
| `projects_locations_transfer_configs_delete` | `DELETE` | `locationsId, projectsId, transferConfigsId` | Deletes a data transfer configuration, including any associated transfer runs and logs. |
| `projects_transfer_configs_delete` | `DELETE` | `projectsId, transferConfigsId` | Deletes a data transfer configuration, including any associated transfer runs and logs. |
| `projects_locations_transfer_configs_get` | `EXEC` | `locationsId, projectsId, transferConfigsId` | Returns information about a data transfer config. |
| `projects_locations_transfer_configs_patch` | `EXEC` | `locationsId, projectsId, transferConfigsId` | Updates a data transfer configuration. All fields must be set, even if they are not updated. |
| `projects_locations_transfer_configs_schedule_runs` | `EXEC` | `locationsId, projectsId, transferConfigsId` | Creates transfer runs for a time range [start_time, end_time]. For each date - or whatever granularity the data source supports - in the range, one transfer run is created. Note that runs are created per UTC time in the time range. DEPRECATED: use StartManualTransferRuns instead. |
| `projects_locations_transfer_configs_start_manual_runs` | `EXEC` | `locationsId, projectsId, transferConfigsId` | Start manual transfer runs to be executed now with schedule_time equal to current time. The transfer runs can be created for a time range where the run_time is between start_time (inclusive) and end_time (exclusive), or for a specific run_time. |
| `projects_transfer_configs_get` | `EXEC` | `projectsId, transferConfigsId` | Returns information about a data transfer config. |
| `projects_transfer_configs_patch` | `EXEC` | `projectsId, transferConfigsId` | Updates a data transfer configuration. All fields must be set, even if they are not updated. |
| `projects_transfer_configs_schedule_runs` | `EXEC` | `projectsId, transferConfigsId` | Creates transfer runs for a time range [start_time, end_time]. For each date - or whatever granularity the data source supports - in the range, one transfer run is created. Note that runs are created per UTC time in the time range. DEPRECATED: use StartManualTransferRuns instead. |
| `projects_transfer_configs_start_manual_runs` | `EXEC` | `projectsId, transferConfigsId` | Start manual transfer runs to be executed now with schedule_time equal to current time. The transfer runs can be created for a time range where the run_time is between start_time (inclusive) and end_time (exclusive), or for a specific run_time. |
