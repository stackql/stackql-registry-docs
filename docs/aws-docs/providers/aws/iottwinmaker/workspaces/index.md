---
title: workspaces
hide_title: false
hide_table_of_contents: false
keywords:
  - workspaces
  - iottwinmaker
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


Used to retrieve a list of <code>workspaces</code> in a region or to create or delete a <code>workspaces</code> resource, use <code>workspace</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>workspaces</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::IoTTwinMaker::Workspace</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.iottwinmaker.workspaces" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="workspace_id" /></td><td><code>string</code></td><td>The ID of the workspace.</td></tr>
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
workspace_id
FROM aws.iottwinmaker.workspaces
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
 "WorkspaceId": "{{ WorkspaceId }}",
 "Role": "{{ Role }}",
 "S3Location": "{{ S3Location }}"
}
>>>
--required properties only
INSERT INTO aws.iottwinmaker.workspaces (
 WorkspaceId,
 Role,
 S3Location,
 region
)
SELECT 
{{ .WorkspaceId }},
 {{ .Role }},
 {{ .S3Location }},
'us-east-1';
```
</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "WorkspaceId": "{{ WorkspaceId }}",
 "Description": "{{ Description }}",
 "Role": "{{ Role }}",
 "S3Location": "{{ S3Location }}",
 "Tags": {}
}
>>>
--all properties
INSERT INTO aws.iottwinmaker.workspaces (
 WorkspaceId,
 Description,
 Role,
 S3Location,
 Tags,
 region
)
SELECT 
 {{ .WorkspaceId }},
 {{ .Description }},
 {{ .Role }},
 {{ .S3Location }},
 {{ .Tags }},
 'us-east-1';
```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.iottwinmaker.workspaces
WHERE data__Identifier = '<WorkspaceId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>workspaces</code> resource, the following permissions are required:

### Create
```json
iam:PassRole,
iottwinmaker:CreateWorkspace,
iottwinmaker:GetWorkspace,
iottwinmaker:ListTagsForResource,
iottwinmaker:TagResource
```

### Delete
```json
iottwinmaker:DeleteWorkspace,
iottwinmaker:GetWorkspace
```

### List
```json
iottwinmaker:GetWorkspace,
iottwinmaker:ListTagsForResource,
iottwinmaker:ListWorkspaces
```

