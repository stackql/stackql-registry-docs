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
Retrieves a list of <code>protection_groups</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>protection_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>protection_groups</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.shield.protection_groups</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>protection_group_arn</code></td><td><code>string</code></td><td>The ARN (Amazon Resource Name) of the protection group.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
protection_group_arn
FROM awscc.shield.protection_groups

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

