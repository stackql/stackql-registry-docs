---
title: accounts
hide_title: false
hide_table_of_contents: false
keywords:
  - accounts
  - intelligent_recommendations
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
<tr><td><b>Name</b></td><td><code>accounts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.intelligent_recommendations.accounts</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `identity` | `object` | Managed service identity (system assigned and/or user assigned identities) |
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | Account resource properties. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `accountName, resourceGroupName, subscriptionId` | Returns RecommendationsService Account resource for a given name. |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | Returns list of RecommendationsService Account resources. |
| `list_by_subscription` | `SELECT` | `subscriptionId` | Returns list of RecommendationsService Account resources. |
| `create_or_update` | `INSERT` | `accountName, resourceGroupName, subscriptionId` | Creates or updates RecommendationsService Account resource. |
| `delete` | `DELETE` | `accountName, resourceGroupName, subscriptionId` | Deletes RecommendationsService Account resource. |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | Returns list of RecommendationsService Account resources. |
| `_list_by_subscription` | `EXEC` | `subscriptionId` | Returns list of RecommendationsService Account resources. |
| `check_name_availability` | `EXEC` | `subscriptionId` | Checks that the RecommendationsService Account name is valid and is not already in use. |
| `update` | `EXEC` | `accountName, resourceGroupName, subscriptionId` | Updates RecommendationsService Account details. |
