---
title: thing_group
hide_title: false
hide_table_of_contents: false
keywords:
  - thing_group
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
Gets an individual <code>thing_group</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>thing_group</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::IoT::ThingGroup</td></tr>
<tr><td><b>Id</b></td><td><code>aws.iot.thing_group</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>thing_group_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>parent_group_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>query_string</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>thing_group_properties</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
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
id,
arn,
thing_group_name,
parent_group_name,
query_string,
thing_group_properties,
tags
FROM aws.iot.thing_group
WHERE data__Identifier = '<ThingGroupName>';
```

## Permissions

To operate on the <code>thing_group</code> resource, the following permissions are required:

### Delete
```json
iot:DescribeThingGroup,
iot:DeleteThingGroup,
iot:DeleteDynamicThingGroup
```

### Read
```json
iot:DescribeThingGroup,
iot:ListTagsForResource
```

### Update
```json
iot:ListTagsForResource,
iot:DescribeThingGroup,
iot:UpdateThingGroup,
iot:UpdateDynamicThingGroup,
iot:TagResource,
iot:UntagResource
```

