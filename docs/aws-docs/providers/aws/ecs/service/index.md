---
title: service
hide_title: false
hide_table_of_contents: false
keywords:
  - service
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


Gets or updates an individual <code>service</code> resource, use <code>services</code> to retrieve a list of resources or to create or delete a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>service</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The ``AWS::ECS::Service`` resource creates an Amazon Elastic Container Service (Amazon ECS) service that runs and maintains the requested number of tasks and associated load balancers.&lt;br&#x2F;&gt;  The stack update fails if you change any properties that require replacement and at least one Amazon ECS Service Connect ``ServiceConnectService`` is configured. This is because AWS CloudFormation creates the replacement service first, but each ``ServiceConnectService`` must have a name that is unique in the namespace.&lt;br&#x2F;&gt;  Starting April 15, 2023, AWS; will not onboard new customers to Amazon Elastic Inference (EI), and will help current customers migrate their workloads to options that offer better price and performance. After April 15, 2023, new customers will not be able to launch instances with Amazon EI accelerators in Amazon SageMaker, ECS, or EC2. However, customers who have used Amazon EI at least once during the past 30-day period are considered current customers and will be able to continue using the service.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ecs.service" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="service_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="capacity_provider_strategy" /></td><td><code>array</code></td><td>The capacity provider strategy to use for the service.&lt;br&#x2F;&gt; If a ``capacityProviderStrategy`` is specified, the ``launchType`` parameter must be omitted. If no ``capacityProviderStrategy`` or ``launchType`` is specified, the ``defaultCapacityProviderStrategy`` for the cluster is used.&lt;br&#x2F;&gt; A capacity provider strategy may contain a maximum of 6 capacity providers.</td></tr>
<tr><td><CopyableCode code="cluster" /></td><td><code>string</code></td><td>The short name or full Amazon Resource Name (ARN) of the cluster that you run your service on. If you do not specify a cluster, the default cluster is assumed.</td></tr>
<tr><td><CopyableCode code="deployment_configuration" /></td><td><code>object</code></td><td>Optional deployment parameters that control how many tasks run during the deployment and the ordering of stopping and starting tasks.</td></tr>
<tr><td><CopyableCode code="deployment_controller" /></td><td><code>object</code></td><td>The deployment controller to use for the service. If no deployment controller is specified, the default value of ``ECS`` is used.</td></tr>
<tr><td><CopyableCode code="desired_count" /></td><td><code>integer</code></td><td>The number of instantiations of the specified task definition to place and keep running in your service.&lt;br&#x2F;&gt; For new services, if a desired count is not specified, a default value of ``1`` is used. When using the ``DAEMON`` scheduling strategy, the desired count is not required.&lt;br&#x2F;&gt; For existing services, if a desired count is not specified, it is omitted from the operation.</td></tr>
<tr><td><CopyableCode code="enable_ecs_managed_tags" /></td><td><code>boolean</code></td><td>Specifies whether to turn on Amazon ECS managed tags for the tasks within the service. For more information, see &#91;Tagging your Amazon ECS resources&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;AmazonECS&#x2F;latest&#x2F;developerguide&#x2F;ecs-using-tags.html) in the *Amazon Elastic Container Service Developer Guide*.&lt;br&#x2F;&gt; When you use Amazon ECS managed tags, you need to set the ``propagateTags`` request parameter.</td></tr>
<tr><td><CopyableCode code="enable_execute_command" /></td><td><code>boolean</code></td><td>Determines whether the execute command functionality is turned on for the service. If ``true``, the execute command functionality is turned on for all containers in tasks as part of the service.</td></tr>
<tr><td><CopyableCode code="health_check_grace_period_seconds" /></td><td><code>integer</code></td><td>The period of time, in seconds, that the Amazon ECS service scheduler ignores unhealthy Elastic Load Balancing target health checks after a task has first started. This is only used when your service is configured to use a load balancer. If your service has a load balancer defined and you don't specify a health check grace period value, the default value of ``0`` is used.&lt;br&#x2F;&gt; If you do not use an Elastic Load Balancing, we recommend that you use the ``startPeriod`` in the task definition health check parameters. For more information, see &#91;Health check&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;AmazonECS&#x2F;latest&#x2F;APIReference&#x2F;API_HealthCheck.html).&lt;br&#x2F;&gt; If your service's tasks take a while to start and respond to Elastic Load Balancing health checks, you can specify a health check grace period of up to 2,147,483,647 seconds (about 69 years). During that time, the Amazon ECS service scheduler ignores health check status. This grace period can prevent the service scheduler from marking tasks as unhealthy and stopping them before they have time to come up.</td></tr>
<tr><td><CopyableCode code="launch_type" /></td><td><code>string</code></td><td>The launch type on which to run your service. For more information, see &#91;Amazon ECS Launch Types&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;AmazonECS&#x2F;latest&#x2F;developerguide&#x2F;launch_types.html) in the *Amazon Elastic Container Service Developer Guide*.</td></tr>
<tr><td><CopyableCode code="load_balancers" /></td><td><code>array</code></td><td>A list of load balancer objects to associate with the service. If you specify the ``Role`` property, ``LoadBalancers`` must be specified as well. For information about the number of load balancers that you can specify per service, see &#91;Service Load Balancing&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;AmazonECS&#x2F;latest&#x2F;developerguide&#x2F;service-load-balancing.html) in the *Amazon Elastic Container Service Developer Guide*.</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="network_configuration" /></td><td><code>object</code></td><td>The network configuration for the service. This parameter is required for task definitions that use the ``awsvpc`` network mode to receive their own elastic network interface, and it is not supported for other network modes. For more information, see &#91;Task Networking&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;AmazonECS&#x2F;latest&#x2F;developerguide&#x2F;task-networking.html) in the *Amazon Elastic Container Service Developer Guide*.</td></tr>
<tr><td><CopyableCode code="placement_constraints" /></td><td><code>array</code></td><td>An array of placement constraint objects to use for tasks in your service. You can specify a maximum of 10 constraints for each task. This limit includes constraints in the task definition and those specified at runtime.</td></tr>
<tr><td><CopyableCode code="placement_strategies" /></td><td><code>array</code></td><td>The placement strategy objects to use for tasks in your service. You can specify a maximum of 5 strategy rules for each service.</td></tr>
<tr><td><CopyableCode code="platform_version" /></td><td><code>string</code></td><td>The platform version that your tasks in the service are running on. A platform version is specified only for tasks using the Fargate launch type. If one isn't specified, the ``LATEST`` platform version is used. For more information, see &#91;platform versions&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;AmazonECS&#x2F;latest&#x2F;developerguide&#x2F;platform_versions.html) in the *Amazon Elastic Container Service Developer Guide*.</td></tr>
<tr><td><CopyableCode code="propagate_tags" /></td><td><code>string</code></td><td>Specifies whether to propagate the tags from the task definition to the task. If no value is specified, the tags aren't propagated. Tags can only be propagated to the task during task creation. To add tags to a task after task creation, use the &#91;TagResource&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;AmazonECS&#x2F;latest&#x2F;APIReference&#x2F;API_TagResource.html) API action.&lt;br&#x2F;&gt; The default is ``NONE``.</td></tr>
<tr><td><CopyableCode code="role" /></td><td><code>string</code></td><td>The name or full Amazon Resource Name (ARN) of the IAM role that allows Amazon ECS to make calls to your load balancer on your behalf. This parameter is only permitted if you are using a load balancer with your service and your task definition doesn't use the ``awsvpc`` network mode. If you specify the ``role`` parameter, you must also specify a load balancer object with the ``loadBalancers`` parameter.&lt;br&#x2F;&gt;  If your account has already created the Amazon ECS service-linked role, that role is used for your service unless you specify a role here. The service-linked role is required if your task definition uses the ``awsvpc`` network mode or if the service is configured to use service discovery, an external deployment controller, multiple target groups, or Elastic Inference accelerators in which case you don't specify a role here. For more information, see &#91;Using service-linked roles for Amazon ECS&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;AmazonECS&#x2F;latest&#x2F;developerguide&#x2F;using-service-linked-roles.html) in the *Amazon Elastic Container Service Developer Guide*.&lt;br&#x2F;&gt;  If your specified role has a path other than ``&#x2F;``, then you must either specify the full role ARN (this is recommended) or prefix the role name with the path. For example, if a role with the name ``bar`` has a path of ``&#x2F;foo&#x2F;`` then you would specify ``&#x2F;foo&#x2F;bar`` as the role name. For more information, see &#91;Friendly names and paths&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;IAM&#x2F;latest&#x2F;UserGuide&#x2F;reference_identifiers.html#identifiers-friendly-names) in the *IAM User Guide*.</td></tr>
<tr><td><CopyableCode code="scheduling_strategy" /></td><td><code>string</code></td><td>The scheduling strategy to use for the service. For more information, see &#91;Services&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;AmazonECS&#x2F;latest&#x2F;developerguide&#x2F;ecs_services.html).&lt;br&#x2F;&gt; There are two service scheduler strategies available:&lt;br&#x2F;&gt;  +   ``REPLICA``-The replica scheduling strategy places and maintains the desired number of tasks across your cluster. By default, the service scheduler spreads tasks across Availability Zones. You can use task placement strategies and constraints to customize task placement decisions. This scheduler strategy is required if the service uses the ``CODE_DEPLOY`` or ``EXTERNAL`` deployment controller types.&lt;br&#x2F;&gt;  +   ``DAEMON``-The daemon scheduling strategy deploys exactly one task on each active container instance that meets all of the task placement constraints that you specify in your cluster. The service scheduler also evaluates the task placement constraints for running tasks and will stop tasks that don't meet the placement constraints. When you're using this strategy, you don't need to specify a desired number of tasks, a task placement strategy, or use Service Auto Scaling policies.&lt;br&#x2F;&gt;  Tasks using the Fargate launch type or the ``CODE_DEPLOY`` or ``EXTERNAL`` deployment controller types don't support the ``DAEMON`` scheduling strategy.</td></tr>
<tr><td><CopyableCode code="service_connect_configuration" /></td><td><code>object</code></td><td>The configuration for this service to discover and connect to services, and be discovered by, and connected from, other services within a namespace.&lt;br&#x2F;&gt; Tasks that run in a namespace can use short names to connect to services in the namespace. Tasks can connect to services across all of the clusters in the namespace. Tasks connect through a managed proxy container that collects logs and metrics for increased visibility. Only the tasks that Amazon ECS services create are supported with Service Connect. For more information, see &#91;Service Connect&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;AmazonECS&#x2F;latest&#x2F;developerguide&#x2F;service-connect.html) in the *Amazon Elastic Container Service Developer Guide*.</td></tr>
<tr><td><CopyableCode code="service_name" /></td><td><code>string</code></td><td>The name of your service. Up to 255 letters (uppercase and lowercase), numbers, underscores, and hyphens are allowed. Service names must be unique within a cluster, but you can have similarly named services in multiple clusters within a Region or across multiple Regions.&lt;br&#x2F;&gt;  The stack update fails if you change any properties that require replacement and the ``ServiceName`` is configured. This is because AWS CloudFormation creates the replacement service first, but each ``ServiceName`` must be unique in the cluster.</td></tr>
<tr><td><CopyableCode code="service_registries" /></td><td><code>array</code></td><td>The details of the service discovery registry to associate with this service. For more information, see &#91;Service discovery&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;AmazonECS&#x2F;latest&#x2F;developerguide&#x2F;service-discovery.html).&lt;br&#x2F;&gt;  Each service may be associated with one service registry. Multiple service registries for each service isn't supported.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>The metadata that you apply to the service to help you categorize and organize them. Each tag consists of a key and an optional value, both of which you define. When a service is deleted, the tags are deleted as well.&lt;br&#x2F;&gt; The following basic restrictions apply to tags:&lt;br&#x2F;&gt;  +  Maximum number of tags per resource - 50&lt;br&#x2F;&gt;  +  For each resource, each tag key must be unique, and each tag key can have only one value.&lt;br&#x2F;&gt;  +  Maximum key length - 128 Unicode characters in UTF-8&lt;br&#x2F;&gt;  +  Maximum value length - 256 Unicode characters in UTF-8&lt;br&#x2F;&gt;  +  If your tagging schema is used across multiple services and resources, remember that other services may have restrictions on allowed characters. Generally allowed characters are: letters, numbers, and spaces representable in UTF-8, and the following characters: + - = . _ : &#x2F; @.&lt;br&#x2F;&gt;  +  Tag keys and values are case-sensitive.&lt;br&#x2F;&gt;  +  Do not use ``aws:``, ``AWS:``, or any upper or lowercase combination of such as a prefix for either keys or values as it is reserved for AWS use. You cannot edit or delete tag keys or values with this prefix. Tags with this prefix do not count against your tags per resource limit.</td></tr>
<tr><td><CopyableCode code="task_definition" /></td><td><code>string</code></td><td>The ``family`` and ``revision`` (``family:revision``) or full ARN of the task definition to run in your service. If a ``revision`` isn't specified, the latest ``ACTIVE`` revision is used.&lt;br&#x2F;&gt; A task definition must be specified if the service uses either the ``ECS`` or ``CODE_DEPLOY`` deployment controllers.&lt;br&#x2F;&gt; For more information about deployment types, see &#91;Amazon ECS deployment types&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;AmazonECS&#x2F;latest&#x2F;developerguide&#x2F;deployment-types.html).</td></tr>
<tr><td><CopyableCode code="volume_configurations" /></td><td><code>array</code></td><td>The configuration for a volume specified in the task definition as a volume that is configured at launch time. Currently, the only supported volume type is an Amazon EBS volume.</td></tr>
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

## `SELECT` Example
```sql
SELECT
region,
service_arn,
capacity_provider_strategy,
cluster,
deployment_configuration,
deployment_controller,
desired_count,
enable_ecs_managed_tags,
enable_execute_command,
health_check_grace_period_seconds,
launch_type,
load_balancers,
name,
network_configuration,
placement_constraints,
placement_strategies,
platform_version,
propagate_tags,
role,
scheduling_strategy,
service_connect_configuration,
service_name,
service_registries,
tags,
task_definition,
volume_configurations
FROM aws.ecs.service
WHERE region = 'us-east-1' AND data__Identifier = '<ServiceArn>|<Cluster>';
```


## Permissions

To operate on the <code>service</code> resource, the following permissions are required:

### Read
```json
ecs:DescribeServices
```

### Update
```json
ecs:DescribeServices,
ecs:ListTagsForResource,
ecs:TagResource,
ecs:UntagResource,
ecs:UpdateService
```

