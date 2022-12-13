---
title: workspace_settings
hide_title: false
hide_table_of_contents: false
keywords:
  - workspace_settings
  - security
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
<tr><td><b>Name</b></td><td><code>workspace_settings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.security.workspace_settings</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125; |
| `name` | `string` | The name of the resource |
| `properties` | `object` | Workspace setting data |
| `type` | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `WorkspaceSettings_Get` | `SELECT` | `api-version, subscriptionId, workspaceSettingName` | Settings about where we should store your security data and logs. If the result is empty, it means that no custom-workspace configuration was set |
| `WorkspaceSettings_List` | `SELECT` | `api-version, subscriptionId` | Settings about where we should store your security data and logs. If the result is empty, it means that no custom-workspace configuration was set |
| `WorkspaceSettings_Create` | `INSERT` | `api-version, subscriptionId, workspaceSettingName` | creating settings about where we should store your security data and logs |
| `WorkspaceSettings_Delete` | `DELETE` | `api-version, subscriptionId, workspaceSettingName` | Deletes the custom workspace settings for this subscription. new VMs will report to the default workspace |
| `WorkspaceSettings_Update` | `EXEC` | `api-version, subscriptionId, workspaceSettingName` | Settings about where we should store your security data and logs |
