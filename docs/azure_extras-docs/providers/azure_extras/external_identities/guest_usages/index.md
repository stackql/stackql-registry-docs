---
title: guest_usages
hide_title: false
hide_table_of_contents: false
keywords:
  - guest_usages
  - external_identities
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
<tr><td><b>Name</b></td><td><code>guest_usages</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.external_identities.guest_usages</code></td></tr>
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
| `GuestUsages_Get` | `SELECT` | `resourceGroupName, resourceName, subscriptionId` | Gets a Guest Usages resource for the Microsoft.AzureActiveDirectory resource provider |
| `GuestUsages_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` | Gets Guest Usages resources under a resource group for the Microsoft.AzureActiveDirectory resource provider |
| `GuestUsages_ListBySubscription` | `SELECT` | `subscriptionId` | Gets Guest Usages resources under a subscription for the Microsoft.AzureActiveDirectory resource provider |
| `GuestUsages_Create` | `INSERT` | `resourceGroupName, resourceName, subscriptionId` | Creates a Guest Usages resource, which is used to linking a subscription to an instance of Azure AD External Identities. [Learn more](https://aka.ms/extidbilling). |
| `GuestUsages_Delete` | `DELETE` | `resourceGroupName, resourceName, subscriptionId` | Deletes a Guest Usages resource for the Microsoft.AzureActiveDirectory resource provider |
| `GuestUsages_Update` | `EXEC` | `resourceGroupName, resourceName, subscriptionId` | Updates a Guest Usages resource for the Microsoft.AzureActiveDirectory resource provider |
