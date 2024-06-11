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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes or gets a <code>task_definition</code> resource or lists <code>task_definitions</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>task_definitions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Registers a new task definition from the supplied <code>family</code> and <code>containerDefinitions</code>. Optionally, you can add data volumes to your containers with the <code>volumes</code> parameter. For more information about task definition parameters and defaults, see &#91;Amazon ECS Task Definitions&#93;(https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task_defintions.html) in the *Amazon Elastic Container Service Developer Guide*. You can specify a role for your task with the <code>taskRoleArn</code> parameter. When you specify a role for a task, its containers can then use the latest versions of the CLI or SDKs to make API requests to the AWS services that are specified in the policy that's associated with the role. For more information, see &#91;IAM Roles for Tasks&#93;(https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-iam-roles.html) in the *Amazon Elastic Container Service Developer Guide*. You can specify a Docker networking mode for the containers in your task definition with the <code>networkMode</code> parameter. The available network modes correspond to those described in &#91;Network settings&#93;(https://docs.aws.amazon.com/https://docs.docker.com/engine/reference/run/#/network-settings) in the Docker run reference. If you specify the <code>awsvpc</code> network mode, the task is allocated an elastic network interface, and you must specify a NetworkConfiguration when you create a service or run a task with the task definition. For more information, see &#91;Task Networking&#93;(https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-networking.html) in the *Amazon Elastic Container Service Developer Guide*. In the following example or examples, the Authorization header contents (<code>AUTHPARAMS</code>) must be replaced with an AWS Signature Version 4 signature. For more information, see &#91;Signature Version 4 Signing Process&#93;(https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) in the *General Reference*. You only need to learn how to sign HTTP requests if you intend to create them manually. When you use the &#91;&#93;(https://docs.aws.amazon.com/cli/) or one of the &#91;SDKs&#93;(https://docs.aws.amazon.com/tools/) to make requests to AWS, these tools automatically sign the requests for you, with the access key that you specify when you configure the tools. When you use these tools, you don't have to sign requests yourself.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ecs.task_definitions" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="task_definition_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="family" /></td><td><code>string</code></td><td>The name of a family that this task definition is registered to. Up to 255 letters (uppercase and lowercase), numbers, hyphens, and underscores are allowed. A family groups multiple versions of a task definition. Amazon ECS gives the first task definition that you registered to a family a revision number of 1. Amazon ECS gives sequential revision numbers to each task definition that you add. To use revision numbers when you update a task definition, specify this property. If you don't specify a value, CFNlong generates a new task definition each time that you update it.</td></tr>
<tr><td><CopyableCode code="container_definitions" /></td><td><code>array</code></td><td>A list of container definitions in JSON format that describe the different containers that make up your task. For more information about container definition parameters and defaults, see &#91;Amazon ECS Task Definitions&#93;(https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task_defintions.html) in the *Amazon Elastic Container Service Developer Guide*.</td></tr>
<tr><td><CopyableCode code="cpu" /></td><td><code>string</code></td><td>The number of <code>cpu</code> units used by the task. If you use the EC2 launch type, this field is optional. Any value can be used. If you use the Fargate launch type, this field is required. You must use one of the following values. The value that you choose determines your range of valid values for the <code>memory</code> parameter. The CPU units cannot be less than 1 vCPU when you use Windows containers on Fargate. + 256 (.25 vCPU) - Available <code>memory</code> values: 512 (0.5 GB), 1024 (1 GB), 2048 (2 GB) + 512 (.5 vCPU) - Available <code>memory</code> values: 1024 (1 GB), 2048 (2 GB), 3072 (3 GB), 4096 (4 GB) + 1024 (1 vCPU) - Available <code>memory</code> values: 2048 (2 GB), 3072 (3 GB), 4096 (4 GB), 5120 (5 GB), 6144 (6 GB), 7168 (7 GB), 8192 (8 GB) + 2048 (2 vCPU) - Available <code>memory</code> values: 4096 (4 GB) and 16384 (16 GB) in increments of 1024 (1 GB) + 4096 (4 vCPU) - Available <code>memory</code> values: 8192 (8 GB) and 30720 (30 GB) in increments of 1024 (1 GB) + 8192 (8 vCPU) - Available <code>memory</code> values: 16 GB and 60 GB in 4 GB increments This option requires Linux platform <code>1.4.0</code> or later. + 16384 (16vCPU) - Available <code>memory</code> values: 32GB and 120 GB in 8 GB increments This option requires Linux platform <code>1.4.0</code> or later.</td></tr>
<tr><td><CopyableCode code="execution_role_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the task execution role that grants the Amazon ECS container agent permission to make AWS API calls on your behalf. The task execution IAM role is required depending on the requirements of your task. For more information, see &#91;Amazon ECS task execution IAM role&#93;(https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task_execution_IAM_role.html) in the *Amazon Elastic Container Service Developer Guide*.</td></tr>
<tr><td><CopyableCode code="ephemeral_storage" /></td><td><code>object</code></td><td>The ephemeral storage settings to use for tasks run with the task definition.</td></tr>
<tr><td><CopyableCode code="inference_accelerators" /></td><td><code>array</code></td><td>The Elastic Inference accelerators to use for the containers in the task.</td></tr>
<tr><td><CopyableCode code="memory" /></td><td><code>string</code></td><td>The amount (in MiB) of memory used by the task. If your tasks runs on Amazon EC2 instances, you must specify either a task-level memory value or a container-level memory value. This field is optional and any value can be used. If a task-level memory value is specified, the container-level memory value is optional. For more information regarding container-level memory and memory reservation, see &#91;ContainerDefinition&#93;(https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ContainerDefinition.html). If your tasks runs on FARGATElong, this field is required. You must use one of the following values. The value you choose determines your range of valid values for the <code>cpu</code> parameter. + 512 (0.5 GB), 1024 (1 GB), 2048 (2 GB) - Available <code>cpu</code> values: 256 (.25 vCPU) + 1024 (1 GB), 2048 (2 GB), 3072 (3 GB), 4096 (4 GB) - Available <code>cpu</code> values: 512 (.5 vCPU) + 2048 (2 GB), 3072 (3 GB), 4096 (4 GB), 5120 (5 GB), 6144 (6 GB), 7168 (7 GB), 8192 (8 GB) - Available <code>cpu</code> values: 1024 (1 vCPU) + Between 4096 (4 GB) and 16384 (16 GB) in increments of 1024 (1 GB) - Available <code>cpu</code> values: 2048 (2 vCPU) + Between 8192 (8 GB) and 30720 (30 GB) in increments of 1024 (1 GB) - Available <code>cpu</code> values: 4096 (4 vCPU) + Between 16 GB and 60 GB in 4 GB increments - Available <code>cpu</code> values: 8192 (8 vCPU) This option requires Linux platform <code>1.4.0</code> or later. + Between 32GB and 120 GB in 8 GB increments - Available <code>cpu</code> values: 16384 (16 vCPU) This option requires Linux platform <code>1.4.0</code> or later.</td></tr>
<tr><td><CopyableCode code="network_mode" /></td><td><code>string</code></td><td>The Docker networking mode to use for the containers in the task. The valid values are <code>none</code>, <code>bridge</code>, <code>awsvpc</code>, and <code>host</code>. If no network mode is specified, the default is <code>bridge</code>. For Amazon ECS tasks on Fargate, the <code>awsvpc</code> network mode is required. For Amazon ECS tasks on Amazon EC2 Linux instances, any network mode can be used. For Amazon ECS tasks on Amazon EC2 Windows instances, <code>default</code> or <code>awsvpc</code> can be used. If the network mode is set to <code>none</code>, you cannot specify port mappings in your container definitions, and the tasks containers do not have external connectivity. The <code>host</code> and <code>awsvpc</code> network modes offer the highest networking performance for containers because they use the EC2 network stack instead of the virtualized network stack provided by the <code>bridge</code> mode. With the <code>host</code> and <code>awsvpc</code> network modes, exposed container ports are mapped directly to the corresponding host port (for the <code>host</code> network mode) or the attached elastic network interface port (for the <code>awsvpc</code> network mode), so you cannot take advantage of dynamic host port mappings. When using the <code>host</code> network mode, you should not run containers using the root user (UID 0). It is considered best practice to use a non-root user. If the network mode is <code>awsvpc</code>, the task is allocated an elastic network interface, and you must specify a NetworkConfiguration value when you create a service or run a task with the task definition. For more information, see &#91;Task Networking&#93;(https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-networking.html) in the *Amazon Elastic Container Service Developer Guide*. If the network mode is <code>host</code>, you cannot run multiple instantiations of the same task on a single container instance when port mappings are used. For more information, see &#91;Network settings&#93;(https://docs.aws.amazon.com/https://docs.docker.com/engine/reference/run/#network-settings) in the *Docker run reference*.</td></tr>
<tr><td><CopyableCode code="placement_constraints" /></td><td><code>array</code></td><td>An array of placement constraint objects to use for tasks. This parameter isn't supported for tasks run on FARGATElong.</td></tr>
<tr><td><CopyableCode code="proxy_configuration" /></td><td><code>object</code></td><td>The configuration details for the App Mesh proxy. Your Amazon ECS container instances require at least version 1.26.0 of the container agent and at least version 1.26.0-1 of the <code>ecs-init</code> package to use a proxy configuration. If your container instances are launched from the Amazon ECS optimized AMI version <code>20190301</code> or later, they contain the required versions of the container agent and <code>ecs-init</code>. For more information, see &#91;Amazon ECS-optimized Linux AMI&#93;(https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-optimized_AMI.html) in the *Amazon Elastic Container Service Developer Guide*.</td></tr>
<tr><td><CopyableCode code="requires_compatibilities" /></td><td><code>array</code></td><td>The task launch types the task definition was validated against. The valid values are <code>EC2</code>, <code>FARGATE</code>, and <code>EXTERNAL</code>. For more information, see &#91;Amazon ECS launch types&#93;(https://docs.aws.amazon.com/AmazonECS/latest/developerguide/launch_types.html) in the *Amazon Elastic Container Service Developer Guide*.</td></tr>
<tr><td><CopyableCode code="task_role_arn" /></td><td><code>string</code></td><td>The short name or full Amazon Resource Name (ARN) of the IAMlong role that grants containers in the task permission to call AWS APIs on your behalf. For more information, see &#91;Amazon ECS Task Role&#93;(https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-iam-roles.html) in the *Amazon Elastic Container Service Developer Guide*. IAM roles for tasks on Windows require that the <code>-EnableTaskIAMRole</code> option is set when you launch the Amazon ECS-optimized Windows AMI. Your containers must also run some configuration code to use the feature. For more information, see &#91;Windows IAM roles for tasks&#93;(https://docs.aws.amazon.com/AmazonECS/latest/developerguide/windows_task_IAM_roles.html) in the *Amazon Elastic Container Service Developer Guide*.</td></tr>
<tr><td><CopyableCode code="volumes" /></td><td><code>array</code></td><td>The list of data volume definitions for the task. For more information, see &#91;Using data volumes in tasks&#93;(https://docs.aws.amazon.com/AmazonECS/latest/developerguide/using_data_volumes.html) in the *Amazon Elastic Container Service Developer Guide*. The <code>host</code> and <code>sourcePath</code> parameters aren't supported for tasks run on FARGATElong.</td></tr>
<tr><td><CopyableCode code="pid_mode" /></td><td><code>string</code></td><td>The process namespace to use for the containers in the task. The valid values are <code>host</code> or <code>task</code>. On Fargate for Linux containers, the only valid value is <code>task</code>. For example, monitoring sidecars might need <code>pidMode</code> to access information about other containers running in the same task. If <code>host</code> is specified, all containers within the tasks that specified the <code>host</code> PID mode on the same container instance share the same process namespace with the host Amazon EC2 instance. If <code>task</code> is specified, all containers within the specified task share the same process namespace. If no value is specified, the default is a private namespace for each container. For more information, see &#91;PID settings&#93;(https://docs.aws.amazon.com/https://docs.docker.com/engine/reference/run/#pid-settings---pid) in the *Docker run reference*. If the <code>host</code> PID mode is used, there's a heightened risk of undesired process namespace exposure. For more information, see &#91;Docker security&#93;(https://docs.aws.amazon.com/https://docs.docker.com/engine/security/security/). This parameter is not supported for Windows containers. This parameter is only supported for tasks that are hosted on FARGATElong if the tasks are using platform version <code>1.4.0</code> or later (Linux). This isn't supported for Windows containers on Fargate.</td></tr>
<tr><td><CopyableCode code="runtime_platform" /></td><td><code>object</code></td><td>The operating system that your tasks definitions run on. A platform family is specified only for tasks using the Fargate launch type.</td></tr>
<tr><td><CopyableCode code="ipc_mode" /></td><td><code>string</code></td><td>The IPC resource namespace to use for the containers in the task. The valid values are <code>host</code>, <code>task</code>, or <code>none</code>. If <code>host</code> is specified, then all containers within the tasks that specified the <code>host</code> IPC mode on the same container instance share the same IPC resources with the host Amazon EC2 instance. If <code>task</code> is specified, all containers within the specified task share the same IPC resources. If <code>none</code> is specified, then IPC resources within the containers of a task are private and not shared with other containers in a task or on the container instance. If no value is specified, then the IPC resource namespace sharing depends on the Docker daemon setting on the container instance. For more information, see &#91;IPC settings&#93;(https://docs.aws.amazon.com/https://docs.docker.com/engine/reference/run/#ipc-settings---ipc) in the *Docker run reference*. If the <code>host</code> IPC mode is used, be aware that there is a heightened risk of undesired IPC namespace expose. For more information, see &#91;Docker security&#93;(https://docs.aws.amazon.com/https://docs.docker.com/engine/security/security/). If you are setting namespaced kernel parameters using <code>systemControls</code> for the containers in the task, the following will apply to your IPC resource namespace. For more information, see &#91;System Controls&#93;(https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task_definition_parameters.html) in the *Amazon Elastic Container Service Developer Guide*. + For tasks that use the <code>host</code> IPC mode, IPC namespace related <code>systemControls</code> are not supported. + For tasks that use the <code>task</code> IPC mode, IPC namespace related <code>systemControls</code> will apply to all containers within a task. This parameter is not supported for Windows containers or tasks run on FARGATElong.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>The metadata that you apply to the task definition to help you categorize and organize them. Each tag consists of a key and an optional value. You define both of them. The following basic restrictions apply to tags: + Maximum number of tags per resource - 50 + For each resource, each tag key must be unique, and each tag key can have only one value. + Maximum key length - 128 Unicode characters in UTF-8 + Maximum value length - 256 Unicode characters in UTF-8 + If your tagging schema is used across multiple services and resources, remember that other services may have restrictions on allowed characters. Generally allowed characters are: letters, numbers, and spaces representable in UTF-8, and the following characters: + - = . _ : / @. + Tag keys and values are case-sensitive. + Do not use <code>aws:</code>, <code>AWS:</code>, or any upper or lowercase combination of such as a prefix for either keys or values as it is reserved for AWS use. You cannot edit or delete tag keys or values with this prefix. Tags with this prefix do not count against your tags per resource limit.</td></tr>
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
    <td><CopyableCode code="create_resource" /></td>
    <td><code>INSERT</code></td>
    <td><CopyableCode code="region" /></td>
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
    <td><CopyableCode code="list_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples
