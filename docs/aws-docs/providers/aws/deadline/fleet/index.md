---
title: fleet
hide_title: false
hide_table_of_contents: false
keywords:
  - fleet
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
Gets an individual <code>fleet</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>fleet</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::Deadline::Fleet Resource Type</td></tr>
<tr><td><b>Id</b></td><td><code>aws.deadline.fleet</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>capabilities</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>configuration</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>display_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>farm_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>fleet_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>max_worker_count</code></td><td><code>integer</code></td><td></td></tr>
<tr><td><code>min_worker_count</code></td><td><code>integer</code></td><td></td></tr>
<tr><td><code>role_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>status</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>worker_count</code></td><td><code>integer</code></td><td></td></tr>
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
capabilities,
configuration,
description,
display_name,
farm_id,
fleet_id,
max_worker_count,
min_worker_count,
role_arn,
status,
worker_count,
arn
FROM aws.deadline.fleet
WHERE data__Identifier = '<Arn>';
```

## Permissions

To operate on the <code>fleet</code> resource, the following permissions are required:

### Read
```json
deadline:GetFleet,
identitystore:ListGroupMembershipsForMember
```

### Update
```json
deadline:UpdateFleet,
deadline:GetFleet,
iam:PassRole,
identitystore:ListGroupMembershipsForMember
```

### Delete
```json
deadline:DeleteFleet,
deadline:GetFleet,
identitystore:ListGroupMembershipsForMember
```

