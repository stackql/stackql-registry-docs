---
title: accounts
hide_title: false
hide_table_of_contents: false
keywords:
  - accounts
  - video_indexer
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
<tr><td><b>Id</b></td><td><code>azure_extras.video_indexer.accounts</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `identity` | `object` | Managed service identity (system assigned and/or user assigned identities) |
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | Azure Video Indexer account properties |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `accountName, resourceGroupName, subscriptionId` | Gets the properties of an Azure Video Indexer account. |
| `list` | `SELECT` | `subscriptionId` | List all Azure Video Indexer accounts available under the subscription |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | List all Azure Video Indexer accounts available under the resource group |
| `create_or_update` | `INSERT` | `accountName, resourceGroupName, subscriptionId` | Creates or updates an Azure Video Indexer account. |
| `delete` | `DELETE` | `accountName, resourceGroupName, subscriptionId` | Delete an Azure Video Indexer account. |
| `_list` | `EXEC` | `subscriptionId` | List all Azure Video Indexer accounts available under the subscription |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | List all Azure Video Indexer accounts available under the resource group |
| `check_name_availability` | `EXEC` | `subscriptionId, data__name, data__type` | Checks that the Video Indexer account name is valid and is not already in use. |
| `update` | `EXEC` | `accountName, resourceGroupName, subscriptionId` | Updates the properties of an existing Azure Video Indexer account. |
