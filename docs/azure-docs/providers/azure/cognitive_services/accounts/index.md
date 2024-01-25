---
title: accounts
hide_title: false
hide_table_of_contents: false
keywords:
  - accounts
  - cognitive_services
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
<tr><td><b>Name</b></td><td><code>accounts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.cognitive_services.accounts</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `etag` | `string` | Resource Etag. |
| `identity` | `object` | Identity for the resource. |
| `kind` | `string` | The kind (type) of cognitive service account. |
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | Properties of Cognitive Services account. |
| `sku` | `object` | The resource model definition representing SKU |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `accountName, resourceGroupName, subscriptionId` | Returns a Cognitive Services account specified by the parameters. |
| `list` | `SELECT` | `subscriptionId` | Returns all the resources of a particular type belonging to a subscription. |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | Returns all the resources of a particular type belonging to a resource group |
| `create` | `INSERT` | `accountName, resourceGroupName, subscriptionId` | Create Cognitive Services Account. Accounts is a resource group wide resource type. It holds the keys for developer to access intelligent APIs. It's also the resource type for billing. |
| `delete` | `DELETE` | `accountName, resourceGroupName, subscriptionId` | Deletes a Cognitive Services account from the resource group.  |
| `_list` | `EXEC` | `subscriptionId` | Returns all the resources of a particular type belonging to a subscription. |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | Returns all the resources of a particular type belonging to a resource group |
| `cognitive_services_accounts` | `EXEC` | `subscriptionId, data__subdomainName, data__type` | Check whether a domain is available. |
| `regenerate_key` | `EXEC` | `accountName, resourceGroupName, subscriptionId, data__keyName` | Regenerates the specified account key for the specified Cognitive Services account. |
| `update` | `EXEC` | `accountName, resourceGroupName, subscriptionId` | Updates a Cognitive Services account |
