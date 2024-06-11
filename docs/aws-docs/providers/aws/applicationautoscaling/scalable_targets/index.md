---
title: scalable_targets
hide_title: false
hide_table_of_contents: false
keywords:
  - scalable_targets
  - applicationautoscaling
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

Creates, updates, deletes or gets a <code>scalable_target</code> resource or lists <code>scalable_targets</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>scalable_targets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The <code>AWS::ApplicationAutoScaling::ScalableTarget</code> resource specifies a resource that Application Auto Scaling can scale, such as an AWS::DynamoDB::Table or AWS::ECS::Service resource.<br/> For more information, see &#91;Getting started&#93;(https://docs.aws.amazon.com/autoscaling/application/userguide/getting-started.html) in the *Application Auto Scaling User Guide*.<br/>  If the resource that you want Application Auto Scaling to scale is not yet created in your account, add a dependency on the resource when registering it as a scalable target using the &#91;DependsOn&#93;(https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-attribute-dependson.html) attribute.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.applicationautoscaling.scalable_targets" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="scheduled_actions" /></td><td><code>array</code></td><td>The scheduled actions for the scalable target. Duplicates aren't allowed.</td></tr>
<tr><td><CopyableCode code="resource_id" /></td><td><code>string</code></td><td>The identifier of the resource associated with the scalable target. This string consists of the resource type and unique identifier.<br/>  +  ECS service - The resource type is <code>service</code> and the unique identifier is the cluster name and service name. Example: <code>service/my-cluster/my-service</code>.<br/>  +  Spot Fleet - The resource type is <code>spot-fleet-request</code> and the unique identifier is the Spot Fleet request ID. Example: <code>spot-fleet-request/sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE</code>.<br/>  +  EMR cluster - The resource type is <code>instancegroup</code> and the unique identifier is the cluster ID and instance group ID. Example: <code>instancegroup/j-2EEZNYKUA1NTV/ig-1791Y4E1L8YI0</code>.<br/>  +  AppStream 2.0 fleet - The resource type is <code>fleet</code> and the unique identifier is the fleet name. Example: <code>fleet/sample-fleet</code>.<br/>  +  DynamoDB table - The resource type is <code>table</code> and the unique identifier is the table name. Example: <code>table/my-table</code>.<br/>  +  DynamoDB global secondary index - The resource type is <code>index</code> and the unique identifier is the index name. Example: <code>table/my-table/index/my-table-index</code>.<br/>  +  Aurora DB cluster - The resource type is <code>cluster</code> and the unique identifier is the cluster name. Example: <code>cluster:my-db-cluster</code>.<br/>  +  SageMaker endpoint variant - The resource type is <code>variant</code> and the unique identifier is the resource ID. Example: <code>endpoint/my-end-point/variant/KMeansClustering</code>.<br/>  +  Custom resources are not supported with a resource type. This parameter must specify the <code>OutputValue</code> from the CloudFormation template stack used to access the resources. The unique identifier is defined by the service provider. More information is available in our &#91;GitHub repository&#93;(https://docs.aws.amazon.com/https://github.com/aws/aws-auto-scaling-custom-resource).<br/>  +  Amazon Comprehend document classification endpoint - The resource type and unique identifier are specified using the endpoint ARN. Example: <code>arn:aws:comprehend:us-west-2:123456789012:document-classifier-endpoint/EXAMPLE</code>.<br/>  +  Amazon Comprehend entity recognizer endpoint - The resource type and unique identifier are specified using the endpoint ARN. Example: <code>arn:aws:comprehend:us-west-2:123456789012:entity-recognizer-endpoint/EXAMPLE</code>.<br/>  +  Lambda provisioned concurrency - The resource type is <code>function</code> and the unique identifier is the function name with a function version or alias name suffix that is not <code>$LATEST</code>. Example: <code>function:my-function:prod</code> or <code>function:my-function:1</code>.<br/>  +  Amazon Keyspaces table - The resource type is <code>table</code> and the unique identifier is the table name. Example: <code>keyspace/mykeyspace/table/mytable</code>.<br/>  +  Amazon MSK cluster - The resource type and unique identifier are specified using the cluster ARN. Example: <code>arn:aws:kafka:us-east-1:123456789012:cluster/demo-cluster-1/6357e0b2-0e6a-4b86-a0b4-70df934c2e31-5</code>.<br/>  +  Amazon ElastiCache replication group - The resource type is <code>replication-group</code> and the unique identifier is the replication group name. Example: <code>replication-group/mycluster</code>.<br/>  +  Neptune cluster - The resource type is <code>cluster</code> and the unique identifier is the cluster name. Example: <code>cluster:mycluster</code>.<br/>  +  SageMaker serverless endpoint - The resource type is <code>variant</code> and the unique identifier is the resource ID. Example: <code>endpoint/my-end-point/variant/KMeansClustering</code>.<br/>  +  SageMaker inference component - The resource type is <code>inference-component</code> and the unique identifier is the resource ID. Example: <code>inference-component/my-inference-component</code>.</td></tr>
<tr><td><CopyableCode code="service_namespace" /></td><td><code>string</code></td><td>The namespace of the AWS service that provides the resource, or a <code>custom-resource</code>.</td></tr>
<tr><td><CopyableCode code="scalable_dimension" /></td><td><code>string</code></td><td>The scalable dimension associated with the scalable target. This string consists of the service namespace, resource type, and scaling property.<br/>  +   <code>ecs:service:DesiredCount</code> - The desired task count of an ECS service.<br/>  +   <code>elasticmapreduce:instancegroup:InstanceCount</code> - The instance count of an EMR Instance Group.<br/>  +   <code>ec2:spot-fleet-request:TargetCapacity</code> - The target capacity of a Spot Fleet.<br/>  +   <code>appstream:fleet:DesiredCapacity</code> - The desired capacity of an AppStream 2.0 fleet.<br/>  +   <code>dynamodb:table:ReadCapacityUnits</code> - The provisioned read capacity for a DynamoDB table.<br/>  +   <code>dynamodb:table:WriteCapacityUnits</code> - The provisioned write capacity for a DynamoDB table.<br/>  +   <code>dynamodb:index:ReadCapacityUnits</code> - The provisioned read capacity for a DynamoDB global secondary index.<br/>  +   <code>dynamodb:index:WriteCapacityUnits</code> - The provisioned write capacity for a DynamoDB global secondary index.<br/>  +   <code>rds:cluster:ReadReplicaCount</code> - The count of Aurora Replicas in an Aurora DB cluster. Available for Aurora MySQL-compatible edition and Aurora PostgreSQL-compatible edition.<br/>  +   <code>sagemaker:variant:DesiredInstanceCount</code> - The number of EC2 instances for a SageMaker model endpoint variant.<br/>  +   <code>custom-resource:ResourceType:Property</code> - The scalable dimension for a custom resource provided by your own application or service.<br/>  +   <code>comprehend:document-classifier-endpoint:DesiredInferenceUnits</code> - The number of inference units for an Amazon Comprehend document classification endpoint.<br/>  +   <code>comprehend:entity-recognizer-endpoint:DesiredInferenceUnits</code> - The number of inference units for an Amazon Comprehend entity recognizer endpoint.<br/>  +   <code>lambda:function:ProvisionedConcurrency</code> - The provisioned concurrency for a Lambda function.<br/>  +   <code>cassandra:table:ReadCapacityUnits</code> - The provisioned read capacity for an Amazon Keyspaces table.<br/>  +   <code>cassandra:table:WriteCapacityUnits</code> - The provisioned write capacity for an Amazon Keyspaces table.<br/>  +   <code>kafka:broker-storage:VolumeSize</code> - The provisioned volume size (in GiB) for brokers in an Amazon MSK cluster.<br/>  +   <code>elasticache:replication-group:NodeGroups</code> - The number of node groups for an Amazon ElastiCache replication group.<br/>  +   <code>elasticache:replication-group:Replicas</code> - The number of replicas per node group for an Amazon ElastiCache replication group.<br/>  +   <code>neptune:cluster:ReadReplicaCount</code> - The count of read replicas in an Amazon Neptune DB cluster.<br/>  +   <code>sagemaker:variant:DesiredProvisionedConcurrency</code> - The provisioned concurrency for a SageMaker serverless endpoint.<br/>  +   <code>sagemaker:inference-component:DesiredCopyCount</code> - The number of copies across an endpoint for a SageMaker inference component.</td></tr>
<tr><td><CopyableCode code="suspended_state" /></td><td><code>object</code></td><td>An embedded object that contains attributes and attribute values that are used to suspend and resume automatic scaling. Setting the value of an attribute to <code>true</code> suspends the specified scaling activities. Setting it to <code>false</code> (default) resumes the specified scaling activities. <br/>  *Suspension Outcomes* <br/>  +  For <code>DynamicScalingInSuspended</code>, while a suspension is in effect, all scale-in activities that are triggered by a scaling policy are suspended.<br/>  +  For <code>DynamicScalingOutSuspended</code>, while a suspension is in effect, all scale-out activities that are triggered by a scaling policy are suspended.<br/>  +  For <code>ScheduledScalingSuspended</code>, while a suspension is in effect, all scaling activities that involve scheduled actions are suspended.</td></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="min_capacity" /></td><td><code>integer</code></td><td>The minimum value that you plan to scale in to. When a scaling policy is in effect, Application Auto Scaling can scale in (contract) as needed to the minimum capacity limit in response to changing demand.</td></tr>
<tr><td><CopyableCode code="role_arn" /></td><td><code>string</code></td><td>Specify the Amazon Resource Name (ARN) of an Identity and Access Management (IAM) role that allows Application Auto Scaling to modify the scalable target on your behalf. This can be either an IAM service role that Application Auto Scaling can assume to make calls to other AWS resources on your behalf, or a service-linked role for the specified service. For more information, see &#91;How Application Auto Scaling works with IAM&#93;(https://docs.aws.amazon.com/autoscaling/application/userguide/security_iam_service-with-iam.html) in the *Application Auto Scaling User Guide*.<br/> To automatically create a service-linked role (recommended), specify the full ARN of the service-linked role in your stack template. To find the exact ARN of the service-linked role for your AWS or custom resource, see the &#91;Service-linked roles&#93;(https://docs.aws.amazon.com/autoscaling/application/userguide/application-auto-scaling-service-linked-roles.html) topic in the *Application Auto Scaling User Guide*. Look for the ARN in the table at the bottom of the page.</td></tr>
<tr><td><CopyableCode code="max_capacity" /></td><td><code>integer</code></td><td>The maximum value that you plan to scale out to. When a scaling policy is in effect, Application Auto Scaling can scale out (expand) as needed to the maximum capacity limit in response to changing demand.</td></tr>
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
    <td><CopyableCode code="ResourceId, ServiceNamespace, ScalableDimension, MinCapacity, MaxCapacity, region" /></td>
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
List all <code>scalable_targets</code> in a region.
```sql
SELECT
region,
resource_id,
scalable_dimension,
service_namespace
FROM aws.applicationautoscaling.scalable_targets
WHERE region = 'us-east-1';
```
Gets all properties from a <code>scalable_target</code>.
```sql
SELECT
region,
scheduled_actions,
resource_id,
service_namespace,
scalable_dimension,
suspended_state,
id,
min_capacity,
role_arn,
max_capacity
FROM aws.applicationautoscaling.scalable_targets
WHERE region = 'us-east-1' AND data__Identifier = '<ResourceId>|<ScalableDimension>|<ServiceNamespace>';
```


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>scalable_target</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.applicationautoscaling.scalable_targets (
 ResourceId,
 ServiceNamespace,
 ScalableDimension,
 MinCapacity,
 MaxCapacity,
 region
)
SELECT 
'{{ ResourceId }}',
 '{{ ServiceNamespace }}',
 '{{ ScalableDimension }}',
 '{{ MinCapacity }}',
 '{{ MaxCapacity }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.applicationautoscaling.scalable_targets (
 ScheduledActions,
 ResourceId,
 ServiceNamespace,
 ScalableDimension,
 SuspendedState,
 MinCapacity,
 RoleARN,
 MaxCapacity,
 region
)
SELECT 
 '{{ ScheduledActions }}',
 '{{ ResourceId }}',
 '{{ ServiceNamespace }}',
 '{{ ScalableDimension }}',
 '{{ SuspendedState }}',
 '{{ MinCapacity }}',
 '{{ RoleARN }}',
 '{{ MaxCapacity }}',
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
  - name: scalable_target
    props:
      - name: ScheduledActions
        value:
          - Timezone: '{{ Timezone }}'
            ScheduledActionName: '{{ ScheduledActionName }}'
            EndTime: '{{ EndTime }}'
            Schedule: '{{ Schedule }}'
            StartTime: '{{ StartTime }}'
            ScalableTargetAction:
              MinCapacity: '{{ MinCapacity }}'
              MaxCapacity: '{{ MaxCapacity }}'
      - name: ResourceId
        value: '{{ ResourceId }}'
      - name: ServiceNamespace
        value: '{{ ServiceNamespace }}'
      - name: ScalableDimension
        value: '{{ ScalableDimension }}'
      - name: SuspendedState
        value:
          DynamicScalingOutSuspended: '{{ DynamicScalingOutSuspended }}'
          ScheduledScalingSuspended: '{{ ScheduledScalingSuspended }}'
          DynamicScalingInSuspended: '{{ DynamicScalingInSuspended }}'
      - name: MinCapacity
        value: '{{ MinCapacity }}'
      - name: RoleARN
        value: '{{ RoleARN }}'
      - name: MaxCapacity
        value: '{{ MaxCapacity }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.applicationautoscaling.scalable_targets
