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


Used to retrieve a list of <code>event_buses</code> in a region or to create or delete a <code>event_buses</code> resource, use <code>event_bus</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>event_buses</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource type definition for AWS::Events::EventBus</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.events.event_buses" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name of the event bus.</td></tr>
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
name
FROM aws.events.event_buses
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
 "Name": "{{ Name }}"
}
>>>
--required properties only
INSERT INTO aws.events.event_buses (
 Name,
 region
)
SELECT 
{{ .Name }},
'us-east-1';
```
</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "EventSourceName": "{{ EventSourceName }}",
 "Name": "{{ Name }}",
 "Tags": [
  {
   "Value": "{{ Value }}",
   "Key": "{{ Key }}"
  }
 ],
 "Policy": {}
}
>>>
--all properties
INSERT INTO aws.events.event_buses (
 EventSourceName,
 Name,
 Tags,
 Policy,
 region
)
SELECT 
 {{ .EventSourceName }},
 {{ .Name }},
 {{ .Tags }},
 {{ .Policy }},
 'us-east-1';
```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
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
events:TagResource
```

### Delete
```json
events:DescribeEventBus,
events:DeleteEventBus
```

### List
```json
events:ListEventBuses,
events:ListTagsForResource
```

