---
title: vpc_connection
hide_title: false
hide_table_of_contents: false
keywords:
  - vpc_connection
  - msk
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


Gets or updates an individual <code>vpc_connection</code> resource, use <code>vpc_connections</code> to retrieve a list of resources or to create or delete a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>vpc_connection</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::MSK::VpcConnection</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.msk.vpc_connection" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="authentication" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="client_subnets" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="target_cluster_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the target cluster</td></tr>
<tr><td><CopyableCode code="security_groups" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="vpc_id" /></td><td><code>string</code></td><td></td></tr>
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
arn,
authentication,
client_subnets,
target_cluster_arn,
security_groups,
tags,
vpc_id
FROM aws.msk.vpc_connection
WHERE region = 'us-east-1' AND data__Identifier = '<Arn>';
```


## Permissions

To operate on the <code>vpc_connection</code> resource, the following permissions are required:

### Read
```json
kafka:DescribeVpcConnection,
kms:CreateGrant,
kms:DescribeKey
```

### Update
```json
kafka:DescribeVpcConnection,
kms:CreateGrant,
kms:DescribeKey,
kafka:TagResource,
kafka:UntagResource
```

