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
Gets an individual <code>recovery_group</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>recovery_group</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>recovery_group</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.route53recoveryreadiness.recovery_group</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>recovery_group_name</code></td><td><code>string</code></td><td>The name of the recovery group to create.</td></tr>
<tr><td><code>cells</code></td><td><code>array</code></td><td>A list of the cell Amazon Resource Names (ARNs) in the recovery group.</td></tr>
<tr><td><code>recovery_group_arn</code></td><td><code>string</code></td><td>A collection of tags associated with a resource.</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>A collection of tags associated with a resource.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
recovery_group_name,
cells,
recovery_group_arn,
tags
FROM awscc.route53recoveryreadiness.recovery_group
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

