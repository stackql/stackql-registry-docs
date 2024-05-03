---
title: workspace
hide_title: false
hide_table_of_contents: false
keywords:
  - workspace
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

Gets or operates on an individual <code>workspace</code> resource, use <code>workspaces</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>workspace</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::IoTTwinMaker::Workspace</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.iottwinmaker.workspace" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="workspace_id" /></td><td><code>string</code></td><td>The ID of the workspace.</td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The ARN of the workspace.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>The description of the workspace.</td></tr>
<tr><td><CopyableCode code="role" /></td><td><code>string</code></td><td>The ARN of the execution role associated with the workspace.</td></tr>
<tr><td><CopyableCode code="s3_location" /></td><td><code>string</code></td><td>The ARN of the S3 bucket where resources associated with the workspace are stored.</td></tr>
<tr><td><CopyableCode code="creation_date_time" /></td><td><code>string</code></td><td>The date and time when the workspace was created.</td></tr>
<tr><td><CopyableCode code="update_date_time" /></td><td><code>string</code></td><td>The date and time of the current update.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>object</code></td><td>A map of key-value pairs to associate with a resource.</td></tr>
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
workspace_id,
arn,
description,
role,
s3_location,
creation_date_time,
update_date_time,
tags
FROM aws.iottwinmaker.workspace
WHERE data__Identifier = '<WorkspaceId>';
```

## Permissions

To operate on the <code>workspace</code> resource, the following permissions are required:

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

