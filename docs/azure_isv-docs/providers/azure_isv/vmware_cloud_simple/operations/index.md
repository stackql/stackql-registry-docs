---
title: operations
hide_title: false
hide_table_of_contents: false
keywords:
  - operations
  - vmware_cloud_simple
  - azure_isv    
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
<tr><td><b>Name</b></td><td><code>operations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.vmware_cloud_simple.operations" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Operation Id |
| <CopyableCode code="name" /> | `string` | Operation ID |
| <CopyableCode code="endTime" /> | `string` | End time of the operation |
| <CopyableCode code="error" /> | `object` | Operation error model |
| <CopyableCode code="startTime" /> | `string` | Start time of the operation |
| <CopyableCode code="status" /> | `string` | Operation status |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="Referer, api-version, operationId, regionId, subscriptionId" /> | Return an async operation |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="api-version" /> | Return list of operations |
