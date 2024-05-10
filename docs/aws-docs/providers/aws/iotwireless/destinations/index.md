---
title: destinations
hide_title: false
hide_table_of_contents: false
keywords:
  - destinations
  - iotwireless
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


Used to retrieve a list of <code>destinations</code> in a region or to create or delete a <code>destinations</code> resource, use <code>destination</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>destinations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Destination's resource schema demonstrating some basic constructs and validation rules.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.iotwireless.destinations" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>Unique name of destination</td></tr>
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
FROM aws.iotwireless.destinations
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
 "Expression": "{{ Expression }}",
 "ExpressionType": "{{ ExpressionType }}"
}
>>>
--required properties only
INSERT INTO aws.iotwireless.destinations (
 Name,
 Expression,
 ExpressionType,
 region
)
SELECT 
{{ Name }},
 {{ Expression }},
 {{ ExpressionType }},
'us-east-1';
```

</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "Name": "{{ Name }}",
 "Expression": "{{ Expression }}",
 "ExpressionType": "{{ ExpressionType }}",
 "Description": "{{ Description }}",
 "Tags": [
  {
   "Key": "{{ Key }}",
   "Value": "{{ Value }}"
  }
 ],
 "RoleArn": "{{ RoleArn }}"
}
>>>
--all properties
INSERT INTO aws.iotwireless.destinations (
 Name,
 Expression,
 ExpressionType,
 Description,
 Tags,
 RoleArn,
 region
)
SELECT 
 {{ Name }},
 {{ Expression }},
 {{ ExpressionType }},
 {{ Description }},
 {{ Tags }},
 {{ RoleArn }},
 'us-east-1';
```

</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.iotwireless.destinations
WHERE data__Identifier = '<Name>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>destinations</code> resource, the following permissions are required:

### Create
```json
iam:PassRole,
iotwireless:CreateDestination,
iotwireless:TagResource,
iotwireless:ListTagsForResource
```

### Delete
```json
iotwireless:DeleteDestination
```

### List
```json
iotwireless:ListDestinations,
iotwireless:ListTagsForResource
```

