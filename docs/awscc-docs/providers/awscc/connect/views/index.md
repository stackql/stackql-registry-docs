---
title: views
hide_title: false
hide_table_of_contents: false
keywords:
  - views
  - connect
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>views</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>views</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>views</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.connect.views</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>view_arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the view.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>views</code> resource, the following permissions are required:

### Create
```json
connect:CreateView,
connect:TagResource
```

### List
```json
connect:ListViews
```


## Example
```sql
SELECT
region,
view_arn
FROM awscc.connect.views
WHERE region = 'us-east-1'
```
