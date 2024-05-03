---
title: start_stop_managed_instance_schedules
hide_title: false
hide_table_of_contents: false
keywords:
  - start_stop_managed_instance_schedules
  - sql
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
<tr><td><b>Name</b></td><td><code>start_stop_managed_instance_schedules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.sql.start_stop_managed_instance_schedules" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Properties of managed instance's Start/Stop schedule. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="managedInstanceName, resourceGroupName, startStopScheduleName, subscriptionId" /> | Gets the managed instance's Start/Stop schedule. |
| <CopyableCode code="list_by_instance" /> | `SELECT` | <CopyableCode code="managedInstanceName, resourceGroupName, subscriptionId" /> | Lists the managed instance's Start/Stop schedules. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="managedInstanceName, resourceGroupName, startStopScheduleName, subscriptionId" /> | Creates or updates the managed instance's Start/Stop schedule. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="managedInstanceName, resourceGroupName, startStopScheduleName, subscriptionId" /> | Deletes the managed instance's Start/Stop schedule. |
| <CopyableCode code="_list_by_instance" /> | `EXEC` | <CopyableCode code="managedInstanceName, resourceGroupName, subscriptionId" /> | Lists the managed instance's Start/Stop schedules. |
