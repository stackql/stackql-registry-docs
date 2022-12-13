---
title: enterprise_knowledge_graph
hide_title: false
hide_table_of_contents: false
keywords:
  - enterprise_knowledge_graph
  - enterprise_knowledge_graph
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
<tr><td><b>Name</b></td><td><code>enterprise_knowledge_graph</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.enterprise_knowledge_graph.enterprise_knowledge_graph</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Specifies the resource ID. |
| `name` | `string` | Specifies the name of the resource. |
| `tags` | `object` | Contains resource tags defined as key/value pairs. |
| `type` | `string` | Specifies the type of the resource. |
| `location` | `string` | Specifies the location of the resource. |
| `properties` | `object` | The parameters to provide for the EnterpriseKnowledgeGraph. |
| `sku` | `object` | The SKU of the EnterpriseKnowledgeGraph service account. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `EnterpriseKnowledgeGraph_Get` | `SELECT` | `resourceGroupName, resourceName, subscriptionId` | Returns a EnterpriseKnowledgeGraph service specified by the parameters. |
| `EnterpriseKnowledgeGraph_List` | `SELECT` | `subscriptionId` | Returns all the resources of a particular type belonging to a subscription. |
| `EnterpriseKnowledgeGraph_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` | Returns all the resources of a particular type belonging to a resource group |
| `EnterpriseKnowledgeGraph_Create` | `INSERT` | `resourceGroupName, resourceName, subscriptionId` | Creates a EnterpriseKnowledgeGraph Service. EnterpriseKnowledgeGraph Service is a resource group wide resource type. |
| `EnterpriseKnowledgeGraph_Delete` | `DELETE` | `resourceGroupName, resourceName, subscriptionId` | Deletes a EnterpriseKnowledgeGraph Service from the resource group.  |
| `EnterpriseKnowledgeGraph_Update` | `EXEC` | `resourceGroupName, resourceName, subscriptionId` | Updates a EnterpriseKnowledgeGraph Service |
