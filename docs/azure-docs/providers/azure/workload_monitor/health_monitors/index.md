---
title: health_monitors
hide_title: false
hide_table_of_contents: false
keywords:
  - health_monitors
  - workload_monitor
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
<tr><td><b>Name</b></td><td><code>health_monitors</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.workload_monitor.health_monitors</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The resource Id. |
| `name` | `string` | The resource name. |
| `properties` | `object` | Properties of the monitor. |
| `type` | `string` | The resource type. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get` | `SELECT` | `api-version, monitorId, providerName, resourceCollectionName, resourceGroupName, resourceName, subscriptionId` |
| `list` | `SELECT` | `api-version, providerName, resourceCollectionName, resourceGroupName, resourceName, subscriptionId` |
| `_list` | `EXEC` | `api-version, providerName, resourceCollectionName, resourceGroupName, resourceName, subscriptionId` |
