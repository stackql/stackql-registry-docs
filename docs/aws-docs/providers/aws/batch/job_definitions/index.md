---
title: job_definitions
hide_title: false
hide_table_of_contents: false
keywords:
  - job_definitions
  - batch
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

Creates, updates, deletes or gets a <code>job_definition</code> resource or lists <code>job_definitions</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>job_definitions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::Batch::JobDefinition</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.batch.job_definitions" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="parameters" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="timeout" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="job_definition_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="propagate_tags" /></td><td><code>boolean</code></td><td></td></tr>
<tr><td><CopyableCode code="platform_capabilities" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="eks_properties" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="type" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="node_properties" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="scheduling_priority" /></td><td><code>integer</code></td><td></td></tr>
<tr><td><CopyableCode code="container_properties" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="ecs_properties" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="retry_strategy" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>object</code></td><td>A key-value pair to associate with a resource.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-batch-jobdefinition.html"><code>AWS::Batch::JobDefinition</code></a>.

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
    <td><CopyableCode code="Type, region" /></td>
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
    <td><CopyableCode code="list_resources" /></td>
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
Gets all <code>job_definitions</code> in a region.
```sql
SELECT
region,
parameters,
timeout,
job_definition_name,
propagate_tags,
platform_capabilities,
eks_properties,
type,
node_properties,
scheduling_priority,
container_properties,
ecs_properties,
retry_strategy,
tags
FROM aws.batch.job_definitions
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>job_definition</code>.
```sql
SELECT
region,
parameters,
timeout,
job_definition_name,
propagate_tags,
platform_capabilities,
eks_properties,
type,
node_properties,
scheduling_priority,
container_properties,
ecs_properties,
retry_strategy,
tags
FROM aws.batch.job_definitions
WHERE region = 'us-east-1' AND data__Identifier = '<JobDefinitionName>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>job_definition</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.batch.job_definitions (
 Type,
 region
)
SELECT 
'{{ Type }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.batch.job_definitions (
 Parameters,
 Timeout,
 JobDefinitionName,
 PropagateTags,
 PlatformCapabilities,
 EksProperties,
 Type,
 NodeProperties,
 SchedulingPriority,
 ContainerProperties,
 EcsProperties,
 RetryStrategy,
 Tags,
 region
)
SELECT 
 '{{ Parameters }}',
 '{{ Timeout }}',
 '{{ JobDefinitionName }}',
 '{{ PropagateTags }}',
 '{{ PlatformCapabilities }}',
 '{{ EksProperties }}',
 '{{ Type }}',
 '{{ NodeProperties }}',
 '{{ SchedulingPriority }}',
 '{{ ContainerProperties }}',
 '{{ EcsProperties }}',
 '{{ RetryStrategy }}',
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
  - name: job_definition
    props:
      - name: Parameters
        value: {}
      - name: Timeout
        value:
          AttemptDurationSeconds: '{{ AttemptDurationSeconds }}'
      - name: JobDefinitionName
        value: '{{ JobDefinitionName }}'
      - name: PropagateTags
        value: '{{ PropagateTags }}'
      - name: PlatformCapabilities
        value:
          - '{{ PlatformCapabilities[0] }}'
      - name: EksProperties
        value:
          PodProperties:
            InitContainers:
              - Args:
                  - '{{ Args[0] }}'
                VolumeMounts:
                  - MountPath: '{{ MountPath }}'
                    ReadOnly: '{{ ReadOnly }}'
                    Name: '{{ Name }}'
                ImagePullPolicy: '{{ ImagePullPolicy }}'
                Command:
                  - '{{ Command[0] }}'
                SecurityContext:
                  RunAsUser: '{{ RunAsUser }}'
                  AllowPrivilegeEscalation: '{{ AllowPrivilegeEscalation }}'
                  RunAsNonRoot: '{{ RunAsNonRoot }}'
                  Privileged: '{{ Privileged }}'
                  ReadOnlyRootFilesystem: '{{ ReadOnlyRootFilesystem }}'
                  RunAsGroup: '{{ RunAsGroup }}'
                Resources:
                  Limits: {}
                  Requests: {}
                Image: '{{ Image }}'
                Env:
                  - Value: '{{ Value }}'
                    Name: '{{ Name }}'
                Name: '{{ Name }}'
            Volumes:
              - Secret:
                  SecretName: '{{ SecretName }}'
                  Optional: '{{ Optional }}'
                EmptyDir:
                  Medium: '{{ Medium }}'
                  SizeLimit: '{{ SizeLimit }}'
                HostPath:
                  Path: '{{ Path }}'
                Name: '{{ Name }}'
            DnsPolicy: '{{ DnsPolicy }}'
            Containers:
              - null
            Metadata:
              Labels: {}
            ServiceAccountName: '{{ ServiceAccountName }}'
            ImagePullSecrets:
              - Name: '{{ Name }}'
            HostNetwork: '{{ HostNetwork }}'
            ShareProcessNamespace: '{{ ShareProcessNamespace }}'
      - name: Type
        value: '{{ Type }}'
      - name: NodeProperties
        value:
          MainNode: '{{ MainNode }}'
          NodeRangeProperties:
            - Container:
                RepositoryCredentials:
                  CredentialsParameter: '{{ CredentialsParameter }}'
                User: '{{ User }}'
                Secrets:
                  - ValueFrom: '{{ ValueFrom }}'
                    Name: '{{ Name }}'
                Memory: '{{ Memory }}'
                Privileged: '{{ Privileged }}'
                LinuxParameters:
                  Swappiness: '{{ Swappiness }}'
                  Tmpfs:
                    - Size: '{{ Size }}'
                      ContainerPath: '{{ ContainerPath }}'
                      MountOptions:
                        - '{{ MountOptions[0] }}'
                  SharedMemorySize: '{{ SharedMemorySize }}'
                  Devices:
                    - HostPath: '{{ HostPath }}'
                      Permissions:
                        - '{{ Permissions[0] }}'
                      ContainerPath: '{{ ContainerPath }}'
                  InitProcessEnabled: '{{ InitProcessEnabled }}'
                  MaxSwap: '{{ MaxSwap }}'
                JobRoleArn: '{{ JobRoleArn }}'
                ReadonlyRootFilesystem: '{{ ReadonlyRootFilesystem }}'
                Vcpus: '{{ Vcpus }}'
                Image: '{{ Image }}'
                ResourceRequirements:
                  - Type: '{{ Type }}'
                    Value: '{{ Value }}'
                LogConfiguration:
                  SecretOptions:
                    - null
                  Options: {}
                  LogDriver: '{{ LogDriver }}'
                MountPoints:
                  - ReadOnly: '{{ ReadOnly }}'
                    SourceVolume: '{{ SourceVolume }}'
                    ContainerPath: '{{ ContainerPath }}'
                ExecutionRoleArn: '{{ ExecutionRoleArn }}'
                RuntimePlatform:
                  OperatingSystemFamily: '{{ OperatingSystemFamily }}'
                  CpuArchitecture: '{{ CpuArchitecture }}'
                Volumes:
                  - Host:
                      SourcePath: '{{ SourcePath }}'
                    EfsVolumeConfiguration:
                      TransitEncryption: '{{ TransitEncryption }}'
                      AuthorizationConfig:
                        Iam: '{{ Iam }}'
                        AccessPointId: '{{ AccessPointId }}'
                      FileSystemId: '{{ FileSystemId }}'
                      RootDirectory: '{{ RootDirectory }}'
                      TransitEncryptionPort: '{{ TransitEncryptionPort }}'
                    Name: '{{ Name }}'
                Command:
                  - '{{ Command[0] }}'
                Environment:
                  - Value: '{{ Value }}'
                    Name: '{{ Name }}'
                Ulimits:
                  - SoftLimit: '{{ SoftLimit }}'
                    HardLimit: '{{ HardLimit }}'
                    Name: '{{ Name }}'
                InstanceType: '{{ InstanceType }}'
                EphemeralStorage:
                  SizeInGiB: '{{ SizeInGiB }}'
              TargetNodes: '{{ TargetNodes }}'
              EcsProperties:
                TaskProperties:
                  - ExecutionRoleArn: '{{ ExecutionRoleArn }}'
                    TaskRoleArn: '{{ TaskRoleArn }}'
                    IpcMode: '{{ IpcMode }}'
                    Volumes:
                      - null
                    Containers:
                      - RepositoryCredentials: null
                        User: '{{ User }}'
                        Secrets:
                          - null
                        Privileged: '{{ Privileged }}'
                        LinuxParameters: null
                        ReadonlyRootFilesystem: '{{ ReadonlyRootFilesystem }}'
                        Image: '{{ Image }}'
                        LogConfiguration: null
                        Essential: '{{ Essential }}'
                        ResourceRequirements:
                          - null
                        Name: '{{ Name }}'
                        MountPoints:
                          - null
                        DependsOn:
                          - Condition: '{{ Condition }}'
                            ContainerName: '{{ ContainerName }}'
                        Command:
                          - '{{ Command[0] }}'
                        Environment:
                          - null
                        Ulimits:
                          - null
                    PidMode: '{{ PidMode }}'
              InstanceTypes:
                - '{{ InstanceTypes[0] }}'
              EksProperties: null
          NumNodes: '{{ NumNodes }}'
      - name: SchedulingPriority
        value: '{{ SchedulingPriority }}'
      - name: ContainerProperties
        value:
          RepositoryCredentials: null
          User: '{{ User }}'
          Secrets:
            - null
          Memory: '{{ Memory }}'
          Privileged: '{{ Privileged }}'
          LinuxParameters: null
          FargatePlatformConfiguration:
            PlatformVersion: '{{ PlatformVersion }}'
          JobRoleArn: '{{ JobRoleArn }}'
          ReadonlyRootFilesystem: '{{ ReadonlyRootFilesystem }}'
          Vcpus: '{{ Vcpus }}'
          Image: '{{ Image }}'
          ResourceRequirements:
            - null
          LogConfiguration: null
          MountPoints:
            - null
          ExecutionRoleArn: '{{ ExecutionRoleArn }}'
          RuntimePlatform: null
          Volumes:
            - null
          Command:
            - '{{ Command[0] }}'
          Environment:
            - null
          Ulimits:
            - null
          NetworkConfiguration:
            AssignPublicIp: '{{ AssignPublicIp }}'
          EphemeralStorage: null
      - name: EcsProperties
        value:
          TaskProperties:
            - PlatformVersion: '{{ PlatformVersion }}'
              ExecutionRoleArn: '{{ ExecutionRoleArn }}'
              RuntimePlatform: null
              TaskRoleArn: '{{ TaskRoleArn }}'
              IpcMode: '{{ IpcMode }}'
              Volumes:
                - null
              Containers:
                - null
              NetworkConfiguration: null
              PidMode: '{{ PidMode }}'
              EphemeralStorage: null
      - name: RetryStrategy
        value:
          EvaluateOnExit:
            - Action: '{{ Action }}'
              OnExitCode: '{{ OnExitCode }}'
              OnReason: '{{ OnReason }}'
              OnStatusReason: '{{ OnStatusReason }}'
          Attempts: '{{ Attempts }}'
      - name: Tags
        value: {}

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.batch.job_definitions
WHERE data__Identifier = '<JobDefinitionName>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>job_definitions</code> resource, the following permissions are required:

### Read
```json
Batch:DescribeJobDefinitions
```

### Create
```json
Batch:RegisterJobDefinition,
Batch:TagResource,
Batch:DescribeJobDefinitions,
Iam:PassRole
```

### Update
```json
Batch:DescribeJobDefinitions,
Batch:RegisterJobDefinition,
Batch:DeregisterJobDefinition,
Batch:TagResource,
Batch:UntagResource,
Iam:PassRole
```

### List
```json
Batch:DescribeJobDefinitions
```

### Delete
```json
Batch:DescribeJobDefinitions,
Batch:DeregisterJobDefinition,
Iam:PassRole
```
