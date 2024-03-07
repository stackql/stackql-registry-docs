---
title: patch_baselines
hide_title: false
hide_table_of_contents: false
keywords:
  - patch_baselines
  - ssm
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>patch_baselines</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>patch_baselines</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>patch_baselines</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.ssm.patch_baselines</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td>The ID of the patch baseline.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>patch_baselines</code> resource, the following permissions are required:

### Create
<pre>
ssm:CreatePatchBaseline,
ssm:RegisterPatchBaselineForPatchGroup,
ssm:AddTagsToResource,
ssm:RemoveTagsFromResource,
ssm:ListTagsForResource,
ssm:GetDefaultPatchBaseline,
ssm:RegisterDefaultPatchBaseline</pre>

### List
<pre>
ssm:DescribePatchBaselines,
ssm:GetDefaultPatchBaseline,
ssm:GetPatchBaseline,
ssm:ListTagsForResource</pre>


## Example
```sql
SELECT
region,
id
FROM awscc.ssm.patch_baselines
WHERE region = 'us-east-1'
```
