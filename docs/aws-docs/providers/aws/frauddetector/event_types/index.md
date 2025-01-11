---
title: event_types
hide_title: false
hide_table_of_contents: false
keywords:
  - event_types
  - frauddetector
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

Creates, updates, deletes or gets an <code>event_type</code> resource or lists <code>event_types</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>event_types</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>A resource schema for an EventType in Amazon Fraud Detector.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.frauddetector.event_types" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name for the event type</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>Tags associated with this event type.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>The description of the event type.</td></tr>
<tr><td><CopyableCode code="event_variables" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="labels" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="entity_types" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The ARN of the event type.</td></tr>
<tr><td><CopyableCode code="created_time" /></td><td><code>string</code></td><td>The time when the event type was created.</td></tr>
<tr><td><CopyableCode code="last_updated_time" /></td><td><code>string</code></td><td>The time when the event type was last updated.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-frauddetector-eventtype.html"><code>AWS::FraudDetector::EventType</code></a>.

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
    <td><CopyableCode code="EntityTypes, EventVariables, Labels, Name, region" /></td>
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
Gets all <code>event_types</code> in a region.
```sql
SELECT
region,
name,
tags,
description,
event_variables,
labels,
entity_types,
arn,
created_time,
last_updated_time
FROM aws.frauddetector.event_types
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>event_type</code>.
```sql
SELECT
region,
name,
tags,
description,
event_variables,
labels,
entity_types,
arn,
created_time,
last_updated_time
FROM aws.frauddetector.event_types
WHERE region = 'us-east-1' AND data__Identifier = '<Arn>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>event_type</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.frauddetector.event_types (
 Name,
 EventVariables,
 Labels,
 EntityTypes,
 region
)
SELECT 
'{{ Name }}',
 '{{ EventVariables }}',
 '{{ Labels }}',
 '{{ EntityTypes }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.frauddetector.event_types (
 Name,
 Tags,
 Description,
 EventVariables,
 Labels,
 EntityTypes,
 region
)
SELECT 
 '{{ Name }}',
 '{{ Tags }}',
 '{{ Description }}',
 '{{ EventVariables }}',
 '{{ Labels }}',
 '{{ EntityTypes }}',
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
  - name: event_type
    props:
      - name: Name
        value: '{{ Name }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'
      - name: Description
        value: '{{ Description }}'
      - name: EventVariables
        value:
          - Arn: '{{ Arn }}'
            Inline: '{{ Inline }}'
            Name: '{{ Name }}'
            DataSource: '{{ DataSource }}'
            DataType: '{{ DataType }}'
            DefaultValue: '{{ DefaultValue }}'
            VariableType: '{{ VariableType }}'
            Description: '{{ Description }}'
            Tags:
              - null
            CreatedTime: '{{ CreatedTime }}'
            LastUpdatedTime: '{{ LastUpdatedTime }}'
      - name: Labels
        value:
          - Name: '{{ Name }}'
            Tags:
              - null
            Description: '{{ Description }}'
      - name: EntityTypes
        value:
          - Arn: '{{ Arn }}'
            Inline: '{{ Inline }}'
            Name: '{{ Name }}'
            Description: '{{ Description }}'
            Tags:
              - null
            CreatedTime: '{{ CreatedTime }}'
            LastUpdatedTime: '{{ LastUpdatedTime }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.frauddetector.event_types
WHERE data__Identifier = '<Arn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>event_types</code> resource, the following permissions are required:

### Create
```json
frauddetector:BatchCreateVariable,
frauddetector:BatchGetVariable,
frauddetector:CreateVariable,
frauddetector:GetVariables,
frauddetector:PutLabel,
frauddetector:PutEntityType,
frauddetector:PutEventType,
frauddetector:GetEventTypes,
frauddetector:GetLabels,
frauddetector:GetEntityTypes,
frauddetector:ListTagsForResource,
frauddetector:TagResource
```

### Update
```json
frauddetector:BatchCreateVariable,
frauddetector:BatchGetVariable,
frauddetector:CreateVariable,
frauddetector:UpdateVariable,
frauddetector:GetVariables,
frauddetector:PutLabel,
frauddetector:PutEntityType,
frauddetector:PutEventType,
frauddetector:GetEventTypes,
frauddetector:GetLabels,
frauddetector:GetEntityTypes,
frauddetector:DeleteEventType,
frauddetector:DeleteVariable,
frauddetector:DeleteLabel,
frauddetector:DeleteEntityType,
frauddetector:ListTagsForResource,
frauddetector:TagResource,
frauddetector:UntagResource
```

### Delete
```json
frauddetector:BatchGetVariable,
frauddetector:GetVariables,
frauddetector:GetEventTypes,
frauddetector:GetLabels,
frauddetector:GetEntityTypes,
frauddetector:DeleteEventType,
frauddetector:DeleteVariable,
frauddetector:DeleteLabel,
frauddetector:DeleteEntityType,
frauddetector:ListTagsForResource
```

### Read
```json
frauddetector:BatchGetVariable,
frauddetector:GetVariables,
frauddetector:GetEventTypes,
frauddetector:GetLabels,
frauddetector:GetEntityTypes,
frauddetector:ListTagsForResource
```

### List
```json
frauddetector:BatchGetVariable,
frauddetector:GetVariables,
frauddetector:GetEventTypes,
frauddetector:GetLabels,
frauddetector:GetEntityTypes,
frauddetector:ListTagsForResource
```
