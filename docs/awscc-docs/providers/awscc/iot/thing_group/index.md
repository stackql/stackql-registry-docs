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
<tr><td><b>Description</b></td><td>thing_group</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.iot.thing_group</code></td></tr>
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
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>thing_group</code> resource, the following permissions are required:

### Delete
<pre>
iot:DescribeThingGroup,
iot:DeleteThingGroup,
iot:DeleteDynamicThingGroup</pre>

### Read
<pre>
iot:DescribeThingGroup,
iot:ListTagsForResource</pre>

### Update
<pre>
iot:ListTagsForResource,
iot:DescribeThingGroup,
iot:UpdateThingGroup,
iot:UpdateDynamicThingGroup,
iot:TagResource,
iot:UntagResource</pre>


## Example
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
FROM awscc.iot.thing_group
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;ThingGroupName&gt;'
```
