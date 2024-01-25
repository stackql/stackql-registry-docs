---
title: document_processor
hide_title: false
hide_table_of_contents: false
keywords:
  - document_processor
  - syntex
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
<tr><td><b>Name</b></td><td><code>document_processor</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.syntex.document_processor</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | Document processor properties |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `processorName, resourceGroupName, subscriptionId` | Returns a document processor for a given name. |
| `list` | `SELECT` | `subscriptionId` | Returns document processors in the subscription. |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | Returns document processors in a resource group. |
| `create` | `INSERT` | `processorName, resourceGroupName, subscriptionId` | Creates a document processor resource for a given name. |
| `delete` | `DELETE` | `processorName, resourceGroupName, subscriptionId` | Deletes document processor resource for a given name. |
| `_list` | `EXEC` | `subscriptionId` | Returns document processors in the subscription. |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | Returns document processors in a resource group. |
| `update` | `EXEC` | `processorName, resourceGroupName, subscriptionId` | Updates a document processor resource for a given name. |
