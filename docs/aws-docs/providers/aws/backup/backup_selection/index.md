---
title: backup_selection
hide_title: false
hide_table_of_contents: false
keywords:
  - backup_selection
  - backup
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

Gets or operates on an individual <code>backup_selection</code> resource, use <code>backup_selections</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>backup_selection</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::Backup::BackupSelection</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.backup.backup_selection" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="backup_plan_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="backup_selection" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="selection_id" /></td><td><code>string</code></td><td></td></tr>
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
id,
backup_plan_id,
backup_selection,
selection_id
FROM aws.backup.backup_selection
WHERE data__Identifier = '<Id>';
```

## Permissions

To operate on the <code>backup_selection</code> resource, the following permissions are required:

### Delete
```json
backup:GetBackupSelection,
backup:DeleteBackupSelection
```

### Read
```json
backup:GetBackupSelection
```

