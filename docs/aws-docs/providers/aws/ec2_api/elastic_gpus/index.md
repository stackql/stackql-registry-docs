---
title: elastic_gpus
hide_title: false
hide_table_of_contents: false
keywords:
  - elastic_gpus
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
<tr><td><b>Name</b></td><td><code>elastic_gpus</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2_api.elastic_gpus" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="availabilityZone" /> | `string` | The Availability Zone in the which the Elastic Graphics accelerator resides. |
| <CopyableCode code="elasticGpuHealth" /> | `object` | Describes the status of an Elastic Graphics accelerator. |
| <CopyableCode code="elasticGpuId" /> | `string` | The ID of the Elastic Graphics accelerator. |
| <CopyableCode code="elasticGpuState" /> | `string` | The state of the Elastic Graphics accelerator. |
| <CopyableCode code="elasticGpuType" /> | `string` | The type of Elastic Graphics accelerator. |
| <CopyableCode code="instanceId" /> | `string` | The ID of the instance to which the Elastic Graphics accelerator is attached. |
| <CopyableCode code="tagSet" /> | `array` | The tags assigned to the Elastic Graphics accelerator. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="elastic_gpus_Describe" /> | `SELECT` | <CopyableCode code="region" /> |
