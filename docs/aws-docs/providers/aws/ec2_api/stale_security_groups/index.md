---
title: stale_security_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - stale_security_groups
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
<tr><td><b>Name</b></td><td><code>stale_security_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2_api.stale_security_groups" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="description" /> | `string` | The description of the security group. |
| <CopyableCode code="groupId" /> | `string` | The ID of the security group. |
| <CopyableCode code="groupName" /> | `string` | The name of the security group. |
| <CopyableCode code="staleIpPermissions" /> | `array` | Information about the stale inbound rules in the security group. |
| <CopyableCode code="staleIpPermissionsEgress" /> | `array` | Information about the stale outbound rules in the security group. |
| <CopyableCode code="vpcId" /> | `string` | The ID of the VPC for the security group. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="stale_security_groups_Describe" /> | `SELECT` | <CopyableCode code="VpcId, region" /> |
