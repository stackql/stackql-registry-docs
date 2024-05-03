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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';

Gets or operates on an individual <code>task_definition</code> resource, use <code>task_definitions</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>task_definition</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Creates a gateway task definition.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.iotwireless.task_definition" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name of the new resource.</td></tr>
<tr><td><CopyableCode code="auto_create_tasks" /></td><td><code>boolean</code></td><td>Whether to automatically create tasks using this task definition for all gateways with the specified current version. If false, the task must me created by calling CreateWirelessGatewayTask.</td></tr>
<tr><td><CopyableCode code="update" /></td><td><code>object</code></td><td>Information about the gateways to update.</td></tr>
<tr><td><CopyableCode code="lo_ra_wan_update_gateway_task_entry" /></td><td><code>object</code></td><td>The list of task definitions.</td></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td>The ID of the new wireless gateway task definition</td></tr>
<tr><td><CopyableCode code="task_definition_type" /></td><td><code>string</code></td><td>A filter to list only the wireless gateway task definitions that use this task definition type</td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>TaskDefinition arn. Returned after successful create.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>A list of key-value pairs that contain metadata for the destination.</td></tr>
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
name,
auto_create_tasks,
update,
lo_ra_wan_update_gateway_task_entry,
id,
task_definition_type,
arn,
tags
FROM aws.iotwireless.task_definition
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

