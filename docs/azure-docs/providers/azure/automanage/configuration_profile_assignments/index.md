---
title: configuration_profile_assignments
hide_title: false
hide_table_of_contents: false
keywords:
  - configuration_profile_assignments
  - automanage
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
<tr><td><b>Name</b></td><td><code>configuration_profile_assignments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.automanage.configuration_profile_assignments</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `managedBy` | `string` | Azure resource id. Indicates if this resource is managed by another Azure resource. |
| `properties` | `object` | Automanage configuration profile assignment properties. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `configurationProfileAssignmentName, resourceGroupName, subscriptionId, vmName` | Get information about a configuration profile assignment |
| `list` | `SELECT` | `resourceGroupName, subscriptionId` | Get list of configuration profile assignments |
| `list_by_cluster_name` | `SELECT` | `clusterName, resourceGroupName, subscriptionId` | Get list of configuration profile assignments |
| `list_by_machine_name` | `SELECT` | `machineName, resourceGroupName, subscriptionId` | Get list of configuration profile assignments |
| `list_by_subscription` | `SELECT` | `subscriptionId` | Get list of configuration profile assignments under a given subscription |
| `list_by_virtual_machines` | `SELECT` | `resourceGroupName, subscriptionId, vmName` | Get list of configuration profile assignments |
| `create_or_update` | `INSERT` | `configurationProfileAssignmentName, resourceGroupName, subscriptionId, vmName` | Creates an association between a VM and Automanage configuration profile |
| `delete` | `DELETE` | `configurationProfileAssignmentName, resourceGroupName, subscriptionId, vmName` | Delete a configuration profile assignment |
| `_list` | `EXEC` | `resourceGroupName, subscriptionId` | Get list of configuration profile assignments |
| `_list_by_cluster_name` | `EXEC` | `clusterName, resourceGroupName, subscriptionId` | Get list of configuration profile assignments |
| `_list_by_machine_name` | `EXEC` | `machineName, resourceGroupName, subscriptionId` | Get list of configuration profile assignments |
| `_list_by_subscription` | `EXEC` | `subscriptionId` | Get list of configuration profile assignments under a given subscription |
| `_list_by_virtual_machines` | `EXEC` | `resourceGroupName, subscriptionId, vmName` | Get list of configuration profile assignments |
