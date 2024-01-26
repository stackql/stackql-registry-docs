---
title: manifests
hide_title: false
hide_table_of_contents: false
keywords:
  - manifests
  - subscriptions_admin
  - azure_stack    
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
<tr><td><b>Name</b></td><td><code>manifests</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_stack.subscriptions_admin.manifests</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | The unique identifier of the registration. |
| `alwaysRoutable` | `boolean` | A value indicating whether the manifest is always routable by all subscriptions. |
| `displayName` | `string` | The display name. |
| `enabled` | `boolean` | A value indicating whether this resource provider is enabled. |
| `extensionCollection` | `object` | The manifest extension collection definition. |
| `linkedNotificationRules` | `object` | List of the linked notification rules. |
| `metadata` | `object` | The metadata. |
| `namespace` | `string` | The namespace. |
| `providerAuthorization` | `object` | The resource provider authorization information. |
| `providerLocation` | `string` | The location of the provider. |
| `providerType` | `string` | The resource provider type. |
| `provisioningState` | `string` | The provisioning state. |
| `resourceGroupName` | `string` | The name of the resource group. |
| `resourceHydrationAccounts` | `object` | List of the resource hydration accounts. |
| `resourceLocation` | `string` | The location of the resource. |
| `resourceTags` | `object` | The resource tags. |
| `resourceTypes` | `object` | List of the resource types. |
| `routingResourceManagerType` | `string` | Resource manager type. |
| `subscriptionId` | `string` | The subscription ID under which RP is registered. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `manifestName, subscriptionId` | Get the specified manifest. |
| `list` | `SELECT` | `subscriptionId` | Get a list of all manifests. |
| `_list` | `EXEC` | `subscriptionId` | Get a list of all manifests. |
