---
title: event_bus
hide_title: false
hide_table_of_contents: false
keywords:
  - event_bus
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
Gets an individual <code>event_bus</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>event_bus</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>event_bus</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.events.event_bus</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>event_source_name</code></td><td><code>string</code></td><td>If you are creating a partner event bus, this specifies the partner event source that the new event bus will be matched with.</td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td>The name of the event bus.</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>Any tags assigned to the event bus.</td></tr>
<tr><td><code>policy</code></td><td><code>object</code></td><td>A JSON string that describes the permission policy statement for the event bus.</td></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) for the event bus.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
event_source_name,
name,
tags,
policy,
arn
FROM awscc.events.event_bus
WHERE region = 'us-east-1'
AND data__Identifier = '{Name}';
```

## Permissions

To operate on the <code>event_bus</code> resource, the following permissions are required:

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
events:DescribeEventBus
```

### Delete
```json
events:DescribeEventBus,
events:DeleteEventBus
```

