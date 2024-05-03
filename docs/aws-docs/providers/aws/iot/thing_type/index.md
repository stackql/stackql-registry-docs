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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';

Gets or operates on an individual <code>thing_type</code> resource, use <code>thing_types</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>thing_type</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::IoT::ThingType</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.iot.thing_type" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td></td></tr>
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
    <td><CopyableCode code="update_resource" /></td>
    <td><code>UPDATE</code></td>
    <td><CopyableCode code="data__Identifier, data__PatchDocument, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
id,
arn,
thing_type_name,
deprecate_thing_type,
thing_type_properties,
tags
FROM aws.iot.thing_type
WHERE data__Identifier = '<ThingTypeName>';
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

