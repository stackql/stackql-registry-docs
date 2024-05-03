---
title: serverless_clusters
hide_title: false
hide_table_of_contents: false
keywords:
  - serverless_clusters
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

Used to retrieve a list of <code>serverless_clusters</code> in a region or create a <code>serverless_clusters</code> resource, use <code>serverless_cluster</code> to operate on an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>serverless_clusters</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::MSK::ServerlessCluster</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.msk.serverless_clusters" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td></td></tr>
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
arn
FROM aws.msk.serverless_clusters
WHERE region = 'us-east-1'
```

## Permissions

To operate on the <code>serverless_clusters</code> resource, the following permissions are required:

### Create
```json
kafka:CreateClusterV2,
kafka:TagResource,
kafka:DescribeClusterV2,
ec2:CreateVpcEndpoint,
ec2:CreateTags,
ec2:DescribeVpcAttribute,
ec2:DescribeSubnets,
ec2:DescribeVpcEndpoints,
ec2:DescribeVpcs,
ec2:DescribeSecurityGroups
```

### List
```json
kafka:ListClustersV2
```

