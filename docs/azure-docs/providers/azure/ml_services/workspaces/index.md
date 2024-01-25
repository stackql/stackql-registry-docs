---
title: workspaces
hide_title: false
hide_table_of_contents: false
keywords:
  - workspaces
  - ml_services
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
<tr><td><b>Name</b></td><td><code>workspaces</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.ml_services.workspaces</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125; |
| `name` | `string` | The name of the resource |
| `identity` | `object` | Managed service identity (system assigned and/or user assigned identities) |
| `kind` | `string` |  |
| `location` | `string` |  |
| `properties` | `object` | The properties of a machine learning workspace. |
| `sku` | `object` | The resource model definition representing SKU |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `tags` | `object` |  |
| `type` | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get` | `SELECT` | `resourceGroupName, subscriptionId, workspaceName` |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` |
| `list_by_subscription` | `SELECT` | `subscriptionId` |
| `create_or_update` | `INSERT` | `resourceGroupName, subscriptionId, workspaceName, data__properties` |
| `delete` | `DELETE` | `resourceGroupName, subscriptionId, workspaceName` |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` |
| `_list_by_subscription` | `EXEC` | `subscriptionId` |
| `diagnose` | `EXEC` | `resourceGroupName, subscriptionId, workspaceName` |
| `prepare_notebook` | `EXEC` | `resourceGroupName, subscriptionId, workspaceName` |
| `resync_keys` | `EXEC` | `resourceGroupName, subscriptionId, workspaceName` |
| `update` | `EXEC` | `resourceGroupName, subscriptionId, workspaceName` |
