---
title: recovery_group
hide_title: false
hide_table_of_contents: false
keywords:
  - recovery_group
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

Gets or operates on an individual <code>recovery_group</code> resource, use <code>recovery_groups</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>recovery_group</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>AWS Route53 Recovery Readiness Recovery Group Schema and API specifications.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.route53recoveryreadiness.recovery_group" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="recovery_group_name" /></td><td><code>string</code></td><td>The name of the recovery group to create.</td></tr>
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
    <td><CopyableCode code="update_resource" /></td>
    <td><code>UPDATE</code></td>
    <td><CopyableCode code="data__Identifier, data__PatchDocument, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
recovery_group_name,
cells,
recovery_group_arn,
tags
FROM aws.route53recoveryreadiness.recovery_group
WHERE data__Identifier = '<RecoveryGroupName>';
```

## Permissions

To operate on the <code>recovery_group</code> resource, the following permissions are required:

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

