---
title: protection_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - protection_groups
  - shield
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

Used to retrieve a list of <code>protection_groups</code> in a region or create a <code>protection_groups</code> resource, use <code>protection_group</code> to operate on an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>protection_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>A grouping of protected resources so they can be handled as a collective. This resource grouping improves the accuracy of detection and reduces false positives.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.shield.protection_groups" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="protection_group_arn" /></td><td><code>string</code></td><td>The ARN (Amazon Resource Name) of the protection group.</td></tr>
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
    <td><CopyableCode code="list_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
protection_group_arn
FROM aws.shield.protection_groups

```

## Permissions

To operate on the <code>protection_groups</code> resource, the following permissions are required:

### Create
```json
shield:CreateProtectionGroup,
shield:TagResource
```

### List
```json
shield:ListProtectionGroups
```
