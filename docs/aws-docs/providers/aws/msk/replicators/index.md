---
title: replicators
hide_title: false
hide_table_of_contents: false
keywords:
  - replicators
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

Used to retrieve a list of <code>replicators</code> in a region or create a <code>replicators</code> resource, use <code>replicator</code> to operate on an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>replicators</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::MSK::Replicator</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.msk.replicators" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="replicator_arn" /></td><td><code>string</code></td><td>Amazon Resource Name for the created replicator.</td></tr>
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
replicator_arn
FROM aws.msk.replicators
WHERE region = 'us-east-1'
```

## Permissions

To operate on the <code>replicators</code> resource, the following permissions are required:

### Create
```json
ec2:CreateNetworkInterface,
ec2:DescribeSecurityGroups,
ec2:DescribeSubnets,
ec2:DescribeVpcs,
iam:CreateServiceLinkedRole,
iam:PassRole,
kafka:CreateReplicator,
kafka:CreateReplicatorReference,
kafka:DescribeClusterV2,
kafka:DescribeReplicator,
kafka:GetBootstrapBrokers,
kafka:ListTagsForResource,
kafka:TagResource
```

### List
```json
kafka:ListReplicators
```

