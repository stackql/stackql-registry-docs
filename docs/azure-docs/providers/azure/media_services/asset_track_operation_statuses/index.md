---
title: asset_track_operation_statuses
hide_title: false
hide_table_of_contents: false
keywords:
  - asset_track_operation_statuses
  - media_services
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
<tr><td><b>Name</b></td><td><code>asset_track_operation_statuses</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.media_services.asset_track_operation_statuses" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Operation resource ID. |
| <CopyableCode code="name" /> | `string` | Operation identifier. |
| <CopyableCode code="endTime" /> | `string` | Operation end time. |
| <CopyableCode code="error" /> | `object` | The error detail. |
| <CopyableCode code="startTime" /> | `string` | Operation start time. |
| <CopyableCode code="status" /> | `string` | Operation status. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="accountName, api-version, assetName, operationId, resourceGroupName, subscriptionId, trackName" /> |
