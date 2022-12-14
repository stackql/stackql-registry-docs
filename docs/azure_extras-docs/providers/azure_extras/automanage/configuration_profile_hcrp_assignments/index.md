---
title: configuration_profile_hcrp_assignments
hide_title: false
hide_table_of_contents: false
keywords:
  - configuration_profile_hcrp_assignments
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
<tr><td><b>Name</b></td><td><code>configuration_profile_hcrp_assignments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.automanage.configuration_profile_hcrp_assignments</code></td></tr>
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
| `ConfigurationProfileHCRPAssignments_Get` | `SELECT` | `configurationProfileAssignmentName, machineName, resourceGroupName, subscriptionId` | Get information about a configuration profile assignment |
| `ConfigurationProfileHCRPAssignments_CreateOrUpdate` | `INSERT` | `configurationProfileAssignmentName, machineName, resourceGroupName, subscriptionId` | Creates an association between a ARC machine and Automanage configuration profile |
| `ConfigurationProfileHCRPAssignments_Delete` | `DELETE` | `configurationProfileAssignmentName, machineName, resourceGroupName, subscriptionId` | Delete a configuration profile assignment |
