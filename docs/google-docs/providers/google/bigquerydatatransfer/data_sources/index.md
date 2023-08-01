---
title: data_sources
hide_title: false
hide_table_of_contents: false
keywords:
  - data_sources
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
<tr><td><b>Name</b></td><td><code>data_sources</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.bigquerydatatransfer.data_sources</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. Data source resource name. |
| `description` | `string` | User friendly data source description string. |
| `displayName` | `string` | User friendly data source name. |
| `minimumScheduleInterval` | `string` | The minimum interval for scheduler to schedule runs. |
| `dataRefreshType` | `string` | Specifies whether the data source supports automatic data refresh for the past few days, and how it's supported. For some data sources, data might not be complete until a few days later, so it's useful to refresh data automatically. |
| `supportsCustomSchedule` | `boolean` | Specifies whether the data source supports a user defined schedule, or operates on the default schedule. When set to `true`, user can override default schedule. |
| `parameters` | `array` | Data source parameters. |
| `transferType` | `string` | Deprecated. This field has no effect. |
| `helpUrl` | `string` | Url for the help document for this data source. |
| `supportsMultipleTransfers` | `boolean` | Deprecated. This field has no effect. |
| `manualRunsDisabled` | `boolean` | Disables backfilling and manual run scheduling for the data source. |
| `dataSourceId` | `string` | Data source id. |
| `scopes` | `array` | Api auth scopes for which refresh token needs to be obtained. These are scopes needed by a data source to prepare data and ingest them into BigQuery, e.g., https://www.googleapis.com/auth/bigquery |
| `authorizationType` | `string` | Indicates the type of authorization. |
| `clientId` | `string` | Data source client id which should be used to receive refresh token. |
| `updateDeadlineSeconds` | `integer` | The number of seconds to wait for an update from the data source before the Data Transfer Service marks the transfer as FAILED. |
| `defaultDataRefreshWindowDays` | `integer` | Default data refresh window on days. Only meaningful when `data_refresh_type` = `SLIDING_WINDOW`. |
| `defaultSchedule` | `string` | Default data transfer schedule. Examples of valid schedules include: `1st,3rd monday of month 15:30`, `every wed,fri of jan,jun 13:15`, and `first sunday of quarter 00:00`. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_data_sources_get` | `SELECT` | `dataSourcesId, projectsId` | Retrieves a supported data source and returns its settings. |
| `projects_data_sources_list` | `SELECT` | `projectsId` | Lists supported data sources and returns their settings. |
| `projects_locations_data_sources_get` | `SELECT` | `dataSourcesId, locationsId, projectsId` | Retrieves a supported data source and returns its settings. |
| `projects_locations_data_sources_list` | `SELECT` | `locationsId, projectsId` | Lists supported data sources and returns their settings. |
| `projects_data_sources_check_valid_creds` | `EXEC` | `dataSourcesId, projectsId` | Returns true if valid credentials exist for the given data source and requesting user. |
| `projects_locations_data_sources_check_valid_creds` | `EXEC` | `dataSourcesId, locationsId, projectsId` | Returns true if valid credentials exist for the given data source and requesting user. |
