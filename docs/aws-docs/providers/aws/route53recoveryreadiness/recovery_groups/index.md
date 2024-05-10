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


Used to retrieve a list of <code>recovery_groups</code> in a region or to create or delete a <code>recovery_groups</code> resource, use <code>recovery_group</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>recovery_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>AWS Route53 Recovery Readiness Recovery Group Schema and API specifications.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.route53recoveryreadiness.recovery_groups" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="recovery_group_name" /></td><td><code>string</code></td><td>The name of the recovery group to create.</td></tr>
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
recovery_group_name
FROM aws.route53recoveryreadiness.recovery_groups
WHERE region = 'us-east-1';
```

## `INSERT` Example

<Tabs
    defaultValue="required"
    values={[
      { label: 'Required Properties', value: 'required', },
      { label: 'All Properties', value: 'all', },
    ]
}>
<TabItem value="required">

```sql
<<<json
{
 "RecoveryGroupName": "{{ RecoveryGroupName }}",
 "Cells": [
  "{{ Cells[0] }}"
 ],
 "Tags": [
  {
   "Key": "{{ Key }}",
   "Value": "{{ Value }}"
  }
 ]
}
>>>
--required properties only
INSERT INTO aws.route53recoveryreadiness.recovery_groups (
 RecoveryGroupName,
 Cells,
 Tags,
 region
)
SELECT 
{{ .RecoveryGroupName }},
 {{ .Cells }},
 {{ .Tags }},
'us-east-1';
```
</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "RecoveryGroupName": "{{ RecoveryGroupName }}",
 "Cells": [
  "{{ Cells[0] }}"
 ],
 "Tags": [
  {
   "Key": "{{ Key }}",
   "Value": "{{ Value }}"
  }
 ]
}
>>>
--all properties
INSERT INTO aws.route53recoveryreadiness.recovery_groups (
 RecoveryGroupName,
 Cells,
 Tags,
 region
)
SELECT 
 {{ .RecoveryGroupName }},
 {{ .Cells }},
 {{ .Tags }},
 'us-east-1';
```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
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

### Delete
```json
route53-recovery-readiness:DeleteRecoveryGroup,
route53-recovery-readiness:GetRecoveryGroup
```

### List
```json
route53-recovery-readiness:ListRecoveryGroups
```

