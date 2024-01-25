---
title: authorization_access_policy
hide_title: false
hide_table_of_contents: false
keywords:
  - authorization_access_policy
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
<tr><td><b>Name</b></td><td><code>authorization_access_policy</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.api_management.authorization_access_policy</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `authorizationAccessPolicyId, authorizationId, authorizationProviderId, resourceGroupName, serviceName, subscriptionId` | Gets the details of the authorization access policy specified by its identifier. |
| `list_by_authorization` | `SELECT` | `authorizationId, authorizationProviderId, resourceGroupName, serviceName, subscriptionId` | Lists a collection of authorization access policy defined within a authorization. |
| `create_or_update` | `INSERT` | `authorizationAccessPolicyId, authorizationId, authorizationProviderId, resourceGroupName, serviceName, subscriptionId` | Creates or updates Authorization Access Policy. |
| `delete` | `DELETE` | `If-Match, authorizationAccessPolicyId, authorizationId, authorizationProviderId, resourceGroupName, serviceName, subscriptionId` | Deletes specific access policy from the Authorization. |
| `_list_by_authorization` | `EXEC` | `authorizationId, authorizationProviderId, resourceGroupName, serviceName, subscriptionId` | Lists a collection of authorization access policy defined within a authorization. |
