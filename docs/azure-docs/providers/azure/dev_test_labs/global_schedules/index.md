---
title: global_schedules
hide_title: false
hide_table_of_contents: false
keywords:
  - global_schedules
  - dev_test_labs
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
<tr><td><b>Name</b></td><td><code>global_schedules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.dev_test_labs.global_schedules" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The identifier of the resource. |
| <CopyableCode code="name" /> | `string` | The name of the resource. |
| <CopyableCode code="location" /> | `string` | The location of the resource. |
| <CopyableCode code="properties" /> | `object` | Properties of a schedule. |
| <CopyableCode code="tags" /> | `object` | The tags of the resource. |
| <CopyableCode code="type" /> | `string` | The type of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="api-version, name, resourceGroupName, subscriptionId" /> | Get schedule. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="api-version, resourceGroupName, subscriptionId" /> | List schedules in a resource group. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="api-version, subscriptionId" /> | List schedules in a subscription. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="api-version, name, resourceGroupName, subscriptionId, data__properties" /> | Create or replace an existing schedule. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="api-version, name, resourceGroupName, subscriptionId" /> | Delete schedule. |
| <CopyableCode code="_list_by_resource_group" /> | `EXEC` | <CopyableCode code="api-version, resourceGroupName, subscriptionId" /> | List schedules in a resource group. |
| <CopyableCode code="_list_by_subscription" /> | `EXEC` | <CopyableCode code="api-version, subscriptionId" /> | List schedules in a subscription. |
| <CopyableCode code="execute" /> | `EXEC` | <CopyableCode code="api-version, name, resourceGroupName, subscriptionId" /> | Execute a schedule. This operation can take a while to complete. |
| <CopyableCode code="retarget" /> | `EXEC` | <CopyableCode code="api-version, name, resourceGroupName, subscriptionId" /> | Updates a schedule's target resource Id. This operation can take a while to complete. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="api-version, name, resourceGroupName, subscriptionId" /> | Allows modifying tags of schedules. All other properties will be ignored. |
