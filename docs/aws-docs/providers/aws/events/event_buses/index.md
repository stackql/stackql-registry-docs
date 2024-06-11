---
title: event_buses
hide_title: false
hide_table_of_contents: false
keywords:
  - event_buses
  - events
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

Creates, updates, deletes or gets an <code>event_bus</code> resource or lists <code>event_buses</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>event_buses</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource type definition for AWS::Events::EventBus</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.events.event_buses" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="event_source_name" /></td><td><code>string</code></td><td>If you are creating a partner event bus, this specifies the partner event source that the new event bus will be matched with.</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name of the event bus.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>Any tags assigned to the event bus.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>The description of the event bus.</td></tr>
<tr><td><CopyableCode code="kms_key_identifier" /></td><td><code>string</code></td><td>Kms Key Identifier used to encrypt events at rest in the event bus.</td></tr>
<tr><td><CopyableCode code="policy" /></td><td><code>object</code></td><td>A JSON string that describes the permission policy statement for the event bus.</td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) for the event bus.</td></tr>
<tr><td><CopyableCode code="dead_letter_config" /></td><td><code>object</code></td><td>Dead Letter Queue for the event bus.</td></tr>
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
    <td><CopyableCode code="Name, region" /></td>
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
    <td><CopyableCode code="list_resource" /></td>
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
List all <code>event_buses</code> in a region.
```sql
SELECT
region,
name
FROM aws.events.event_buses
WHERE region = 'us-east-1';
```
Gets all properties from an <code>event_bus</code>.
```sql
SELECT
region,
event_source_name,
name,
tags,
description,
kms_key_identifier,
policy,
arn,
dead_letter_config
FROM aws.events.event_buses
WHERE region = 'us-east-1' AND data__Identifier = '<Name>';
```


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>event_bus</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.events.event_buses (
 Name,
 region
)
SELECT 
'{{ Name }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.events.event_buses (
 EventSourceName,
 Name,
 Tags,
 Description,
 KmsKeyIdentifier,
 Policy,
 DeadLetterConfig,
 region
)
SELECT 
 '{{ EventSourceName }}',
 '{{ Name }}',
 '{{ Tags }}',
 '{{ Description }}',
 '{{ KmsKeyIdentifier }}',
 '{{ Policy }}',
 '{{ DeadLetterConfig }}',
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
  - name: event_bus
    props:
      - name: EventSourceName
        value: '{{ EventSourceName }}'
      - name: Name
        value: '{{ Name }}'
      - name: Tags
        value:
          - Value: '{{ Value }}'
            Key: '{{ Key }}'
      - name: Description
        value: '{{ Description }}'
      - name: KmsKeyIdentifier
        value: '{{ KmsKeyIdentifier }}'
      - name: Policy
        value: {}
      - name: DeadLetterConfig
        value:
          Arn: '{{ Arn }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.events.event_buses
WHERE data__Identifier = '<Name>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>event_buses</code> resource, the following permissions are required:

### Create
```json
events:CreateEventBus,
events:DescribeEventBus,
events:PutPermission,
events:ListTagsForResource,
events:TagResource,
kms:DescribeKey,
kms:GenerateDataKey,
kms:Decrypt
```

### Read
```json
events:DescribeEventBus,
events:ListTagsForResource
```

### Update
```json
events:TagResource,
events:UntagResource,
events:PutPermission,
events:DescribeEventBus,
events:UpdateEventBus,
kms:DescribeKey,
kms:GenerateDataKey,
kms:Decrypt
```

### Delete
```json
events:DescribeEventBus,
events:UpdateEventBus,
events:ListTagsForResource,
events:UntagResource,
events:RemovePermission,
events:DeleteEventBus
```

### List
```json
events:ListEventBuses,
events:ListTagsForResource
```

