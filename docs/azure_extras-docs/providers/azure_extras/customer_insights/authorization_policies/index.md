---
title: authorization_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - authorization_policies
  - customer_insights
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
<tr><td><b>Name</b></td><td><code>authorization_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.customer_insights.authorization_policies</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource ID. |
| `name` | `string` | Resource name. |
| `properties` | `object` | The authorization policy. |
| `type` | `string` | Resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `AuthorizationPolicies_Get` | `SELECT` | `authorizationPolicyName, hubName, resourceGroupName, subscriptionId` | Gets an authorization policy in the hub. |
| `AuthorizationPolicies_ListByHub` | `SELECT` | `hubName, resourceGroupName, subscriptionId` | Gets all the authorization policies in a specified hub. |
| `AuthorizationPolicies_CreateOrUpdate` | `INSERT` | `authorizationPolicyName, hubName, resourceGroupName, subscriptionId` | Creates an authorization policy or updates an existing authorization policy. |
| `AuthorizationPolicies_RegeneratePrimaryKey` | `EXEC` | `authorizationPolicyName, hubName, resourceGroupName, subscriptionId` | Regenerates the primary policy key of the specified authorization policy. |
| `AuthorizationPolicies_RegenerateSecondaryKey` | `EXEC` | `authorizationPolicyName, hubName, resourceGroupName, subscriptionId` | Regenerates the secondary policy key of the specified authorization policy. |
