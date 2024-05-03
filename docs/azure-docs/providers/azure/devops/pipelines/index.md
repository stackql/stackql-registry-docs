---
title: pipelines
hide_title: false
hide_table_of_contents: false
keywords:
  - pipelines
  - devops
  - azure    
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
<tr><td><b>Name</b></td><td><code>pipelines</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.devops.pipelines" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id |
| <CopyableCode code="name" /> | `string` | Resource Name |
| <CopyableCode code="location" /> | `string` | Resource Location |
| <CopyableCode code="properties" /> | `object` | Custom properties of a Pipeline. |
| <CopyableCode code="tags" /> | `object` | Resource Tags |
| <CopyableCode code="type" /> | `string` | Resource Type |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="pipelineName, resourceGroupName, subscriptionId" /> | Gets an existing Azure Pipeline. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Lists all Azure Pipelines under the specified resource group. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Lists all Azure Pipelines under the specified subscription. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="pipelineName, resourceGroupName, subscriptionId, data__properties" /> | Creates or updates an Azure Pipeline. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="pipelineName, resourceGroupName, subscriptionId" /> | Deletes an Azure Pipeline. |
| <CopyableCode code="_list_by_resource_group" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Lists all Azure Pipelines under the specified resource group. |
| <CopyableCode code="_list_by_subscription" /> | `EXEC` | <CopyableCode code="subscriptionId" /> | Lists all Azure Pipelines under the specified subscription. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="pipelineName, resourceGroupName, subscriptionId" /> | Updates the properties of an Azure Pipeline. Currently, only tags can be updated. |
