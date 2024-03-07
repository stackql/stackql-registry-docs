---
title: stages
hide_title: false
hide_table_of_contents: false
keywords:
  - stages
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
Retrieves a list of <code>stages</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>stages</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>stages</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.ivs.stages</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td>Stage ARN is automatically generated on creation and assigned as the unique identifier.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>stages</code> resource, the following permissions are required:

### Create
<pre>
ivs:CreateStage,
ivs:GetStage,
ivs:TagResource,
ivs:ListTagsForResource</pre>

### List
<pre>
ivs:ListStages,
ivs:ListTagsForResource</pre>


## Example
```sql
SELECT
region,
arn
FROM awscc.ivs.stages
WHERE region = 'us-east-1'
```
