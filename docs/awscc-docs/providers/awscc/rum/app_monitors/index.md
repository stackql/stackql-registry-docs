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
Retrieves a list of <code>app_monitors</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>app_monitors</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>app_monitors</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.rum.app_monitors</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td>A name for the app monitor</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

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


## Example
```sql
SELECT
region,
name
FROM awscc.rum.app_monitors
WHERE region = 'us-east-1'
```
