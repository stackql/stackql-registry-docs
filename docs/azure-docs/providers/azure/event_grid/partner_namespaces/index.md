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
| `tags` | `object` | Tags of the resource. |
| `location` | `string` | Location of the resource. |
| `properties` | `object` | Properties of the partner namespace. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `PartnerNamespaces_Get` | `SELECT` | `partnerNamespaceName, resourceGroupName, subscriptionId` | Get properties of a partner namespace. |
| `PartnerNamespaces_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` | List all the partner namespaces under a resource group. |
| `PartnerNamespaces_ListBySubscription` | `SELECT` | `subscriptionId` | List all the partner namespaces under an Azure subscription. |
| `PartnerNamespaces_CreateOrUpdate` | `INSERT` | `partnerNamespaceName, resourceGroupName, subscriptionId` | Asynchronously creates a new partner namespace with the specified parameters. |
| `PartnerNamespaces_Delete` | `DELETE` | `partnerNamespaceName, resourceGroupName, subscriptionId` | Delete existing partner namespace. |
| `PartnerNamespaces_ListSharedAccessKeys` | `EXEC` | `partnerNamespaceName, resourceGroupName, subscriptionId` | List the two keys used to publish to a partner namespace. |
| `PartnerNamespaces_RegenerateKey` | `EXEC` | `partnerNamespaceName, resourceGroupName, subscriptionId, data__keyName` | Regenerate a shared access key for a partner namespace. |
| `PartnerNamespaces_Update` | `EXEC` | `partnerNamespaceName, resourceGroupName, subscriptionId` | Asynchronously updates a partner namespace with the specified parameters. |
