---
title: place_index
hide_title: false
hide_table_of_contents: false
keywords:
  - place_index
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
Gets an individual <code>place_index</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>place_index</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>place_index</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.location.place_index</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>create_time</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>data_source</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>data_source_configuration</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>index_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>index_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>pricing_plan</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
<tr><td><code>update_time</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>place_index</code> resource, the following permissions are required:

### Read
<pre>
geo:DescribePlaceIndex</pre>

### Update
<pre>
geo:CreatePlaceIndex,
geo:DescribePlaceIndex,
geo:TagResource,
geo:UntagResource,
geo:UpdatePlaceIndex</pre>

### Delete
<pre>
geo:DeletePlaceIndex,
geo:DescribePlaceIndex</pre>


## Example
```sql
SELECT
region,
create_time,
data_source,
data_source_configuration,
description,
index_arn,
index_name,
pricing_plan,
tags,
update_time,
arn
FROM awscc.location.place_index
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;IndexName&gt;'
```
