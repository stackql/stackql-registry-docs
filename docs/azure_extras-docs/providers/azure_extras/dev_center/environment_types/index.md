---
title: environment_types
hide_title: false
hide_table_of_contents: false
keywords:
  - environment_types
  - dev_center
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
<tr><td><b>Name</b></td><td><code>environment_types</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.dev_center.environment_types</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125; |
| `name` | `string` | The name of the resource |
| `properties` | `object` | Properties of an environment type. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `tags` | `object` | Resource tags. |
| `type` | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `EnvironmentTypes_Get` | `SELECT` | `devCenterName, environmentTypeName, resourceGroupName, subscriptionId` | Gets an environment type. |
| `EnvironmentTypes_ListByDevCenter` | `SELECT` | `devCenterName, resourceGroupName, subscriptionId` | Lists environment types for the devcenter. |
| `EnvironmentTypes_CreateOrUpdate` | `INSERT` | `devCenterName, environmentTypeName, resourceGroupName, subscriptionId` | Creates or updates an environment type. |
| `EnvironmentTypes_Delete` | `DELETE` | `devCenterName, environmentTypeName, resourceGroupName, subscriptionId` | Deletes an environment type. |
| `EnvironmentTypes_Update` | `EXEC` | `devCenterName, environmentTypeName, resourceGroupName, subscriptionId` | Partially updates an environment type. |
