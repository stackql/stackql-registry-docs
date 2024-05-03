---
title: ipams
hide_title: false
hide_table_of_contents: false
keywords:
  - ipams
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

Used to retrieve a list of <code>ipams</code> in a region or create a <code>ipams</code> resource, use <code>ipam</code> to operate on an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>ipams</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Schema of AWS::EC2::IPAM Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2.ipams" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="ipam_id" /></td><td><code>string</code></td><td>Id of the IPAM.</td></tr>
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
ipam_id
FROM aws.ec2.ipams
WHERE region = 'us-east-1'
```

## Permissions

To operate on the <code>ipams</code> resource, the following permissions are required:

### Create
```json
ec2:CreateIpam,
iam:CreateServiceLinkedRole,
ec2:CreateTags,
ec2:DescribeIpams
```

### List
```json
ec2:DescribeIpams
```

