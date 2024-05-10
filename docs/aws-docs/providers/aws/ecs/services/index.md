---
title: services
hide_title: false
hide_table_of_contents: false
keywords:
  - services
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


Used to retrieve a list of <code>services</code> in a region or to create or delete a <code>services</code> resource, use <code>service</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>services</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The ``AWS::ECS::Service`` resource creates an Amazon Elastic Container Service (Amazon ECS) service that runs and maintains the requested number of tasks and associated load balancers.&lt;br&#x2F;&gt;  The stack update fails if you change any properties that require replacement and at least one Amazon ECS Service Connect ``ServiceConnectService`` is configured. This is because AWS CloudFormation creates the replacement service first, but each ``ServiceConnectService`` must have a name that is unique in the namespace.&lt;br&#x2F;&gt;  Starting April 15, 2023, AWS; will not onboard new customers to Amazon Elastic Inference (EI), and will help current customers migrate their workloads to options that offer better price and performance. After April 15, 2023, new customers will not be able to launch instances with Amazon EI accelerators in Amazon SageMaker, ECS, or EC2. However, customers who have used Amazon EI at least once during the past 30-day period are considered current customers and will be able to continue using the service.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ecs.services" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="service_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="cluster" /></td><td><code>string</code></td><td>The short name or full Amazon Resource Name (ARN) of the cluster that you run your service on. If you do not specify a cluster, the default cluster is assumed.</td></tr>
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
service_arn,
cluster
FROM aws.ecs.services
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
 "CapacityProviderStrategy": [
  {
   "Base": "{{ Base }}",
   "CapacityProvider": "{{ CapacityProvider }}",
   "Weight": "{{ Weight }}"
  }
 ],
 "Cluster": "{{ Cluster }}",
 "DeploymentConfiguration": {
  "DeploymentCircuitBreaker": {
   "Enable": "{{ Enable }}",
   "Rollback": "{{ Rollback }}"
  },
  "MaximumPercent": "{{ MaximumPercent }}",
  "MinimumHealthyPercent": "{{ MinimumHealthyPercent }}",
  "Alarms": {
   "AlarmNames": [
    "{{ AlarmNames[0] }}"
   ],
   "Rollback": "{{ Rollback }}",
   "Enable": "{{ Enable }}"
  }
 },
 "DeploymentController": {
  "Type": "{{ Type }}"
 },
 "DesiredCount": "{{ DesiredCount }}",
 "EnableECSManagedTags": "{{ EnableECSManagedTags }}",
 "EnableExecuteCommand": "{{ EnableExecuteCommand }}",
 "HealthCheckGracePeriodSeconds": "{{ HealthCheckGracePeriodSeconds }}",
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
 "PlacementConstraints": [
  {
   "Expression": "{{ Expression }}",
   "Type": "{{ Type }}"
  }
 ],
 "PlacementStrategies": [
  {
   "Field": "{{ Field }}",
   "Type": "{{ Type }}"
  }
 ],
 "PlatformVersion": "{{ PlatformVersion }}",
 "PropagateTags": "{{ PropagateTags }}",
 "Role": "{{ Role }}",
 "SchedulingStrategy": "{{ SchedulingStrategy }}",
 "ServiceConnectConfiguration": {
  "Enabled": "{{ Enabled }}",
  "Namespace": "{{ Namespace }}",
  "Services": [
   {
    "PortName": "{{ PortName }}",
    "DiscoveryName": "{{ DiscoveryName }}",
    "ClientAliases": [
     {
      "Port": "{{ Port }}",
      "DnsName": "{{ DnsName }}"
     }
    ],
    "IngressPortOverride": "{{ IngressPortOverride }}",
    "Tls": {
     "IssuerCertificateAuthority": {
      "AwsPcaAuthorityArn": "{{ AwsPcaAuthorityArn }}"
     },
     "KmsKey": "{{ KmsKey }}",
     "RoleArn": "{{ RoleArn }}"
    },
    "Timeout": {
     "IdleTimeoutSeconds": "{{ IdleTimeoutSeconds }}",
     "PerRequestTimeoutSeconds": "{{ PerRequestTimeoutSeconds }}"
    }
   }
  ],
  "LogConfiguration": {
   "LogDriver": "{{ LogDriver }}",
   "Options": {},
   "SecretOptions": [
    {
     "Name": "{{ Name }}",
     "ValueFrom": "{{ ValueFrom }}"
    }
   ]
  }
 },
 "ServiceName": "{{ ServiceName }}",
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
 "TaskDefinition": "{{ TaskDefinition }}",
 "VolumeConfigurations": [
  {
   "Name": "{{ Name }}",
   "ManagedEBSVolume": {
    "Encrypted": "{{ Encrypted }}",
    "KmsKeyId": "{{ KmsKeyId }}",
    "VolumeType": "{{ VolumeType }}",
    "SizeInGiB": "{{ SizeInGiB }}",
    "SnapshotId": "{{ SnapshotId }}",
    "Iops": "{{ Iops }}",
    "Throughput": "{{ Throughput }}",
    "TagSpecifications": [
     {
      "ResourceType": "{{ ResourceType }}",
      "Tags": [
       null
      ],
      "PropagateTags": "{{ PropagateTags }}"
     }
    ],
    "RoleArn": "{{ RoleArn }}",
    "FilesystemType": "{{ FilesystemType }}"
   }
  }
 ]
}
>>>
--required properties only
INSERT INTO aws.ecs.services (
 CapacityProviderStrategy,
 Cluster,
 DeploymentConfiguration,
 DeploymentController,
 DesiredCount,
 EnableECSManagedTags,
 EnableExecuteCommand,
 HealthCheckGracePeriodSeconds,
 LaunchType,
 LoadBalancers,
 NetworkConfiguration,
 PlacementConstraints,
 PlacementStrategies,
 PlatformVersion,
 PropagateTags,
 Role,
 SchedulingStrategy,
 ServiceConnectConfiguration,
 ServiceName,
 ServiceRegistries,
 Tags,
 TaskDefinition,
 VolumeConfigurations,
 region
)
SELECT 
{{ CapacityProviderStrategy }},
 {{ Cluster }},
 {{ DeploymentConfiguration }},
 {{ DeploymentController }},
 {{ DesiredCount }},
 {{ EnableECSManagedTags }},
 {{ EnableExecuteCommand }},
 {{ HealthCheckGracePeriodSeconds }},
 {{ LaunchType }},
 {{ LoadBalancers }},
 {{ NetworkConfiguration }},
 {{ PlacementConstraints }},
 {{ PlacementStrategies }},
 {{ PlatformVersion }},
 {{ PropagateTags }},
 {{ Role }},
 {{ SchedulingStrategy }},
 {{ ServiceConnectConfiguration }},
 {{ ServiceName }},
 {{ ServiceRegistries }},
 {{ Tags }},
 {{ TaskDefinition }},
 {{ VolumeConfigurations }},
