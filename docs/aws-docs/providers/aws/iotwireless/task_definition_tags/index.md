---
title: task_definition_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - task_definition_tags
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
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Expands all tag keys and values for <code>task_definitions</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>task_definition_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Creates a gateway task definition.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.iotwireless.task_definition_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name of the new resource.</td></tr>
<tr><td><CopyableCode code="auto_create_tasks" /></td><td><code>boolean</code></td><td>Whether to automatically create tasks using this task definition for all gateways with the specified current version. If false, the task must me created by calling CreateWirelessGatewayTask.</td></tr>
<tr><td><CopyableCode code="update" /></td><td><code>object</code></td><td>Information about the gateways to update.</td></tr>
<tr><td><CopyableCode code="lo_ra_wan_update_gateway_task_entry" /></td><td><code>object</code></td><td>The list of task definitions.</td></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td>The ID of the new wireless gateway task definition</td></tr>
<tr><td><CopyableCode code="task_definition_type" /></td><td><code>string</code></td><td>A filter to list only the wireless gateway task definitions that use this task definition type</td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>TaskDefinition arn. Returned after successful create.</td></tr>
<tr><td><CopyableCode code="tag_key" /></td><td><code>string</code></td><td>Tag key.</td></tr>
<tr><td><CopyableCode code="tag_value" /></td><td><code>string</code></td><td>Tag value.</td></tr>
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
    <td><CopyableCode code="list_resources" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples
Expands tags for all <code>task_definitions</code> in a region.
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
tag_key,
tag_value
FROM aws.iotwireless.task_definition_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>task_definition_tags</code> resource, see <a href="/providers/aws/iotwireless/task_definitions/#permissions"><code>task_definitions</code></a>


