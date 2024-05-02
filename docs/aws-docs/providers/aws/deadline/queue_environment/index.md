---
title: queue_environment
hide_title: false
hide_table_of_contents: false
keywords:
  - queue_environment
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
Gets an individual <code>queue_environment</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>queue_environment</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::Deadline::QueueEnvironment Resource Type</td></tr>
<tr><td><b>Id</b></td><td><code>aws.deadline.queue_environment</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>farm_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>priority</code></td><td><code>integer</code></td><td></td></tr>
<tr><td><code>queue_environment_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>queue_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>template</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>template_type</code></td><td><code>string</code></td><td></td></tr>
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
farm_id,
name,
priority,
queue_environment_id,
queue_id,
template,
template_type
FROM aws.deadline.queue_environment
WHERE data__Identifier = '<FarmId>|<QueueId>|<QueueEnvironmentId>';
```

## Permissions

To operate on the <code>queue_environment</code> resource, the following permissions are required:

### Read
```json
deadline:GetQueueEnvironment,
identitystore:ListGroupMembershipsForMember
```

### Update
```json
deadline:UpdateQueueEnvironment,
identitystore:ListGroupMembershipsForMember
```

### Delete
```json
deadline:DeleteQueueEnvironment,
deadline:GetQueueEnvironment,
identitystore:ListGroupMembershipsForMember
```

