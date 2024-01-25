---
title: instance_failover_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - instance_failover_groups
  - sql
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
<tr><td><b>Name</b></td><td><code>instance_failover_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.sql.instance_failover_groups</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `failoverGroupName, locationName, resourceGroupName, subscriptionId` | Gets a failover group. |
| `list_by_location` | `SELECT` | `locationName, resourceGroupName, subscriptionId` | Lists the failover groups in a location. |
| `create_or_update` | `INSERT` | `failoverGroupName, locationName, resourceGroupName, subscriptionId` | Creates or updates a failover group. |
| `delete` | `DELETE` | `failoverGroupName, locationName, resourceGroupName, subscriptionId` | Deletes a failover group. |
| `_list_by_location` | `EXEC` | `locationName, resourceGroupName, subscriptionId` | Lists the failover groups in a location. |
| `failover` | `EXEC` | `failoverGroupName, locationName, resourceGroupName, subscriptionId` | Fails over from the current primary managed instance to this managed instance. |
| `force_failover_allow_data_loss` | `EXEC` | `failoverGroupName, locationName, resourceGroupName, subscriptionId` | Fails over from the current primary managed instance to this managed instance. This operation might result in data loss. |
