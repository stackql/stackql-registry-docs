---
title: queue
hide_title: false
hide_table_of_contents: false
keywords:
  - queue
  - deadline
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>queue</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>queue</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::Deadline::Queue Resource Type</td></tr>
<tr><td><b>Id</b></td><td><code>aws.deadline.queue</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>allowed_storage_profile_ids</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>default_budget_action</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>display_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>farm_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>job_attachment_settings</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>job_run_as_user</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>queue_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>required_file_system_location_names</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>role_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td></td></tr>
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
    <td><code>update_resource</code></td>
    <td><code>UPDATE</code></td>
    <td><code>data__Identifier, data__PatchDocument, region</code></td>
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
allowed_storage_profile_ids,
default_budget_action,
description,
display_name,
farm_id,
job_attachment_settings,
job_run_as_user,
queue_id,
required_file_system_location_names,
role_arn,
arn
FROM aws.deadline.queue
WHERE data__Identifier = '<Arn>';
```

## Permissions

To operate on the <code>queue</code> resource, the following permissions are required:

### Read
```json
deadline:GetQueue,
identitystore:ListGroupMembershipsForMember
```

### Update
```json
deadline:UpdateQueue,
deadline:GetQueue,
iam:PassRole,
identitystore:ListGroupMembershipsForMember,
logs:CreateLogGroup,
s3:ListBucket
```

### Delete
```json
deadline:DeleteQueue,
deadline:GetQueue,
identitystore:ListGroupMembershipsForMember
```

