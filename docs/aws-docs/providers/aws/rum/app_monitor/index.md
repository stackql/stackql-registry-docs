---
title: app_monitor
hide_title: false
hide_table_of_contents: false
keywords:
  - app_monitor
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

Gets or operates on an individual <code>app_monitor</code> resource, use <code>app_monitors</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>app_monitor</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::RUM::AppMonitor</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.rum.app_monitor" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td>The unique ID of the new app monitor.</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>A name for the app monitor</td></tr>
<tr><td><CopyableCode code="domain" /></td><td><code>string</code></td><td>The top-level internet domain name for which your application has administrative authority.</td></tr>
<tr><td><CopyableCode code="cw_log_enabled" /></td><td><code>boolean</code></td><td>Data collected by RUM is kept by RUM for 30 days and then deleted. This parameter specifies whether RUM sends a copy of this telemetry data to CWLlong in your account. This enables you to keep the telemetry data for more than 30 days, but it does incur CWLlong charges. If you omit this parameter, the default is false</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="app_monitor_configuration" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="custom_events" /></td><td><code>object</code></td><td></td></tr>
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
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
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
id,
name,
domain,
cw_log_enabled,
tags,
app_monitor_configuration,
custom_events
FROM aws.rum.app_monitor
WHERE data__Identifier = '<Name>';
```

## Permissions

To operate on the <code>app_monitor</code> resource, the following permissions are required:

### Read
```json
rum:GetAppMonitor,
dynamodb:GetItem,
s3:GetObject,
s3:DoesObjectExist,
s3:GetObjectAcl,
rum:ListTagsForResource,
rum:ListRumMetricsDestinations,
rum:BatchGetRumMetricDefinitions
```

### Update
```json
rum:UpdateAppMonitor,
dynamodb:GetItem,
dynamodb:PutItem,
dynamodb:UpdateItem,
dynamodb:Query,
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
rum:UntagResource,
rum:ListTagsForResource,
iam:GetRole,
iam:CreateServiceLinkedRole,
rum:PutRumMetricsDestination,
rum:DeleteRumMetricsDestination,
rum:ListRumMetricsDestinations,
rum:BatchCreateRumMetricDefinitions,
rum:BatchDeleteRumMetricDefinitions,
rum:BatchGetRumMetricDefinitions,
rum:UpdateRumMetricDefinition
```

### Delete
```json
rum:DeleteAppMonitor,
dynamodb:DeleteItem,
dynamodb:Query,
logs:DeleteLogDelivery,
s3:DeleteObject,
s3:DoesObjectExist,
rum:UntagResource,
rum:DeleteRumMetricsDestination,
rum:BatchDeleteRumMetricDefinitions
```

