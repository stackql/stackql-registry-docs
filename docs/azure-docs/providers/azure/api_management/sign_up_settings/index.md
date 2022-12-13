---
title: sign_up_settings
hide_title: false
hide_table_of_contents: false
keywords:
  - sign_up_settings
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
<tr><td><b>Name</b></td><td><code>sign_up_settings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.api_management.sign_up_settings</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125; |
| `name` | `string` | The name of the resource |
| `properties` | `object` | Sign-up settings contract properties. |
| `type` | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `SignUpSettings_Get` | `SELECT` | `resourceGroupName, serviceName, subscriptionId` | Get Sign Up Settings for the Portal |
| `SignUpSettings_CreateOrUpdate` | `INSERT` | `resourceGroupName, serviceName, subscriptionId` | Create or Update Sign-Up settings. |
| `SignUpSettings_GetEntityTag` | `EXEC` | `resourceGroupName, serviceName, subscriptionId` | Gets the entity state (Etag) version of the SignUpSettings. |
| `SignUpSettings_Update` | `EXEC` | `If-Match, resourceGroupName, serviceName, subscriptionId` | Update Sign-Up settings. |
