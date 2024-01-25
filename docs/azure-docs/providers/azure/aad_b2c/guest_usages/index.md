---
title: guest_usages
hide_title: false
hide_table_of_contents: false
keywords:
  - guest_usages
  - aad_b2c
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
<tr><td><b>Name</b></td><td><code>guest_usages</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.aad_b2c.guest_usages</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | An identifier that represents the Guest Usages resource. |
| `name` | `string` | The name of the Guest Usages resource. |
| `location` | `string` | Location of the Guest Usages resource. |
| `properties` | `object` | Guest Usages Resource Properties |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `tags` | `object` | Key-value pairs of additional resource provisioning properties. |
| `type` | `string` | The type of the Guest Usages resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `resourceGroupName, resourceName, subscriptionId` | Gets a Guest Usages resource for the Microsoft.AzureActiveDirectory resource provider |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | Gets Guest Usages resources under a resource group for the Microsoft.AzureActiveDirectory resource provider |
| `list_by_subscription` | `SELECT` | `subscriptionId` | Gets Guest Usages resources under a subscription for the Microsoft.AzureActiveDirectory resource provider |
| `create` | `INSERT` | `resourceGroupName, resourceName, subscriptionId` | Creates a Guest Usages resource, which is used to linking a subscription to an instance of Azure AD External Identities. [Learn more](https://aka.ms/extidbilling). |
| `delete` | `DELETE` | `resourceGroupName, resourceName, subscriptionId` | Deletes a Guest Usages resource for the Microsoft.AzureActiveDirectory resource provider |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | Gets Guest Usages resources under a resource group for the Microsoft.AzureActiveDirectory resource provider |
| `_list_by_subscription` | `EXEC` | `subscriptionId` | Gets Guest Usages resources under a subscription for the Microsoft.AzureActiveDirectory resource provider |
| `update` | `EXEC` | `resourceGroupName, resourceName, subscriptionId` | Updates a Guest Usages resource for the Microsoft.AzureActiveDirectory resource provider |
