---
title: task_definition
hide_title: false
hide_table_of_contents: false
keywords:
  - task_definition
  - ecs
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
<tr><td><b>Id</b></td><td><code>aws.ecs.task_definition</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>task_definition_arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the Amazon ECS task definition</td></tr>
<tr><td><code>family</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>container_definitions</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>cpu</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>execution_role_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>ephemeral_storage</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>inference_accelerators</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>memory</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>network_mode</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>placement_constraints</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>proxy_configuration</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>requires_compatibilities</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>task_role_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>volumes</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>pid_mode</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>runtime_platform</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>ipc_mode</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
task_definition_arn,
family,
container_definitions,
cpu,
execution_role_arn,
ephemeral_storage,
inference_accelerators,
memory,
network_mode,
placement_constraints,
proxy_configuration,
requires_compatibilities,
task_role_arn,
volumes,
pid_mode,
runtime_platform,
ipc_mode,
tags
FROM aws.ecs.task_definition
WHERE region = 'us-east-1'
AND data__Identifier = '<TaskDefinitionArn>'
```
