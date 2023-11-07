---
title: task_set
hide_title: false
hide_table_of_contents: false
keywords:
  - task_set
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
Gets an individual <code>task_set</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>task_set</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>task_set</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ecs.task_set</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>Cluster</code></td><td><code>string</code></td><td>The short name or full Amazon Resource Name (ARN) of the cluster that hosts the service to create the task set in.</td></tr>
<tr><td><code>ExternalId</code></td><td><code>string</code></td><td>An optional non-unique tag that identifies this task set in external systems. If the task set is associated with a service discovery registry, the tasks in this task set will have the ECS_TASK_SET_EXTERNAL_ID AWS Cloud Map attribute set to the provided value. </td></tr>
<tr><td><code>Id</code></td><td><code>string</code></td><td>The ID of the task set.</td></tr>
<tr><td><code>LaunchType</code></td><td><code>string</code></td><td>The launch type that new tasks in the task set will use. For more information, see https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;AmazonECS&#x2F;latest&#x2F;developerguide&#x2F;launch_types.html in the Amazon Elastic Container Service Developer Guide. </td></tr>
<tr><td><code>LoadBalancers</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>NetworkConfiguration</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>PlatformVersion</code></td><td><code>string</code></td><td>The platform version that the tasks in the task set should use. A platform version is specified only for tasks using the Fargate launch type. If one isn't specified, the LATEST platform version is used by default.</td></tr>
<tr><td><code>Scale</code></td><td><code>undefined</code></td><td>A floating-point percentage of the desired number of tasks to place and keep running in the task set.</td></tr>
<tr><td><code>Service</code></td><td><code>string</code></td><td>The short name or full Amazon Resource Name (ARN) of the service to create the task set in.</td></tr>
<tr><td><code>ServiceRegistries</code></td><td><code>array</code></td><td>The details of the service discovery registries to assign to this task set. For more information, see https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;AmazonECS&#x2F;latest&#x2F;developerguide&#x2F;service-discovery.html.</td></tr>
<tr><td><code>TaskDefinition</code></td><td><code>string</code></td><td>The short name or full Amazon Resource Name (ARN) of the task definition for the tasks in the task set to use.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.ecs.task_set
WHERE region = 'us-east-1' AND data__Identifier = '&lt;Cluster&gt;' AND data__Identifier = '&lt;Service&gt;' AND data__Identifier = '&lt;Id&gt;'
</pre>
