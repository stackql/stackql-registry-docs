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

Creates, updates, deletes or gets a <code>service</code> resource or lists <code>services</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>services</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The <code>AWS::ECS::Service</code> resource creates an Amazon Elastic Container Service (Amazon ECS) service that runs and maintains the requested number of tasks and associated load balancers.<br />The stack update fails if you change any properties that require replacement and at least one ECS Service Connect <code>ServiceConnectConfiguration</code> property the is configured. This is because AWS CloudFormation creates the replacement service first, but each <code>ServiceConnectService</code> must have a name that is unique in the namespace.<br />Starting April 15, 2023, AWS; will not onboard new customers to Amazon Elastic Inference (EI), and will help current customers migrate their workloads to options that offer better price and performance. After April 15, 2023, new customers will not be able to launch instances with Amazon EI accelerators in Amazon SageMaker, ECS, or EC2. However, customers who have used Amazon EI at least once during the past 30-day period are considered current customers and will be able to continue using the service.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ecs.services" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="platform_version" /></td><td><code>string</code></td><td>The platform version that your tasks in the service are running on. A platform version is specified only for tasks using the Fargate launch type. If one isn't specified, the <code>LATEST</code> platform version is used. For more information, see &#91;platform versions&#93;(https://docs.aws.amazon.com/AmazonECS/latest/developerguide/platform_versions.html) in the *Amazon Elastic Container Service Developer Guide*.</td></tr>
<tr><td><CopyableCode code="propagate_tags" /></td><td><code>string</code></td><td>Specifies whether to propagate the tags from the task definition to the task. If no value is specified, the tags aren't propagated. Tags can only be propagated to the task during task creation. To add tags to a task after task creation, use the &#91;TagResource&#93;(https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_TagResource.html) API action.<br />You must set this to a value other than <code>NONE</code> when you use Cost Explorer. For more information, see &#91;Amazon ECS usage reports&#93;(https://docs.aws.amazon.com/AmazonECS/latest/developerguide/usage-reports.html) in the *Amazon Elastic Container Service Developer Guide*.<br />The default is <code>NONE</code>.</td></tr>
<tr><td><CopyableCode code="service_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="placement_strategies" /></td><td><code>array</code></td><td>The placement strategy objects to use for tasks in your service. You can specify a maximum of 5 strategy rules for each service.</td></tr>
<tr><td><CopyableCode code="service_registries" /></td><td><code>array</code></td><td>The details of the service discovery registry to associate with this service. For more information, see &#91;Service discovery&#93;(https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-discovery.html).<br />Each service may be associated with one service registry. Multiple service registries for each service isn't supported.</td></tr>
<tr><td><CopyableCode code="volume_configurations" /></td><td><code>array</code></td><td>The configuration for a volume specified in the task definition as a volume that is configured at launch time. Currently, the only supported volume type is an Amazon EBS volume.</td></tr>
<tr><td><CopyableCode code="capacity_provider_strategy" /></td><td><code>array</code></td><td>The capacity provider strategy to use for the service.<br />If a <code>capacityProviderStrategy</code> is specified, the <code>launchType</code> parameter must be omitted. If no <code>capacityProviderStrategy</code> or <code>launchType</code> is specified, the <code>defaultCapacityProviderStrategy</code> for the cluster is used.<br />A capacity provider strategy can contain a maximum of 20 capacity providers.</td></tr>
<tr><td><CopyableCode code="launch_type" /></td><td><code>string</code></td><td>The launch type on which to run your service. For more information, see &#91;Amazon ECS Launch Types&#93;(https://docs.aws.amazon.com/AmazonECS/latest/developerguide/launch_types.html) in the *Amazon Elastic Container Service Developer Guide*.</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="availability_zone_rebalancing" /></td><td><code>string</code></td><td>Indicates whether to use Availability Zone rebalancing for the service.<br />For more information, see &#91;Balancing an Amazon ECS service across Availability Zones&#93;(https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-rebalancing.html) in the *Amazon Elastic Container Service Developer Guide*.</td></tr>
<tr><td><CopyableCode code="scheduling_strategy" /></td><td><code>string</code></td><td>The scheduling strategy to use for the service. For more information, see &#91;Services&#93;(https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs_services.html).<br />There are two service scheduler strategies available:<br />+ <code>REPLICA</code>-The replica scheduling strategy places and maintains the desired number of tasks across your cluster. By default, the service scheduler spreads tasks across Availability Zones. You can use task placement strategies and constraints to customize task placement decisions. This scheduler strategy is required if the service uses the <code>CODE_DEPLOY</code> or <code>EXTERNAL</code> deployment controller types.<br />+ <code>DAEMON</code>-The daemon scheduling strategy deploys exactly one task on each active container instance that meets all of the task placement constraints that you specify in your cluster. The service scheduler also evaluates the task placement constraints for running tasks and will stop tasks that don't meet the placement constraints. When you're using this strategy, you don't need to specify a desired number of tasks, a task placement strategy, or use Service Auto Scaling policies.<br />Tasks using the Fargate launch type or the <code>CODE_DEPLOY</code> or <code>EXTERNAL</code> deployment controller types don't support the <code>DAEMON</code> scheduling strategy.</td></tr>
<tr><td><CopyableCode code="network_configuration" /></td><td><code>object</code></td><td>The network configuration for the service. This parameter is required for task definitions that use the <code>awsvpc</code> network mode to receive their own elastic network interface, and it is not supported for other network modes. For more information, see &#91;Task Networking&#93;(https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-networking.html) in the *Amazon Elastic Container Service Developer Guide*.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>The metadata that you apply to the service to help you categorize and organize them. Each tag consists of a key and an optional value, both of which you define. When a service is deleted, the tags are deleted as well.<br />The following basic restrictions apply to tags:<br />+ Maximum number of tags per resource - 50<br />+ For each resource, each tag key must be unique, and each tag key can have only one value.<br />+ Maximum key length - 128 Unicode characters in UTF-8<br />+ Maximum value length - 256 Unicode characters in UTF-8<br />+ If your tagging schema is used across multiple services and resources, remember that other services may have restrictions on allowed characters. Generally allowed characters are: letters, numbers, and spaces representable in UTF-8, and the following characters: + - = . _ : / @.<br />+ Tag keys and values are case-sensitive.<br />+ Do not use <code>aws:</code>, <code>AWS:</code>, or any upper or lowercase combination of such as a prefix for either keys or values as it is reserved for AWS use. You cannot edit or delete tag keys or values with this prefix. Tags with this prefix do not count against your tags per resource limit.</td></tr>
<tr><td><CopyableCode code="health_check_grace_period_seconds" /></td><td><code>integer</code></td><td>The period of time, in seconds, that the Amazon ECS service scheduler ignores unhealthy Elastic Load Balancing, VPC Lattice, and container health checks after a task has first started. If you don't specify a health check grace period value, the default value of <code>0</code> is used. If you don't use any of the health checks, then <code>healthCheckGracePeriodSeconds</code> is unused.<br />If your service's tasks take a while to start and respond to health checks, you can specify a health check grace period of up to 2,147,483,647 seconds (about 69 years). During that time, the Amazon ECS service scheduler ignores health check status. This grace period can prevent the service scheduler from marking tasks as unhealthy and stopping them before they have time to come up.</td></tr>
<tr><td><CopyableCode code="enable_ecs_managed_tags" /></td><td><code>boolean</code></td><td>Specifies whether to turn on Amazon ECS managed tags for the tasks within the service. For more information, see &#91;Tagging your Amazon ECS resources&#93;(https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-using-tags.html) in the *Amazon Elastic Container Service Developer Guide*.<br />When you use Amazon ECS managed tags, you need to set the <code>propagateTags</code> request parameter.</td></tr>
<tr><td><CopyableCode code="enable_execute_command" /></td><td><code>boolean</code></td><td>Determines whether the execute command functionality is turned on for the service. If <code>true</code>, the execute command functionality is turned on for all containers in tasks as part of the service.</td></tr>
<tr><td><CopyableCode code="placement_constraints" /></td><td><code>array</code></td><td>An array of placement constraint objects to use for tasks in your service. You can specify a maximum of 10 constraints for each task. This limit includes constraints in the task definition and those specified at runtime.</td></tr>
<tr><td><CopyableCode code="cluster" /></td><td><code>string</code></td><td>The short name or full Amazon Resource Name (ARN) of the cluster that you run your service on. If you do not specify a cluster, the default cluster is assumed.</td></tr>
<tr><td><CopyableCode code="load_balancers" /></td><td><code>array</code></td><td>A list of load balancer objects to associate with the service. If you specify the <code>Role</code> property, <code>LoadBalancers</code> must be specified as well. For information about the number of load balancers that you can specify per service, see &#91;Service Load Balancing&#93;(https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-load-balancing.html) in the *Amazon Elastic Container Service Developer Guide*.</td></tr>
<tr><td><CopyableCode code="service_connect_configuration" /></td><td><code>object</code></td><td>The configuration for this service to discover and connect to services, and be discovered by, and connected from, other services within a namespace.<br />Tasks that run in a namespace can use short names to connect to services in the namespace. Tasks can connect to services across all of the clusters in the namespace. Tasks connect through a managed proxy container that collects logs and metrics for increased visibility. Only the tasks that Amazon ECS services create are supported with Service Connect. For more information, see &#91;Service Connect&#93;(https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-connect.html) in the *Amazon Elastic Container Service Developer Guide*.</td></tr>
<tr><td><CopyableCode code="desired_count" /></td><td><code>integer</code></td><td>The number of instantiations of the specified task definition to place and keep running in your service.<br />For new services, if a desired count is not specified, a default value of <code>1</code> is used. When using the <code>DAEMON</code> scheduling strategy, the desired count is not required.<br />For existing services, if a desired count is not specified, it is omitted from the operation.</td></tr>
<tr><td><CopyableCode code="vpc_lattice_configurations" /></td><td><code>array</code></td><td>The VPC Lattice configuration for the service being created.</td></tr>
<tr><td><CopyableCode code="deployment_controller" /></td><td><code>object</code></td><td>The deployment controller to use for the service. If no deployment controller is specified, the default value of <code>ECS</code> is used.</td></tr>
<tr><td><CopyableCode code="role" /></td><td><code>string</code></td><td>The name or full Amazon Resource Name (ARN) of the IAM role that allows Amazon ECS to make calls to your load balancer on your behalf. This parameter is only permitted if you are using a load balancer with your service and your task definition doesn't use the <code>awsvpc</code> network mode. If you specify the <code>role</code> parameter, you must also specify a load balancer object with the <code>loadBalancers</code> parameter.<br />If your account has already created the Amazon ECS service-linked role, that role is used for your service unless you specify a role here. The service-linked role is required if your task definition uses the <code>awsvpc</code> network mode or if the service is configured to use service discovery, an external deployment controller, multiple target groups, or Elastic Inference accelerators in which case you don't specify a role here. For more information, see &#91;Using service-linked roles for Amazon ECS&#93;(https://docs.aws.amazon.com/AmazonECS/latest/developerguide/using-service-linked-roles.html) in the *Amazon Elastic Container Service Developer Guide*.<br />If your specified role has a path other than <code>/</code>, then you must either specify the full role ARN (this is recommended) or prefix the role name with the path. For example, if a role with the name <code>bar</code> has a path of <code>/foo/</code> then you would specify <code>/foo/bar</code> as the role name. For more information, see &#91;Friendly names and paths&#93;(https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_identifiers.html#identifiers-friendly-names) in the *IAM User Guide*.</td></tr>
<tr><td><CopyableCode code="task_definition" /></td><td><code>string</code></td><td>The <code>family</code> and <code>revision</code> (<code>family:revision</code>) or full ARN of the task definition to run in your service. If a <code>revision</code> isn't specified, the latest <code>ACTIVE</code> revision is used.<br />A task definition must be specified if the service uses either the <code>ECS</code> or <code>CODE_DEPLOY</code> deployment controllers.<br />For more information about deployment types, see &#91;Amazon ECS deployment types&#93;(https://docs.aws.amazon.com/AmazonECS/latest/developerguide/deployment-types.html).</td></tr>
<tr><td><CopyableCode code="service_name" /></td><td><code>string</code></td><td>The name of your service. Up to 255 letters (uppercase and lowercase), numbers, underscores, and hyphens are allowed. Service names must be unique within a cluster, but you can have similarly named services in multiple clusters within a Region or across multiple Regions.<br />The stack update fails if you change any properties that require replacement and the <code>ServiceName</code> is configured. This is because AWS CloudFormation creates the replacement service first, but each <code>ServiceName</code> must be unique in the cluster.</td></tr>
<tr><td><CopyableCode code="deployment_configuration" /></td><td><code>object</code></td><td>Optional deployment parameters that control how many tasks run during the deployment and the ordering of stopping and starting tasks.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-service.html"><code>AWS::ECS::Service</code></a>.

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
Gets all <code>services</code> in a region.
```sql
SELECT
region,
platform_version,
propagate_tags,
service_arn,
placement_strategies,
service_registries,
volume_configurations,
capacity_provider_strategy,
launch_type,
name,
availability_zone_rebalancing,
scheduling_strategy,
network_configuration,
tags,
health_check_grace_period_seconds,
enable_ecs_managed_tags,
enable_execute_command,
placement_constraints,
cluster,
load_balancers,
service_connect_configuration,
desired_count,
vpc_lattice_configurations,
deployment_controller,
role,
task_definition,
service_name,
deployment_configuration
FROM aws.ecs.services
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>service</code>.
```sql
SELECT
region,
platform_version,
propagate_tags,
service_arn,
placement_strategies,
service_registries,
volume_configurations,
capacity_provider_strategy,
launch_type,
name,
availability_zone_rebalancing,
scheduling_strategy,
network_configuration,
tags,
health_check_grace_period_seconds,
enable_ecs_managed_tags,
enable_execute_command,
placement_constraints,
cluster,
load_balancers,
service_connect_configuration,
desired_count,
vpc_lattice_configurations,
deployment_controller,
role,
task_definition,
service_name,
deployment_configuration
FROM aws.ecs.services
WHERE region = 'us-east-1' AND data__Identifier = '<ServiceArn>|<Cluster>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>service</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.ecs.services (
 PlatformVersion,
 PropagateTags,
 PlacementStrategies,
 ServiceRegistries,
 VolumeConfigurations,
 CapacityProviderStrategy,
 LaunchType,
 AvailabilityZoneRebalancing,
 SchedulingStrategy,
 NetworkConfiguration,
 Tags,
 HealthCheckGracePeriodSeconds,
 EnableECSManagedTags,
 EnableExecuteCommand,
 PlacementConstraints,
 Cluster,
 LoadBalancers,
 ServiceConnectConfiguration,
 DesiredCount,
 VpcLatticeConfigurations,
 DeploymentController,
 Role,
 TaskDefinition,
 ServiceName,
 DeploymentConfiguration,
 region
)
SELECT 
'{{ PlatformVersion }}',
 '{{ PropagateTags }}',
 '{{ PlacementStrategies }}',
 '{{ ServiceRegistries }}',
 '{{ VolumeConfigurations }}',
 '{{ CapacityProviderStrategy }}',
 '{{ LaunchType }}',
 '{{ AvailabilityZoneRebalancing }}',
 '{{ SchedulingStrategy }}',
 '{{ NetworkConfiguration }}',
 '{{ Tags }}',
 '{{ HealthCheckGracePeriodSeconds }}',
 '{{ EnableECSManagedTags }}',
 '{{ EnableExecuteCommand }}',
 '{{ PlacementConstraints }}',
 '{{ Cluster }}',
 '{{ LoadBalancers }}',
 '{{ ServiceConnectConfiguration }}',
 '{{ DesiredCount }}',
 '{{ VpcLatticeConfigurations }}',
 '{{ DeploymentController }}',
 '{{ Role }}',
 '{{ TaskDefinition }}',
 '{{ ServiceName }}',
 '{{ DeploymentConfiguration }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.ecs.services (
 PlatformVersion,
 PropagateTags,
 PlacementStrategies,
 ServiceRegistries,
 VolumeConfigurations,
 CapacityProviderStrategy,
 LaunchType,
 AvailabilityZoneRebalancing,
 SchedulingStrategy,
 NetworkConfiguration,
 Tags,
 HealthCheckGracePeriodSeconds,
 EnableECSManagedTags,
 EnableExecuteCommand,
 PlacementConstraints,
 Cluster,
 LoadBalancers,
 ServiceConnectConfiguration,
 DesiredCount,
 VpcLatticeConfigurations,
 DeploymentController,
 Role,
 TaskDefinition,
 ServiceName,
 DeploymentConfiguration,
 region
)
SELECT 
 '{{ PlatformVersion }}',
 '{{ PropagateTags }}',
 '{{ PlacementStrategies }}',
 '{{ ServiceRegistries }}',
 '{{ VolumeConfigurations }}',
 '{{ CapacityProviderStrategy }}',
 '{{ LaunchType }}',
 '{{ AvailabilityZoneRebalancing }}',
 '{{ SchedulingStrategy }}',
 '{{ NetworkConfiguration }}',
 '{{ Tags }}',
 '{{ HealthCheckGracePeriodSeconds }}',
 '{{ EnableECSManagedTags }}',
 '{{ EnableExecuteCommand }}',
 '{{ PlacementConstraints }}',
 '{{ Cluster }}',
 '{{ LoadBalancers }}',
 '{{ ServiceConnectConfiguration }}',
 '{{ DesiredCount }}',
 '{{ VpcLatticeConfigurations }}',
 '{{ DeploymentController }}',
 '{{ Role }}',
 '{{ TaskDefinition }}',
 '{{ ServiceName }}',
 '{{ DeploymentConfiguration }}',
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
  - name: service
    props:
      - name: PlatformVersion
        value: '{{ PlatformVersion }}'
      - name: PropagateTags
        value: '{{ PropagateTags }}'
      - name: PlacementStrategies
        value:
          - Field: '{{ Field }}'
            Type: '{{ Type }}'
      - name: ServiceRegistries
        value:
          - ContainerName: '{{ ContainerName }}'
            Port: '{{ Port }}'
            ContainerPort: '{{ ContainerPort }}'
            RegistryArn: '{{ RegistryArn }}'
      - name: VolumeConfigurations
        value:
          - ManagedEBSVolume:
              SnapshotId: '{{ SnapshotId }}'
              VolumeType: '{{ VolumeType }}'
              KmsKeyId: '{{ KmsKeyId }}'
              TagSpecifications:
                - PropagateTags: '{{ PropagateTags }}'
                  ResourceType: '{{ ResourceType }}'
                  Tags:
                    - Value: '{{ Value }}'
                      Key: '{{ Key }}'
              FilesystemType: '{{ FilesystemType }}'
              Encrypted: '{{ Encrypted }}'
              Throughput: '{{ Throughput }}'
              Iops: '{{ Iops }}'
              SizeInGiB: '{{ SizeInGiB }}'
              RoleArn: '{{ RoleArn }}'
            Name: '{{ Name }}'
      - name: CapacityProviderStrategy
        value:
          - CapacityProvider: '{{ CapacityProvider }}'
            Base: '{{ Base }}'
            Weight: '{{ Weight }}'
      - name: LaunchType
        value: '{{ LaunchType }}'
      - name: AvailabilityZoneRebalancing
        value: '{{ AvailabilityZoneRebalancing }}'
      - name: SchedulingStrategy
        value: '{{ SchedulingStrategy }}'
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
          - null
      - name: HealthCheckGracePeriodSeconds
        value: '{{ HealthCheckGracePeriodSeconds }}'
      - name: EnableECSManagedTags
        value: '{{ EnableECSManagedTags }}'
      - name: EnableExecuteCommand
        value: '{{ EnableExecuteCommand }}'
      - name: PlacementConstraints
        value:
          - Type: '{{ Type }}'
            Expression: '{{ Expression }}'
      - name: Cluster
        value: '{{ Cluster }}'
      - name: LoadBalancers
        value:
          - TargetGroupArn: '{{ TargetGroupArn }}'
            ContainerName: '{{ ContainerName }}'
            ContainerPort: '{{ ContainerPort }}'
      - name: ServiceConnectConfiguration
        value:
          Services:
            - Timeout:
                PerRequestTimeoutSeconds: '{{ PerRequestTimeoutSeconds }}'
                IdleTimeoutSeconds: '{{ IdleTimeoutSeconds }}'
              IngressPortOverride: '{{ IngressPortOverride }}'
              ClientAliases:
                - DnsName: '{{ DnsName }}'
                  Port: '{{ Port }}'
              Tls:
                IssuerCertificateAuthority:
                  AwsPcaAuthorityArn: '{{ AwsPcaAuthorityArn }}'
                KmsKey: '{{ KmsKey }}'
                RoleArn: '{{ RoleArn }}'
              DiscoveryName: '{{ DiscoveryName }}'
              PortName: '{{ PortName }}'
          Enabled: '{{ Enabled }}'
          LogConfiguration:
            SecretOptions:
              - ValueFrom: '{{ ValueFrom }}'
                Name: '{{ Name }}'
            Options: {}
            LogDriver: '{{ LogDriver }}'
          Namespace: '{{ Namespace }}'
      - name: DesiredCount
        value: '{{ DesiredCount }}'
      - name: VpcLatticeConfigurations
        value:
          - TargetGroupArn: '{{ TargetGroupArn }}'
            PortName: '{{ PortName }}'
            RoleArn: '{{ RoleArn }}'
      - name: DeploymentController
        value:
          Type: '{{ Type }}'
      - name: Role
        value: '{{ Role }}'
      - name: TaskDefinition
        value: '{{ TaskDefinition }}'
      - name: ServiceName
        value: '{{ ServiceName }}'
      - name: DeploymentConfiguration
        value:
          Alarms:
            AlarmNames:
              - '{{ AlarmNames[0] }}'
            Enable: '{{ Enable }}'
            Rollback: '{{ Rollback }}'
          DeploymentCircuitBreaker:
            Enable: '{{ Enable }}'
            Rollback: '{{ Rollback }}'
          MaximumPercent: '{{ MaximumPercent }}'
          MinimumHealthyPercent: '{{ MinimumHealthyPercent }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.ecs.services
WHERE data__Identifier = '<ServiceArn|Cluster>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>services</code> resource, the following permissions are required:

### Read
```json
ecs:DescribeServices
```

### Create
```json
ecs:CreateService,
ecs:DescribeServices,
iam:PassRole,
ecs:TagResource
```

### Update
```json
ecs:DescribeServices,
ecs:ListTagsForResource,
ecs:TagResource,
ecs:UntagResource,
ecs:UpdateService
```

### List
```json
ecs:DescribeServices,
ecs:ListClusters,
ecs:ListServices
```

### Delete
```json
ecs:DeleteService,
ecs:DescribeServices
```
