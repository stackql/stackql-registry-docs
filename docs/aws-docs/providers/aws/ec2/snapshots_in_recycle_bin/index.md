---
title: snapshots_in_recycle_bin
hide_title: false
hide_table_of_contents: false
keywords:
  - snapshots_in_recycle_bin
  - ec2
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
<tr><td><b>Name</b></td><td><code>snapshots_in_recycle_bin</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ec2.snapshots_in_recycle_bin</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `description` | `string` | The description for the snapshot. |
| `recycleBinEnterTime` | `string` | The date and time when the snaphsot entered the Recycle Bin. |
| `recycleBinExitTime` | `string` | The date and time when the snapshot is to be permanently deleted from the Recycle Bin. |
| `snapshotId` | `string` | The ID of the snapshot. |
| `volumeId` | `string` | The ID of the volume from which the snapshot was created. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `snapshots_in_recycle_bin_List` | `SELECT` | `region` |
