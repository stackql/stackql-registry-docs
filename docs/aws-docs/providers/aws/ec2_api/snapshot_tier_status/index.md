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
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>snapshot_tier_status</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ec2_api.snapshot_tier_status</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `archivalCompleteTime` | `string` | The date and time when the last archive process was completed. |
| `lastTieringOperationStatus` | `string` | The status of the last archive or restore process. |
| `lastTieringOperationStatusDetail` | `string` | A message describing the status of the last archive or restore process. |
| `lastTieringProgress` | `integer` | The progress of the last archive or restore process, as a percentage. |
| `lastTieringStartTime` | `string` | The date and time when the last archive or restore process was started. |
| `ownerId` | `string` | The ID of the Amazon Web Services account that owns the snapshot. |
| `restoreExpiryTime` | `string` | Only for archived snapshots that are temporarily restored. Indicates the date and time when a temporarily restored snapshot will be automatically re-archived. |
| `snapshotId` | `string` | The ID of the snapshot. |
| `status` | `string` | The state of the snapshot. |
| `storageTier` | `string` | The storage tier in which the snapshot is stored. &lt;code&gt;standard&lt;/code&gt; indicates that the snapshot is stored in the standard snapshot storage tier and that it is ready for use. &lt;code&gt;archive&lt;/code&gt; indicates that the snapshot is currently archived and that it must be restored before it can be used. |
| `tagSet` | `array` | The tags that are assigned to the snapshot. |
| `volumeId` | `string` | The ID of the volume from which the snapshot was created. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `snapshot_tier_status_Describe` | `SELECT` | `region` |
