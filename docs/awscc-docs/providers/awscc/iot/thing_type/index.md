---
title: thing_type
hide_title: false
hide_table_of_contents: false
keywords:
  - thing_type
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
Gets an individual <code>thing_type</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>thing_type</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>thing_type</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.iot.thing_type</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>thing_type_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>deprecate_thing_type</code></td><td><code>boolean</code></td><td></td></tr>
<tr><td><code>thing_type_properties</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
id,
arn,
thing_type_name,
deprecate_thing_type,
thing_type_properties,
tags
FROM awscc.iot.thing_type
WHERE region = 'us-east-1'
AND data__Identifier = '{ThingTypeName}';
```

## Permissions

To operate on the <code>thing_type</code> resource, the following permissions are required:

### Delete
```json
iot:DescribeThingType,
iot:DeleteThingType,
iot:DeprecateThingType
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

