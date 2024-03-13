---
title: wal_workspace
hide_title: false
hide_table_of_contents: false
keywords:
  - wal_workspace
  - emr
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>wal_workspace</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>wal_workspace</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>wal_workspace</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.emr.wal_workspace</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>wal_workspace_name</code></td><td><code>string</code></td><td>The name of the emrwal container</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
wal_workspace_name,
tags
FROM awscc.emr.wal_workspace
WHERE region = 'us-east-1'
AND data__Identifier = '{WALWorkspaceName}';
```

## Permissions

To operate on the <code>wal_workspace</code> resource, the following permissions are required:

### Read
```json
emrwal:ListTagsForResource
```

### Delete
```json
emrwal:DeleteWorkspace
```

### Update
```json
emrwal:TagResource,
emrwal:UntagResource,
emrwal:ListTagsForResource
```

