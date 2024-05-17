---
title: classic_link_instances
hide_title: false
hide_table_of_contents: false
keywords:
  - classic_link_instances
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
<tr><td><b>Name</b></td><td><code>classic_link_instances</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2_api.classic_link_instances" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="groupSet" /> | `array` | A list of security groups. |
| <CopyableCode code="instanceId" /> | `string` | The ID of the instance. |
| <CopyableCode code="tagSet" /> | `array` | Any tags assigned to the instance. |
| <CopyableCode code="vpcId" /> | `string` | The ID of the VPC. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="classic_link_instances_Describe" /> | `SELECT` | <CopyableCode code="region" /> |
