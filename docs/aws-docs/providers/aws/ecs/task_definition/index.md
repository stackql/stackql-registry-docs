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
<tr><td><b>Description</b></td><td>Registers a new task definition from the supplied ``family`` and ``containerDefinitions``. Optionally, you can add data volumes to your containers with the ``volumes`` parameter. For more information about task definition parameters and defaults, see &#91;Amazon ECS Task Definitions&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;AmazonECS&#x2F;latest&#x2F;developerguide&#x2F;task_defintions.html) in the *Amazon Elastic Container Service Developer Guide*.&lt;br&#x2F;&gt; You can specify a role for your task with the ``taskRoleArn`` parameter. When you specify a role for a task, its containers can then use the latest versions of the CLI or SDKs to make API requests to the AWS services that are specified in the policy that's associated with the role. For more information, see &#91;IAM Roles for Tasks&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;AmazonECS&#x2F;latest&#x2F;developerguide&#x2F;task-iam-roles.html) in the *Amazon Elastic Container Service Developer Guide*.&lt;br&#x2F;&gt; You can specify a Docker networking mode for the containers in your task definition with the ``networkMode`` parameter. The available network modes correspond to those described in &#91;Network settings&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;https:&#x2F;&#x2F;docs.docker.com&#x2F;engine&#x2F;reference&#x2F;run&#x2F;#&#x2F;network-settings) in the Docker run reference. If you specify the ``awsvpc`` network mode, the task is allocated an elastic network interface, and you must specify a NetworkConfiguration when you create a service or run a task with the task definition. For more information, see &#91;Task Networking&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;AmazonECS&#x2F;latest&#x2F;developerguide&#x2F;task-networking.html) in the *Amazon Elastic Container Service Developer Guide*.&lt;br&#x2F;&gt;  In the following example or examples, the Authorization header contents (``AUTHPARAMS``) must be replaced with an AWS Signature Version 4 signature. For more information, see &#91;Signature Version 4 Signing Process&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;general&#x2F;latest&#x2F;gr&#x2F;signature-version-4.html) in the *General Reference*.&lt;br&#x2F;&gt; You only need to learn how to sign HTTP requests if you intend to create them manually. When you use the &#91;&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;cli&#x2F;) or one of the &#91;SDKs&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;tools&#x2F;) to make requests to AWS, these tools automatically sign the requests for you, with the access key that you specify when you configure the tools. When you use these tools, you don't have to sign requests yourself.</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ecs.task_definition</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>task_definition_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>family</code></td><td><code>string</code></td><td>The name of a family that this task definition is registered to. Up to 255 letters (uppercase and lowercase), numbers, hyphens, and underscores are allowed.&lt;br&#x2F;&gt; A family groups multiple versions of a task definition. Amazon ECS gives the first task definition that you registered to a family a revision number of 1. Amazon ECS gives sequential revision numbers to each task definition that you add.&lt;br&#x2F;&gt;  To use revision numbers when you update a task definition, specify this property. If you don't specify a value, CFNlong generates a new task definition each time that you update it.</td></tr>
<tr><td><code>container_definitions</code></td><td><code>array</code></td><td>A list of container definitions in JSON format that describe the different containers that make up your task. For more information about container definition parameters and defaults, see &#91;Amazon ECS Task Definitions&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;AmazonECS&#x2F;latest&#x2F;developerguide&#x2F;task_defintions.html) in the *Amazon Elastic Container Service Developer Guide*.</td></tr>
<tr><td><code>cpu</code></td><td><code>string</code></td><td>The number of ``cpu`` units used by the task. If you use the EC2 launch type, this field is optional. Any value can be used. If you use the Fargate launch type, this field is required. You must use one of the following values. The value that you choose determines your range of valid values for the ``memory`` parameter.&lt;br&#x2F;&gt; The CPU units cannot be less than 1 vCPU when you use Windows containers on Fargate.&lt;br&#x2F;&gt;  +  256 (.25 vCPU) - Available ``memory`` values: 512 (0.5 GB), 1024 (1 GB), 2048 (2 GB)&lt;br&#x2F;&gt;  +  512 (.5 vCPU) - Available ``memory`` values: 1024 (1 GB), 2048 (2 GB), 3072 (3 GB), 4096 (4 GB)&lt;br&#x2F;&gt;  +  1024 (1 vCPU) - Available ``memory`` values: 2048 (2 GB), 3072 (3 GB), 4096 (4 GB), 5120 (5 GB), 6144 (6 GB), 7168 (7 GB), 8192 (8 GB)&lt;br&#x2F;&gt;  +  2048 (2 vCPU) - Available ``memory`` values: 4096 (4 GB) and 16384 (16 GB) in increments of 1024 (1 GB)&lt;br&#x2F;&gt;  +  4096 (4 vCPU) - Available ``memory`` values: 8192 (8 GB) and 30720 (30 GB) in increments of 1024 (1 GB)&lt;br&#x2F;&gt;  +  8192 (8 vCPU) - Available ``memory`` values: 16 GB and 60 GB in 4 GB increments&lt;br&#x2F;&gt; This option requires Linux platform ``1.4.0`` or later.&lt;br&#x2F;&gt;  +  16384 (16vCPU) - Available ``memory`` values: 32GB and 120 GB in 8 GB increments&lt;br&#x2F;&gt; This option requires Linux platform ``1.4.0`` or later.</td></tr>
<tr><td><code>execution_role_arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the task execution role that grants the Amazon ECS container agent permission to make AWS API calls on your behalf. The task execution IAM role is required depending on the requirements of your task. For more information, see &#91;Amazon ECS task execution IAM role&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;AmazonECS&#x2F;latest&#x2F;developerguide&#x2F;task_execution_IAM_role.html) in the *Amazon Elastic Container Service Developer Guide*.</td></tr>
<tr><td><code>ephemeral_storage</code></td><td><code>object</code></td><td>The ephemeral storage settings to use for tasks run with the task definition.</td></tr>
<tr><td><code>inference_accelerators</code></td><td><code>array</code></td><td>The Elastic Inference accelerators to use for the containers in the task.</td></tr>
<tr><td><code>memory</code></td><td><code>string</code></td><td>The amount (in MiB) of memory used by the task.&lt;br&#x2F;&gt; If your tasks runs on Amazon EC2 instances, you must specify either a task-level memory value or a container-level memory value. This field is optional and any value can be used. If a task-level memory value is specified, the container-level memory value is optional. For more information regarding container-level memory and memory reservation, see &#91;ContainerDefinition&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;AmazonECS&#x2F;latest&#x2F;APIReference&#x2F;API_ContainerDefinition.html).&lt;br&#x2F;&gt; If your tasks runs on FARGATElong, this field is required. You must use one of the following values. The value you choose determines your range of valid values for the ``cpu`` parameter.&lt;br&#x2F;&gt;  +  512 (0.5 GB), 1024 (1 GB), 2048 (2 GB) - Available ``cpu`` values: 256 (.25 vCPU)&lt;br&#x2F;&gt;  +  1024 (1 GB), 2048 (2 GB), 3072 (3 GB), 4096 (4 GB) - Available ``cpu`` values: 512 (.5 vCPU)&lt;br&#x2F;&gt;  +  2048 (2 GB), 3072 (3 GB), 4096 (4 GB), 5120 (5 GB), 6144 (6 GB), 7168 (7 GB), 8192 (8 GB) - Available ``cpu`` values: 1024 (1 vCPU)&lt;br&#x2F;&gt;  +  Between 4096 (4 GB) and 16384 (16 GB) in increments of 1024 (1 GB) - Available ``cpu`` values: 2048 (2 vCPU)&lt;br&#x2F;&gt;  +  Between 8192 (8 GB) and 30720 (30 GB) in increments of 1024 (1 GB) - Available ``cpu`` values: 4096 (4 vCPU)&lt;br&#x2F;&gt;  +  Between 16 GB and 60 GB in 4 GB increments - Available ``cpu`` values: 8192 (8 vCPU)&lt;br&#x2F;&gt; This option requires Linux platform ``1.4.0`` or later.&lt;br&#x2F;&gt;  +  Between 32GB and 120 GB in 8 GB increments - Available ``cpu`` values: 16384 (16 vCPU)&lt;br&#x2F;&gt; This option requires Linux platform ``1.4.0`` or later.</td></tr>
<tr><td><code>network_mode</code></td><td><code>string</code></td><td>The Docker networking mode to use for the containers in the task. The valid values are ``none``, ``bridge``, ``awsvpc``, and ``host``. If no network mode is specified, the default is ``bridge``.&lt;br&#x2F;&gt; For Amazon ECS tasks on Fargate, the ``awsvpc`` network mode is required. For Amazon ECS tasks on Amazon EC2 Linux instances, any network mode can be used. For Amazon ECS tasks on Amazon EC2 Windows instances, ``&lt;default&gt;`` or ``awsvpc`` can be used. If the network mode is set to ``none``, you cannot specify port mappings in your container definitions, and the tasks containers do not have external connectivity. The ``host`` and ``awsvpc`` network modes offer the highest networking performance for containers because they use the EC2 network stack instead of the virtualized network stack provided by the ``bridge`` mode.&lt;br&#x2F;&gt; With the ``host`` and ``awsvpc`` network modes, exposed container ports are mapped directly to the corresponding host port (for the ``host`` network mode) or the attached elastic network interface port (for the ``awsvpc`` network mode), so you cannot take advantage of dynamic host port mappings. &lt;br&#x2F;&gt;  When using the ``host`` network mode, you should not run containers using the root user (UID 0). It is considered best practice to use a non-root user.&lt;br&#x2F;&gt;  If the network mode is ``awsvpc``, the task is allocated an elastic network interface, and you must specify a NetworkConfiguration value when you create a service or run a task with the task definition. For more information, see &#91;Task Networking&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;AmazonECS&#x2F;latest&#x2F;developerguide&#x2F;task-networking.html) in the *Amazon Elastic Container Service Developer Guide*.&lt;br&#x2F;&gt; If the network mode is ``host``, you cannot run multiple instantiations of the same task on a single container instance when port mappings are used.&lt;br&#x2F;&gt; For more information, see &#91;Network settings&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;https:&#x2F;&#x2F;docs.docker.com&#x2F;engine&#x2F;reference&#x2F;run&#x2F;#network-settings) in the *Docker run reference*.</td></tr>
<tr><td><code>placement_constraints</code></td><td><code>array</code></td><td>An array of placement constraint objects to use for tasks.&lt;br&#x2F;&gt;  This parameter isn't supported for tasks run on FARGATElong.</td></tr>
<tr><td><code>proxy_configuration</code></td><td><code>object</code></td><td>The configuration details for the App Mesh proxy.&lt;br&#x2F;&gt; Your Amazon ECS container instances require at least version 1.26.0 of the container agent and at least version 1.26.0-1 of the ``ecs-init`` package to use a proxy configuration. If your container instances are launched from the Amazon ECS optimized AMI version ``20190301`` or later, they contain the required versions of the container agent and ``ecs-init``. For more information, see &#91;Amazon ECS-optimized Linux AMI&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;AmazonECS&#x2F;latest&#x2F;developerguide&#x2F;ecs-optimized_AMI.html) in the *Amazon Elastic Container Service Developer Guide*.</td></tr>
<tr><td><code>requires_compatibilities</code></td><td><code>array</code></td><td>The task launch types the task definition was validated against. The valid values are ``EC2``, ``FARGATE``, and ``EXTERNAL``. For more information, see &#91;Amazon ECS launch types&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;AmazonECS&#x2F;latest&#x2F;developerguide&#x2F;launch_types.html) in the *Amazon Elastic Container Service Developer Guide*.</td></tr>
<tr><td><code>task_role_arn</code></td><td><code>string</code></td><td>The short name or full Amazon Resource Name (ARN) of the IAMlong role that grants containers in the task permission to call AWS APIs on your behalf. For more information, see &#91;Amazon ECS Task Role&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;AmazonECS&#x2F;latest&#x2F;developerguide&#x2F;task-iam-roles.html) in the *Amazon Elastic Container Service Developer Guide*.&lt;br&#x2F;&gt; IAM roles for tasks on Windows require that the ``-EnableTaskIAMRole`` option is set when you launch the Amazon ECS-optimized Windows AMI. Your containers must also run some configuration code to use the feature. For more information, see &#91;Windows IAM roles for tasks&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;AmazonECS&#x2F;latest&#x2F;developerguide&#x2F;windows_task_IAM_roles.html) in the *Amazon Elastic Container Service Developer Guide*.</td></tr>
<tr><td><code>volumes</code></td><td><code>array</code></td><td>The list of data volume definitions for the task. For more information, see &#91;Using data volumes in tasks&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;AmazonECS&#x2F;latest&#x2F;developerguide&#x2F;using_data_volumes.html) in the *Amazon Elastic Container Service Developer Guide*.&lt;br&#x2F;&gt;  The ``host`` and ``sourcePath`` parameters aren't supported for tasks run on FARGATElong.</td></tr>
<tr><td><code>pid_mode</code></td><td><code>string</code></td><td>The process namespace to use for the containers in the task. The valid values are ``host`` or ``task``. On Fargate for Linux containers, the only valid value is ``task``. For example, monitoring sidecars might need ``pidMode`` to access information about other containers running in the same task.&lt;br&#x2F;&gt; If ``host`` is specified, all containers within the tasks that specified the ``host`` PID mode on the same container instance share the same process namespace with the host Amazon EC2 instance.&lt;br&#x2F;&gt; If ``task`` is specified, all containers within the specified task share the same process namespace.&lt;br&#x2F;&gt; If no value is specified, the default is a private namespace for each container. For more information, see &#91;PID settings&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;https:&#x2F;&#x2F;docs.docker.com&#x2F;engine&#x2F;reference&#x2F;run&#x2F;#pid-settings---pid) in the *Docker run reference*.&lt;br&#x2F;&gt; If the ``host`` PID mode is used, there's a heightened risk of undesired process namespace exposure. For more information, see &#91;Docker security&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;https:&#x2F;&#x2F;docs.docker.com&#x2F;engine&#x2F;security&#x2F;security&#x2F;).&lt;br&#x2F;&gt;  This parameter is not supported for Windows containers.&lt;br&#x2F;&gt;   This parameter is only supported for tasks that are hosted on FARGATElong if the tasks are using platform version ``1.4.0`` or later (Linux). This isn't supported for Windows containers on Fargate.</td></tr>
<tr><td><code>runtime_platform</code></td><td><code>object</code></td><td>The operating system that your tasks definitions run on. A platform family is specified only for tasks using the Fargate launch type. &lt;br&#x2F;&gt; When you specify a task definition in a service, this value must match the ``runtimePlatform`` value of the service.</td></tr>
<tr><td><code>ipc_mode</code></td><td><code>string</code></td><td>The IPC resource namespace to use for the containers in the task. The valid values are ``host``, ``task``, or ``none``. If ``host`` is specified, then all containers within the tasks that specified the ``host`` IPC mode on the same container instance share the same IPC resources with the host Amazon EC2 instance. If ``task`` is specified, all containers within the specified task share the same IPC resources. If ``none`` is specified, then IPC resources within the containers of a task are private and not shared with other containers in a task or on the container instance. If no value is specified, then the IPC resource namespace sharing depends on the Docker daemon setting on the container instance. For more information, see &#91;IPC settings&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;https:&#x2F;&#x2F;docs.docker.com&#x2F;engine&#x2F;reference&#x2F;run&#x2F;#ipc-settings---ipc) in the *Docker run reference*.&lt;br&#x2F;&gt; If the ``host`` IPC mode is used, be aware that there is a heightened risk of undesired IPC namespace expose. For more information, see &#91;Docker security&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;https:&#x2F;&#x2F;docs.docker.com&#x2F;engine&#x2F;security&#x2F;security&#x2F;).&lt;br&#x2F;&gt; If you are setting namespaced kernel parameters using ``systemControls`` for the containers in the task, the following will apply to your IPC resource namespace. For more information, see &#91;System Controls&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;AmazonECS&#x2F;latest&#x2F;developerguide&#x2F;task_definition_parameters.html) in the *Amazon Elastic Container Service Developer Guide*.&lt;br&#x2F;&gt;  +  For tasks that use the ``host`` IPC mode, IPC namespace related ``systemControls`` are not supported.&lt;br&#x2F;&gt;  +  For tasks that use the ``task`` IPC mode, IPC namespace related ``systemControls`` will apply to all containers within a task.&lt;br&#x2F;&gt;  &lt;br&#x2F;&gt;  This parameter is not supported for Windows containers or tasks run on FARGATElong.</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>The metadata that you apply to the task definition to help you categorize and organize them. Each tag consists of a key and an optional value. You define both of them.&lt;br&#x2F;&gt; The following basic restrictions apply to tags:&lt;br&#x2F;&gt;  +  Maximum number of tags per resource - 50&lt;br&#x2F;&gt;  +  For each resource, each tag key must be unique, and each tag key can have only one value.&lt;br&#x2F;&gt;  +  Maximum key length - 128 Unicode characters in UTF-8&lt;br&#x2F;&gt;  +  Maximum value length - 256 Unicode characters in UTF-8&lt;br&#x2F;&gt;  +  If your tagging schema is used across multiple services and resources, remember that other services may have restrictions on allowed characters. Generally allowed characters are: letters, numbers, and spaces representable in UTF-8, and the following characters: + - = . _ : &#x2F; @.&lt;br&#x2F;&gt;  +  Tag keys and values are case-sensitive.&lt;br&#x2F;&gt;  +  Do not use ``aws:``, ``AWS:``, or any upper or lowercase combination of such as a prefix for either keys or values as it is reserved for AWS use. You cannot edit or delete tag keys or values with this prefix. Tags with this prefix do not count against your tags per resource limit.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods

<table><tbody>
  <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
  </tr>
  <tr>
    <td><code>update_resource</code></td>
    <td><code>UPDATE</code></td>
    <td><code>data__Identifier, data__PatchDocument, region</code></td>
  </tr>
  <tr>
    <td><code>delete_resource</code></td>
    <td><code>DELETE</code></td>
    <td><code>data__Identifier, region</code></td>
  </tr>
  <tr>
    <td><code>get_resource</code></td>
    <td><code>SELECT</code></td>
    <td><code>data__Identifier, region</code></td>
  </tr>
</tbody></table>

## `SELECT` Example
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
WHERE data__Identifier = '<TaskDefinitionArn>';
```

## Permissions

To operate on the <code>task_definition</code> resource, the following permissions are required:

### Read
```json
ecs:DescribeTaskDefinition
```

### Update
```json
ecs:TagResource,
ecs:UntagResource,
ecs:ListTagsForResource,
ecs:DescribeTaskDefinition,
iam:GetRole,
iam:PassRole
```

### Delete
```json
ecs:DeregisterTaskDefinition,
ecs:DescribeTaskDefinition,
iam:GetRole,
iam:PassRole
```

