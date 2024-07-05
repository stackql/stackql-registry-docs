---
title: queues
hide_title: false
hide_table_of_contents: false
keywords:
  - queues
  - connect
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

Creates, updates, deletes or gets a <code>queue</code> resource or lists <code>queues</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>queues</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::Connect::Queue</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.connect.queues" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="instance_arn" /></td><td><code>string</code></td><td>The identifier of the Amazon Connect instance.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>The description of the queue.</td></tr>
<tr><td><CopyableCode code="hours_of_operation_arn" /></td><td><code>string</code></td><td>The identifier for the hours of operation.</td></tr>
<tr><td><CopyableCode code="max_contacts" /></td><td><code>integer</code></td><td>The maximum number of contacts that can be in the queue before it is considered full.</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name of the queue.</td></tr>
<tr><td><CopyableCode code="outbound_caller_config" /></td><td><code>object</code></td><td>The outbound caller ID name, number, and outbound whisper flow.</td></tr>
<tr><td><CopyableCode code="queue_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) for the queue.</td></tr>
<tr><td><CopyableCode code="status" /></td><td><code>string</code></td><td>The status of the queue.</td></tr>
<tr><td><CopyableCode code="quick_connect_arns" /></td><td><code>array</code></td><td>The quick connects available to agents who are working the queue.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
<tr><td><CopyableCode code="type" /></td><td><code>string</code></td><td>The type of queue.</td></tr>
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
    <td><CopyableCode code="InstanceArn, HoursOfOperationArn, Name, region" /></td>
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
Gets all <code>queues</code> in a region.
```sql
SELECT
region,
instance_arn,
description,
hours_of_operation_arn,
max_contacts,
name,
outbound_caller_config,
queue_arn,
status,
quick_connect_arns,
tags,
type
FROM aws.connect.queues
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>queue</code>.
```sql
SELECT
region,
instance_arn,
description,
hours_of_operation_arn,
max_contacts,
name,
outbound_caller_config,
queue_arn,
status,
quick_connect_arns,
tags,
type
FROM aws.connect.queues
WHERE region = 'us-east-1' AND data__Identifier = '<QueueArn>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>queue</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.connect.queues (
 InstanceArn,
 HoursOfOperationArn,
 Name,
 region
)
SELECT 
'{{ InstanceArn }}',
 '{{ HoursOfOperationArn }}',
 '{{ Name }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.connect.queues (
 InstanceArn,
 Description,
 HoursOfOperationArn,
 MaxContacts,
 Name,
 OutboundCallerConfig,
 Status,
 QuickConnectArns,
 Tags,
 region
)
SELECT 
 '{{ InstanceArn }}',
 '{{ Description }}',
 '{{ HoursOfOperationArn }}',
 '{{ MaxContacts }}',
 '{{ Name }}',
 '{{ OutboundCallerConfig }}',
 '{{ Status }}',
 '{{ QuickConnectArns }}',
 '{{ Tags }}',
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
  - name: queue
    props:
      - name: InstanceArn
        value: '{{ InstanceArn }}'
      - name: Description
        value: '{{ Description }}'
      - name: HoursOfOperationArn
        value: '{{ HoursOfOperationArn }}'
      - name: MaxContacts
        value: '{{ MaxContacts }}'
      - name: Name
        value: '{{ Name }}'
      - name: OutboundCallerConfig
        value:
          OutboundCallerIdName: '{{ OutboundCallerIdName }}'
          OutboundCallerIdNumberArn: '{{ OutboundCallerIdNumberArn }}'
          OutboundFlowArn: '{{ OutboundFlowArn }}'
      - name: Status
        value: '{{ Status }}'
      - name: QuickConnectArns
        value:
          - '{{ QuickConnectArns[0] }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.connect.queues
WHERE data__Identifier = '<QueueArn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>queues</code> resource, the following permissions are required:

### Create
```json
connect:CreateQueue,
connect:TagResource
```

### Read
```json
connect:DescribeQueue,
connect:ListQueueQuickConnects
```

### Delete
```json
connect:DeleteQueue,
connect:UntagResource
```

### Update
```json
connect:UpdateQueueHoursOfOperation,
connect:UpdateQueueMaxContacts,
connect:UpdateQueueName,
connect:UpdateQueueOutboundCallerConfig,
connect:UpdateQueueStatus,
connect:AssociateQueueQuickConnects,
connect:DisassociateQueueQuickConnects,
connect:TagResource,
connect:UntagResource
```

### List
```json
connect:ListQueues,
connect:ListQueueQuickConnects
```

