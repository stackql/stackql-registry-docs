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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';

Gets or operates on an individual <code>wal_workspace</code> resource, use <code>wal_workspaces</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>wal_workspace</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::EMR::WALWorkspace Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.emr.wal_workspace" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="wal_workspace_name" /></td><td><code>string</code></td><td>The name of the emrwal container</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
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
wal_workspace_name,
tags
FROM aws.emr.wal_workspace
WHERE data__Identifier = '<WALWorkspaceName>';
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

