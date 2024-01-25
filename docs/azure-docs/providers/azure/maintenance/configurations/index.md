---
title: configurations
hide_title: false
hide_table_of_contents: false
keywords:
  - configurations
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
<tr><td><b>Name</b></td><td><code>configurations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.maintenance.configurations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. E.g. "/subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;" |
| `name` | `string` | The name of the resource |
| `location` | `string` | Gets or sets location of the resource |
| `properties` | `object` | Properties for maintenance configuration |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `tags` | `object` | Gets or sets tags of the resource |
| `type` | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get` | `SELECT` | `resourceGroupName, resourceName, subscriptionId` |
| `list` | `SELECT` | `subscriptionId` |
| `create_or_update` | `INSERT` | `resourceGroupName, resourceName, subscriptionId` |
| `delete` | `DELETE` | `resourceGroupName, resourceName, subscriptionId` |
| `_list` | `EXEC` | `subscriptionId` |
| `update` | `EXEC` | `resourceGroupName, resourceName, subscriptionId` |
