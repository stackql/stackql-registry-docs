---
title: failover_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - failover_groups
  - azure_arc_data
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
<tr><td><b>Name</b></td><td><code>failover_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.azure_arc_data.failover_groups</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `api-version, failoverGroupName, resourceGroupName, sqlManagedInstanceName, subscriptionId` | Retrieves a failover group resource |
| `list` | `SELECT` | `api-version, resourceGroupName, sqlManagedInstanceName, subscriptionId` |  |
| `create` | `INSERT` | `api-version, failoverGroupName, resourceGroupName, sqlManagedInstanceName, subscriptionId, data__properties` | Creates or replaces a failover group resource. |
| `delete` | `DELETE` | `api-version, failoverGroupName, resourceGroupName, sqlManagedInstanceName, subscriptionId` | Deletes a failover group resource |
| `_list` | `EXEC` | `api-version, resourceGroupName, sqlManagedInstanceName, subscriptionId` |  |
