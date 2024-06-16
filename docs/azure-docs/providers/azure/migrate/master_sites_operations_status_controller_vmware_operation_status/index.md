---
title: master_sites_operations_status_controller_vmware_operation_status
hide_title: false
hide_table_of_contents: false
keywords:
  - master_sites_operations_status_controller_vmware_operation_status
  - migrate
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
<tr><td><b>Name</b></td><td><code>master_sites_operations_status_controller_vmware_operation_status</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.migrate.master_sites_operations_status_controller_vmware_operation_status" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Gets the Id. |
| <CopyableCode code="name" /> | `string` | Gets the operation name. |
| <CopyableCode code="endTime" /> | `string` | Gets the start time. |
| <CopyableCode code="error" /> | `object` | Class for operation status errors. |
| <CopyableCode code="properties" /> | `object` | Class for operation result properties. |
| <CopyableCode code="startTime" /> | `string` | Gets the start time. |
| <CopyableCode code="status" /> | `string` | Gets the status of the operation. ARM expects the terminal status to be one<br />of<br />            Succeeded/ Failed/ Canceled. All other values imply that the<br />operation is still running. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="operationStatusName, resourceGroupName, siteName, subscriptionId" /> |
