---
title: web_apps_network_traces
hide_title: false
hide_table_of_contents: false
keywords:
  - web_apps_network_traces
  - app_service
  - azure    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Azure resources using SQL
custom_edit_url: null
image: /img/providers/azure/stackql-azure-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>web_apps_network_traces</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.app_service.web_apps_network_traces</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `message` | `string` | Detailed message of a network trace operation, e.g. error message in case of failure. |
| `path` | `string` | Local file path for the captured network trace file. |
| `status` | `string` | Current status of the network trace operation, same as Operation.Status (InProgress/Succeeded/Failed). |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get` | `SELECT` | `name, operationId, resourceGroupName, subscriptionId` |
