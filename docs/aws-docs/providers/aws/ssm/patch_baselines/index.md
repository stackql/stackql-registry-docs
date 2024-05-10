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


Used to retrieve a list of <code>patch_baselines</code> in a region or to create or delete a <code>patch_baselines</code> resource, use <code>patch_baseline</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>patch_baselines</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::SSM::PatchBaseline</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ssm.patch_baselines" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td>The ID of the patch baseline.</td></tr>
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
    <td><CopyableCode code="create_resource" /></td>
    <td><code>INSERT</code></td>
    <td><CopyableCode code="data__DesiredState, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="list_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
id
FROM aws.ssm.patch_baselines
WHERE region = 'us-east-1';
```

## `INSERT` Example

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
-- patch_baseline.iql (required properties only)
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
-- patch_baseline.iql (all properties)
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

## `DELETE` Example

```sql
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

