---
title: subscriber_notifications
hide_title: false
hide_table_of_contents: false
keywords:
  - subscriber_notifications
  - securitylake
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

Creates, updates, deletes or gets a <code>subscriber_notification</code> resource or lists <code>subscriber_notifications</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>subscriber_notifications</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::SecurityLake::SubscriberNotification</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.securitylake.subscriber_notifications" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="notification_configuration" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="subscriber_arn" /></td><td><code>string</code></td><td>The ARN for the subscriber</td></tr>
<tr><td><CopyableCode code="subscriber_endpoint" /></td><td><code>string</code></td><td>The endpoint the subscriber should listen to for notifications</td></tr>
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
    <td><CopyableCode code="SubscriberArn, NotificationConfiguration, region" /></td>
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
Gets all <code>subscriber_notifications</code> in a region.
```sql
SELECT
region,
notification_configuration,
subscriber_arn,
subscriber_endpoint
FROM aws.securitylake.subscriber_notifications
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>subscriber_notification</code>.
```sql
SELECT
region,
notification_configuration,
subscriber_arn,
subscriber_endpoint
FROM aws.securitylake.subscriber_notifications
WHERE region = 'us-east-1' AND data__Identifier = '<SubscriberArn>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>subscriber_notification</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.securitylake.subscriber_notifications (
 NotificationConfiguration,
 SubscriberArn,
 region
)
SELECT 
'{{ NotificationConfiguration }}',
 '{{ SubscriberArn }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.securitylake.subscriber_notifications (
 NotificationConfiguration,
 SubscriberArn,
 region
)
SELECT 
 '{{ NotificationConfiguration }}',
 '{{ SubscriberArn }}',
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
  - name: subscriber_notification
    props:
      - name: NotificationConfiguration
        value:
          HttpsNotificationConfiguration:
            AuthorizationApiKeyName: '{{ AuthorizationApiKeyName }}'
            AuthorizationApiKeyValue: '{{ AuthorizationApiKeyValue }}'
            Endpoint: '{{ Endpoint }}'
            HttpMethod: '{{ HttpMethod }}'
            TargetRoleArn: '{{ TargetRoleArn }}'
          SqsNotificationConfiguration: {}
      - name: SubscriberArn
        value: '{{ SubscriberArn }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.securitylake.subscriber_notifications
WHERE data__Identifier = '<SubscriberArn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>subscriber_notifications</code> resource, the following permissions are required:

### Create
```json
securitylake:CreateDataLake,
securitylake:CreateSubscriber,
securitylake:CreateSubscriberNotification,
securitylake:GetSubscriber,
iam:CreateServiceLinkedRole,
iam:PutRolePolicy,
iam:DeleteRolePolicy,
iam:PassRole,
s3:PutBucketNotification,
s3:GetBucketNotification,
events:CreateApiDestination,
events:CreateConnection,
events:CreateRule,
events:UpdateConnection,
events:DeleteConnection,
events:UpdateApiDestination,
events:DeleteApiDestination,
events:ListApiDestinations,
events:ListConnections,
events:PutRule,
events:DescribeRule,
events:DeleteRule,
events:PutTargets,
events:RemoveTargets,
events:ListTargetsByRule,
secretsmanager:CreateSecret,
sqs:CreateQueue,
sqs:GetQueueAttributes,
sqs:GetQueueUrl,
sqs:SetQueueAttributes
```

### Read
```json
securitylake:GetSubscriber
```

### Update
```json
securitylake:UpdateSubscriberNotification,
securitylake:GetSubscriber,
iam:CreateServiceLinkedRole,
iam:PutRolePolicy,
iam:DeleteRolePolicy,
iam:PassRole,
events:CreateApiDestination,
events:CreateConnection,
events:UpdateConnection,
events:DeleteConnection,
events:UpdateApiDestination,
events:DeleteApiDestination,
events:DeleteRule,
events:ListApiDestinations,
events:ListConnections,
events:PutRule,
events:DescribeRule,
events:DeleteRule,
events:PutTargets,
events:RemoveTargets,
events:ListTargetsByRule,
secretsmanager:CreateSecret,
s3:GetBucketNotificationConfiguration,
s3:PutBucketNotificationConfiguration,
s3:PutBucketNotification,
s3:GetBucketNotification,
sqs:CreateQueue,
sqs:DeleteQueue,
sqs:GetQueueAttributes,
sqs:SetQueueAttributes
```

### Delete
```json
securitylake:DeleteSubscriberNotification,
securitylake:GetSubscriber,
iam:DeleteRole,
iam:DeleteRolePolicy,
events:DeleteApiDestination,
events:DeleteConnection,
events:DeleteRule,
events:ListTargetsByRule,
events:DescribeRule,
events:RemoveTargets,
sqs:DeleteQueue
```

### List
```json
securitylake:ListSubscribers
```

