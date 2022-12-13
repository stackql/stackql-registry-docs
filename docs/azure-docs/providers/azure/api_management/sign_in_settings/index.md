---
title: sign_in_settings
hide_title: false
hide_table_of_contents: false
keywords:
  - sign_in_settings
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
<tr><td><b>Name</b></td><td><code>sign_in_settings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.api_management.sign_in_settings</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125; |
| `name` | `string` | The name of the resource |
| `properties` | `object` | Sign-in settings contract properties. |
| `type` | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `SignInSettings_Get` | `SELECT` | `resourceGroupName, serviceName, subscriptionId` | Get Sign In Settings for the Portal |
| `SignInSettings_CreateOrUpdate` | `INSERT` | `resourceGroupName, serviceName, subscriptionId` | Create or Update Sign-In settings. |
| `SignInSettings_GetEntityTag` | `EXEC` | `resourceGroupName, serviceName, subscriptionId` | Gets the entity state (Etag) version of the SignInSettings. |
| `SignInSettings_Update` | `EXEC` | `If-Match, resourceGroupName, serviceName, subscriptionId` | Update Sign-In settings. |
