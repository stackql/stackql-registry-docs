---
title: sync_job
hide_title: false
hide_table_of_contents: false
keywords:
  - sync_job
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
Gets an individual <code>sync_job</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>sync_job</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::IoTTwinMaker::SyncJob</td></tr>
<tr><td><b>Id</b></td><td><code>aws.iottwinmaker.sync_job</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>workspace_id</code></td><td><code>string</code></td><td>The ID of the workspace.</td></tr>
<tr><td><code>sync_source</code></td><td><code>string</code></td><td>The source of the SyncJob.</td></tr>
<tr><td><code>sync_role</code></td><td><code>string</code></td><td>The IAM Role that execute SyncJob.</td></tr>
<tr><td><code>creation_date_time</code></td><td><code>string</code></td><td>The date and time when the sync job was created.</td></tr>
<tr><td><code>update_date_time</code></td><td><code>string</code></td><td>The date and time when the sync job was updated.</td></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td>The ARN of the SyncJob.</td></tr>
<tr><td><code>state</code></td><td><code>string</code></td><td>The state of SyncJob.</td></tr>
<tr><td><code>tags</code></td><td><code>object</code></td><td>A key-value pair to associate with a resource.</td></tr>
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
    <td><code>delete_resource</code></td>
    <td><code>DELETE</code></td>
    <td><code>data__Identifier, region</code></td>
  </tr>
  <tr>
    <td><code>get_resource</code></td>
    <td><code>SELECT</code></td>
    <td><code>data__Identifier, region</code></td>
  </tr>
</tbody></table>

## `SELECT` Example
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
FROM aws.iottwinmaker.sync_job
WHERE data__Identifier = '<WorkspaceId>|<SyncSource>';
```

## Permissions

To operate on the <code>sync_job</code> resource, the following permissions are required:

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

