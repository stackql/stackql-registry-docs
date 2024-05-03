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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>enterprise_knowledge_graph</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.enterprise_knowledge_graph.enterprise_knowledge_graph" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Specifies the resource ID. |
| <CopyableCode code="name" /> | `string` | Specifies the name of the resource. |
| <CopyableCode code="location" /> | `string` | Specifies the location of the resource. |
| <CopyableCode code="properties" /> | `object` | The parameters to provide for the EnterpriseKnowledgeGraph. |
| <CopyableCode code="sku" /> | `object` | The SKU of the EnterpriseKnowledgeGraph service account. |
| <CopyableCode code="tags" /> | `object` | Contains resource tags defined as key/value pairs. |
| <CopyableCode code="type" /> | `string` | Specifies the type of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, resourceName, subscriptionId" /> | Returns a EnterpriseKnowledgeGraph service specified by the parameters. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Returns all the resources of a particular type belonging to a subscription. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Returns all the resources of a particular type belonging to a resource group |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="resourceGroupName, resourceName, subscriptionId" /> | Creates a EnterpriseKnowledgeGraph Service. EnterpriseKnowledgeGraph Service is a resource group wide resource type. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceGroupName, resourceName, subscriptionId" /> | Deletes a EnterpriseKnowledgeGraph Service from the resource group.  |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="subscriptionId" /> | Returns all the resources of a particular type belonging to a subscription. |
| <CopyableCode code="_list_by_resource_group" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Returns all the resources of a particular type belonging to a resource group |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="resourceGroupName, resourceName, subscriptionId" /> | Updates a EnterpriseKnowledgeGraph Service |
