---
title: partner_namespaces
hide_title: false
hide_table_of_contents: false
keywords:
  - partner_namespaces
  - event_grid
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
<tr><td><b>Name</b></td><td><code>partner_namespaces</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.event_grid.partner_namespaces</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | Properties of the partner namespace. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `partnerNamespaceName, resourceGroupName, subscriptionId` | Get properties of a partner namespace. |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | List all the partner namespaces under a resource group. |
| `list_by_subscription` | `SELECT` | `subscriptionId` | List all the partner namespaces under an Azure subscription. |
| `create_or_update` | `INSERT` | `partnerNamespaceName, resourceGroupName, subscriptionId` | Asynchronously creates a new partner namespace with the specified parameters. |
| `delete` | `DELETE` | `partnerNamespaceName, resourceGroupName, subscriptionId` | Delete existing partner namespace. |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | List all the partner namespaces under a resource group. |
| `_list_by_subscription` | `EXEC` | `subscriptionId` | List all the partner namespaces under an Azure subscription. |
| `regenerate_key` | `EXEC` | `partnerNamespaceName, resourceGroupName, subscriptionId, data__keyName` | Regenerate a shared access key for a partner namespace. |
| `update` | `EXEC` | `partnerNamespaceName, resourceGroupName, subscriptionId` | Asynchronously updates a partner namespace with the specified parameters. |
