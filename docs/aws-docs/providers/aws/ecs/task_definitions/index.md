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


Used to retrieve a list of <code>task_definitions</code> in a region or to create or delete a <code>task_definitions</code> resource, use <code>task_definition</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>task_definitions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Registers a new task definition from the supplied ``family`` and ``containerDefinitions``. Optionally, you can add data volumes to your containers with the ``volumes`` parameter. For more information about task definition parameters and defaults, see &#91;Amazon ECS Task Definitions&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;AmazonECS&#x2F;latest&#x2F;developerguide&#x2F;task_defintions.html) in the *Amazon Elastic Container Service Developer Guide*.&lt;br&#x2F;&gt; You can specify a role for your task with the ``taskRoleArn`` parameter. When you specify a role for a task, its containers can then use the latest versions of the CLI or SDKs to make API requests to the AWS services that are specified in the policy that's associated with the role. For more information, see &#91;IAM Roles for Tasks&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;AmazonECS&#x2F;latest&#x2F;developerguide&#x2F;task-iam-roles.html) in the *Amazon Elastic Container Service Developer Guide*.&lt;br&#x2F;&gt; You can specify a Docker networking mode for the containers in your task definition with the ``networkMode`` parameter. The available network modes correspond to those described in &#91;Network settings&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;https:&#x2F;&#x2F;docs.docker.com&#x2F;engine&#x2F;reference&#x2F;run&#x2F;#&#x2F;network-settings) in the Docker run reference. If you specify the ``awsvpc`` network mode, the task is allocated an elastic network interface, and you must specify a NetworkConfiguration when you create a service or run a task with the task definition. For more information, see &#91;Task Networking&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;AmazonECS&#x2F;latest&#x2F;developerguide&#x2F;task-networking.html) in the *Amazon Elastic Container Service Developer Guide*.&lt;br&#x2F;&gt;  In the following example or examples, the Authorization header contents (``AUTHPARAMS``) must be replaced with an AWS Signature Version 4 signature. For more information, see &#91;Signature Version 4 Signing Process&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;general&#x2F;latest&#x2F;gr&#x2F;signature-version-4.html) in the *General Reference*.&lt;br&#x2F;&gt; You only need to learn how to sign HTTP requests if you intend to create them manually. When you use the &#91;&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;cli&#x2F;) or one of the &#91;SDKs&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;tools&#x2F;) to make requests to AWS, these tools automatically sign the requests for you, with the access key that you specify when you configure the tools. When you use these tools, you don't have to sign requests yourself.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ecs.task_definitions" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="task_definition_arn" /></td><td><code>string</code></td><td></td></tr>
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
    <td><CopyableCode code="data__DesiredState, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="list_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
task_definition_arn
FROM aws.ecs.task_definitions
WHERE region = 'us-east-1';
```

## `INSERT` Example

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
-- task_definition.iql (required properties only)
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
-- task_definition.iql (all properties)
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

## `DELETE` Example

```sql
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

