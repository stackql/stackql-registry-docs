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
<tr><td><b>Id</b></td><td><code>awscc.ssm.patch_baseline</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td>The ID of the patch baseline.</td></tr>
<tr><td><code>default_baseline</code></td><td><code>boolean</code></td><td>Set the baseline as default baseline. Only registering to default patch baseline is allowed.</td></tr>
<tr><td><code>operating_system</code></td><td><code>string</code></td><td>Defines the operating system the patch baseline applies to. The Default value is WINDOWS.</td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td>The description of the patch baseline.</td></tr>
<tr><td><code>approval_rules</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>sources</code></td><td><code>array</code></td><td>Information about the patches to use to update the instances, including target operating systems and source repository. Applies to Linux instances only.</td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td>The name of the patch baseline.</td></tr>
<tr><td><code>rejected_patches</code></td><td><code>array</code></td><td>A list of explicitly rejected patches for the baseline.</td></tr>
<tr><td><code>approved_patches</code></td><td><code>array</code></td><td>A list of explicitly approved patches for the baseline.</td></tr>
<tr><td><code>rejected_patches_action</code></td><td><code>string</code></td><td>The action for Patch Manager to take on patches included in the RejectedPackages list.</td></tr>
<tr><td><code>patch_groups</code></td><td><code>array</code></td><td>PatchGroups is used to associate instances with a specific patch baseline</td></tr>
<tr><td><code>approved_patches_compliance_level</code></td><td><code>string</code></td><td>Defines the compliance level for approved patches. This means that if an approved patch is reported as missing, this is the severity of the compliance violation. The default value is UNSPECIFIED.</td></tr>
<tr><td><code>approved_patches_enable_non_security</code></td><td><code>boolean</code></td><td>Indicates whether the list of approved patches includes non-security updates that should be applied to the instances. The default value is 'false'. Applies to Linux instances only.</td></tr>
<tr><td><code>global_filters</code></td><td><code>object</code></td><td>A set of global filters used to include patches in the baseline.</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>Optional metadata that you assign to a resource. Tags enable you to categorize a resource in different ways.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
id,
default_baseline,
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
global_filters,
tags
FROM awscc.ssm.patch_baseline
WHERE data__Identifier = '<Id>';
```

## Permissions

To operate on the <code>patch_baseline</code> resource, the following permissions are required:

### Delete
```json
ssm:DeletePatchBaseline,
ssm:GetPatchBaseline,
ssm:DeregisterPatchBaselineForPatchGroup
```

### Read
```json
ssm:GetDefaultPatchBaseline,
ssm:GetPatchBaseline,
ssm:ListTagsForResource
```

### Update
```json
ssm:UpdatePatchBaseline,
ssm:DeregisterPatchBaselineForPatchGroup,
ssm:AddTagsToResource,
ssm:RemoveTagsFromResource,
ssm:ListTagsForResource,
ssm:GetDefaultPatchBaseline,
ssm:RegisterDefaultPatchBaseline
```

