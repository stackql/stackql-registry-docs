---
title: delegated_network
hide_title: false
hide_table_of_contents: false
keywords:
  - delegated_network
  - delegated_network
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
<tr><td><b>Name</b></td><td><code>delegated_network</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.delegated_network.delegated_network</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | An identifier that represents the resource. |
| `name` | `string` | The name of the resource. |
| `tags` | `object` | The resource tags. |
| `type` | `string` | The type of resource. |
| `location` | `string` | Location of the resource. |
| `properties` | `object` | Properties of Delegated controller resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `DelegatedNetwork_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` | Get all the delegatedController resources in a resource group. |
| `DelegatedNetwork_ListBySubscription` | `SELECT` | `subscriptionId` | Get all the delegatedController resources in a subscription. |
