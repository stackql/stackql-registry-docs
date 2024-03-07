---
title: notification_channels
hide_title: false
hide_table_of_contents: false
keywords:
  - notification_channels
  - fms
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>notification_channels</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>notification_channels</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>notification_channels</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.fms.notification_channels</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>sns_topic_arn</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
sns_topic_arn
FROM awscc.fms.notification_channels
WHERE region = 'us-east-1'
```

## Permissions

To operate on the <code>notification_channels</code> resource, the following permissions are required:

### Create
```json
fms:PutNotificationChannel,
iam:PassRole
```

### List
```json
fms:GetNotificationChannel
```

