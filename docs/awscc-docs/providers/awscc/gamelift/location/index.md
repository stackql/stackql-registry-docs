---
title: location
hide_title: false
hide_table_of_contents: false
keywords:
  - location
  - gamelift
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>location</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>location</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>location</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.gamelift.location</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>location_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>location_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>location</code> resource, the following permissions are required:

### Read
<pre>
gamelift:ListLocations,
gamelift:ListTagsForResource</pre>

### Delete
<pre>
gamelift:DeleteLocation</pre>

### Update
<pre>
gamelift:ListLocations,
gamelift:ListTagsForResource,
gamelift:TagResource,
gamelift:UntagResource</pre>


## Example
```sql
SELECT
region,
location_name,
location_arn,
tags
FROM awscc.gamelift.location
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;LocationName&gt;'
```
