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
| `InstanceFailoverGroups_Get` | `SELECT` | `failoverGroupName, locationName, resourceGroupName, subscriptionId` | Gets a failover group. |
| `InstanceFailoverGroups_ListByLocation` | `SELECT` | `locationName, resourceGroupName, subscriptionId` | Lists the failover groups in a location. |
| `InstanceFailoverGroups_CreateOrUpdate` | `INSERT` | `failoverGroupName, locationName, resourceGroupName, subscriptionId` | Creates or updates a failover group. |
| `InstanceFailoverGroups_Delete` | `DELETE` | `failoverGroupName, locationName, resourceGroupName, subscriptionId` | Deletes a failover group. |
| `InstanceFailoverGroups_Failover` | `EXEC` | `failoverGroupName, locationName, resourceGroupName, subscriptionId` | Fails over from the current primary managed instance to this managed instance. |
| `InstanceFailoverGroups_ForceFailoverAllowDataLoss` | `EXEC` | `failoverGroupName, locationName, resourceGroupName, subscriptionId` | Fails over from the current primary managed instance to this managed instance. This operation might result in data loss. |
