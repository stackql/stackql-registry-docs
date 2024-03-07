---
title: view
hide_title: false
hide_table_of_contents: false
keywords:
  - view
  - resourceexplorer2
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>view</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>view</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>view</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.resourceexplorer2.view</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>filters</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>included_properties</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>scope</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>view_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>view_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>view</code> resource, the following permissions are required:

### Read
<pre>
resource-explorer-2:GetView</pre>

### Update
<pre>
resource-explorer-2:UpdateView,
resource-explorer-2:TagResource,
resource-explorer-2:UntagResource,
resource-explorer-2:ListTagsForResource</pre>

### Delete
<pre>
resource-explorer-2:DeleteView,
resource-explorer-2:GetView,
resource-explorer-2:UntagResource</pre>


## Example
```sql
SELECT
region,
filters,
included_properties,
scope,
tags,
view_arn,
view_name
FROM awscc.resourceexplorer2.view
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;ViewArn&gt;'
```