List all <code>task_definitions</code> in a region.
```sql
SELECT
region,
task_definition_arn
FROM aws.ecs.task_definitions
WHERE region = 'us-east-1';
```
Gets all properties from a <code>task_definition</code>.
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
FROM aws.ecs.task_definitions
WHERE region = 'us-east-1' AND data__Identifier = '<TaskDefinitionArn>';
```


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>task_definition</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.ecs.task_definitions (
 Family,
 ContainerDefinitions,
 Cpu,
 ExecutionRoleArn,
 EphemeralStorage,
 InferenceAccelerators,
 Memory,
 NetworkMode,
 PlacementConstraints,
 ProxyConfiguration,
 RequiresCompatibilities,
 TaskRoleArn,
 Volumes,
 PidMode,
 RuntimePlatform,
 IpcMode,
 Tags,
 region
)
SELECT 
'{{ Family }}',
 '{{ ContainerDefinitions }}',
 '{{ Cpu }}',
 '{{ ExecutionRoleArn }}',
 '{{ EphemeralStorage }}',
 '{{ InferenceAccelerators }}',
 '{{ Memory }}',
 '{{ NetworkMode }}',
 '{{ PlacementConstraints }}',
 '{{ ProxyConfiguration }}',
 '{{ RequiresCompatibilities }}',
 '{{ TaskRoleArn }}',
 '{{ Volumes }}',
 '{{ PidMode }}',
 '{{ RuntimePlatform }}',
 '{{ IpcMode }}',
 '{{ Tags }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.ecs.task_definitions (
 Family,
 ContainerDefinitions,
 Cpu,
 ExecutionRoleArn,
 EphemeralStorage,
 InferenceAccelerators,
 Memory,
 NetworkMode,
 PlacementConstraints,
 ProxyConfiguration,
 RequiresCompatibilities,
 TaskRoleArn,
 Volumes,
 PidMode,
 RuntimePlatform,
 IpcMode,
 Tags,
 region
)
SELECT 
 '{{ Family }}',
 '{{ ContainerDefinitions }}',
 '{{ Cpu }}',
 '{{ ExecutionRoleArn }}',
 '{{ EphemeralStorage }}',
 '{{ InferenceAccelerators }}',
 '{{ Memory }}',
 '{{ NetworkMode }}',
 '{{ PlacementConstraints }}',
 '{{ ProxyConfiguration }}',
 '{{ RequiresCompatibilities }}',
 '{{ TaskRoleArn }}',
 '{{ Volumes }}',
 '{{ PidMode }}',
 '{{ RuntimePlatform }}',
 '{{ IpcMode }}',
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
  - name: task_definition
    props:
      - name: Family
        value: '{{ Family }}'
      - name: ContainerDefinitions
        value:
          - Command:
              - '{{ Command[0] }}'
            Cpu: '{{ Cpu }}'
            CredentialSpecs:
              - '{{ CredentialSpecs[0] }}'
            DependsOn:
              - ContainerName: '{{ ContainerName }}'
                Condition: '{{ Condition }}'
            DisableNetworking: '{{ DisableNetworking }}'
            DnsSearchDomains:
              - '{{ DnsSearchDomains[0] }}'
            DnsServers:
              - '{{ DnsServers[0] }}'
            DockerLabels: {}
            DockerSecurityOptions:
              - '{{ DockerSecurityOptions[0] }}'
            EntryPoint:
              - '{{ EntryPoint[0] }}'
            Environment:
              - Name: '{{ Name }}'
                Value: '{{ Value }}'
            EnvironmentFiles:
              - Value: '{{ Value }}'
                Type: '{{ Type }}'
            Essential: '{{ Essential }}'
            ExtraHosts:
              - Hostname: '{{ Hostname }}'
                IpAddress: '{{ IpAddress }}'
            FirelensConfiguration:
              Type: '{{ Type }}'
              Options: {}
            HealthCheck:
              Command:
                - '{{ Command[0] }}'
              Interval: '{{ Interval }}'
              Timeout: '{{ Timeout }}'
              Retries: '{{ Retries }}'
              StartPeriod: '{{ StartPeriod }}'
            Hostname: '{{ Hostname }}'
            Image: '{{ Image }}'
            Links:
              - '{{ Links[0] }}'
            LinuxParameters:
              Capabilities:
                Add:
                  - '{{ Add[0] }}'
                Drop:
                  - '{{ Drop[0] }}'
              Devices:
                - ContainerPath: '{{ ContainerPath }}'
                  HostPath: '{{ HostPath }}'
                  Permissions:
                    - '{{ Permissions[0] }}'
              InitProcessEnabled: '{{ InitProcessEnabled }}'
              MaxSwap: '{{ MaxSwap }}'
              SharedMemorySize: '{{ SharedMemorySize }}'
              Swappiness: '{{ Swappiness }}'
              Tmpfs:
                - ContainerPath: '{{ ContainerPath }}'
                  MountOptions:
                    - '{{ MountOptions[0] }}'
                  Size: '{{ Size }}'
            LogConfiguration:
              LogDriver: '{{ LogDriver }}'
              Options: {}
              SecretOptions:
                - Name: '{{ Name }}'
                  ValueFrom: '{{ ValueFrom }}'
            Memory: '{{ Memory }}'
            MemoryReservation: '{{ MemoryReservation }}'
            MountPoints:
              - ContainerPath: '{{ ContainerPath }}'
                ReadOnly: '{{ ReadOnly }}'
                SourceVolume: '{{ SourceVolume }}'
            Name: '{{ Name }}'
            PortMappings:
              - Name: '{{ Name }}'
                ContainerPort: '{{ ContainerPort }}'
                ContainerPortRange: '{{ ContainerPortRange }}'
                HostPort: '{{ HostPort }}'
                Protocol: '{{ Protocol }}'
                AppProtocol: '{{ AppProtocol }}'
            Privileged: '{{ Privileged }}'
            ReadonlyRootFilesystem: '{{ ReadonlyRootFilesystem }}'
            RepositoryCredentials:
              CredentialsParameter: '{{ CredentialsParameter }}'
            ResourceRequirements:
              - Type: '{{ Type }}'
                Value: '{{ Value }}'
            Secrets:
              - null
            StartTimeout: '{{ StartTimeout }}'
            StopTimeout: '{{ StopTimeout }}'
            Ulimits:
              - HardLimit: '{{ HardLimit }}'
                Name: '{{ Name }}'
                SoftLimit: '{{ SoftLimit }}'
            User: '{{ User }}'
            VolumesFrom:
              - ReadOnly: '{{ ReadOnly }}'
                SourceContainer: '{{ SourceContainer }}'
            WorkingDirectory: '{{ WorkingDirectory }}'
            Interactive: '{{ Interactive }}'
            PseudoTerminal: '{{ PseudoTerminal }}'
            SystemControls:
              - Namespace: '{{ Namespace }}'
                Value: '{{ Value }}'
      - name: Cpu
        value: '{{ Cpu }}'
      - name: ExecutionRoleArn
        value: '{{ ExecutionRoleArn }}'
      - name: EphemeralStorage
        value:
          SizeInGiB: '{{ SizeInGiB }}'
      - name: InferenceAccelerators
        value:
          - DeviceName: '{{ DeviceName }}'
            DeviceType: '{{ DeviceType }}'
      - name: Memory
        value: '{{ Memory }}'
      - name: NetworkMode
        value: '{{ NetworkMode }}'
      - name: PlacementConstraints
        value:
          - Type: '{{ Type }}'
            Expression: '{{ Expression }}'
      - name: ProxyConfiguration
        value:
          ContainerName: '{{ ContainerName }}'
          ProxyConfigurationProperties:
            - null
          Type: '{{ Type }}'
      - name: RequiresCompatibilities
        value:
          - '{{ RequiresCompatibilities[0] }}'
      - name: TaskRoleArn
        value: '{{ TaskRoleArn }}'
      - name: Volumes
        value:
          - ConfiguredAtLaunch: '{{ ConfiguredAtLaunch }}'
            DockerVolumeConfiguration:
              Autoprovision: '{{ Autoprovision }}'
              Driver: '{{ Driver }}'
              DriverOpts: {}
              Labels: {}
              Scope: '{{ Scope }}'
            EFSVolumeConfiguration:
              FilesystemId: '{{ FilesystemId }}'
              RootDirectory: '{{ RootDirectory }}'
              TransitEncryption: '{{ TransitEncryption }}'
              TransitEncryptionPort: '{{ TransitEncryptionPort }}'
              AuthorizationConfig:
                IAM: '{{ IAM }}'
                AccessPointId: '{{ AccessPointId }}'
            FSxWindowsFileServerVolumeConfiguration:
              FileSystemId: '{{ FileSystemId }}'
              RootDirectory: '{{ RootDirectory }}'
              AuthorizationConfig:
                CredentialsParameter: '{{ CredentialsParameter }}'
                Domain: '{{ Domain }}'
            Host:
              SourcePath: '{{ SourcePath }}'
            Name: '{{ Name }}'
      - name: PidMode
        value: '{{ PidMode }}'
      - name: RuntimePlatform
        value:
          CpuArchitecture: '{{ CpuArchitecture }}'
          OperatingSystemFamily: '{{ OperatingSystemFamily }}'
      - name: IpcMode
        value: '{{ IpcMode }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.ecs.task_definitions
WHERE data__Identifier = '<TaskDefinitionArn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>task_definitions</code> resource, the following permissions are required:

### Create
```json
ecs:RegisterTaskDefinition,
ecs:DescribeTaskDefinition,
ecs:TagResource,
iam:GetRole,
iam:PassRole
```

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

### List
```json
ecs:ListTaskDefinitions,
ecs:DescribeTaskDefinition
```

