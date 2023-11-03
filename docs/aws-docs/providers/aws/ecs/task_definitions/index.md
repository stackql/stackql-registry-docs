---
title: task_definitions
hide_title: false
hide_table_of_contents: false
keywords:
  - task_definitions
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
Retrieves a list of <code>task_definitions</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>task_definitions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ecs.task_definitions</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>TaskDefinitionArn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the Amazon ECS task definition</td></tr><tr><td><code>Family</code></td><td><code>string</code></td><td></td></tr><tr><td><code>ContainerDefinitions</code></td><td><code>array</code></td><td></td></tr><tr><td><code>Cpu</code></td><td><code>string</code></td><td></td></tr><tr><td><code>ExecutionRoleArn</code></td><td><code>string</code></td><td></td></tr><tr><td><code>EphemeralStorage</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>InferenceAccelerators</code></td><td><code>array</code></td><td></td></tr><tr><td><code>Memory</code></td><td><code>string</code></td><td></td></tr><tr><td><code>NetworkMode</code></td><td><code>string</code></td><td></td></tr><tr><td><code>PlacementConstraints</code></td><td><code>array</code></td><td></td></tr><tr><td><code>ProxyConfiguration</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>RequiresCompatibilities</code></td><td><code>array</code></td><td></td></tr><tr><td><code>TaskRoleArn</code></td><td><code>string</code></td><td></td></tr><tr><td><code>Volumes</code></td><td><code>array</code></td><td></td></tr><tr><td><code>PidMode</code></td><td><code>string</code></td><td></td></tr><tr><td><code>RuntimePlatform</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>IpcMode</code></td><td><code>string</code></td><td></td></tr><tr><td><code>Tags</code></td><td><code>array</code></td><td></td></tr>
</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT * 
FROM aws.ecs.task_definitions
WHERE region = 'us-east-1'
```
