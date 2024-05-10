---
title: sync_jobs
hide_title: false
hide_table_of_contents: false
keywords:
  - sync_jobs
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


Used to retrieve a list of <code>sync_jobs</code> in a region or to create or delete a <code>sync_jobs</code> resource, use <code>sync_job</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>sync_jobs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::IoTTwinMaker::SyncJob</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.iottwinmaker.sync_jobs" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="workspace_id" /></td><td><code>string</code></td><td>The ID of the workspace.</td></tr>
<tr><td><CopyableCode code="sync_source" /></td><td><code>string</code></td><td>The source of the SyncJob.</td></tr>
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
workspace_id,
sync_source
FROM aws.iottwinmaker.sync_jobs
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
 "SyncSource": "{{ SyncSource }}",
 "SyncRole": "{{ SyncRole }}"
}
>>>
--required properties only
INSERT INTO aws.iottwinmaker.sync_jobs (
 WorkspaceId,
 SyncSource,
 SyncRole,
 region
)
SELECT 
{{ .WorkspaceId }},
 {{ .SyncSource }},
 {{ .SyncRole }},
'us-east-1';
```
</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "WorkspaceId": "{{ WorkspaceId }}",
 "SyncSource": "{{ SyncSource }}",
 "SyncRole": "{{ SyncRole }}",
 "Tags": {}
}
>>>
--all properties
INSERT INTO aws.iottwinmaker.sync_jobs (
 WorkspaceId,
 SyncSource,
 SyncRole,
 Tags,
 region
)
SELECT 
 {{ .WorkspaceId }},
 {{ .SyncSource }},
 {{ .SyncRole }},
 {{ .Tags }},
 'us-east-1';
```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.iottwinmaker.sync_jobs
WHERE data__Identifier = '<WorkspaceId|SyncSource>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>sync_jobs</code> resource, the following permissions are required:

### Create
```json
iam:PassRole,
iottwinmaker:CreateSyncJob,
iottwinmaker:GetSyncJob,
iottwinmaker:GetWorkspace,
iottwinmaker:ListTagsForResource,
iottwinmaker:TagResource
```

### Delete
```json
iottwinmaker:DeleteSyncJob,
iottwinmaker:GetSyncJob,
iottwinmaker:GetWorkspace
```

### List
```json
iottwinmaker:GetWorkspace,
iottwinmaker:ListSyncJobs,
iottwinmaker:ListTagsForResource
```

