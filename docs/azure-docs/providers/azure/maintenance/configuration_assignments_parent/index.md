---
title: configuration_assignments_parent
hide_title: false
hide_table_of_contents: false
keywords:
  - configuration_assignments_parent
  - maintenance
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
<tr><td><b>Name</b></td><td><code>configuration_assignments_parent</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.maintenance.configuration_assignments_parent</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. E.g. "/subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;" |
| `name` | `string` | The name of the resource |
| `location` | `string` | Location of the resource |
| `properties` | `object` | Properties for configuration assignment |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `type` | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `configurationAssignmentName, providerName, resourceGroupName, resourceName, resourceParentName, resourceParentType, resourceType, subscriptionId` | Get configuration assignment for resource.. |
| `list` | `SELECT` | `providerName, resourceGroupName, resourceName, resourceParentName, resourceParentType, resourceType, subscriptionId` | List configurationAssignments for resource. |
| `create_or_update` | `INSERT` | `configurationAssignmentName, providerName, resourceGroupName, resourceName, resourceParentName, resourceParentType, resourceType, subscriptionId` | Register configuration for resource. |
| `delete` | `DELETE` | `configurationAssignmentName, providerName, resourceGroupName, resourceName, resourceParentName, resourceParentType, resourceType, subscriptionId` | Unregister configuration for resource. |
| `_list` | `EXEC` | `providerName, resourceGroupName, resourceName, resourceParentName, resourceParentType, resourceType, subscriptionId` | List configurationAssignments for resource. |
