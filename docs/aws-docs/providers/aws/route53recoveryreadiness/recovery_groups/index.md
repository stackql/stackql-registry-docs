---
title: recovery_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - recovery_groups
  - route53recoveryreadiness
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

Creates, updates, deletes or gets a <code>recovery_group</code> resource or lists <code>recovery_groups</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>recovery_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>AWS Route53 Recovery Readiness Recovery Group Schema and API specifications.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.route53recoveryreadiness.recovery_groups" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="recovery_group_name" /></td><td><code>string</code></td><td>The name of the recovery group to create.</td></tr>
<tr><td><CopyableCode code="cells" /></td><td><code>array</code></td><td>A list of the cell Amazon Resource Names (ARNs) in the recovery group.</td></tr>
<tr><td><CopyableCode code="recovery_group_arn" /></td><td><code>string</code></td><td>A collection of tags associated with a resource.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>A collection of tags associated with a resource.</td></tr>
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
    <td><CopyableCode code="region" /></td>
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
Gets all <code>recovery_groups</code> in a region.
```sql
SELECT
region,
recovery_group_name,
cells,
recovery_group_arn,
tags
FROM aws.route53recoveryreadiness.recovery_groups
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>recovery_group</code>.
```sql
SELECT
region,
recovery_group_name,
cells,
recovery_group_arn,
tags
FROM aws.route53recoveryreadiness.recovery_groups
WHERE region = 'us-east-1' AND data__Identifier = '<RecoveryGroupName>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>recovery_group</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.route53recoveryreadiness.recovery_groups (
 RecoveryGroupName,
 Cells,
 Tags,
 region
)
SELECT 
'{{ RecoveryGroupName }}',
 '{{ Cells }}',
 '{{ Tags }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.route53recoveryreadiness.recovery_groups (
 RecoveryGroupName,
 Cells,
 Tags,
 region
)
SELECT 
 '{{ RecoveryGroupName }}',
 '{{ Cells }}',
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
  - name: recovery_group
    props:
      - name: RecoveryGroupName
        value: '{{ RecoveryGroupName }}'
      - name: Cells
        value:
          - '{{ Cells[0] }}'
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
DELETE FROM aws.route53recoveryreadiness.recovery_groups
WHERE data__Identifier = '<RecoveryGroupName>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>recovery_groups</code> resource, the following permissions are required:

### Create
```json
route53-recovery-readiness:CreateRecoveryGroup,
route53-recovery-readiness:GetRecoveryGroup,
route53-recovery-readiness:GetCell,
route53-recovery-readiness:ListTagsForResources,
route53-recovery-readiness:TagResource
```

### Read
```json
route53-recovery-readiness:GetRecoveryGroup,
route53-recovery-readiness:ListTagsForResources
```

### Update
```json
route53-recovery-readiness:UpdateRecoveryGroup,
route53-recovery-readiness:GetRecoveryGroup,
route53-recovery-readiness:GetCell,
route53-recovery-readiness:ListTagsForResources,
route53-recovery-readiness:TagResource,
route53-recovery-readiness:UntagResource
```

### Delete
```json
route53-recovery-readiness:DeleteRecoveryGroup,
route53-recovery-readiness:GetRecoveryGroup
```

### List
```json
route53-recovery-readiness:ListRecoveryGroups
```

