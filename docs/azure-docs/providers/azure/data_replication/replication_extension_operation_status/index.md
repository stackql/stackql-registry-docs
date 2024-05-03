---
title: replication_extension_operation_status
hide_title: false
hide_table_of_contents: false
keywords:
  - replication_extension_operation_status
  - data_replication
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
<tr><td><b>Name</b></td><td><code>replication_extension_operation_status</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.data_replication.replication_extension_operation_status" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Gets or sets the Id. |
| <CopyableCode code="name" /> | `string` | Gets or sets the operation name. |
| <CopyableCode code="endTime" /> | `string` | Gets or sets the end time. |
| <CopyableCode code="startTime" /> | `string` | Gets or sets the start time. |
| <CopyableCode code="status" /> | `string` | Gets or sets the status of the operation. ARM expects the terminal status to be one of<br />Succeeded/ Failed/ Canceled. All other values imply that the operation is still running. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="operationId, replicationExtensionName, resourceGroupName, subscriptionId, vaultName" /> |
