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
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
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
| `defaultDataRefreshWindowDays` | `integer` | Default data refresh window on days. Only meaningful when `data_refresh_type` = `SLIDING_WINDOW`. |
| `dataSourceId` | `string` | Data source id. |
| `clientId` | `string` | Data source client id which should be used to receive refresh token. |
| `helpUrl` | `string` | Url for the help document for this data source. |
| `minimumScheduleInterval` | `string` | The minimum interval for scheduler to schedule runs. |
| `displayName` | `string` | User friendly data source name. |
| `dataRefreshType` | `string` | Specifies whether the data source supports automatic data refresh for the past few days, and how it's supported. For some data sources, data might not be complete until a few days later, so it's useful to refresh data automatically. |
| `scopes` | `array` | Api auth scopes for which refresh token needs to be obtained. These are scopes needed by a data source to prepare data and ingest them into BigQuery, e.g., https://www.googleapis.com/auth/bigquery |
| `defaultSchedule` | `string` | Default data transfer schedule. Examples of valid schedules include: `1st,3rd monday of month 15:30`, `every wed,fri of jan,jun 13:15`, and `first sunday of quarter 00:00`. |
| `supportsMultipleTransfers` | `boolean` | Deprecated. This field has no effect. |
| `authorizationType` | `string` | Indicates the type of authorization. |
| `transferType` | `string` | Deprecated. This field has no effect. |
| `updateDeadlineSeconds` | `integer` | The number of seconds to wait for an update from the data source before the Data Transfer Service marks the transfer as FAILED. |
| `parameters` | `array` | Data source parameters. |
| `supportsCustomSchedule` | `boolean` | Specifies whether the data source supports a user defined schedule, or operates on the default schedule. When set to `true`, user can override default schedule. |
| `manualRunsDisabled` | `boolean` | Disables backfilling and manual run scheduling for the data source. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_dataSources_get` | `SELECT` | `dataSourcesId, projectsId` | Retrieves a supported data source and returns its settings. |
| `projects_dataSources_list` | `SELECT` | `projectsId` | Lists supported data sources and returns their settings. |
| `projects_locations_dataSources_get` | `SELECT` | `dataSourcesId, locationsId, projectsId` | Retrieves a supported data source and returns its settings. |
| `projects_locations_dataSources_list` | `SELECT` | `locationsId, projectsId` | Lists supported data sources and returns their settings. |
| `projects_dataSources_checkValidCreds` | `EXEC` | `dataSourcesId, projectsId` | Returns true if valid credentials exist for the given data source and requesting user. |
| `projects_locations_dataSources_checkValidCreds` | `EXEC` | `dataSourcesId, locationsId, projectsId` | Returns true if valid credentials exist for the given data source and requesting user. |
