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
null
<tr><td><b>Id</b></td><td><code>aws.ssm.patch_baseline</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>OperatingSystem</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>Description</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>ApprovalRules</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>Sources</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>Name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>RejectedPatches</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>ApprovedPatches</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>RejectedPatchesAction</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>PatchGroups</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>ApprovedPatchesComplianceLevel</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>ApprovedPatchesEnableNonSecurity</code></td><td><code>boolean</code></td><td></td></tr>
<tr><td><code>Id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>GlobalFilters</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>Tags</code></td><td><code>array</code></td><td></td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.ssm.patch_baseline
WHERE region = 'us-east-1' AND data__Identifier = '&lt;Id&gt;'
</pre>
