---
title: task_definition_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - task_definition_tags
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

Expands all tag keys and values for <code>task_definitions</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>task_definition_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Registers a new task definition from the supplied <code>family</code> and <code>containerDefinitions</code>. Optionally, you can add data volumes to your containers with the <code>volumes</code> parameter. For more information about task definition parameters and defaults, see &#91;Amazon ECS Task Definitions&#93;(https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task_defintions.html) in the *Amazon Elastic Container Service Developer Guide*.<br />You can specify a role for your task with the <code>taskRoleArn</code> parameter. When you specify a role for a task, its containers can then use the latest versions of the CLI or SDKs to make API requests to the AWS services that are specified in the policy that's associated with the role. For more information, see &#91;IAM Roles for Tasks&#93;(https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-iam-roles.html) in the *Amazon Elastic Container Service Developer Guide*.<br />You can specify a Docker networking mode for the containers in your task definition with the <code>networkMode</code> parameter. If you specify the <code>awsvpc</code> network mode, the task is allocated an elastic network interface, and you must specify a &#91;NetworkConfiguration&#93;(https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_NetworkConfiguration.html) when you create a service or run a task with the task definition. For more information, see &#91;Task Networking&#93;(https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-networking.html) in the *Amazon Elastic Container Service Developer Guide*.<br />In the following example or examples, the Authorization header contents (<code>AUTHPARAMS</code>) must be replaced with an AWS Signature Version 4 signature. For more information, see &#91;Signature Version 4 Signing Process&#93;(https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) in the *General Reference*.<br />You only need to learn how to sign HTTP requests if you intend to create them manually. When you use the &#91;&#93;(https://docs.aws.amazon.com/cli/) or one of the &#91;SDKs&#93;(https://docs.aws.amazon.com/tools/) to make requests to AWS, these tools automatically sign the requests for you, with the access key that you specify when you configure the tools. When you use these tools, you don't have to sign requests yourself.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ecs.task_definition_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="task_role_arn" /></td><td><code>string</code></td><td>The short name or full Amazon Resource Name (ARN) of the IAMlong role that grants containers in the task permission to call AWS APIs on your behalf. For more information, see &#91;Amazon ECS Task Role&#93;(https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-iam-roles.html) in the *Amazon Elastic Container Service Developer Guide*.<br />IAM roles for tasks on Windows require that the <code>-EnableTaskIAMRole</code> option is set when you launch the Amazon ECS-optimized Windows AMI. Your containers must also run some configuration code to use the feature. For more information, see &#91;Windows IAM roles for tasks&#93;(https://docs.aws.amazon.com/AmazonECS/latest/developerguide/windows_task_IAM_roles.html) in the *Amazon Elastic Container Service Developer Guide*.<br />String validation is done on the ECS side. If an invalid string value is given for <code>TaskRoleArn</code>, it may cause the Cloudformation job to hang.</td></tr>
<tr><td><CopyableCode code="ipc_mode" /></td><td><code>string</code></td><td>The IPC resource namespace to use for the containers in the task. The valid values are <code>host</code>, <code>task</code>, or <code>none</code>. If <code>host</code> is specified, then all containers within the tasks that specified the <code>host</code> IPC mode on the same container instance share the same IPC resources with the host Amazon EC2 instance. If <code>task</code> is specified, all containers within the specified task share the same IPC resources. If <code>none</code> is specified, then IPC resources within the containers of a task are private and not shared with other containers in a task or on the container instance. If no value is specified, then the IPC resource namespace sharing depends on the Docker daemon setting on the container instance.<br />If the <code>host</code> IPC mode is used, be aware that there is a heightened risk of undesired IPC namespace expose.<br />If you are setting namespaced kernel parameters using <code>systemControls</code> for the containers in the task, the following will apply to your IPC resource namespace. For more information, see &#91;System Controls&#93;(https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task_definition_parameters.html) in the *Amazon Elastic Container Service Developer Guide*.<br />+ For tasks that use the <code>host</code> IPC mode, IPC namespace related <code>systemControls</code> are not supported.<br />+ For tasks that use the <code>task</code> IPC mode, IPC namespace related <code>systemControls</code> will apply to all containers within a task.<br /><br />This parameter is not supported for Windows containers or tasks run on FARGATElong.</td></tr>
<tr><td><CopyableCode code="inference_accelerators" /></td><td><code>array</code></td><td>The Elastic Inference accelerators to use for the containers in the task.</td></tr>
<tr><td><CopyableCode code="memory" /></td><td><code>string</code></td><td>The amount (in MiB) of memory used by the task.<br />If your tasks runs on Amazon EC2 instances, you must specify either a task-level memory value or a container-level memory value. This field is optional and any value can be used. If a task-level memory value is specified, the container-level memory value is optional. For more information regarding container-level memory and memory reservation, see &#91;ContainerDefinition&#93;(https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ContainerDefinition.html).<br />If your tasks runs on FARGATElong, this field is required. You must use one of the following values. The value you choose determines your range of valid values for the <code>cpu</code> parameter.<br />+ 512 (0.5 GB), 1024 (1 GB), 2048 (2 GB) - Available <code>cpu</code> values: 256 (.25 vCPU)<br />+ 1024 (1 GB), 2048 (2 GB), 3072 (3 GB), 4096 (4 GB) - Available <code>cpu</code> values: 512 (.5 vCPU)<br />+ 2048 (2 GB), 3072 (3 GB), 4096 (4 GB), 5120 (5 GB), 6144 (6 GB), 7168 (7 GB), 8192 (8 GB) - Available <code>cpu</code> values: 1024 (1 vCPU)<br />+ Between 4096 (4 GB) and 16384 (16 GB) in increments of 1024 (1 GB) - Available <code>cpu</code> values: 2048 (2 vCPU)<br />+ Between 8192 (8 GB) and 30720 (30 GB) in increments of 1024 (1 GB) - Available <code>cpu</code> values: 4096 (4 vCPU)<br />+ Between 16 GB and 60 GB in 4 GB increments - Available <code>cpu</code> values: 8192 (8 vCPU)<br />This option requires Linux platform <code>1.4.0</code> or later.<br />+ Between 32GB and 120 GB in 8 GB increments - Available <code>cpu</code> values: 16384 (16 vCPU)<br />This option requires Linux platform <code>1.4.0</code> or later.</td></tr>
<tr><td><CopyableCode code="placement_constraints" /></td><td><code>array</code></td><td>An array of placement constraint objects to use for tasks.<br />This parameter isn't supported for tasks run on FARGATElong.</td></tr>
<tr><td><CopyableCode code="cpu" /></td><td><code>string</code></td><td>The number of <code>cpu</code> units used by the task. If you use the EC2 launch type, this field is optional. Any value can be used. If you use the Fargate launch type, this field is required. You must use one of the following values. The value that you choose determines your range of valid values for the <code>memory</code> parameter.<br />If you use the EC2 launch type, this field is optional. Supported values are between <code>128</code> CPU units (<code>0.125</code> vCPUs) and <code>10240</code> CPU units (<code>10</code> vCPUs).<br />The CPU units cannot be less than 1 vCPU when you use Windows containers on Fargate.<br />+ 256 (.25 vCPU) - Available <code>memory</code> values: 512 (0.5 GB), 1024 (1 GB), 2048 (2 GB)<br />+ 512 (.5 vCPU) - Available <code>memory</code> values: 1024 (1 GB), 2048 (2 GB), 3072 (3 GB), 4096 (4 GB)<br />+ 1024 (1 vCPU) - Available <code>memory</code> values: 2048 (2 GB), 3072 (3 GB), 4096 (4 GB), 5120 (5 GB), 6144 (6 GB), 7168 (7 GB), 8192 (8 GB)<br />+ 2048 (2 vCPU) - Available <code>memory</code> values: 4096 (4 GB) and 16384 (16 GB) in increments of 1024 (1 GB)<br />+ 4096 (4 vCPU) - Available <code>memory</code> values: 8192 (8 GB) and 30720 (30 GB) in increments of 1024 (1 GB)<br />+ 8192 (8 vCPU) - Available <code>memory</code> values: 16 GB and 60 GB in 4 GB increments<br />This option requires Linux platform <code>1.4.0</code> or later.<br />+ 16384 (16vCPU) - Available <code>memory</code> values: 32GB and 120 GB in 8 GB increments<br />This option requires Linux platform <code>1.4.0</code> or later.</td></tr>
<tr><td><CopyableCode code="requires_compatibilities" /></td><td><code>array</code></td><td>The task launch types the task definition was validated against. The valid values are <code>EC2</code>, <code>FARGATE</code>, and <code>EXTERNAL</code>. For more information, see &#91;Amazon ECS launch types&#93;(https://docs.aws.amazon.com/AmazonECS/latest/developerguide/launch_types.html) in the *Amazon Elastic Container Service Developer Guide*.</td></tr>
<tr><td><CopyableCode code="network_mode" /></td><td><code>string</code></td><td>The Docker networking mode to use for the containers in the task. The valid values are <code>none</code>, <code>bridge</code>, <code>awsvpc</code>, and <code>host</code>. If no network mode is specified, the default is <code>bridge</code>.<br />For Amazon ECS tasks on Fargate, the <code>awsvpc</code> network mode is required. For Amazon ECS tasks on Amazon EC2 Linux instances, any network mode can be used. For Amazon ECS tasks on Amazon EC2 Windows instances, <code>&lt;default&gt;</code> or <code>awsvpc</code> can be used. If the network mode is set to <code>none</code>, you cannot specify port mappings in your container definitions, and the tasks containers do not have external connectivity. The <code>host</code> and <code>awsvpc</code> network modes offer the highest networking performance for containers because they use the EC2 network stack instead of the virtualized network stack provided by the <code>bridge</code> mode.<br />With the <code>host</code> and <code>awsvpc</code> network modes, exposed container ports are mapped directly to the corresponding host port (for the <code>host</code> network mode) or the attached elastic network interface port (for the <code>awsvpc</code> network mode), so you cannot take advantage of dynamic host port mappings. <br />When using the <code>host</code> network mode, you should not run containers using the root user (UID 0). It is considered best practice to use a non-root user.<br />If the network mode is <code>awsvpc</code>, the task is allocated an elastic network interface, and you must specify a &#91;NetworkConfiguration&#93;(https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_NetworkConfiguration.html) value when you create a service or run a task with the task definition. For more information, see &#91;Task Networking&#93;(https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-networking.html) in the *Amazon Elastic Container Service Developer Guide*.<br />If the network mode is <code>host</code>, you cannot run multiple instantiations of the same task on a single container instance when port mappings are used.</td></tr>
<tr><td><CopyableCode code="pid_mode" /></td><td><code>string</code></td><td>The process namespace to use for the containers in the task. The valid values are <code>host</code> or <code>task</code>. On Fargate for Linux containers, the only valid value is <code>task</code>. For example, monitoring sidecars might need <code>pidMode</code> to access information about other containers running in the same task.<br />If <code>host</code> is specified, all containers within the tasks that specified the <code>host</code> PID mode on the same container instance share the same process namespace with the host Amazon EC2 instance.<br />If <code>task</code> is specified, all containers within the specified task share the same process namespace.<br />If no value is specified, the default is a private namespace for each container.<br />If the <code>host</code> PID mode is used, there's a heightened risk of undesired process namespace exposure.<br />This parameter is not supported for Windows containers.<br />This parameter is only supported for tasks that are hosted on FARGATElong if the tasks are using platform version <code>1.4.0</code> or later (Linux). This isn't supported for Windows containers on Fargate.</td></tr>
<tr><td><CopyableCode code="enable_fault_injection" /></td><td><code>boolean</code></td><td>Enables fault injection and allows for fault injection requests to be accepted from the task's containers. The default value is <code>false</code>.</td></tr>
<tr><td><CopyableCode code="execution_role_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the task execution role that grants the Amazon ECS container agent permission to make AWS API calls on your behalf. For informationabout the required IAM roles for Amazon ECS, see &#91;IAM roles for Amazon ECS&#93;(https://docs.aws.amazon.com/AmazonECS/latest/developerguide/security-ecs-iam-role-overview.html) in the *Amazon Elastic Container Service Developer Guide*.</td></tr>
<tr><td><CopyableCode code="runtime_platform" /></td><td><code>object</code></td><td>The operating system that your tasks definitions run on. A platform family is specified only for tasks using the Fargate launch type.</td></tr>
<tr><td><CopyableCode code="proxy_configuration" /></td><td><code>object</code></td><td>The configuration details for the App Mesh proxy.<br />Your Amazon ECS container instances require at least version 1.26.0 of the container agent and at least version 1.26.0-1 of the <code>ecs-init</code> package to use a proxy configuration. If your container instances are launched from the Amazon ECS optimized AMI version <code>20190301</code> or later, they contain the required versions of the container agent and <code>ecs-init</code>. For more information, see &#91;Amazon ECS-optimized Linux AMI&#93;(https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-optimized_AMI.html) in the *Amazon Elastic Container Service Developer Guide*.</td></tr>
<tr><td><CopyableCode code="volumes" /></td><td><code>array</code></td><td>The list of data volume definitions for the task. For more information, see &#91;Using data volumes in tasks&#93;(https://docs.aws.amazon.com/AmazonECS/latest/developerguide/using_data_volumes.html) in the *Amazon Elastic Container Service Developer Guide*.<br />The <code>host</code> and <code>sourcePath</code> parameters aren't supported for tasks run on FARGATElong.</td></tr>
<tr><td><CopyableCode code="container_definitions" /></td><td><code>array</code></td><td>A list of container definitions in JSON format that describe the different containers that make up your task. For more information about container definition parameters and defaults, see &#91;Amazon ECS Task Definitions&#93;(https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task_defintions.html) in the *Amazon Elastic Container Service Developer Guide*.</td></tr>
<tr><td><CopyableCode code="family" /></td><td><code>string</code></td><td>The name of a family that this task definition is registered to. Up to 255 letters (uppercase and lowercase), numbers, hyphens, and underscores are allowed.<br />A family groups multiple versions of a task definition. Amazon ECS gives the first task definition that you registered to a family a revision number of 1. Amazon ECS gives sequential revision numbers to each task definition that you add.<br />To use revision numbers when you update a task definition, specify this property. If you don't specify a value, CFNlong generates a new task definition each time that you update it.</td></tr>
<tr><td><CopyableCode code="ephemeral_storage" /></td><td><code>object</code></td><td>The ephemeral storage settings to use for tasks run with the task definition.</td></tr>
<tr><td><CopyableCode code="task_definition_arn" /></td><td><code>string</code></td><td></td></tr>
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
task_role_arn,
ipc_mode,
inference_accelerators,
memory,
placement_constraints,
cpu,
requires_compatibilities,
network_mode,
pid_mode,
enable_fault_injection,
execution_role_arn,
runtime_platform,
proxy_configuration,
volumes,
container_definitions,
family,
ephemeral_storage,
task_definition_arn,
tag_key,
tag_value
FROM aws.ecs.task_definition_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>task_definition_tags</code> resource, see <a href="/providers/aws/ecs/task_definitions/#permissions"><code>task_definitions</code></a>

