---
title: channels
hide_title: false
hide_table_of_contents: false
keywords:
  - channels
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
Retrieves a list of <code>channels</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>channels</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>channels</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.ivs.channels</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td>Channel ARN is automatically generated on creation and assigned as the unique identifier.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>channels</code> resource, the following permissions are required:

### Create
<pre>
ivs:CreateChannel,
ivs:TagResource</pre>

### List
<pre>
ivs:ListChannels,
ivs:ListTagsForResource</pre>


## Example
```sql
SELECT
region,
arn
FROM awscc.ivs.channels
WHERE region = 'us-east-1'
```
