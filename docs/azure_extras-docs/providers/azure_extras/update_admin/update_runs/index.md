---
title: update_runs
hide_title: false
hide_table_of_contents: false
keywords:
  - update_runs
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
<tr><td><b>Name</b></td><td><code>update_runs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.update_admin.update_runs</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125; |
| `name` | `string` | The name of the resource |
| `type` | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
| `properties` | `object` | Properties of an update run. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `UpdateRuns_Get` | `SELECT` | `resourceGroupName, runName, subscriptionId, updateLocation, updateName` | Get an instance of update run using the ID. |
| `UpdateRuns_List` | `SELECT` | `resourceGroupName, subscriptionId, updateLocation, updateName` | Get the list of update runs. |
| `UpdateRuns_GetTopLevel` | `EXEC` | `resourceGroupName, runName, subscriptionId, updateLocation` | Get an instance of update run using the ID. |
| `UpdateRuns_ListTopLevel` | `EXEC` | `resourceGroupName, subscriptionId, updateLocation` | Get the list of update runs. |
| `UpdateRuns_Rerun` | `EXEC` | `resourceGroupName, runName, subscriptionId, updateLocation, updateName` | Resume a failed update. |
