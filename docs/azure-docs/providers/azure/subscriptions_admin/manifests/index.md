---
title: manifests
hide_title: false
hide_table_of_contents: false
keywords:
  - manifests
  - subscriptions_admin
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
<tr><td><b>Name</b></td><td><code>manifests</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.subscriptions_admin.manifests</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | The unique identifier of the registration. |
| `namespace` | `string` | The namespace. |
| `linkedNotificationRules` | `object` | List of the linked notification rules. |
| `providerAuthorization` | `object` | The resource provider authorization information. |
| `displayName` | `string` | The display name. |
| `routingResourceManagerType` | `string` | Resource manager type. |
| `resourceHydrationAccounts` | `object` | List of the resource hydration accounts. |
| `providerLocation` | `string` | The location of the provider. |
| `extensionCollection` | `object` | The manifest extension collection definition. |
| `providerType` | `string` | The resource provider type. |
| `resourceTypes` | `object` | List of the resource types. |
| `resourceTags` | `object` | The resource tags. |
| `resourceLocation` | `string` | The location of the resource. |
| `provisioningState` | `string` | The provisioning state. |
| `enabled` | `boolean` | A value indicating whether this resource provider is enabled. |
| `alwaysRoutable` | `boolean` | A value indicating whether the manifest is always routable by all subscriptions. |
| `resourceGroupName` | `string` | The name of the resource group. |
| `metadata` | `object` | The metadata. |
| `subscriptionId` | `string` | The subscription ID under which RP is registered. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Manifests_Get` | `SELECT` | `manifestName, subscriptionId` | Get the specified manifest. |
| `Manifests_List` | `SELECT` | `subscriptionId` | Get a list of all manifests. |
