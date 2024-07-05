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

Creates, updates, deletes or gets a <code>sync_job</code> resource or lists <code>sync_jobs</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>sync_jobs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::IoTTwinMaker::SyncJob</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.iottwinmaker.sync_jobs" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="workspace_id" /></td><td><code>string</code></td><td>The ID of the workspace.</td></tr>
<tr><td><CopyableCode code="sync_source" /></td><td><code>string</code></td><td>The source of the SyncJob.</td></tr>
<tr><td><CopyableCode code="sync_role" /></td><td><code>string</code></td><td>The IAM Role that execute SyncJob.</td></tr>
<tr><td><CopyableCode code="creation_date_time" /></td><td><code>string</code></td><td>The date and time when the sync job was created.</td></tr>
<tr><td><CopyableCode code="update_date_time" /></td><td><code>string</code></td><td>The date and time when the sync job was updated.</td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The ARN of the SyncJob.</td></tr>
<tr><td><CopyableCode code="state" /></td><td><code>string</code></td><td>The state of SyncJob.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>object</code></td><td>A key-value pair to associate with a resource.</td></tr>
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
    <td><CopyableCode code="WorkspaceId, SyncSource, SyncRole, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
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
Gets all <code>sync_jobs</code> in a region.
```sql
SELECT
region,
workspace_id,
sync_source,
sync_role,
creation_date_time,
update_date_time,
arn,
state,
tags
FROM aws.iottwinmaker.sync_jobs
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>sync_job</code>.
```sql
SELECT
region,
workspace_id,
sync_source,
sync_role,
creation_date_time,
update_date_time,
arn,
state,
tags
FROM aws.iottwinmaker.sync_jobs
WHERE region = 'us-east-1' AND data__Identifier = '<WorkspaceId>|<SyncSource>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>sync_job</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.iottwinmaker.sync_jobs (
 WorkspaceId,
 SyncSource,
 SyncRole,
 region
)
SELECT 
'{{ WorkspaceId }}',
 '{{ SyncSource }}',
 '{{ SyncRole }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.iottwinmaker.sync_jobs (
 WorkspaceId,
 SyncSource,
 SyncRole,
 Tags,
 region
)
SELECT 
 '{{ WorkspaceId }}',
 '{{ SyncSource }}',
 '{{ SyncRole }}',
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
  - name: sync_job
    props:
      - name: WorkspaceId
        value: '{{ WorkspaceId }}'
      - name: SyncSource
        value: '{{ SyncSource }}'
      - name: SyncRole
        value: '{{ SyncRole }}'
      - name: Tags
        value: {}

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
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

### Read
```json
iottwinmaker:GetSyncJob,
iottwinmaker:GetWorkspace,
iottwinmaker:ListTagsForResource
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

