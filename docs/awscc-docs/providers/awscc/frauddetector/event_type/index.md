---
title: event_type
hide_title: false
hide_table_of_contents: false
keywords:
  - event_type
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
Gets an individual <code>event_type</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>event_type</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>event_type</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.frauddetector.event_type</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td>The name for the event type</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>Tags associated with this event type.</td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td>The description of the event type.</td></tr>
<tr><td><code>event_variables</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>labels</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>entity_types</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td>The ARN of the event type.</td></tr>
<tr><td><code>created_time</code></td><td><code>string</code></td><td>The time when the event type was created.</td></tr>
<tr><td><code>last_updated_time</code></td><td><code>string</code></td><td>The time when the event type was last updated.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
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
FROM awscc.frauddetector.event_type
WHERE data__Identifier = '<Arn>';
```

## Permissions

To operate on the <code>event_type</code> resource, the following permissions are required:

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

