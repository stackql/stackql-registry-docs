---
title: security_group
hide_title: false
hide_table_of_contents: false
keywords:
  - security_group
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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';


Gets or updates an individual <code>security_group</code> resource, use <code>security_groups</code> to retrieve a list of resources or to create or delete a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>security_group</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::EC2::SecurityGroup</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2.security_group" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="group_description" /></td><td><code>string</code></td><td>A description for the security group.</td></tr>
<tr><td><CopyableCode code="group_name" /></td><td><code>string</code></td><td>The name of the security group.</td></tr>
<tr><td><CopyableCode code="vpc_id" /></td><td><code>string</code></td><td>The ID of the VPC for the security group.</td></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td>The group name or group ID depending on whether the SG is created in default or specific VPC</td></tr>
<tr><td><CopyableCode code="security_group_ingress" /></td><td><code>array</code></td><td>The inbound rules associated with the security group. There is a short interruption during which you cannot connect to the security group.</td></tr>
<tr><td><CopyableCode code="security_group_egress" /></td><td><code>array</code></td><td>&#91;VPC only&#93; The outbound rules associated with the security group. There is a short interruption during which you cannot connect to the security group.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>Any tags assigned to the security group.</td></tr>
<tr><td><CopyableCode code="group_id" /></td><td><code>string</code></td><td>The group ID of the specified security group.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods

<table><tbody>
  <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
  </tr>
  <tr>
    <td><CopyableCode code="update_resource" /></td>
    <td><code>UPDATE</code></td>
    <td><CopyableCode code="data__Identifier, data__PatchDocument, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
group_description,
group_name,
vpc_id,
id,
security_group_ingress,
security_group_egress,
tags,
group_id
FROM aws.ec2.security_group
WHERE region = 'us-east-1' AND data__Identifier = '<Id>';
```


## Permissions

To operate on the <code>security_group</code> resource, the following permissions are required:

### Read
```json
ec2:DescribeSecurityGroups
```

### Update
```json
ec2:RevokeSecurityGroupEgress,
ec2:RevokeSecurityGroupIngress,
ec2:DescribeSecurityGroups,
ec2:AuthorizeSecurityGroupEgress,
ec2:AuthorizeSecurityGroupIngress,
ec2:CreateTags,
ec2:DeleteTags
```

