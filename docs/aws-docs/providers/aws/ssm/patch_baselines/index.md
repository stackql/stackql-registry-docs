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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes or gets a <code>patch_baseline</code> resource or lists <code>patch_baselines</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>patch_baselines</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::SSM::PatchBaseline</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ssm.patch_baselines" /></td></tr>
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
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>Optional metadata that you assign to a resource. Tags enable you to categorize a resource in different ways.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-patchbaseline.html"><code>AWS::SSM::PatchBaseline</code></a>.

## Methods

<table><tbody>
  <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
  </tr>
  <tr>
    <td><CopyableCode code="create_resource" /></td>
    <td><code>INSERT</code></td>
    <td><CopyableCode code="Name, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="update_resource" /></td>
    <td><code>UPDATE</code></td>
    <td><CopyableCode code="data__Identifier, data__PatchDocument, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="list_resources" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples
Gets all <code>patch_baselines</code> in a region.
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
FROM aws.ssm.patch_baselines
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>patch_baseline</code>.
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
FROM aws.ssm.patch_baselines
WHERE region = 'us-east-1' AND data__Identifier = '<Id>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>patch_baseline</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

<Tabs
    defaultValue="required"
    values={[
      { label: 'Required Properties', value: 'required', },
      { label: 'All Properties', value: 'all', },
      { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="required">

```sql
/*+ create */
INSERT INTO aws.ssm.patch_baselines (
 Name,
 region
)
SELECT 
'{{ Name }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.ssm.patch_baselines (
 DefaultBaseline,
 OperatingSystem,
 Description,
 ApprovalRules,
 Sources,
 Name,
 RejectedPatches,
 ApprovedPatches,
 RejectedPatchesAction,
 PatchGroups,
 ApprovedPatchesComplianceLevel,
 ApprovedPatchesEnableNonSecurity,
 GlobalFilters,
 Tags,
 region
)
SELECT 
 '{{ DefaultBaseline }}',
 '{{ OperatingSystem }}',
 '{{ Description }}',
 '{{ ApprovalRules }}',
 '{{ Sources }}',
 '{{ Name }}',
 '{{ RejectedPatches }}',
 '{{ ApprovedPatches }}',
 '{{ RejectedPatchesAction }}',
 '{{ PatchGroups }}',
 '{{ ApprovedPatchesComplianceLevel }}',
 '{{ ApprovedPatchesEnableNonSecurity }}',
 '{{ GlobalFilters }}',
 '{{ Tags }}',
 '{{ region }}';
```
</TabItem>
<TabItem value="manifest">

```yaml
version: 1
name: stack name
description: stack description
providers:
  - aws
globals:
  - name: region
    value: '{{ vars.AWS_REGION }}'
resources:
  - name: patch_baseline
    props:
      - name: DefaultBaseline
        value: '{{ DefaultBaseline }}'
      - name: OperatingSystem
        value: '{{ OperatingSystem }}'
      - name: Description
        value: '{{ Description }}'
      - name: ApprovalRules
        value:
          PatchRules:
            - ApproveUntilDate: '{{ ApproveUntilDate }}'
              EnableNonSecurity: '{{ EnableNonSecurity }}'
              PatchFilterGroup:
                PatchFilters:
                  - Values:
                      - '{{ Values[0] }}'
                    Key: '{{ Key }}'
              ApproveAfterDays: '{{ ApproveAfterDays }}'
              ComplianceLevel: '{{ ComplianceLevel }}'
      - name: Sources
        value:
          - Products:
              - '{{ Products[0] }}'
            Configuration: '{{ Configuration }}'
            Name: '{{ Name }}'
      - name: Name
        value: '{{ Name }}'
      - name: RejectedPatches
        value:
          - '{{ RejectedPatches[0] }}'
      - name: ApprovedPatches
        value:
          - '{{ ApprovedPatches[0] }}'
      - name: RejectedPatchesAction
        value: '{{ RejectedPatchesAction }}'
      - name: PatchGroups
        value:
          - '{{ PatchGroups[0] }}'
      - name: ApprovedPatchesComplianceLevel
        value: '{{ ApprovedPatchesComplianceLevel }}'
      - name: ApprovedPatchesEnableNonSecurity
        value: '{{ ApprovedPatchesEnableNonSecurity }}'
      - name: GlobalFilters
        value: null
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.ssm.patch_baselines
WHERE data__Identifier = '<Id>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>patch_baselines</code> resource, the following permissions are required:

### Create
```json
ssm:CreatePatchBaseline,
ssm:RegisterPatchBaselineForPatchGroup,
ssm:AddTagsToResource,
ssm:RemoveTagsFromResource,
ssm:ListTagsForResource,
ssm:GetDefaultPatchBaseline,
ssm:RegisterDefaultPatchBaseline
```

### Delete
```json
ssm:DeletePatchBaseline,
ssm:GetPatchBaseline,
ssm:DeregisterPatchBaselineForPatchGroup
```

### List
```json
ssm:DescribePatchBaselines,
ssm:GetDefaultPatchBaseline,
ssm:GetPatchBaseline,
ssm:ListTagsForResource
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
