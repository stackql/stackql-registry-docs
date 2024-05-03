---
title: wal_workspaces
hide_title: false
hide_table_of_contents: false
keywords:
  - wal_workspaces
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

Used to retrieve a list of <code>wal_workspaces</code> in a region or create a <code>wal_workspaces</code> resource, use <code>wal_workspace</code> to operate on an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>wal_workspaces</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::EMR::WALWorkspace Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.emr.wal_workspaces" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="wal_workspace_name" /></td><td><code>string</code></td><td>The name of the emrwal container</td></tr>
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
wal_workspace_name
FROM aws.emr.wal_workspaces
WHERE region = 'us-east-1'
```

## Permissions

To operate on the <code>wal_workspaces</code> resource, the following permissions are required:

### Create
```json
emrwal:CreateWorkspace,
emrwal:TagResource,
iam:CreateServiceLinkedRole
```

### List
```json
emrwal:ListWorkspaces
```

