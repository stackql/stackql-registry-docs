---
title: snapshots_in_recycle_bin
hide_title: false
hide_table_of_contents: false
keywords:
  - snapshots_in_recycle_bin
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
<tr><td><b>Name</b></td><td><code>snapshots_in_recycle_bin</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2_api.snapshots_in_recycle_bin" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="description" /> | `string` | The description for the snapshot. |
| <CopyableCode code="recycleBinEnterTime" /> | `string` | The date and time when the snaphsot entered the Recycle Bin. |
| <CopyableCode code="recycleBinExitTime" /> | `string` | The date and time when the snapshot is to be permanently deleted from the Recycle Bin. |
| <CopyableCode code="snapshotId" /> | `string` | The ID of the snapshot. |
| <CopyableCode code="volumeId" /> | `string` | The ID of the volume from which the snapshot was created. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="snapshots_in_recycle_bin_List" /> | `SELECT` | <CopyableCode code="region" /> |
