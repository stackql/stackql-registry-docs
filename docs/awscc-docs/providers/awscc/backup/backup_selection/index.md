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
Gets an individual <code>backup_selection</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>backup_selection</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>backup_selection</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.backup.backup_selection</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>backup_plan_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>backup_selection</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>selection_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
id,
backup_plan_id,
backup_selection,
selection_id
FROM awscc.backup.backup_selection
WHERE region = 'us-east-1'
AND data__Identifier = '{Id}';
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

