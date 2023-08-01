---
title: uptime_check_configs
hide_title: false
hide_table_of_contents: false
keywords:
  - uptime_check_configs
  - monitoring
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
<tr><td><b>Name</b></td><td><code>uptime_check_configs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.monitoring.uptime_check_configs</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `nextPageToken` | `string` | This field represents the pagination token to retrieve the next page of results. If the value is empty, it means no further results for the request. To retrieve the next page of results, the value of the next_page_token is passed to the subsequent List method call (in the request message's page_token field). |
| `totalSize` | `integer` | The total number of Uptime check configurations for the project, irrespective of any pagination. |
| `uptimeCheckConfigs` | `array` | The returned Uptime check configurations. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_uptime_check_configs_list` | `SELECT` | `projectsId` | Lists the existing valid Uptime check configurations for the project (leaving out any invalid configurations). |
| `projects_uptime_check_configs_create` | `INSERT` | `projectsId` | Creates a new Uptime check configuration. |
| `projects_uptime_check_configs_delete` | `DELETE` | `projectsId, uptimeCheckConfigsId` | Deletes an Uptime check configuration. Note that this method will fail if the Uptime check configuration is referenced by an alert policy or other dependent configs that would be rendered invalid by the deletion. |
| `projects_uptime_check_configs_get` | `EXEC` | `projectsId, uptimeCheckConfigsId` | Gets a single Uptime check configuration. |
| `projects_uptime_check_configs_patch` | `EXEC` | `projectsId, uptimeCheckConfigsId` | Updates an Uptime check configuration. You can either replace the entire configuration with a new one or replace only certain fields in the current configuration by specifying the fields to be updated via updateMask. Returns the updated configuration. |
