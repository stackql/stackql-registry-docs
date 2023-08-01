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
| `nextPageToken` | `string` | Output only. The next-pagination token. For multiple-page list results, this token can be used as the `ListTransferRunsRequest.page_token` to request the next page of list results. |
| `transferRuns` | `array` | Output only. The stored pipeline transfer runs. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_transfer_configs_runs_list` | `SELECT` | `locationsId, projectsId, transferConfigsId` | Returns information about running and completed transfer runs. |
| `projects_transfer_configs_runs_list` | `SELECT` | `projectsId, transferConfigsId` | Returns information about running and completed transfer runs. |
| `projects_locations_transfer_configs_runs_delete` | `DELETE` | `locationsId, projectsId, runsId, transferConfigsId` | Deletes the specified transfer run. |
| `projects_transfer_configs_runs_delete` | `DELETE` | `projectsId, runsId, transferConfigsId` | Deletes the specified transfer run. |
| `projects_locations_transfer_configs_runs_get` | `EXEC` | `locationsId, projectsId, runsId, transferConfigsId` | Returns information about the particular transfer run. |
| `projects_transfer_configs_runs_get` | `EXEC` | `projectsId, runsId, transferConfigsId` | Returns information about the particular transfer run. |
