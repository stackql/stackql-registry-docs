---
title: task_definition
hide_title: false
hide_table_of_contents: false
keywords:
  - task_definition
  - iotwireless
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>task_definition</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>task_definition</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>task_definition</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.iotwireless.task_definition</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td>The name of the new resource.</td></tr>
<tr><td><code>auto_create_tasks</code></td><td><code>boolean</code></td><td>Whether to automatically create tasks using this task definition for all gateways with the specified current version. If false, the task must me created by calling CreateWirelessGatewayTask.</td></tr>
<tr><td><code>update</code></td><td><code>object</code></td><td>Information about the gateways to update.</td></tr>
<tr><td><code>lo_ra_wan_update_gateway_task_entry</code></td><td><code>object</code></td><td>The list of task definitions.</td></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td>The ID of the new wireless gateway task definition</td></tr>
<tr><td><code>task_definition_type</code></td><td><code>string</code></td><td>A filter to list only the wireless gateway task definitions that use this task definition type</td></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td>TaskDefinition arn. Returned after successful create.</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>A list of key-value pairs that contain metadata for the destination.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
name,
auto_create_tasks,
update,
lo_ra_wan_update_gateway_task_entry,
id,
task_definition_type,
arn,
tags
FROM awscc.iotwireless.task_definition
WHERE data__Identifier = '<Id>';
```

## Permissions

To operate on the <code>task_definition</code> resource, the following permissions are required:

### Read
```json
iotwireless:GetWirelessGatewayTaskDefinition,
iotwireless:ListTagsForResource
```

### Delete
```json
iotwireless:DeleteWirelessGatewayTaskDefinition
```

