---
title: logs
hide_title: false
hide_table_of_contents: false
keywords:
  - logs
  - apps
  - digitalocean    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Sumologic resources using SQL
custom_edit_url: null
image: /img/providers/digitalocean/stackql-digitalocean-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>logs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>digitalocean.apps.logs</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `live_url` | `string` | A URL of the real-time live logs. This URL may use either the `https://` or `wss://` protocols and will keep pushing live logs as they become available. |
| `historic_urls` | `array` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_logs` | `SELECT` | `app_id, component_name, deployment_id, type` | Retrieve the logs of a past, in-progress, or active deployment. The response will include links to either real-time logs of an in-progress or active deployment or archived logs of a past deployment. |
| `get_logs_active_deployment` | `SELECT` | `app_id, component_name, type` | Retrieve the logs of the active deployment if one exists. The response will include links to either real-time logs of an in-progress or active deployment or archived logs of a past deployment. Note log_type=BUILD logs will return logs associated with the current active deployment (being served). To view build logs associated with in-progress build, the query must explicitly reference the deployment id. |
| `get_logs_active_deployment_aggregate` | `SELECT` | `app_id, type` | Retrieve the logs of the active deployment if one exists. The response will include links to either real-time logs of an in-progress or active deployment or archived logs of a past deployment. Note log_type=BUILD logs will return logs associated with the current active deployment (being served). To view build logs associated with in-progress build, the query must explicitly reference the deployment id. |
| `get_logs_aggregate` | `SELECT` | `app_id, deployment_id, type` | Retrieve the logs of a past, in-progress, or active deployment. If a component name is specified, the logs will be limited to only that component. The response will include links to either real-time logs of an in-progress or active deployment or archived logs of a past deployment. |
