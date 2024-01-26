---
title: container_registry_configuration
hide_title: false
hide_table_of_contents: false
keywords:
  - container_registry_configuration
  - container_registry_admin
  - azure_stack    
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
<tr><td><b>Name</b></td><td><code>container_registry_configuration</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_stack.container_registry_admin.container_registry_configuration</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125; |
| `name` | `string` | The name of the resource |
| `properties` | `object` | Container registry configuration property. |
| `type` | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `configurationName, location, subscriptionId` | Returns the specified configuration details. |
| `list` | `SELECT` | `location, subscriptionId` | Returns a list of configuration at the given location. |
| `delete` | `DELETE` | `configurationName, location, subscriptionId` | Delete an existing container registry configuration |
| `_list` | `EXEC` | `location, subscriptionId` | Returns a list of configuration at the given location. |
| `put` | `EXEC` | `configurationName, location, subscriptionId, data__properties` | Configure container registry overall configuration properties. |
