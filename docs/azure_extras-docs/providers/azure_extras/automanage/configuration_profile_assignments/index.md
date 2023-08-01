---
title: configuration_profile_assignments
hide_title: false
hide_table_of_contents: false
keywords:
  - configuration_profile_assignments
  - automanage
  - azure_extras    
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
<tr><td><b>Id</b></td><td><code>azure_extras.automanage.configuration_profile_assignments</code></td></tr>
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
| `ConfigurationProfileAssignments_Get` | `SELECT` | `configurationProfileAssignmentName, resourceGroupName, subscriptionId, vmName` | Get information about a configuration profile assignment |
| `ConfigurationProfileAssignments_List` | `SELECT` | `resourceGroupName, subscriptionId` | Get list of configuration profile assignments |
| `ConfigurationProfileAssignments_ListByClusterName` | `SELECT` | `clusterName, resourceGroupName, subscriptionId` | Get list of configuration profile assignments |
| `ConfigurationProfileAssignments_ListByMachineName` | `SELECT` | `machineName, resourceGroupName, subscriptionId` | Get list of configuration profile assignments |
| `ConfigurationProfileAssignments_ListBySubscription` | `SELECT` | `subscriptionId` | Get list of configuration profile assignments under a given subscription |
| `ConfigurationProfileAssignments_ListByVirtualMachines` | `SELECT` | `resourceGroupName, subscriptionId, vmName` | Get list of configuration profile assignments |
| `ConfigurationProfileAssignments_CreateOrUpdate` | `INSERT` | `configurationProfileAssignmentName, resourceGroupName, subscriptionId, vmName` | Creates an association between a VM and Automanage configuration profile |
| `ConfigurationProfileAssignments_Delete` | `DELETE` | `configurationProfileAssignmentName, resourceGroupName, subscriptionId, vmName` | Delete a configuration profile assignment |
