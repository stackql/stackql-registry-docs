---
title: service_fabric_schedules
hide_title: false
hide_table_of_contents: false
keywords:
  - service_fabric_schedules
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
<tr><td><b>Name</b></td><td><code>service_fabric_schedules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.dev_test_labs.service_fabric_schedules" /></td></tr>
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
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="api-version, labName, name, resourceGroupName, serviceFabricName, subscriptionId, userName" /> | Get schedule. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="api-version, labName, resourceGroupName, serviceFabricName, subscriptionId, userName" /> | List schedules in a given service fabric. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="api-version, labName, name, resourceGroupName, serviceFabricName, subscriptionId, userName, data__properties" /> | Create or replace an existing schedule. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="api-version, labName, name, resourceGroupName, serviceFabricName, subscriptionId, userName" /> | Delete schedule. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="api-version, labName, resourceGroupName, serviceFabricName, subscriptionId, userName" /> | List schedules in a given service fabric. |
| <CopyableCode code="execute" /> | `EXEC` | <CopyableCode code="api-version, labName, name, resourceGroupName, serviceFabricName, subscriptionId, userName" /> | Execute a schedule. This operation can take a while to complete. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="api-version, labName, name, resourceGroupName, serviceFabricName, subscriptionId, userName" /> | Allows modifying tags of schedules. All other properties will be ignored. |