WHERE data__Identifier = '<ResourceId|ScalableDimension|ServiceNamespace>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>scalable_targets</code> resource, the following permissions are required:

### Read
```json
application-autoscaling:DescribeScalableTargets,
application-autoscaling:DescribeScheduledActions
```

### Create
```json
application-autoscaling:DescribeScalableTargets,
application-autoscaling:RegisterScalableTarget,
application-autoscaling:DescribeScheduledActions,
application-autoscaling:PutScheduledAction,
iam:PassRole,
iam:CreateServiceLinkedRole,
cloudwatch:PutMetricAlarm,
cloudwatch:DeleteAlarms,
cloudwatch:DescribeAlarms,
lambda:GetProvisionedConcurrencyConfig,
lambda:PutProvisionedConcurrencyConfig,
lambda:DeleteProvisionedConcurrencyConfig
```

### Update
```json
application-autoscaling:RegisterScalableTarget,
application-autoscaling:DescribeScalableTargets,
application-autoscaling:DescribeScheduledActions,
application-autoscaling:DeleteScheduledAction,
application-autoscaling:PutScheduledAction,
cloudwatch:PutMetricAlarm,
cloudwatch:DeleteAlarms,
cloudwatch:DescribeAlarms,
lambda:GetProvisionedConcurrencyConfig,
lambda:PutProvisionedConcurrencyConfig,
lambda:DeleteProvisionedConcurrencyConfig
```

### List
```json
application-autoscaling:DescribeScalableTargets
```

### Delete
```json
application-autoscaling:DeregisterScalableTarget
```

