---
title: tables
hide_title: false
hide_table_of_contents: false
keywords:
  - tables
  - cassandra
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

Used to retrieve a list of <code>tables</code> in a region or create a <code>tables</code> resource, use <code>table</code> to operate on an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>tables</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::Cassandra::Table</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.cassandra.tables" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="keyspace_name" /></td><td><code>string</code></td><td>Name for Cassandra keyspace</td></tr>
<tr><td><CopyableCode code="table_name" /></td><td><code>string</code></td><td>Name for Cassandra table</td></tr>
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
keyspace_name,
table_name
FROM aws.cassandra.tables
WHERE region = 'us-east-1'
```

## Permissions

To operate on the <code>tables</code> resource, the following permissions are required:

### Create
```json
cassandra:Create,
cassandra:CreateMultiRegionResource,
cassandra:Select,
cassandra:SelectMultiRegionResource,
cassandra:TagResource,
cassandra:TagMultiRegionResource,
kms:CreateGrant,
kms:DescribeKey,
kms:Encrypt,
kms:Decrypt,
application-autoscaling:DescribeScalableTargets,
application-autoscaling:DescribeScalingPolicies,
application-autoscaling:DeregisterScalableTarget,
application-autoscaling:RegisterScalableTarget,
application-autoscaling:PutScalingPolicy,
cloudwatch:DeleteAlarms,
cloudwatch:DescribeAlarms,
cloudwatch:GetMetricData,
cloudwatch:PutMetricAlarm
```

### List
```json
cassandra:Select,
cassandra:SelectMultiRegionResource,
application-autoscaling:DescribeScalableTargets,
application-autoscaling:DescribeScalingPolicies,
application-autoscaling:DeregisterScalableTarget,
application-autoscaling:RegisterScalableTarget,
application-autoscaling:PutScalingPolicy,
cloudwatch:DeleteAlarms,
cloudwatch:DescribeAlarms,
cloudwatch:GetMetricData,
cloudwatch:PutMetricAlarm
```

