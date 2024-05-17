---
title: snapshot_tier_status
hide_title: false
hide_table_of_contents: false
keywords:
  - snapshot_tier_status
  - ec2_api
  - aws    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>snapshot_tier_status</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2_api.snapshot_tier_status" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="archivalCompleteTime" /> | `string` | The date and time when the last archive process was completed. |
| <CopyableCode code="lastTieringOperationStatus" /> | `string` | The status of the last archive or restore process. |
| <CopyableCode code="lastTieringOperationStatusDetail" /> | `string` | A message describing the status of the last archive or restore process. |
| <CopyableCode code="lastTieringProgress" /> | `integer` | The progress of the last archive or restore process, as a percentage. |
| <CopyableCode code="lastTieringStartTime" /> | `string` | The date and time when the last archive or restore process was started. |
| <CopyableCode code="ownerId" /> | `string` | The ID of the Amazon Web Services account that owns the snapshot. |
| <CopyableCode code="restoreExpiryTime" /> | `string` | Only for archived snapshots that are temporarily restored. Indicates the date and time when a temporarily restored snapshot will be automatically re-archived. |
| <CopyableCode code="snapshotId" /> | `string` | The ID of the snapshot. |
| <CopyableCode code="status" /> | `string` | The state of the snapshot. |
| <CopyableCode code="storageTier" /> | `string` | The storage tier in which the snapshot is stored. &lt;code&gt;standard&lt;/code&gt; indicates that the snapshot is stored in the standard snapshot storage tier and that it is ready for use. &lt;code&gt;archive&lt;/code&gt; indicates that the snapshot is currently archived and that it must be restored before it can be used. |
| <CopyableCode code="tagSet" /> | `array` | The tags that are assigned to the snapshot. |
| <CopyableCode code="volumeId" /> | `string` | The ID of the volume from which the snapshot was created. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="snapshot_tier_status_Describe" /> | `SELECT` | <CopyableCode code="region" /> |
