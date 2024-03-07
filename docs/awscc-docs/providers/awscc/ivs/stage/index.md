---
title: stage
hide_title: false
hide_table_of_contents: false
keywords:
  - stage
  - ivs
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>stage</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>stage</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>stage</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.ivs.stage</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td>Stage ARN is automatically generated on creation and assigned as the unique identifier.</td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td>Stage name</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
<tr><td><code>active_session_id</code></td><td><code>string</code></td><td>ID of the active session within the stage.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>stage</code> resource, the following permissions are required:

### Read
<pre>
ivs:GetStage,
ivs:ListTagsForResource</pre>

### Update
<pre>
ivs:GetStage,
ivs:UpdateStage,
ivs:TagResource,
ivs:UnTagResource,
ivs:ListTagsForResource</pre>

### Delete
<pre>
ivs:DeleteStage,
ivs:UnTagResource</pre>


## Example
```sql
SELECT
region,
arn,
name,
tags,
active_session_id
FROM awscc.ivs.stage
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;Arn&gt;'
```
