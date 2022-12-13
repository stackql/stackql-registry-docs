---
title: security_partner_providers
hide_title: false
hide_table_of_contents: false
keywords:
  - security_partner_providers
  - network
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
<tr><td><b>Name</b></td><td><code>security_partner_providers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.network.security_partner_providers</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource ID. |
| `name` | `string` | Resource name. |
| `properties` | `object` | Properties of the Security Partner Provider. |
| `tags` | `object` | Resource tags. |
| `type` | `string` | Resource type. |
| `etag` | `string` | A unique read-only string that changes whenever the resource is updated. |
| `location` | `string` | Resource location. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `SecurityPartnerProviders_Get` | `SELECT` | `resourceGroupName, securityPartnerProviderName, subscriptionId` | Gets the specified Security Partner Provider. |
| `SecurityPartnerProviders_List` | `SELECT` | `subscriptionId` | Gets all the Security Partner Providers in a subscription. |
| `SecurityPartnerProviders_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` | Lists all Security Partner Providers in a resource group. |
| `SecurityPartnerProviders_CreateOrUpdate` | `INSERT` | `resourceGroupName, securityPartnerProviderName, subscriptionId` | Creates or updates the specified Security Partner Provider. |
| `SecurityPartnerProviders_Delete` | `DELETE` | `resourceGroupName, securityPartnerProviderName, subscriptionId` | Deletes the specified Security Partner Provider. |
| `SecurityPartnerProviders_UpdateTags` | `EXEC` | `resourceGroupName, securityPartnerProviderName, subscriptionId` | Updates tags of a Security Partner Provider resource. |
