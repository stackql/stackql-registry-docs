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


Used to retrieve a list of <code>queues</code> in a region or to create or delete a <code>queues</code> resource, use <code>queue</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>queues</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::Connect::Queue</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.connect.queues" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="queue_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) for the queue.</td></tr>
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
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
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
queue_arn
FROM aws.connect.queues
WHERE region = 'us-east-1';
```

## `INSERT` Example

<Tabs
    defaultValue="required"
    values={[
      { label: 'Required Properties', value: 'required', },
      { label: 'All Properties', value: 'all', },
    ]
}>
<TabItem value="required">

```sql
<<<json
{
 "InstanceArn": "{{ InstanceArn }}",
 "HoursOfOperationArn": "{{ HoursOfOperationArn }}",
 "Name": "{{ Name }}"
}
>>>
--required properties only
INSERT INTO aws.connect.queues (
 InstanceArn,
 HoursOfOperationArn,
 Name,
 region
)
SELECT 
{{ .InstanceArn }},
 {{ .HoursOfOperationArn }},
 {{ .Name }},
'us-east-1';
```
</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "InstanceArn": "{{ InstanceArn }}",
 "Description": "{{ Description }}",
 "HoursOfOperationArn": "{{ HoursOfOperationArn }}",
 "MaxContacts": "{{ MaxContacts }}",
 "Name": "{{ Name }}",
 "OutboundCallerConfig": {
  "OutboundCallerIdName": "{{ OutboundCallerIdName }}",
  "OutboundCallerIdNumberArn": "{{ OutboundCallerIdNumberArn }}",
  "OutboundFlowArn": "{{ OutboundFlowArn }}"
 },
 "Status": "{{ Status }}",
 "QuickConnectArns": [
  "{{ QuickConnectArns[0] }}"
 ],
 "Tags": [
  {
   "Key": "{{ Key }}",
   "Value": "{{ Value }}"
  }
 ]
}
>>>
--all properties
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
 {{ .InstanceArn }},
 {{ .Description }},
 {{ .HoursOfOperationArn }},
 {{ .MaxContacts }},
 {{ .Name }},
 {{ .OutboundCallerConfig }},
 {{ .Status }},
 {{ .QuickConnectArns }},
 {{ .Tags }},
 'us-east-1';
```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
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

### Delete
```json
connect:DeleteQueue,
connect:UntagResource
```

### List
```json
connect:ListQueues,
connect:ListQueueQuickConnects
```

