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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes or gets a <code>notification_channel</code> resource or lists <code>notification_channels</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>notification_channels</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Designates the IAM role and Amazon Simple Notification Service (SNS) topic that AWS Firewall Manager uses to record SNS logs.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.fms.notification_channels" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="sns_role_name" /></td><td><code>string</code></td><td>A resource ARN.</td></tr>
<tr><td><CopyableCode code="sns_topic_arn" /></td><td><code>string</code></td><td>A resource ARN.</td></tr>
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
    <td><CopyableCode code="SnsRoleName, SnsTopicArn, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="update_resource" /></td>
    <td><code>UPDATE</code></td>
    <td><CopyableCode code="data__Identifier, data__PatchDocument, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="list_resources" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples
Gets all <code>notification_channels</code> in a region.
```sql
SELECT
region,
sns_role_name,
sns_topic_arn
FROM aws.fms.notification_channels
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>notification_channel</code>.
```sql
SELECT
region,
sns_role_name,
sns_topic_arn
FROM aws.fms.notification_channels
WHERE region = 'us-east-1' AND data__Identifier = '<SnsTopicArn>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>notification_channel</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

<Tabs
    defaultValue="required"
    values={[
      { label: 'Required Properties', value: 'required', },
      { label: 'All Properties', value: 'all', },
      { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="required">

```sql
/*+ create */
INSERT INTO aws.fms.notification_channels (
 SnsRoleName,
 SnsTopicArn,
 region
)
SELECT 
'{{ SnsRoleName }}',
 '{{ SnsTopicArn }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.fms.notification_channels (
 SnsRoleName,
 SnsTopicArn,
 region
)
SELECT 
 '{{ SnsRoleName }}',
 '{{ SnsTopicArn }}',
 '{{ region }}';
```
</TabItem>
<TabItem value="manifest">

```yaml
version: 1
name: stack name
description: stack description
providers:
  - aws
globals:
  - name: region
    value: '{{ vars.AWS_REGION }}'
resources:
  - name: notification_channel
    props:
      - name: SnsRoleName
        value: '{{ SnsRoleName }}'
      - name: SnsTopicArn
        value: null

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.fms.notification_channels
WHERE data__Identifier = '<SnsTopicArn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>notification_channels</code> resource, the following permissions are required:

### Create
```json
fms:PutNotificationChannel,
iam:PassRole
```

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

### List
```json
fms:GetNotificationChannel
```

