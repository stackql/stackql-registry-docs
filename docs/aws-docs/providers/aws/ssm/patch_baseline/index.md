---
title: patch_baseline
hide_title: false
hide_table_of_contents: false
keywords:
  - patch_baseline
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
Gets an individual <code>patch_baseline</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>patch_baseline</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>patch_baseline</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ssm.patch_baseline</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>operating_system</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>approval_rules</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>sources</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>rejected_patches</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>approved_patches</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>rejected_patches_action</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>patch_groups</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>approved_patches_compliance_level</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>approved_patches_enable_non_security</code></td><td><code>boolean</code></td><td></td></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>global_filters</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
operating_system,
description,
approval_rules,
sources,
name,
rejected_patches,
approved_patches,
rejected_patches_action,
patch_groups,
approved_patches_compliance_level,
approved_patches_enable_non_security,
id,
global_filters,
tags
FROM aws.ssm.patch_baseline
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;Id&gt;'
```
