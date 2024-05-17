---
title: volume_status
hide_title: false
hide_table_of_contents: false
keywords:
  - volume_status
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
<tr><td><b>Name</b></td><td><code>volume_status</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2_api.volume_status" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="actionsSet" /> | `array` | The details of the operation. |
| <CopyableCode code="attachmentStatuses" /> | `array` | Information about the instances to which the volume is attached. |
| <CopyableCode code="availabilityZone" /> | `string` | The Availability Zone of the volume. |
| <CopyableCode code="eventsSet" /> | `array` | A list of events associated with the volume. |
| <CopyableCode code="outpostArn" /> | `string` | The Amazon Resource Name (ARN) of the Outpost. |
| <CopyableCode code="volumeId" /> | `string` | The volume ID. |
| <CopyableCode code="volumeStatus" /> | `object` | Describes the status of a volume. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="volume_status_Describe" /> | `SELECT` | <CopyableCode code="region" /> |
