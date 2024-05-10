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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';


Gets or updates an individual <code>task_set</code> resource, use <code>task_sets</code> to retrieve a list of resources or to create or delete a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>task_set</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Create a task set in the specified cluster and service. This is used when a service uses the EXTERNAL deployment controller type. For more information, see https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;AmazonECS&#x2F;latest&#x2F;developerguide&#x2F;deployment-types.htmlin the Amazon Elastic Container Service Developer Guide.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ecs.task_set" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="cluster" /></td><td><code>string</code></td><td>The short name or full Amazon Resource Name (ARN) of the cluster that hosts the service to create the task set in.</td></tr>
<tr><td><CopyableCode code="external_id" /></td><td><code>string</code></td><td>An optional non-unique tag that identifies this task set in external systems. If the task set is associated with a service discovery registry, the tasks in this task set will have the ECS_TASK_SET_EXTERNAL_ID AWS Cloud Map attribute set to the provided value. </td></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td>The ID of the task set.</td></tr>
<tr><td><CopyableCode code="launch_type" /></td><td><code>string</code></td><td>The launch type that new tasks in the task set will use. For more information, see https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;AmazonECS&#x2F;latest&#x2F;developerguide&#x2F;launch_types.html in the Amazon Elastic Container Service Developer Guide. </td></tr>
<tr><td><CopyableCode code="load_balancers" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="network_configuration" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="platform_version" /></td><td><code>string</code></td><td>The platform version that the tasks in the task set should use. A platform version is specified only for tasks using the Fargate launch type. If one isn't specified, the LATEST platform version is used by default.</td></tr>
<tr><td><CopyableCode code="scale" /></td><td><code>object</code></td><td>A floating-point percentage of the desired number of tasks to place and keep running in the task set.</td></tr>
<tr><td><CopyableCode code="service" /></td><td><code>string</code></td><td>The short name or full Amazon Resource Name (ARN) of the service to create the task set in.</td></tr>
<tr><td><CopyableCode code="service_registries" /></td><td><code>array</code></td><td>The details of the service discovery registries to assign to this task set. For more information, see https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;AmazonECS&#x2F;latest&#x2F;developerguide&#x2F;service-discovery.html.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="task_definition" /></td><td><code>string</code></td><td>The short name or full Amazon Resource Name (ARN) of the task definition for the tasks in the task set to use.</td></tr>
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
    <td><CopyableCode code="update_resource" /></td>
    <td><code>UPDATE</code></td>
    <td><CopyableCode code="data__Identifier, data__PatchDocument, region" /></td>
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
cluster,
external_id,
id,
launch_type,
load_balancers,
network_configuration,
platform_version,
scale,
service,
service_registries,
tags,
task_definition
FROM aws.ecs.task_set
WHERE region = 'us-east-1' AND data__Identifier = '<Cluster>|<Service>|<Id>';
```


## Permissions

To operate on the <code>task_set</code> resource, the following permissions are required:

### Read
```json
ecs:DescribeTaskSets
```

### Update
```json
ecs:DescribeTaskSets,
ecs:TagResource,
ecs:UntagResource,
ecs:UpdateTaskSet
```

