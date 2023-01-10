---
title: updates
hide_title: false
hide_table_of_contents: false
keywords:
  - updates
  - update_admin
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
<tr><td><b>Name</b></td><td><code>updates</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.update_admin.updates</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125; |
| `name` | `string` | The name of the resource |
| `properties` | `object` | Properties of an update. |
| `type` | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Updates_Get` | `SELECT` | `resourceGroupName, subscriptionId, updateLocation, updateName` | Get a specific update at an update location. |
| `Updates_List` | `SELECT` | `resourceGroupName, subscriptionId, updateLocation` | Get the list of updates at an update locations |
| `Updates_Apply` | `EXEC` | `resourceGroupName, subscriptionId, updateLocation, updateName` | Apply a specific update at an update location. |
| `Updates_HealthCheck` | `EXEC` | `resourceGroupName, subscriptionId, updateLocation, updateName` | Run health check for a specified update at an update location. |
| `Updates_Prepare` | `EXEC` | `resourceGroupName, subscriptionId, updateLocation, updateName` | Prepare a specified update at an update location. |
