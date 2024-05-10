---
title: thing_types
hide_title: false
hide_table_of_contents: false
keywords:
  - thing_types
  - iot
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


Used to retrieve a list of <code>thing_types</code> in a region or to create or delete a <code>thing_types</code> resource, use <code>thing_type</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>thing_types</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::IoT::ThingType</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.iot.thing_types" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="thing_type_name" /></td><td><code>string</code></td><td></td></tr>
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
thing_type_name
FROM aws.iot.thing_types
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
 "ThingTypeName": "{{ ThingTypeName }}",
 "DeprecateThingType": "{{ DeprecateThingType }}",
 "ThingTypeProperties": {
  "SearchableAttributes": [
   "{{ SearchableAttributes[0] }}"
  ],
  "ThingTypeDescription": "{{ ThingTypeDescription }}"
 },
 "Tags": [
  {
   "Key": "{{ Key }}",
   "Value": "{{ Value }}"
  }
 ]
}
>>>
--required properties only
INSERT INTO aws.iot.thing_types (
 ThingTypeName,
 DeprecateThingType,
 ThingTypeProperties,
 Tags,
 region
)
SELECT 
{{ ThingTypeName }},
 {{ DeprecateThingType }},
 {{ ThingTypeProperties }},
 {{ Tags }},
'us-east-1';
```

</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "ThingTypeName": "{{ ThingTypeName }}",
 "DeprecateThingType": "{{ DeprecateThingType }}",
 "ThingTypeProperties": {
  "SearchableAttributes": [
   "{{ SearchableAttributes[0] }}"
  ],
  "ThingTypeDescription": "{{ ThingTypeDescription }}"
 },
 "Tags": [
  {
   "Key": "{{ Key }}",
   "Value": "{{ Value }}"
  }
 ]
}
>>>
--all properties
INSERT INTO aws.iot.thing_types (
 ThingTypeName,
 DeprecateThingType,
 ThingTypeProperties,
 Tags,
 region
)
SELECT 
 {{ ThingTypeName }},
 {{ DeprecateThingType }},
 {{ ThingTypeProperties }},
 {{ Tags }},
 'us-east-1';
```

</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.iot.thing_types
WHERE data__Identifier = '<ThingTypeName>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>thing_types</code> resource, the following permissions are required:

### Create
```json
iot:DescribeThingType,
iot:ListTagsForResource,
iot:CreateThingType,
iot:DeprecateThingType,
iot:TagResource
```

### Delete
```json
iot:DescribeThingType,
iot:DeleteThingType,
iot:DeprecateThingType
```

### List
```json
iot:ListThingTypes,
iot:ListTagsForResource
```