'us-east-1';
```

</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "CapacityProviderStrategy": [
  {
   "Base": "{{ Base }}",
   "CapacityProvider": "{{ CapacityProvider }}",
   "Weight": "{{ Weight }}"
  }
 ],
 "Cluster": "{{ Cluster }}",
 "DeploymentConfiguration": {
  "DeploymentCircuitBreaker": {
   "Enable": "{{ Enable }}",
   "Rollback": "{{ Rollback }}"
  },
  "MaximumPercent": "{{ MaximumPercent }}",
  "MinimumHealthyPercent": "{{ MinimumHealthyPercent }}",
  "Alarms": {
   "AlarmNames": [
    "{{ AlarmNames[0] }}"
   ],
   "Rollback": "{{ Rollback }}",
   "Enable": "{{ Enable }}"
  }
 },
 "DeploymentController": {
  "Type": "{{ Type }}"
 },
 "DesiredCount": "{{ DesiredCount }}",
 "EnableECSManagedTags": "{{ EnableECSManagedTags }}",
 "EnableExecuteCommand": "{{ EnableExecuteCommand }}",
 "HealthCheckGracePeriodSeconds": "{{ HealthCheckGracePeriodSeconds }}",
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
 "PlacementConstraints": [
  {
   "Expression": "{{ Expression }}",
   "Type": "{{ Type }}"
  }
 ],
 "PlacementStrategies": [
  {
   "Field": "{{ Field }}",
   "Type": "{{ Type }}"
  }
 ],
 "PlatformVersion": "{{ PlatformVersion }}",
 "PropagateTags": "{{ PropagateTags }}",
 "Role": "{{ Role }}",
 "SchedulingStrategy": "{{ SchedulingStrategy }}",
 "ServiceConnectConfiguration": {
  "Enabled": "{{ Enabled }}",
  "Namespace": "{{ Namespace }}",
  "Services": [
   {
    "PortName": "{{ PortName }}",
    "DiscoveryName": "{{ DiscoveryName }}",
    "ClientAliases": [
     {
      "Port": "{{ Port }}",
      "DnsName": "{{ DnsName }}"
     }
    ],
    "IngressPortOverride": "{{ IngressPortOverride }}",
    "Tls": {
     "IssuerCertificateAuthority": {
      "AwsPcaAuthorityArn": "{{ AwsPcaAuthorityArn }}"
     },
     "KmsKey": "{{ KmsKey }}",
     "RoleArn": "{{ RoleArn }}"
    },
    "Timeout": {
     "IdleTimeoutSeconds": "{{ IdleTimeoutSeconds }}",
     "PerRequestTimeoutSeconds": "{{ PerRequestTimeoutSeconds }}"
    }
   }
  ],
  "LogConfiguration": {
   "LogDriver": "{{ LogDriver }}",
   "Options": {},
   "SecretOptions": [
    {
     "Name": "{{ Name }}",
     "ValueFrom": "{{ ValueFrom }}"
    }
   ]
  }
 },
 "ServiceName": "{{ ServiceName }}",
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
 "TaskDefinition": "{{ TaskDefinition }}",
 "VolumeConfigurations": [
  {
   "Name": "{{ Name }}",
   "ManagedEBSVolume": {
    "Encrypted": "{{ Encrypted }}",
    "KmsKeyId": "{{ KmsKeyId }}",
    "VolumeType": "{{ VolumeType }}",
    "SizeInGiB": "{{ SizeInGiB }}",
    "SnapshotId": "{{ SnapshotId }}",
    "Iops": "{{ Iops }}",
    "Throughput": "{{ Throughput }}",
    "TagSpecifications": [
     {
      "ResourceType": "{{ ResourceType }}",
      "Tags": [
       null
      ],
      "PropagateTags": "{{ PropagateTags }}"
     }
    ],
    "RoleArn": "{{ RoleArn }}",
    "FilesystemType": "{{ FilesystemType }}"
   }
  }
 ]
}
>>>
--all properties
INSERT INTO aws.ecs.services (
 CapacityProviderStrategy,
 Cluster,
 DeploymentConfiguration,
 DeploymentController,
 DesiredCount,
 EnableECSManagedTags,
 EnableExecuteCommand,
 HealthCheckGracePeriodSeconds,
 LaunchType,
 LoadBalancers,
 NetworkConfiguration,
 PlacementConstraints,
 PlacementStrategies,
 PlatformVersion,
 PropagateTags,
 Role,
 SchedulingStrategy,
 ServiceConnectConfiguration,
 ServiceName,
 ServiceRegistries,
 Tags,
 TaskDefinition,
 VolumeConfigurations,
 region
)
SELECT 
 {{ CapacityProviderStrategy }},
 {{ Cluster }},
 {{ DeploymentConfiguration }},
 {{ DeploymentController }},
 {{ DesiredCount }},
 {{ EnableECSManagedTags }},
 {{ EnableExecuteCommand }},
 {{ HealthCheckGracePeriodSeconds }},
 {{ LaunchType }},
 {{ LoadBalancers }},
 {{ NetworkConfiguration }},
 {{ PlacementConstraints }},
 {{ PlacementStrategies }},
 {{ PlatformVersion }},
 {{ PropagateTags }},
 {{ Role }},
 {{ SchedulingStrategy }},
 {{ ServiceConnectConfiguration }},
 {{ ServiceName }},
 {{ ServiceRegistries }},
 {{ Tags }},
 {{ TaskDefinition }},
 {{ VolumeConfigurations }},
 'us-east-1';
```

</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.ecs.services
WHERE data__Identifier = '<ServiceArn|Cluster>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>services</code> resource, the following permissions are required:

### Create
```json
ecs:CreateService,
ecs:DescribeServices,
iam:PassRole,
ecs:TagResource
```

### Delete
```json
ecs:DeleteService,
ecs:DescribeServices
```

### List
```json
ecs:DescribeServices,
ecs:ListClusters,
ecs:ListServices
```

