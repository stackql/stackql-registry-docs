---
title: app_monitors
hide_title: false
hide_table_of_contents: false
keywords:
  - app_monitors
  - rum
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

Used to retrieve a list of <code>app_monitors</code> in a region or create a <code>app_monitors</code> resource, use <code>app_monitor</code> to operate on an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>app_monitors</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::RUM::AppMonitor</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.rum.app_monitors" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>A name for the app monitor</td></tr>
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
name
FROM aws.rum.app_monitors
WHERE region = 'us-east-1'
```

## Permissions

To operate on the <code>app_monitors</code> resource, the following permissions are required:

### Create
```json
rum:CreateAppMonitor,
dynamodb:GetItem,
dynamodb:PutItem,
s3:GetObject,
s3:PutObject,
s3:GetObjectAcl,
s3:DoesObjectExist,
logs:CreateLogDelivery,
logs:CreateLogGroup,
logs:GetLogDelivery,
logs:UpdateLogDelivery,
logs:PutResourcePolicy,
logs:DescribeResourcePolicies,
logs:DescribeLogGroups,
logs:PutRetentionPolicy,
rum:TagResource,
cognito-identity:DescribeIdentityPool,
iam:GetRole,
iam:CreateServiceLinkedRole,
rum:PutRumMetricsDestination,
rum:BatchCreateRumMetricDefinitions
```

### List
```json
rum:ListAppMonitors,
dynamodb:DescribeTable,
rum:GetAppMonitor,
dynamodb:GetItem,
dynamodb:BatchGetItem,
dynamodb:Query,
s3:GetObject,
s3:DoesObjectExist,
s3:GetObjectAcl,
logs:DescribeLogGroups,
rum:ListTagsForResource
```

