---
title: solutions
hide_title: false
hide_table_of_contents: false
keywords:
  - solutions
  - operations_management
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
<tr><td><b>Name</b></td><td><code>solutions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.operations_management.solutions" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource ID. |
| <CopyableCode code="name" /> | `string` | Resource name. |
| <CopyableCode code="location" /> | `string` | Resource location |
| <CopyableCode code="plan" /> | `object` | Plan for solution object supported by the OperationsManagement resource provider. |
| <CopyableCode code="properties" /> | `object` | Solution properties supported by the OperationsManagement resource provider. |
| <CopyableCode code="tags" /> | `object` | Resource tags |
| <CopyableCode code="type" /> | `string` | Resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, solutionName, subscriptionId" /> | Retrieves the user solution. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Retrieves the solution list. It will retrieve both first party and third party solutions |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Retrieves the solution list. It will retrieve both first party and third party solutions |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="resourceGroupName, solutionName, subscriptionId" /> | Creates or updates the Solution. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceGroupName, solutionName, subscriptionId" /> | Deletes the solution in the subscription. |
| <CopyableCode code="_list_by_resource_group" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Retrieves the solution list. It will retrieve both first party and third party solutions |
| <CopyableCode code="_list_by_subscription" /> | `EXEC` | <CopyableCode code="subscriptionId" /> | Retrieves the solution list. It will retrieve both first party and third party solutions |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="resourceGroupName, solutionName, subscriptionId" /> | Patch a Solution. Only updating tags supported. |
