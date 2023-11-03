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
<tr><td><b>Id</b></td><td><code>aws.ecs.task_definition</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>TaskDefinitionArn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the Amazon ECS task definition</td></tr><tr><td><code>Family</code></td><td><code>string</code></td><td></td></tr><tr><td><code>ContainerDefinitions</code></td><td><code>array</code></td><td></td></tr><tr><td><code>Cpu</code></td><td><code>string</code></td><td></td></tr><tr><td><code>ExecutionRoleArn</code></td><td><code>string</code></td><td></td></tr><tr><td><code>EphemeralStorage</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>InferenceAccelerators</code></td><td><code>array</code></td><td></td></tr><tr><td><code>Memory</code></td><td><code>string</code></td><td></td></tr><tr><td><code>NetworkMode</code></td><td><code>string</code></td><td></td></tr><tr><td><code>PlacementConstraints</code></td><td><code>array</code></td><td></td></tr><tr><td><code>ProxyConfiguration</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>RequiresCompatibilities</code></td><td><code>array</code></td><td></td></tr><tr><td><code>TaskRoleArn</code></td><td><code>string</code></td><td></td></tr><tr><td><code>Volumes</code></td><td><code>array</code></td><td></td></tr><tr><td><code>PidMode</code></td><td><code>string</code></td><td></td></tr><tr><td><code>RuntimePlatform</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>IpcMode</code></td><td><code>string</code></td><td></td></tr><tr><td><code>Tags</code></td><td><code>array</code></td><td></td></tr>
</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.ecs.task_definition
WHERE region = 'us-east-1' AND data__Identifier = '{TaskDefinitionArn}'
</pre>
