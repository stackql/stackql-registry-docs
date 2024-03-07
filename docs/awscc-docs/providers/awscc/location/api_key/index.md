---
title: api_key
hide_title: false
hide_table_of_contents: false
keywords:
  - api_key
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
Gets an individual <code>api_key</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>api_key</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>api_key</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.location.api_key</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>create_time</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>expire_time</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>force_update</code></td><td><code>boolean</code></td><td></td></tr>
<tr><td><code>key_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>key_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>no_expiry</code></td><td><code>boolean</code></td><td></td></tr>
<tr><td><code>restrictions</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
<tr><td><code>update_time</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>force_delete</code></td><td><code>boolean</code></td><td></td></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>api_key</code> resource, the following permissions are required:

### Read
```json
geo:DescribeKey
```

### Update
```json
geo:CreateKey,
geo:DescribeKey,
geo:TagResource,
geo:UntagResource,
geo:GetMapTile,
geo:GetMapStyleDescriptor,
geo:GetMapSprites,
geo:GetMapGlyphs,
geo:SearchPlaceIndexForText,
geo:SearchPlaceIndexForPosition,
geo:SearchPlaceIndexForSuggestions,
geo:GetPlace,
geo:CalculateRoute,
geo:CalculateRouteMatrix,
geo:UpdateKey
```

### Delete
```json
geo:DeleteKey,
geo:DescribeKey
```


## Example
```sql
SELECT
region,
create_time,
description,
expire_time,
force_update,
key_arn,
key_name,
no_expiry,
restrictions,
tags,
update_time,
force_delete,
arn
FROM awscc.location.api_key
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;KeyName&gt;'
```
