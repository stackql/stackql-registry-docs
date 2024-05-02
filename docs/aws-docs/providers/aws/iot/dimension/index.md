---
title: dimension
hide_title: false
hide_table_of_contents: false
keywords:
  - dimension
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
Gets an individual <code>dimension</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>dimension</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>A dimension can be used to limit the scope of a metric used in a security profile for AWS IoT Device Defender.</td></tr>
<tr><td><b>Id</b></td><td><code>aws.iot.dimension</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td>A unique identifier for the dimension.</td></tr>
<tr><td><code>type</code></td><td><code>string</code></td><td>Specifies the type of the dimension.</td></tr>
<tr><td><code>string_values</code></td><td><code>array</code></td><td>Specifies the value or list of values for the dimension.</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>Metadata that can be used to manage the dimension.</td></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td>The ARN (Amazon resource name) of the created dimension.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods

<table><tbody>
  <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
  </tr>
  <tr>
    <td><code>update_resource</code></td>
    <td><code>UPDATE</code></td>
    <td><code>data__Identifier, data__PatchDocument, region</code></td>
  </tr>
  <tr>
    <td><code>delete_resource</code></td>
    <td><code>DELETE</code></td>
    <td><code>data__Identifier, region</code></td>
  </tr>
  <tr>
    <td><code>get_resource</code></td>
    <td><code>SELECT</code></td>
    <td><code>data__Identifier, region</code></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
name,
type,
string_values,
tags,
arn
FROM aws.iot.dimension
WHERE data__Identifier = '<Name>';
```

## Permissions

To operate on the <code>dimension</code> resource, the following permissions are required:

### Read
```json
iot:DescribeDimension,
iot:ListTagsForResource
```

### Update
```json
iot:UpdateDimension,
iot:ListTagsForResource,
iot:UntagResource,
iot:TagResource
```

### Delete
```json
iot:DescribeDimension,
iot:DeleteDimension
```

