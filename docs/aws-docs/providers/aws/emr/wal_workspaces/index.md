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
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';


Used to retrieve a list of <code>wal_workspaces</code> in a region or to create or delete a <code>wal_workspaces</code> resource, use <code>wal_workspace</code> to read or update an individual resource.

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
    <td><CopyableCode code="region" /></td>
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
wal_workspace_name
FROM aws.emr.wal_workspaces
WHERE region = 'us-east-1';
```

## `INSERT` Example

Use the following StackQL query and manifest file to create a new <code>wal_workspace</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

<Tabs
    defaultValue="required"
    values={[
      { label: 'Required Properties', value: 'required', },
      { label: 'All Properties', value: 'all', },
      { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="required">

```sql
/*+ create */
INSERT INTO aws.emr.wal_workspaces (
 WALWorkspaceName,
 Tags,
 region
)
SELECT 
'{{ WALWorkspaceName }}',
 '{{ Tags }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.emr.wal_workspaces (
 WALWorkspaceName,
 Tags,
 region
)
SELECT 
 '{{ WALWorkspaceName }}',
 '{{ Tags }}',
 '{{ region }}';
```
</TabItem>
<TabItem value="manifest">

```yaml
version: 1
name: stack name
description: stack description
providers:
  - aws
globals:
  - name: region
    value: '{{ vars.AWS_REGION }}'
resources:
  - name: wal_workspace
    props:
      - name: WALWorkspaceName
        value: '{{ WALWorkspaceName }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'

```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
/*+ delete */
DELETE FROM aws.emr.wal_workspaces
WHERE data__Identifier = '<WALWorkspaceName>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>wal_workspaces</code> resource, the following permissions are required:

### Create
```json
emrwal:CreateWorkspace,
emrwal:TagResource,
iam:CreateServiceLinkedRole
```

### Delete
```json
emrwal:DeleteWorkspace
```

### List
```json
emrwal:ListWorkspaces
```

