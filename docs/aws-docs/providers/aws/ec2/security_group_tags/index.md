---
title: security_group_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - security_group_tags
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

Expands all tag keys and values for <code>security_groups</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>security_group_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::EC2::SecurityGroup</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2.security_group_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="group_description" /></td><td><code>string</code></td><td>A description for the security group.</td></tr>
<tr><td><CopyableCode code="group_name" /></td><td><code>string</code></td><td>The name of the security group.</td></tr>
<tr><td><CopyableCode code="vpc_id" /></td><td><code>string</code></td><td>The ID of the VPC for the security group.</td></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td>The group name or group ID depending on whether the SG is created in default or specific VPC</td></tr>
<tr><td><CopyableCode code="security_group_ingress" /></td><td><code>array</code></td><td>The inbound rules associated with the security group. There is a short interruption during which you cannot connect to the security group.</td></tr>
<tr><td><CopyableCode code="security_group_egress" /></td><td><code>array</code></td><td>&#91;VPC only&#93; The outbound rules associated with the security group. There is a short interruption during which you cannot connect to the security group.</td></tr>
<tr><td><CopyableCode code="group_id" /></td><td><code>string</code></td><td>The group ID of the specified security group.</td></tr>
<tr><td><CopyableCode code="tag_key" /></td><td><code>string</code></td><td>Tag key.</td></tr>
<tr><td><CopyableCode code="tag_value" /></td><td><code>string</code></td><td>Tag value.</td></tr>
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
    <td><CopyableCode code="list_resources" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples
Expands tags for all <code>security_groups</code> in a region.
```sql
SELECT
region,
group_description,
group_name,
vpc_id,
id,
security_group_ingress,
security_group_egress,
group_id,
tag_key,
tag_value
FROM aws.ec2.security_group_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>security_group_tags</code> resource, see <a href="/providers/aws/ec2/security_groups/#permissions"><code>security_groups</code></a>


