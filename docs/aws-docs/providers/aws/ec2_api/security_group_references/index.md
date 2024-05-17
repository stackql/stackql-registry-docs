---
title: security_group_references
hide_title: false
hide_table_of_contents: false
keywords:
  - security_group_references
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
<tr><td><b>Name</b></td><td><code>security_group_references</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2_api.security_group_references" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="groupId" /> | `string` | The ID of your security group. |
| <CopyableCode code="referencingVpcId" /> | `string` | The ID of the VPC with the referencing security group. |
| <CopyableCode code="vpcPeeringConnectionId" /> | `string` | The ID of the VPC peering connection. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="security_group_references_Describe" /> | `SELECT` | <CopyableCode code="GroupId, region" /> |
