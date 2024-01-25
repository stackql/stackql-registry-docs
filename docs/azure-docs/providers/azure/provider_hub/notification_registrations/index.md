---
title: notification_registrations
hide_title: false
hide_table_of_contents: false
keywords:
  - notification_registrations
  - provider_hub
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
<tr><td><b>Name</b></td><td><code>notification_registrations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.provider_hub.notification_registrations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125; |
| `name` | `string` | The name of the resource |
| `properties` | `object` |  |
| `type` | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `notificationRegistrationName, providerNamespace, subscriptionId` | Gets the notification registration details. |
| `list_by_provider_registration` | `SELECT` | `providerNamespace, subscriptionId` | Gets the list of the notification registrations for the given provider. |
| `create_or_update` | `INSERT` | `notificationRegistrationName, providerNamespace, subscriptionId` | Creates or updates a notification registration. |
| `delete` | `DELETE` | `notificationRegistrationName, providerNamespace, subscriptionId` | Deletes a notification registration. |
| `_list_by_provider_registration` | `EXEC` | `providerNamespace, subscriptionId` | Gets the list of the notification registrations for the given provider. |
