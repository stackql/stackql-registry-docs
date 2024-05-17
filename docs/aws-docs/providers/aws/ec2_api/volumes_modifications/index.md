---
title: volumes_modifications
hide_title: false
hide_table_of_contents: false
keywords:
  - volumes_modifications
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
<tr><td><b>Name</b></td><td><code>volumes_modifications</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2_api.volumes_modifications" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="endTime" /> | `string` | The modification completion or failure time. |
| <CopyableCode code="modificationState" /> | `string` | The current modification state. The modification state is null for unmodified volumes. |
| <CopyableCode code="originalIops" /> | `integer` | The original IOPS rate of the volume. |
| <CopyableCode code="originalMultiAttachEnabled" /> | `boolean` | The original setting for Amazon EBS Multi-Attach. |
| <CopyableCode code="originalSize" /> | `integer` | The original size of the volume, in GiB. |
| <CopyableCode code="originalThroughput" /> | `integer` | The original throughput of the volume, in MiB/s. |
| <CopyableCode code="originalVolumeType" /> | `string` | The original EBS volume type of the volume. |
| <CopyableCode code="progress" /> | `integer` | The modification progress, from 0 to 100 percent complete. |
| <CopyableCode code="startTime" /> | `string` | The modification start time. |
| <CopyableCode code="statusMessage" /> | `string` | A status message about the modification progress or failure. |
| <CopyableCode code="targetIops" /> | `integer` | The target IOPS rate of the volume. |
| <CopyableCode code="targetMultiAttachEnabled" /> | `boolean` | The target setting for Amazon EBS Multi-Attach. |
| <CopyableCode code="targetSize" /> | `integer` | The target size of the volume, in GiB. |
| <CopyableCode code="targetThroughput" /> | `integer` | The target throughput of the volume, in MiB/s. |
| <CopyableCode code="targetVolumeType" /> | `string` | The target EBS volume type of the volume. |
| <CopyableCode code="volumeId" /> | `string` | The ID of the volume. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="volumes_modifications_Describe" /> | `SELECT` | <CopyableCode code="region" /> |
