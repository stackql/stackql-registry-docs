---
title: machine_pools
hide_title: false
hide_table_of_contents: false
keywords:
  - machine_pools
  - redhat_openshift
  - azure_isv    
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
<tr><td><b>Name</b></td><td><code>machine_pools</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_isv.redhat_openshift.machine_pools</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `properties` | `object` | MachinePoolProperties represents the properties of a MachinePool |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `childResourceName, resourceGroupName, resourceName, subscriptionId` | The operation returns properties of a MachinePool. |
| `list` | `SELECT` | `resourceGroupName, resourceName, subscriptionId` | The operation returns properties of each MachinePool. |
| `create_or_update` | `INSERT` | `childResourceName, resourceGroupName, resourceName, subscriptionId` | The operation returns properties of a MachinePool. |
| `delete` | `DELETE` | `childResourceName, resourceGroupName, resourceName, subscriptionId` | The operation returns nothing. |
| `_list` | `EXEC` | `resourceGroupName, resourceName, subscriptionId` | The operation returns properties of each MachinePool. |
| `update` | `EXEC` | `childResourceName, resourceGroupName, resourceName, subscriptionId` | The operation returns properties of a MachinePool. |
