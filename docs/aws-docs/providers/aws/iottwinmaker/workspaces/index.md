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
Retrieves a list of <code>workspaces</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>workspaces</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::IoTTwinMaker::Workspace</td></tr>
<tr><td><b>Id</b></td><td><code>aws.iottwinmaker.workspaces</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>workspace_id</code></td><td><code>string</code></td><td>The ID of the workspace.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods

<table><tbody>
  <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
  </tr>
  <tr>
    <td><code>create_resource</code></td>
    <td><code>INSERT</code></td>
    <td><code>data__DesiredState, region</code></td>
  </tr>
  <tr>
    <td><code>list_resource</code></td>
    <td><code>SELECT</code></td>
    <td><code>region</code></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
workspace_id
FROM aws.iottwinmaker.workspaces
WHERE region = 'us-east-1'
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

### List
```json
iottwinmaker:GetWorkspace,
iottwinmaker:ListTagsForResource,
iottwinmaker:ListWorkspaces
```

