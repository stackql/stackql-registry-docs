---
title: container_group_definitions
hide_title: false
hide_table_of_contents: false
keywords:
  - container_group_definitions
  - gamelift
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

Creates, updates, deletes or gets a <code>container_group_definition</code> resource or lists <code>container_group_definitions</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>container_group_definitions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::GameLift::ContainerGroupDefinition resource creates an Amazon GameLift container group definition.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.gamelift.container_group_definitions" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="container_group_definition_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) that is assigned to a Amazon GameLift container group resource and uniquely identifies it across all AWS Regions.</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>A descriptive label for the container group definition.</td></tr>
<tr><td><CopyableCode code="creation_time" /></td><td><code>string</code></td><td>A time stamp indicating when this data object was created. Format is a number expressed in Unix time as milliseconds (for example "1469498468.057").</td></tr>
<tr><td><CopyableCode code="scheduling_strategy" /></td><td><code>string</code></td><td>Specifies whether the container group includes replica or daemon containers.</td></tr>
<tr><td><CopyableCode code="total_memory_limit" /></td><td><code>integer</code></td><td>The maximum amount of memory (in MiB) to allocate for this container group.</td></tr>
<tr><td><CopyableCode code="total_cpu_limit" /></td><td><code>integer</code></td><td>The maximum number of CPU units reserved for this container group. The value is expressed as an integer amount of CPU units. (1 vCPU is equal to 1024 CPU units.)</td></tr>
<tr><td><CopyableCode code="container_definitions" /></td><td><code>array</code></td><td>A collection of container definitions that define the containers in this group.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
<tr><td><CopyableCode code="operating_system" /></td><td><code>string</code></td><td>The operating system of the container group</td></tr>
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
    <td><CopyableCode code="Name, TotalMemoryLimit, TotalCpuLimit, ContainerDefinitions, OperatingSystem, region" /></td>
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
Gets all <code>container_group_definitions</code> in a region.
```sql
SELECT
region,
container_group_definition_arn,
name,
creation_time,
scheduling_strategy,
total_memory_limit,
total_cpu_limit,
container_definitions,
tags,
operating_system
FROM aws.gamelift.container_group_definitions
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>container_group_definition</code>.
```sql
SELECT
region,
container_group_definition_arn,
name,
creation_time,
scheduling_strategy,
total_memory_limit,
total_cpu_limit,
container_definitions,
tags,
operating_system
FROM aws.gamelift.container_group_definitions
WHERE region = 'us-east-1' AND data__Identifier = '<Name>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>container_group_definition</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.gamelift.container_group_definitions (
 Name,
 TotalMemoryLimit,
 TotalCpuLimit,
 ContainerDefinitions,
 OperatingSystem,
 region
)
SELECT 
'{{ Name }}',
 '{{ TotalMemoryLimit }}',
 '{{ TotalCpuLimit }}',
 '{{ ContainerDefinitions }}',
 '{{ OperatingSystem }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.gamelift.container_group_definitions (
 Name,
 SchedulingStrategy,
 TotalMemoryLimit,
 TotalCpuLimit,
 ContainerDefinitions,
 Tags,
 OperatingSystem,
 region
)
SELECT 
 '{{ Name }}',
 '{{ SchedulingStrategy }}',
 '{{ TotalMemoryLimit }}',
 '{{ TotalCpuLimit }}',
 '{{ ContainerDefinitions }}',
 '{{ Tags }}',
 '{{ OperatingSystem }}',
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
  - name: container_group_definition
    props:
      - name: Name
        value: '{{ Name }}'
      - name: SchedulingStrategy
        value: '{{ SchedulingStrategy }}'
      - name: TotalMemoryLimit
        value: '{{ TotalMemoryLimit }}'
      - name: TotalCpuLimit
        value: '{{ TotalCpuLimit }}'
      - name: ContainerDefinitions
        value:
          - ContainerName: '{{ ContainerName }}'
            ImageUri: '{{ ImageUri }}'
            ResolvedImageDigest: '{{ ResolvedImageDigest }}'
            MemoryLimits:
              SoftLimit: '{{ SoftLimit }}'
              HardLimit: '{{ HardLimit }}'
            PortConfiguration:
              ContainerPortRanges:
                - FromPort: '{{ FromPort }}'
                  Protocol: '{{ Protocol }}'
                  ToPort: '{{ ToPort }}'
            Cpu: '{{ Cpu }}'
            HealthCheck:
              Command:
                - '{{ Command[0] }}'
              Interval: '{{ Interval }}'
              Timeout: '{{ Timeout }}'
              Retries: '{{ Retries }}'
              StartPeriod: '{{ StartPeriod }}'
            Command:
              - '{{ Command[0] }}'
            Essential: '{{ Essential }}'
            EntryPoint:
              - '{{ EntryPoint[0] }}'
            WorkingDirectory: '{{ WorkingDirectory }}'
            Environment:
              - Name: '{{ Name }}'
                Value: '{{ Value }}'
            DependsOn:
              - ContainerName: '{{ ContainerName }}'
                Condition: '{{ Condition }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'
      - name: OperatingSystem
        value: '{{ OperatingSystem }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.gamelift.container_group_definitions
WHERE data__Identifier = '<Name>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>container_group_definitions</code> resource, the following permissions are required:

### Create
```json
gamelift:CreateContainerGroupDefinition,
gamelift:DescribeContainerGroupDefinition,
gamelift:ListTagsForResource,
gamelift:TagResource,
ecr:BatchCheckLayerAvailability,
ecr:BatchGetImage,
ecr:GetDownloadUrlForLayer,
ecr:DescribeImages
```

### Read
```json
gamelift:DescribeContainerGroupDefinition,
gamelift:ListTagsForResource
```

### Update
```json
gamelift:ListTagsForResource,
gamelift:TagResource,
gamelift:UntagResource
```

### Delete
```json
gamelift:DescribeContainerGroupDefinition,
gamelift:DeleteContainerGroupDefinition
```

### List
```json
gamelift:ListContainerGroupDefinitions
```

