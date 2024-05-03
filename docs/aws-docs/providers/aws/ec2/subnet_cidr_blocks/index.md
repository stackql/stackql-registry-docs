---
title: subnet_cidr_blocks
hide_title: false
hide_table_of_contents: false
keywords:
  - subnet_cidr_blocks
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

Used to retrieve a list of <code>subnet_cidr_blocks</code> in a region or create a <code>subnet_cidr_blocks</code> resource, use <code>subnet_cidr_block</code> to operate on an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>subnet_cidr_blocks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::EC2::SubnetCidrBlock resource creates association between subnet and IPv6 CIDR</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2.subnet_cidr_blocks" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td>Information about the IPv6 association.</td></tr>
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
    <td><CopyableCode code="create_resource" /></td>
    <td><code>INSERT</code></td>
    <td><CopyableCode code="data__DesiredState, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="list_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
id
FROM aws.ec2.subnet_cidr_blocks
WHERE region = 'us-east-1'
```

## Permissions

To operate on the <code>subnet_cidr_blocks</code> resource, the following permissions are required:

### Create
```json
ec2:AssociateSubnetCidrBlock,
ec2:DescribeSubnets
```

### List
```json
ec2:DescribeSubnets
```

