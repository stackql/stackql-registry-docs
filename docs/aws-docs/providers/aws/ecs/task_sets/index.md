---
title: task_sets
hide_title: false
hide_table_of_contents: false
keywords:
  - task_sets
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

Creates, updates, deletes or gets a <code>task_set</code> resource or lists <code>task_sets</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>task_sets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Create a task set in the specified cluster and service. This is used when a service uses the EXTERNAL deployment controller type. For more information, see https://docs.aws.amazon.com/AmazonECS/latest/developerguide/deployment-types.htmlin the Amazon Elastic Container Service Developer Guide.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ecs.task_sets" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="platform_version" /></td><td><code>string</code></td><td>The platform version that the tasks in the task set should use. A platform version is specified only for tasks using the Fargate launch type. If one isn't specified, the LATEST platform version is used by default.</td></tr>
<tr><td><CopyableCode code="external_id" /></td><td><code>string</code></td><td>An optional non-unique tag that identifies this task set in external systems. If the task set is associated with a service discovery registry, the tasks in this task set will have the ECS_TASK_SET_EXTERNAL_ID AWS Cloud Map attribute set to the provided value.</td></tr>
<tr><td><CopyableCode code="cluster" /></td><td><code>string</code></td><td>The short name or full Amazon Resource Name (ARN) of the cluster that hosts the service to create the task set in.</td></tr>
<tr><td><CopyableCode code="load_balancers" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="service" /></td><td><code>string</code></td><td>The short name or full Amazon Resource Name (ARN) of the service to create the task set in.</td></tr>
<tr><td><CopyableCode code="scale" /></td><td><code>object</code></td><td>A floating-point percentage of the desired number of tasks to place and keep running in the task set.</td></tr>
<tr><td><CopyableCode code="service_registries" /></td><td><code>array</code></td><td>The details of the service discovery registries to assign to this task set. For more information, see https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-discovery.html.</td></tr>
<tr><td><CopyableCode code="capacity_provider_strategy" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="launch_type" /></td><td><code>string</code></td><td>The launch type that new tasks in the task set will use. For more information, see https://docs.aws.amazon.com/AmazonECS/latest/developerguide/launch_types.html in the Amazon Elastic Container Service Developer Guide.</td></tr>
<tr><td><CopyableCode code="task_definition" /></td><td><code>string</code></td><td>The short name or full Amazon Resource Name (ARN) of the task definition for the tasks in the task set to use.</td></tr>
<tr><td><CopyableCode code="network_configuration" /></td><td><code>object</code></td><td>An object representing the network configuration for a task or service.</td></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td>The ID of the task set.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-taskset.html"><code>AWS::ECS::TaskSet</code></a>.

## Methods

<table><tbody>
  <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
  </tr>
  <tr>
    <td><CopyableCode code="create_resource" /></td>
    <td><code>INSERT</code></td>
    <td><CopyableCode code="Cluster, Service, TaskDefinition, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
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

## `SELECT` examples

Gets all properties from an individual <code>task_set</code>.
```sql
SELECT
region,
platform_version,
external_id,
cluster,
load_balancers,
service,
scale,
service_registries,
capacity_provider_strategy,
launch_type,
task_definition,
network_configuration,
id,
tags
FROM aws.ecs.task_sets
WHERE region = 'us-east-1' AND data__Identifier = '<Cluster>|<Service>|<Id>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>task_set</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

<Tabs
    defaultValue="required"
    values={[
      { label: 'Required Properties', value: 'required', },
      { label: 'All Properties', value: 'all', },
      { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="required">

```sql
/*+ create */
INSERT INTO aws.ecs.task_sets (
 Cluster,
 Service,
 TaskDefinition,
 region
)
SELECT 
'{{ Cluster }}',
 '{{ Service }}',
 '{{ TaskDefinition }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.ecs.task_sets (
 PlatformVersion,
 ExternalId,
 Cluster,
 LoadBalancers,
 Service,
 Scale,
 ServiceRegistries,
 CapacityProviderStrategy,
 LaunchType,
 TaskDefinition,
 NetworkConfiguration,
 Tags,
 region
)
SELECT 
 '{{ PlatformVersion }}',
 '{{ ExternalId }}',
 '{{ Cluster }}',
 '{{ LoadBalancers }}',
 '{{ Service }}',
 '{{ Scale }}',
 '{{ ServiceRegistries }}',
 '{{ CapacityProviderStrategy }}',
 '{{ LaunchType }}',
 '{{ TaskDefinition }}',
 '{{ NetworkConfiguration }}',
 '{{ Tags }}',
 '{{ region }}';
```
</TabItem>
<TabItem value="manifest">

```yaml
version: 1
name: stack name
description: stack description
providers:
  - aws
globals:
  - name: region
    value: '{{ vars.AWS_REGION }}'
resources:
  - name: task_set
    props:
      - name: PlatformVersion
        value: '{{ PlatformVersion }}'
      - name: ExternalId
        value: '{{ ExternalId }}'
      - name: Cluster
        value: '{{ Cluster }}'
      - name: LoadBalancers
        value:
          - TargetGroupArn: '{{ TargetGroupArn }}'
            ContainerName: '{{ ContainerName }}'
            ContainerPort: '{{ ContainerPort }}'
      - name: Service
        value: '{{ Service }}'
      - name: Scale
        value:
          Value: null
          Unit: '{{ Unit }}'
      - name: ServiceRegistries
        value:
          - ContainerName: '{{ ContainerName }}'
            Port: '{{ Port }}'
            ContainerPort: '{{ ContainerPort }}'
            RegistryArn: '{{ RegistryArn }}'
      - name: CapacityProviderStrategy
        value:
          - CapacityProvider: '{{ CapacityProvider }}'
            Base: '{{ Base }}'
            Weight: '{{ Weight }}'
      - name: LaunchType
        value: '{{ LaunchType }}'
      - name: TaskDefinition
        value: '{{ TaskDefinition }}'
      - name: NetworkConfiguration
        value:
          AwsVpcConfiguration:
            SecurityGroups:
              - '{{ SecurityGroups[0] }}'
            Subnets:
              - '{{ Subnets[0] }}'
            AssignPublicIp: '{{ AssignPublicIp }}'
      - name: Tags
        value:
          - Value: '{{ Value }}'
            Key: '{{ Key }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.ecs.task_sets
WHERE data__Identifier = '<Cluster|Service|Id>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>task_sets</code> resource, the following permissions are required:

### Read
```json
ecs:DescribeTaskSets
```

### Create
```json
ecs:CreateTaskSet,
ecs:DescribeTaskSets,
ecs:TagResource
```

### Update
```json
ecs:DescribeTaskSets,
ecs:TagResource,
ecs:UntagResource,
ecs:UpdateTaskSet
```

### Delete
```json
ecs:DeleteTaskSet,
ecs:DescribeTaskSets
```
