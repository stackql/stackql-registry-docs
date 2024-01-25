---
title: app_resiliency
hide_title: false
hide_table_of_contents: false
keywords:
  - app_resiliency
  - container_apps
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
<tr><td><b>Name</b></td><td><code>app_resiliency</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.container_apps.app_resiliency</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `appName, name, resourceGroupName, subscriptionId` | Get container app resiliency policy. |
| `list` | `SELECT` | `appName, resourceGroupName, subscriptionId` | List container app resiliency policies. |
| `create_or_update` | `INSERT` | `appName, name, resourceGroupName, subscriptionId` | Create or update container app resiliency policy. |
| `delete` | `DELETE` | `appName, name, resourceGroupName, subscriptionId` | Delete container app resiliency policy. |
| `_list` | `EXEC` | `appName, resourceGroupName, subscriptionId` | List container app resiliency policies. |
| `update` | `EXEC` | `appName, name, resourceGroupName, subscriptionId` | Update container app resiliency policy. |
