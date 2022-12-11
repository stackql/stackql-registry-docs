---
title: volume_status
hide_title: false
hide_table_of_contents: false
keywords:
  - volume_status
  - ec2
  - aws    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>volume_status</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ec2.volume_status</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `actionsSet` | `array` | The details of the operation. |
| `attachmentStatuses` | `array` | Information about the instances to which the volume is attached. |
| `availabilityZone` | `string` | The Availability Zone of the volume. |
| `eventsSet` | `array` | A list of events associated with the volume. |
| `outpostArn` | `string` | The Amazon Resource Name (ARN) of the Outpost. |
| `volumeId` | `string` | The volume ID. |
| `volumeStatus` | `object` | Describes the status of a volume. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `volume_status_Describe` | `SELECT` |  |
