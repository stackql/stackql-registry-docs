---
title: domains
hide_title: false
hide_table_of_contents: false
keywords:
  - domains
  - web_apps
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
<tr><td><b>Name</b></td><td><code>domains</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.web_apps.domains</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource Id. |
| `name` | `string` | Resource Name. |
| `properties` | `object` | Domain resource specific properties |
| `tags` | `object` | Resource tags. |
| `type` | `string` | Resource type. |
| `kind` | `string` | Kind of resource. |
| `location` | `string` | Resource Location. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Domains_Get` | `SELECT` | `domainName, resourceGroupName, subscriptionId` | Description for Get a domain. |
| `Domains_List` | `SELECT` | `subscriptionId` | Description for Get all domains in a subscription. |
| `Domains_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` | Description for Get all domains in a resource group. |
| `Domains_CreateOrUpdate` | `INSERT` | `domainName, resourceGroupName, subscriptionId` | Description for Creates or updates a domain. |
| `Domains_Delete` | `DELETE` | `domainName, resourceGroupName, subscriptionId` | Description for Delete a domain. |
| `Domains_CheckAvailability` | `EXEC` | `subscriptionId` | Description for Check if a domain is available for registration. |
| `Domains_CreateOrUpdateOwnershipIdentifier` | `EXEC` | `domainName, name, resourceGroupName, subscriptionId` | Description for Creates an ownership identifier for a domain or updates identifier details for an existing identifier |
| `Domains_DeleteOwnershipIdentifier` | `EXEC` | `domainName, name, resourceGroupName, subscriptionId` | Description for Delete ownership identifier for domain |
| `Domains_GetControlCenterSsoRequest` | `EXEC` | `subscriptionId` | Description for Generate a single sign-on request for the domain management portal. |
| `Domains_GetOwnershipIdentifier` | `EXEC` | `domainName, name, resourceGroupName, subscriptionId` | Description for Get ownership identifier for domain |
| `Domains_ListOwnershipIdentifiers` | `EXEC` | `domainName, resourceGroupName, subscriptionId` | Description for Lists domain ownership identifiers. |
| `Domains_ListRecommendations` | `EXEC` | `subscriptionId` | Description for Get domain name recommendations based on keywords. |
| `Domains_Renew` | `EXEC` | `domainName, resourceGroupName, subscriptionId` | Description for Renew a domain. |
| `Domains_TransferOut` | `EXEC` | `domainName, resourceGroupName, subscriptionId` |  |
| `Domains_Update` | `EXEC` | `domainName, resourceGroupName, subscriptionId` | Description for Creates or updates a domain. |
| `Domains_UpdateOwnershipIdentifier` | `EXEC` | `domainName, name, resourceGroupName, subscriptionId` | Description for Creates an ownership identifier for a domain or updates identifier details for an existing identifier |
