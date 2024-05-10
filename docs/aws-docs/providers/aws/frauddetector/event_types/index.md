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


Used to retrieve a list of <code>event_types</code> in a region or to create or delete a <code>event_types</code> resource, use <code>event_type</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>event_types</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>A resource schema for an EventType in Amazon Fraud Detector.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.frauddetector.event_types" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The ARN of the event type.</td></tr>
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
arn
FROM aws.frauddetector.event_types
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
 "Name": "{{ Name }}",
 "EventVariables": [
  {
   "Arn": "{{ Arn }}",
   "Inline": "{{ Inline }}",
   "Name": "{{ Name }}",
   "DataSource": "{{ DataSource }}",
   "DataType": "{{ DataType }}",
   "DefaultValue": "{{ DefaultValue }}",
   "VariableType": "{{ VariableType }}",
   "Description": "{{ Description }}",
   "Tags": [
    {
     "Key": "{{ Key }}",
     "Value": "{{ Value }}"
    }
   ],
   "CreatedTime": "{{ CreatedTime }}",
   "LastUpdatedTime": "{{ LastUpdatedTime }}"
  }
 ],
 "Labels": [
  {
   "Name": "{{ Name }}"
  }
 ],
 "EntityTypes": [
  {
   "Arn": "{{ Arn }}",
   "Inline": "{{ Inline }}",
   "Name": "{{ Name }}",
   "Description": "{{ Description }}",
   "Tags": [
    null
   ],
   "CreatedTime": "{{ CreatedTime }}",
   "LastUpdatedTime": "{{ LastUpdatedTime }}"
  }
 ]
}
>>>
--required properties only
INSERT INTO aws.frauddetector.event_types (
 Name,
 EventVariables,
 Labels,
 EntityTypes,
 region
)
SELECT 
{{ Name }},
 {{ EventVariables }},
 {{ Labels }},
 {{ EntityTypes }},
'us-east-1';
```

</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "Name": "{{ Name }}",
 "Tags": [
  {
   "Key": "{{ Key }}",
   "Value": "{{ Value }}"
  }
 ],
 "Description": "{{ Description }}",
 "EventVariables": [
  {
   "Arn": "{{ Arn }}",
   "Inline": "{{ Inline }}",
   "Name": "{{ Name }}",
   "DataSource": "{{ DataSource }}",
   "DataType": "{{ DataType }}",
   "DefaultValue": "{{ DefaultValue }}",
   "VariableType": "{{ VariableType }}",
   "Description": "{{ Description }}",
   "Tags": [
    null
   ],
   "CreatedTime": "{{ CreatedTime }}",
   "LastUpdatedTime": "{{ LastUpdatedTime }}"
  }
 ],
 "Labels": [
  {
   "Name": "{{ Name }}",
   "Tags": [
    null
   ],
   "Description": "{{ Description }}"
  }
 ],
 "EntityTypes": [
  {
   "Arn": "{{ Arn }}",
   "Inline": "{{ Inline }}",
   "Name": "{{ Name }}",
   "Description": "{{ Description }}",
   "Tags": [
    null
   ],
   "CreatedTime": "{{ CreatedTime }}",
   "LastUpdatedTime": "{{ LastUpdatedTime }}"
  }
 ]
}
>>>
--all properties
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
 {{ Name }},
 {{ Tags }},
 {{ Description }},
 {{ EventVariables }},
 {{ Labels }},
 {{ EntityTypes }},
 'us-east-1';
```

</TabItem>
</Tabs>

## `DELETE` Example

```sql
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

### List
```json
frauddetector:BatchGetVariable,
frauddetector:GetVariables,
frauddetector:GetEventTypes,
frauddetector:GetLabels,
frauddetector:GetEntityTypes,
frauddetector:ListTagsForResource
```

