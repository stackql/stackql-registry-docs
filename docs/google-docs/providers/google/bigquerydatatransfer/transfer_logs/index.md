---
title: transfer_logs
hide_title: false
hide_table_of_contents: false
keywords:
  - transfer_logs
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
<tr><td><b>Name</b></td><td><code>transfer_logs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.bigquerydatatransfer.transfer_logs</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `nextPageToken` | `string` | Output only. The next-pagination token. For multiple-page list results, this token can be used as the `GetTransferRunLogRequest.page_token` to request the next page of list results. |
| `transferMessages` | `array` | Output only. The stored pipeline transfer messages. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `projects_locations_transfer_configs_runs_transfer_logs_list` | `SELECT` | `locationsId, projectsId, runsId, transferConfigsId` |
| `projects_transfer_configs_runs_transfer_logs_list` | `SELECT` | `projectsId, runsId, transferConfigsId` |
