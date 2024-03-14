---
title: map
hide_title: false
hide_table_of_contents: false
keywords:
  - map
  - location
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>map</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>map</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>map</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.location.map</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>configuration</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>create_time</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>map_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>map_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>pricing_plan</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
<tr><td><code>update_time</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
configuration,
create_time,
description,
map_arn,
map_name,
pricing_plan,
tags,
update_time,
arn
FROM awscc.location.map
WHERE data__Identifier = '<MapName>';
```

## Permissions

To operate on the <code>map</code> resource, the following permissions are required:

### Read
```json
geo:DescribeMap
```

### Update
```json
geo:CreateMap,
geo:DescribeMap,
geo:TagResource,
geo:UntagResource,
geo:UpdateMap
```

### Delete
```json
geo:DeleteMap,
geo:DescribeMap
```

