---
title: prompts
hide_title: false
hide_table_of_contents: false
keywords:
  - prompts
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
Retrieves a list of <code>prompts</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>prompts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>prompts</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.connect.prompts</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>prompt_arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) for the prompt.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>prompts</code> resource, the following permissions are required:

### Create
```json
connect:CreatePrompt,
connect:TagResource,
s3:GetObject,
kms:Decrypt,
s3:GetObjectAcl
```

### List
```json
connect:ListPrompts
```


## Example
```sql
SELECT
region,
prompt_arn
FROM awscc.connect.prompts
WHERE region = 'us-east-1'
```
