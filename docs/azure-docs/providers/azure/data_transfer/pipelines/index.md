---
title: pipelines
hide_title: false
hide_table_of_contents: false
keywords:
  - pipelines
  - data_transfer
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
<tr><td><b>Id</b></td><td><CopyableCode code="azure.data_transfer.pipelines" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Properties of pipeline |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="pipelineName, resourceGroupName, subscriptionId" /> | Gets pipeline resource. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Gets pipelines in a resource group. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Gets pipelines in a subscription. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="pipelineName, resourceGroupName, subscriptionId, data__location" /> | Creates or updates the pipeline resource. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="pipelineName, resourceGroupName, subscriptionId" /> | Deletes the pipeline resource. |
| <CopyableCode code="approve_connection" /> | `EXEC` | <CopyableCode code="pipelineName, resourceGroupName, subscriptionId, data__id" /> | Approves the specified connection in a pipeline. |
| <CopyableCode code="reject_connection" /> | `EXEC` | <CopyableCode code="pipelineName, resourceGroupName, subscriptionId, data__id" /> | Rejects the specified connection in a pipeline. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="pipelineName, resourceGroupName, subscriptionId" /> | Updates the pipeline resource. |
