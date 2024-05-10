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


Used to retrieve a list of <code>task_sets</code> in a region or to create or delete a <code>task_sets</code> resource, use <code>task_set</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>task_sets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Create a task set in the specified cluster and service. This is used when a service uses the EXTERNAL deployment controller type. For more information, see https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;AmazonECS&#x2F;latest&#x2F;developerguide&#x2F;deployment-types.htmlin the Amazon Elastic Container Service Developer Guide.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ecs.task_sets" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="cluster" /></td><td><code>string</code></td><td>The short name or full Amazon Resource Name (ARN) of the cluster that hosts the service to create the task set in.</td></tr>
<tr><td><CopyableCode code="service" /></td><td><code>string</code></td><td>The short name or full Amazon Resource Name (ARN) of the service to create the task set in.</td></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td>The ID of the task set.</td></tr>
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
cluster,
service,
id
FROM aws.ecs.task_sets
WHERE region = 'us-east-1';
```

## `INSERT` Example

<Tabs
    defaultValue="required"
    values={[
      { label: 'Required Properties', value: 'required', },
      { label: 'All Properties', value: 'all', },
    ]
}>
<TabItem value="required">

```sql
<<<json
{
 "Cluster": "{{ Cluster }}",
 "Service": "{{ Service }}",
 "TaskDefinition": "{{ TaskDefinition }}"
}
>>>
--required properties only
INSERT INTO aws.ecs.task_sets (
 Cluster,
 Service,
 TaskDefinition,
 region
)
SELECT 
{{ .Cluster }},
 {{ .Service }},
 {{ .TaskDefinition }},
'us-east-1';
```
</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "Cluster": "{{ Cluster }}",
 "ExternalId": "{{ ExternalId }}",
 "LaunchType": "{{ LaunchType }}",
 "LoadBalancers": [
  {
   "ContainerName": "{{ ContainerName }}",
   "ContainerPort": "{{ ContainerPort }}",
   "TargetGroupArn": "{{ TargetGroupArn }}"
  }
 ],
 "NetworkConfiguration": {
  "AwsVpcConfiguration": {
   "AssignPublicIp": "{{ AssignPublicIp }}",
   "SecurityGroups": [
    "{{ SecurityGroups[0] }}"
   ],
   "Subnets": [
    "{{ Subnets[0] }}"
   ]
  }
 },
 "PlatformVersion": "{{ PlatformVersion }}",
 "Scale": {
  "Unit": "{{ Unit }}",
  "Value": null
 },
 "Service": "{{ Service }}",
 "ServiceRegistries": [
  {
   "ContainerName": "{{ ContainerName }}",
   "ContainerPort": "{{ ContainerPort }}",
   "Port": "{{ Port }}",
   "RegistryArn": "{{ RegistryArn }}"
  }
 ],
 "Tags": [
  {
   "Key": "{{ Key }}",
   "Value": "{{ Value }}"
  }
 ],
 "TaskDefinition": "{{ TaskDefinition }}"
}
>>>
--all properties
INSERT INTO aws.ecs.task_sets (
 Cluster,
 ExternalId,
 LaunchType,
 LoadBalancers,
 NetworkConfiguration,
 PlatformVersion,
 Scale,
 Service,
 ServiceRegistries,
 Tags,
 TaskDefinition,
 region
)
SELECT 
 {{ .Cluster }},
 {{ .ExternalId }},
 {{ .LaunchType }},
 {{ .LoadBalancers }},
 {{ .NetworkConfiguration }},
 {{ .PlatformVersion }},
 {{ .Scale }},
 {{ .Service }},
 {{ .ServiceRegistries }},
 {{ .Tags }},
 {{ .TaskDefinition }},
 'us-east-1';
```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.ecs.task_sets
WHERE data__Identifier = '<Cluster|Service|Id>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>task_sets</code> resource, the following permissions are required:

### Create
```json
ecs:CreateTaskSet,
ecs:DescribeTaskSets,
ecs:TagResource
```

### Delete
```json
ecs:DeleteTaskSet,
ecs:DescribeTaskSets
```

