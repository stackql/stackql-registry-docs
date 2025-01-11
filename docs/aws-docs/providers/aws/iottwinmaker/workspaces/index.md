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

Creates, updates, deletes or gets a <code>workspace</code> resource or lists <code>workspaces</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>workspaces</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::IoTTwinMaker::Workspace</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.iottwinmaker.workspaces" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="workspace_id" /></td><td><code>string</code></td><td>The ID of the workspace.</td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The ARN of the workspace.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>The description of the workspace.</td></tr>
<tr><td><CopyableCode code="role" /></td><td><code>string</code></td><td>The ARN of the execution role associated with the workspace.</td></tr>
<tr><td><CopyableCode code="s3_location" /></td><td><code>string</code></td><td>The ARN of the S3 bucket where resources associated with the workspace are stored.</td></tr>
<tr><td><CopyableCode code="creation_date_time" /></td><td><code>string</code></td><td>The date and time when the workspace was created.</td></tr>
<tr><td><CopyableCode code="update_date_time" /></td><td><code>string</code></td><td>The date and time of the current update.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>object</code></td><td>A map of key-value pairs to associate with a resource.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iottwinmaker-workspace.html"><code>AWS::IoTTwinMaker::Workspace</code></a>.

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
    <td><CopyableCode code="WorkspaceId, Role, S3Location, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="update_resource" /></td>
    <td><code>UPDATE</code></td>
    <td><CopyableCode code="data__Identifier, data__PatchDocument, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="list_resources" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples
Gets all <code>workspaces</code> in a region.
```sql
SELECT
region,
workspace_id,
arn,
description,
role,
s3_location,
creation_date_time,
update_date_time,
tags
FROM aws.iottwinmaker.workspaces
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>workspace</code>.
```sql
SELECT
region,
workspace_id,
arn,
description,
role,
s3_location,
creation_date_time,
update_date_time,
tags
FROM aws.iottwinmaker.workspaces
WHERE region = 'us-east-1' AND data__Identifier = '<WorkspaceId>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>workspace</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.iottwinmaker.workspaces (
 WorkspaceId,
 Role,
 S3Location,
 region
)
SELECT 
'{{ WorkspaceId }}',
 '{{ Role }}',
 '{{ S3Location }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.iottwinmaker.workspaces (
 WorkspaceId,
 Description,
 Role,
 S3Location,
 Tags,
 region
)
SELECT 
 '{{ WorkspaceId }}',
 '{{ Description }}',
 '{{ Role }}',
 '{{ S3Location }}',
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
  - name: workspace
    props:
      - name: WorkspaceId
        value: '{{ WorkspaceId }}'
      - name: Description
        value: '{{ Description }}'
      - name: Role
        value: '{{ Role }}'
      - name: S3Location
        value: '{{ S3Location }}'
      - name: Tags
        value: {}

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
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

### Read
```json
iottwinmaker:GetWorkspace,
iottwinmaker:ListTagsForResource
```

### Update
```json
iottwinmaker:GetWorkspace,
iottwinmaker:ListTagsForResource,
iottwinmaker:TagResource,
iottwinmaker:UntagResource,
iottwinmaker:UpdateWorkspace
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
