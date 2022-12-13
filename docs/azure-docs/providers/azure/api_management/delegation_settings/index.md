---
title: delegation_settings
hide_title: false
hide_table_of_contents: false
keywords:
  - delegation_settings
  - api_management
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
<tr><td><b>Name</b></td><td><code>delegation_settings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.api_management.delegation_settings</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125; |
| `name` | `string` | The name of the resource |
| `type` | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
| `properties` | `object` | Delegation settings contract properties. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `DelegationSettings_Get` | `SELECT` | `resourceGroupName, serviceName, subscriptionId` | Get Delegation Settings for the Portal. |
| `DelegationSettings_CreateOrUpdate` | `INSERT` | `resourceGroupName, serviceName, subscriptionId` | Create or Update Delegation settings. |
| `DelegationSettings_GetEntityTag` | `EXEC` | `resourceGroupName, serviceName, subscriptionId` | Gets the entity state (Etag) version of the DelegationSettings. |
| `DelegationSettings_ListSecrets` | `EXEC` | `resourceGroupName, serviceName, subscriptionId` | Gets the secret validation key of the DelegationSettings. |
| `DelegationSettings_Update` | `EXEC` | `If-Match, resourceGroupName, serviceName, subscriptionId` | Update Delegation settings. |
