---
title: patch_baseline_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - patch_baseline_tags
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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Expands all tag keys and values for <code>patch_baselines</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>patch_baseline_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::SSM::PatchBaseline</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ssm.patch_baseline_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td>The ID of the patch baseline.</td></tr>
<tr><td><CopyableCode code="default_baseline" /></td><td><code>boolean</code></td><td>Set the baseline as default baseline. Only registering to default patch baseline is allowed.</td></tr>
<tr><td><CopyableCode code="operating_system" /></td><td><code>string</code></td><td>Defines the operating system the patch baseline applies to. The Default value is WINDOWS.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>The description of the patch baseline.</td></tr>
<tr><td><CopyableCode code="approval_rules" /></td><td><code>object</code></td><td>A set of rules defining the approval rules for a patch baseline.</td></tr>
<tr><td><CopyableCode code="sources" /></td><td><code>array</code></td><td>Information about the patches to use to update the instances, including target operating systems and source repository. Applies to Linux instances only.</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name of the patch baseline.</td></tr>
<tr><td><CopyableCode code="rejected_patches" /></td><td><code>array</code></td><td>A list of explicitly rejected patches for the baseline.</td></tr>
<tr><td><CopyableCode code="approved_patches" /></td><td><code>array</code></td><td>A list of explicitly approved patches for the baseline.</td></tr>
<tr><td><CopyableCode code="rejected_patches_action" /></td><td><code>string</code></td><td>The action for Patch Manager to take on patches included in the RejectedPackages list.</td></tr>
<tr><td><CopyableCode code="patch_groups" /></td><td><code>array</code></td><td>PatchGroups is used to associate instances with a specific patch baseline</td></tr>
<tr><td><CopyableCode code="approved_patches_compliance_level" /></td><td><code>string</code></td><td>Defines the compliance level for approved patches. This means that if an approved patch is reported as missing, this is the severity of the compliance violation. The default value is UNSPECIFIED.</td></tr>
<tr><td><CopyableCode code="approved_patches_enable_non_security" /></td><td><code>boolean</code></td><td>Indicates whether the list of approved patches includes non-security updates that should be applied to the instances. The default value is 'false'. Applies to Linux instances only.</td></tr>
<tr><td><CopyableCode code="global_filters" /></td><td><code>object</code></td><td>A set of global filters used to include patches in the baseline.</td></tr>
<tr><td><CopyableCode code="tag_key" /></td><td><code>string</code></td><td>Tag key.</td></tr>
<tr><td><CopyableCode code="tag_value" /></td><td><code>string</code></td><td>Tag value.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

## Methods

<table><tbody>
  <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
  </tr>
  <tr>
    <td><CopyableCode code="list_resources" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples
Expands tags for all <code>patch_baselines</code> in a region.
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
tag_key,
tag_value
FROM aws.ssm.patch_baseline_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>patch_baseline_tags</code> resource, see <a href="/providers/aws/ssm/patch_baselines/#permissions"><code>patch_baselines</code></a>


