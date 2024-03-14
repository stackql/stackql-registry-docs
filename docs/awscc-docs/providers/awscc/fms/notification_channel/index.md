---
title: notification_channel
hide_title: false
hide_table_of_contents: false
keywords:
  - notification_channel
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
Gets an individual <code>notification_channel</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>notification_channel</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>notification_channel</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.fms.notification_channel</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>sns_role_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>sns_topic_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
sns_role_name,
sns_topic_arn
FROM awscc.fms.notification_channel
WHERE data__Identifier = '<SnsTopicArn>';
```

## Permissions

To operate on the <code>notification_channel</code> resource, the following permissions are required:

### Update
```json
fms:PutNotificationChannel,
iam:PassRole
```

### Read
```json
fms:GetNotificationChannel
```

### Delete
```json
fms:DeleteNotificationChannel
```

