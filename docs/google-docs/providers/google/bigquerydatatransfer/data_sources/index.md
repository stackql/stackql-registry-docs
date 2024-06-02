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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>data_sources</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="bigquerydatatransfer.data_sources" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. Data source resource name. |
| <CopyableCode code="description" /> | `string` | User friendly data source description string. |
| <CopyableCode code="authorizationType" /> | `string` | Indicates the type of authorization. |
| <CopyableCode code="clientId" /> | `string` | Data source client id which should be used to receive refresh token. |
| <CopyableCode code="dataRefreshType" /> | `string` | Specifies whether the data source supports automatic data refresh for the past few days, and how it's supported. For some data sources, data might not be complete until a few days later, so it's useful to refresh data automatically. |
| <CopyableCode code="dataSourceId" /> | `string` | Data source id. |
| <CopyableCode code="defaultDataRefreshWindowDays" /> | `integer` | Default data refresh window on days. Only meaningful when `data_refresh_type` = `SLIDING_WINDOW`. |
| <CopyableCode code="defaultSchedule" /> | `string` | Default data transfer schedule. Examples of valid schedules include: `1st,3rd monday of month 15:30`, `every wed,fri of jan,jun 13:15`, and `first sunday of quarter 00:00`. |
| <CopyableCode code="displayName" /> | `string` | User friendly data source name. |
| <CopyableCode code="helpUrl" /> | `string` | Url for the help document for this data source. |
| <CopyableCode code="manualRunsDisabled" /> | `boolean` | Disables backfilling and manual run scheduling for the data source. |
| <CopyableCode code="minimumScheduleInterval" /> | `string` | The minimum interval for scheduler to schedule runs. |
| <CopyableCode code="parameters" /> | `array` | Data source parameters. |
| <CopyableCode code="scopes" /> | `array` | Api auth scopes for which refresh token needs to be obtained. These are scopes needed by a data source to prepare data and ingest them into BigQuery, e.g., https://www.googleapis.com/auth/bigquery |
| <CopyableCode code="supportsCustomSchedule" /> | `boolean` | Specifies whether the data source supports a user defined schedule, or operates on the default schedule. When set to `true`, user can override default schedule. |
| <CopyableCode code="supportsMultipleTransfers" /> | `boolean` | Deprecated. This field has no effect. |
| <CopyableCode code="transferType" /> | `string` | Deprecated. This field has no effect. |
| <CopyableCode code="updateDeadlineSeconds" /> | `integer` | The number of seconds to wait for an update from the data source before the Data Transfer Service marks the transfer as FAILED. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_data_sources_get" /> | `SELECT` | <CopyableCode code="dataSourcesId, projectsId" /> | Retrieves a supported data source and returns its settings. |
| <CopyableCode code="projects_data_sources_list" /> | `SELECT` | <CopyableCode code="projectsId" /> | Lists supported data sources and returns their settings. |
| <CopyableCode code="projects_locations_data_sources_get" /> | `SELECT` | <CopyableCode code="dataSourcesId, locationsId, projectsId" /> | Retrieves a supported data source and returns its settings. |
| <CopyableCode code="projects_locations_data_sources_list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists supported data sources and returns their settings. |
| <CopyableCode code="_projects_data_sources_list" /> | `EXEC` | <CopyableCode code="projectsId" /> | Lists supported data sources and returns their settings. |
| <CopyableCode code="_projects_locations_data_sources_list" /> | `EXEC` | <CopyableCode code="locationsId, projectsId" /> | Lists supported data sources and returns their settings. |
| <CopyableCode code="projects_data_sources_check_valid_creds" /> | `EXEC` | <CopyableCode code="dataSourcesId, projectsId" /> | Returns true if valid credentials exist for the given data source and requesting user. |
| <CopyableCode code="projects_locations_data_sources_check_valid_creds" /> | `EXEC` | <CopyableCode code="dataSourcesId, locationsId, projectsId" /> | Returns true if valid credentials exist for the given data source and requesting user. |
