---
title: web_apps_perf_mon_counters_slot
hide_title: false
hide_table_of_contents: false
keywords:
  - web_apps_perf_mon_counters_slot
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
<tr><td><b>Name</b></td><td><code>web_apps_perf_mon_counters_slot</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.app_service.web_apps_perf_mon_counters_slot</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `code` | `string` | The response code. |
| `data` | `object` | Metric information. |
| `message` | `string` | The message. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list` | `SELECT` | `name, resourceGroupName, slot, subscriptionId` |
| `_list` | `EXEC` | `name, resourceGroupName, slot, subscriptionId` |
