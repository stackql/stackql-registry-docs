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
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `identityProviderName, resourceGroupName, serviceName, subscriptionId` | Gets the configuration details of the identity Provider configured in specified service instance. |
| `list_by_service` | `SELECT` | `resourceGroupName, serviceName, subscriptionId` | Lists a collection of Identity Provider configured in the specified service instance. |
| `create_or_update` | `INSERT` | `identityProviderName, resourceGroupName, serviceName, subscriptionId` | Creates or Updates the IdentityProvider configuration. |
| `delete` | `DELETE` | `If-Match, identityProviderName, resourceGroupName, serviceName, subscriptionId` | Deletes the specified identity provider configuration. |
| `_list_by_service` | `EXEC` | `resourceGroupName, serviceName, subscriptionId` | Lists a collection of Identity Provider configured in the specified service instance. |
| `update` | `EXEC` | `If-Match, identityProviderName, resourceGroupName, serviceName, subscriptionId` | Updates an existing IdentityProvider configuration. |
