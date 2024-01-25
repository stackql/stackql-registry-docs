---
title: enterprise_knowledge_graph
hide_title: false
hide_table_of_contents: false
keywords:
  - enterprise_knowledge_graph
  - enterprise_knowledge_graph
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
<tr><td><b>Name</b></td><td><code>enterprise_knowledge_graph</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.enterprise_knowledge_graph.enterprise_knowledge_graph</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Specifies the resource ID. |
| `name` | `string` | Specifies the name of the resource. |
| `location` | `string` | Specifies the location of the resource. |
| `properties` | `object` | The parameters to provide for the EnterpriseKnowledgeGraph. |
| `sku` | `object` | The SKU of the EnterpriseKnowledgeGraph service account. |
| `tags` | `object` | Contains resource tags defined as key/value pairs. |
| `type` | `string` | Specifies the type of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `resourceGroupName, resourceName, subscriptionId` | Returns a EnterpriseKnowledgeGraph service specified by the parameters. |
| `list` | `SELECT` | `subscriptionId` | Returns all the resources of a particular type belonging to a subscription. |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | Returns all the resources of a particular type belonging to a resource group |
| `create` | `INSERT` | `resourceGroupName, resourceName, subscriptionId` | Creates a EnterpriseKnowledgeGraph Service. EnterpriseKnowledgeGraph Service is a resource group wide resource type. |
| `delete` | `DELETE` | `resourceGroupName, resourceName, subscriptionId` | Deletes a EnterpriseKnowledgeGraph Service from the resource group.  |
| `_list` | `EXEC` | `subscriptionId` | Returns all the resources of a particular type belonging to a subscription. |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | Returns all the resources of a particular type belonging to a resource group |
| `update` | `EXEC` | `resourceGroupName, resourceName, subscriptionId` | Updates a EnterpriseKnowledgeGraph Service |
