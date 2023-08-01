---
title: accounts
hide_title: false
hide_table_of_contents: false
keywords:
  - accounts
  - recommendations_service
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
<tr><td><b>Id</b></td><td><code>azure_extras.recommendations_service.accounts</code></td></tr>
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
| `Accounts_Get` | `SELECT` | `accountName, resourceGroupName, subscriptionId` | Returns RecommendationsService Account resource for a given name. |
| `Accounts_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` | Returns list of RecommendationsService Account resources. |
| `Accounts_ListBySubscription` | `SELECT` | `subscriptionId` | Returns list of RecommendationsService Account resources. |
| `Accounts_CreateOrUpdate` | `INSERT` | `accountName, resourceGroupName, subscriptionId` | Creates or updates RecommendationsService Account resource. |
| `Accounts_Delete` | `DELETE` | `accountName, resourceGroupName, subscriptionId` | Deletes RecommendationsService Account resource. |
| `Accounts_CheckNameAvailability` | `EXEC` | `subscriptionId` | Checks that the RecommendationsService Account name is valid and is not already in use. |
| `Accounts_GetStatus` | `EXEC` | `accountName, resourceGroupName, subscriptionId` | Returns RecommendationsService Account status. |
| `Accounts_Update` | `EXEC` | `accountName, resourceGroupName, subscriptionId` | Updates RecommendationsService Account details. |
