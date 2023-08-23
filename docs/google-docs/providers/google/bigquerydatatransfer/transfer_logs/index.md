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
| `messageTime` | `string` | Time when message was logged. |
| `severity` | `string` | Message severity. |
| `messageText` | `string` | Message text. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `projects_locations_transfer_configs_runs_transfer_logs_list` | `SELECT` | `locationsId, projectsId, runsId, transferConfigsId` |
| `projects_transfer_configs_runs_transfer_logs_list` | `SELECT` | `projectsId, runsId, transferConfigsId` |
| `_projects_locations_transfer_configs_runs_transfer_logs_list` | `EXEC` | `locationsId, projectsId, runsId, transferConfigsId` |
| `_projects_transfer_configs_runs_transfer_logs_list` | `EXEC` | `projectsId, runsId, transferConfigsId` |
