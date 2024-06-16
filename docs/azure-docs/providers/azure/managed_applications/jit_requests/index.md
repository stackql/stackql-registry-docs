---
title: jit_requests
hide_title: false
hide_table_of_contents: false
keywords:
  - jit_requests
  - managed_applications
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
<tr><td><b>Name</b></td><td><code>jit_requests</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.managed_applications.jit_requests" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource ID |
| <CopyableCode code="name" /> | `string` | Resource name |
| <CopyableCode code="location" /> | `string` | Resource location |
| <CopyableCode code="properties" /> | `object` | Information about JIT request properties |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="tags" /> | `object` | Resource tags |
| <CopyableCode code="type" /> | `string` | Resource type |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="jitRequestName, resourceGroupName, subscriptionId" /> | Gets the JIT request. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Lists all JIT requests within the resource group. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Lists all JIT requests within the subscription. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="jitRequestName, resourceGroupName, subscriptionId" /> | Creates or updates the JIT request. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="jitRequestName, resourceGroupName, subscriptionId" /> | Deletes the JIT request. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="jitRequestName, resourceGroupName, subscriptionId" /> | Updates the JIT request. |
