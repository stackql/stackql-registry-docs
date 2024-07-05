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

Creates, updates, deletes or gets a <code>thing_type</code> resource or lists <code>thing_types</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>thing_types</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::IoT::ThingType</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.iot.thing_types" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="thing_type_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="deprecate_thing_type" /></td><td><code>boolean</code></td><td></td></tr>
<tr><td><CopyableCode code="thing_type_properties" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
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
    <td><CopyableCode code="region" /></td>
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
Gets all <code>thing_types</code> in a region.
```sql
SELECT
region,
id,
arn,
thing_type_name,
deprecate_thing_type,
thing_type_properties,
tags
FROM aws.iot.thing_types
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>thing_type</code>.
```sql
SELECT
region,
id,
arn,
thing_type_name,
deprecate_thing_type,
thing_type_properties,
tags
FROM aws.iot.thing_types
WHERE region = 'us-east-1' AND data__Identifier = '<ThingTypeName>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>thing_type</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.iot.thing_types (
 ThingTypeName,
 DeprecateThingType,
 ThingTypeProperties,
 Tags,
 region
)
SELECT 
'{{ ThingTypeName }}',
 '{{ DeprecateThingType }}',
 '{{ ThingTypeProperties }}',
 '{{ Tags }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.iot.thing_types (
 ThingTypeName,
 DeprecateThingType,
 ThingTypeProperties,
 Tags,
 region
)
SELECT 
 '{{ ThingTypeName }}',
 '{{ DeprecateThingType }}',
 '{{ ThingTypeProperties }}',
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
  - name: thing_type
    props:
      - name: ThingTypeName
        value: '{{ ThingTypeName }}'
      - name: DeprecateThingType
        value: '{{ DeprecateThingType }}'
      - name: ThingTypeProperties
        value:
          SearchableAttributes:
            - '{{ SearchableAttributes[0] }}'
          ThingTypeDescription: '{{ ThingTypeDescription }}'
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

### Read
```json
iot:DescribeThingType,
iot:ListTagsForResource
```

### Update
```json
iot:DescribeThingType,
iot:UpdateThingType,
iot:ListTagsForResource,
iot:TagResource,
iot:UntagResource,
iot:DeprecateThingType
```

