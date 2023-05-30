---
title: volumes_modifications
hide_title: false
hide_table_of_contents: false
keywords:
  - volumes_modifications
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
<tr><td><b>Name</b></td><td><code>volumes_modifications</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ec2.volumes_modifications</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `volumeId` | `string` | The ID of the volume. |
| `targetMultiAttachEnabled` | `boolean` | The target setting for Amazon EBS Multi-Attach. |
| `originalMultiAttachEnabled` | `boolean` | The original setting for Amazon EBS Multi-Attach. |
| `endTime` | `string` | The modification completion or failure time. |
| `originalIops` | `integer` | The original IOPS rate of the volume. |
| `targetVolumeType` | `string` | The target EBS volume type of the volume. |
| `targetIops` | `integer` | The target IOPS rate of the volume. |
| `originalVolumeType` | `string` | The original EBS volume type of the volume. |
| `modificationState` | `string` | The current modification state. The modification state is null for unmodified volumes. |
| `startTime` | `string` | The modification start time. |
| `originalThroughput` | `integer` | The original throughput of the volume, in MiB/s. |
| `progress` | `integer` | The modification progress, from 0 to 100 percent complete. |
| `statusMessage` | `string` | A status message about the modification progress or failure. |
| `targetSize` | `integer` | The target size of the volume, in GiB. |
| `targetThroughput` | `integer` | The target throughput of the volume, in MiB/s. |
| `originalSize` | `integer` | The original size of the volume, in GiB. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `volumes_modifications_Describe` | `SELECT` | `region` |
