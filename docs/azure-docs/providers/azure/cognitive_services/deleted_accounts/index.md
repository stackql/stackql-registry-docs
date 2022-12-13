---
title: deleted_accounts
hide_title: false
hide_table_of_contents: false
keywords:
  - deleted_accounts
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
<tr><td><b>Name</b></td><td><code>deleted_accounts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.cognitive_services.deleted_accounts</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `tags` | `object` | Resource tags. |
| `etag` | `string` | Resource Etag. |
| `identity` | `object` | Identity for the resource. |
| `kind` | `string` | The kind (type) of cognitive service account. |
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | Properties of Cognitive Services account. |
| `sku` | `object` | The resource model definition representing SKU |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `DeletedAccounts_Get` | `SELECT` | `accountName, location, resourceGroupName, subscriptionId` | Returns a Cognitive Services account specified by the parameters. |
| `DeletedAccounts_List` | `SELECT` | `subscriptionId` | Returns all the resources of a particular type belonging to a subscription. |
| `DeletedAccounts_Purge` | `EXEC` | `accountName, location, resourceGroupName, subscriptionId` | Deletes a Cognitive Services account from the resource group.  |
