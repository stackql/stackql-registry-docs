---
title: identity_provider
hide_title: false
hide_table_of_contents: false
keywords:
  - identity_provider
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
<tr><td><b>Name</b></td><td><code>identity_provider</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.api_management.identity_provider</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125; |
| `name` | `string` | The name of the resource |
| `type` | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
| `properties` | `object` | The external Identity Providers like Facebook, Google, Microsoft, Twitter or Azure Active Directory which can be used to enable access to the API Management service developer portal for all users. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `IdentityProvider_Get` | `SELECT` | `identityProviderName, resourceGroupName, serviceName, subscriptionId` | Gets the configuration details of the identity Provider configured in specified service instance. |
| `IdentityProvider_ListByService` | `SELECT` | `resourceGroupName, serviceName, subscriptionId` | Lists a collection of Identity Provider configured in the specified service instance. |
| `IdentityProvider_CreateOrUpdate` | `INSERT` | `identityProviderName, resourceGroupName, serviceName, subscriptionId` | Creates or Updates the IdentityProvider configuration. |
| `IdentityProvider_Delete` | `DELETE` | `If-Match, identityProviderName, resourceGroupName, serviceName, subscriptionId` | Deletes the specified identity provider configuration. |
| `IdentityProvider_GetEntityTag` | `EXEC` | `identityProviderName, resourceGroupName, serviceName, subscriptionId` | Gets the entity state (Etag) version of the identityProvider specified by its identifier. |
| `IdentityProvider_ListSecrets` | `EXEC` | `identityProviderName, resourceGroupName, serviceName, subscriptionId` | Gets the client secret details of the Identity Provider. |
| `IdentityProvider_Update` | `EXEC` | `If-Match, identityProviderName, resourceGroupName, serviceName, subscriptionId` | Updates an existing IdentityProvider configuration. |
