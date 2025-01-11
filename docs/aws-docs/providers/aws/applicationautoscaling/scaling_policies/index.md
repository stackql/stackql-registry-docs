---
title: scaling_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - scaling_policies
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

Creates, updates, deletes or gets a <code>scaling_policy</code> resource or lists <code>scaling_policies</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>scaling_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The <code>AWS::ApplicationAutoScaling::ScalingPolicy</code> resource defines a scaling policy that Application Auto Scaling uses to adjust the capacity of a scalable target. <br />For more information, see &#91;Target tracking scaling policies&#93;(https://docs.aws.amazon.com/autoscaling/application/userguide/application-auto-scaling-target-tracking.html) and &#91;Step scaling policies&#93;(https://docs.aws.amazon.com/autoscaling/application/userguide/application-auto-scaling-step-scaling-policies.html) in the *Application Auto Scaling User Guide*.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.applicationautoscaling.scaling_policies" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="policy_type" /></td><td><code>string</code></td><td>The scaling policy type.<br />The following policy types are supported: <br /><code>TargetTrackingScaling</code>—Not supported for Amazon EMR<br /><code>StepScaling</code>—Not supported for DynamoDB, Amazon Comprehend, Lambda, Amazon Keyspaces, Amazon MSK, Amazon ElastiCache, or Neptune.</td></tr>
<tr><td><CopyableCode code="resource_id" /></td><td><code>string</code></td><td>The identifier of the resource associated with the scaling policy. This string consists of the resource type and unique identifier.<br />+ ECS service - The resource type is <code>service</code> and the unique identifier is the cluster name and service name. Example: <code>service/my-cluster/my-service</code>.<br />+ Spot Fleet - The resource type is <code>spot-fleet-request</code> and the unique identifier is the Spot Fleet request ID. Example: <code>spot-fleet-request/sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE</code>.<br />+ EMR cluster - The resource type is <code>instancegroup</code> and the unique identifier is the cluster ID and instance group ID. Example: <code>instancegroup/j-2EEZNYKUA1NTV/ig-1791Y4E1L8YI0</code>.<br />+ AppStream 2.0 fleet - The resource type is <code>fleet</code> and the unique identifier is the fleet name. Example: <code>fleet/sample-fleet</code>.<br />+ DynamoDB table - The resource type is <code>table</code> and the unique identifier is the table name. Example: <code>table/my-table</code>.<br />+ DynamoDB global secondary index - The resource type is <code>index</code> and the unique identifier is the index name. Example: <code>table/my-table/index/my-table-index</code>.<br />+ Aurora DB cluster - The resource type is <code>cluster</code> and the unique identifier is the cluster name. Example: <code>cluster:my-db-cluster</code>.<br />+ SageMaker endpoint variant - The resource type is <code>variant</code> and the unique identifier is the resource ID. Example: <code>endpoint/my-end-point/variant/KMeansClustering</code>.<br />+ Custom resources are not supported with a resource type. This parameter must specify the <code>OutputValue</code> from the CloudFormation template stack used to access the resources. The unique identifier is defined by the service provider. More information is available in our &#91;GitHub repository&#93;(https://docs.aws.amazon.com/https://github.com/aws/aws-auto-scaling-custom-resource).<br />+ Amazon Comprehend document classification endpoint - The resource type and unique identifier are specified using the endpoint ARN. Example: <code>arn:aws:comprehend:us-west-2:123456789012:document-classifier-endpoint/EXAMPLE</code>.<br />+ Amazon Comprehend entity recognizer endpoint - The resource type and unique identifier are specified using the endpoint ARN. Example: <code>arn:aws:comprehend:us-west-2:123456789012:entity-recognizer-endpoint/EXAMPLE</code>.<br />+ Lambda provisioned concurrency - The resource type is <code>function</code> and the unique identifier is the function name with a function version or alias name suffix that is not <code>$LATEST</code>. Example: <code>function:my-function:prod</code> or <code>function:my-function:1</code>.<br />+ Amazon Keyspaces table - The resource type is <code>table</code> and the unique identifier is the table name. Example: <code>keyspace/mykeyspace/table/mytable</code>.<br />+ Amazon MSK cluster - The resource type and unique identifier are specified using the cluster ARN. Example: <code>arn:aws:kafka:us-east-1:123456789012:cluster/demo-cluster-1/6357e0b2-0e6a-4b86-a0b4-70df934c2e31-5</code>.<br />+ Amazon ElastiCache replication group - The resource type is <code>replication-group</code> and the unique identifier is the replication group name. Example: <code>replication-group/mycluster</code>.<br />+ Neptune cluster - The resource type is <code>cluster</code> and the unique identifier is the cluster name. Example: <code>cluster:mycluster</code>.<br />+ SageMaker serverless endpoint - The resource type is <code>variant</code> and the unique identifier is the resource ID. Example: <code>endpoint/my-end-point/variant/KMeansClustering</code>.<br />+ SageMaker inference component - The resource type is <code>inference-component</code> and the unique identifier is the resource ID. Example: <code>inference-component/my-inference-component</code>.<br />+ Pool of WorkSpaces - The resource type is <code>workspacespool</code> and the unique identifier is the pool ID. Example: <code>workspacespool/wspool-123456</code>.</td></tr>
<tr><td><CopyableCode code="scaling_target_id" /></td><td><code>string</code></td><td>The CloudFormation-generated ID of an Application Auto Scaling scalable target. For more information about the ID, see the Return Value section of the <code>AWS::ApplicationAutoScaling::ScalableTarget</code> resource.<br />You must specify either the <code>ScalingTargetId</code> property, or the <code>ResourceId</code>, <code>ScalableDimension</code>, and <code>ServiceNamespace</code> properties, but not both.</td></tr>
<tr><td><CopyableCode code="policy_name" /></td><td><code>string</code></td><td>The name of the scaling policy.<br />Updates to the name of a target tracking scaling policy are not supported, unless you also update the metric used for scaling. To change only a target tracking scaling policy's name, first delete the policy by removing the existing <code>AWS::ApplicationAutoScaling::ScalingPolicy</code> resource from the template and updating the stack. Then, recreate the resource with the same settings and a different name.</td></tr>
<tr><td><CopyableCode code="service_namespace" /></td><td><code>string</code></td><td>The namespace of the AWS service that provides the resource, or a <code>custom-resource</code>.</td></tr>
<tr><td><CopyableCode code="scalable_dimension" /></td><td><code>string</code></td><td>The scalable dimension. This string consists of the service namespace, resource type, and scaling property.<br />+ <code>ecs:service:DesiredCount</code> - The task count of an ECS service.<br />+ <code>elasticmapreduce:instancegroup:InstanceCount</code> - The instance count of an EMR Instance Group.<br />+ <code>ec2:spot-fleet-request:TargetCapacity</code> - The target capacity of a Spot Fleet.<br />+ <code>appstream:fleet:DesiredCapacity</code> - The capacity of an AppStream 2.0 fleet.<br />+ <code>dynamodb:table:ReadCapacityUnits</code> - The provisioned read capacity for a DynamoDB table.<br />+ <code>dynamodb:table:WriteCapacityUnits</code> - The provisioned write capacity for a DynamoDB table.<br />+ <code>dynamodb:index:ReadCapacityUnits</code> - The provisioned read capacity for a DynamoDB global secondary index.<br />+ <code>dynamodb:index:WriteCapacityUnits</code> - The provisioned write capacity for a DynamoDB global secondary index.<br />+ <code>rds:cluster:ReadReplicaCount</code> - The count of Aurora Replicas in an Aurora DB cluster. Available for Aurora MySQL-compatible edition and Aurora PostgreSQL-compatible edition.<br />+ <code>sagemaker:variant:DesiredInstanceCount</code> - The number of EC2 instances for a SageMaker model endpoint variant.<br />+ <code>custom-resource:ResourceType:Property</code> - The scalable dimension for a custom resource provided by your own application or service.<br />+ <code>comprehend:document-classifier-endpoint:DesiredInferenceUnits</code> - The number of inference units for an Amazon Comprehend document classification endpoint.<br />+ <code>comprehend:entity-recognizer-endpoint:DesiredInferenceUnits</code> - The number of inference units for an Amazon Comprehend entity recognizer endpoint.<br />+ <code>lambda:function:ProvisionedConcurrency</code> - The provisioned concurrency for a Lambda function.<br />+ <code>cassandra:table:ReadCapacityUnits</code> - The provisioned read capacity for an Amazon Keyspaces table.<br />+ <code>cassandra:table:WriteCapacityUnits</code> - The provisioned write capacity for an Amazon Keyspaces table.<br />+ <code>kafka:broker-storage:VolumeSize</code> - The provisioned volume size (in GiB) for brokers in an Amazon MSK cluster.<br />+ <code>elasticache:replication-group:NodeGroups</code> - The number of node groups for an Amazon ElastiCache replication group.<br />+ <code>elasticache:replication-group:Replicas</code> - The number of replicas per node group for an Amazon ElastiCache replication group.<br />+ <code>neptune:cluster:ReadReplicaCount</code> - The count of read replicas in an Amazon Neptune DB cluster.<br />+ <code>sagemaker:variant:DesiredProvisionedConcurrency</code> - The provisioned concurrency for a SageMaker serverless endpoint.<br />+ <code>sagemaker:inference-component:DesiredCopyCount</code> - The number of copies across an endpoint for a SageMaker inference component.<br />+ <code>workspaces:workspacespool:DesiredUserSessions</code> - The number of user sessions for the WorkSpaces in the pool.</td></tr>
<tr><td><CopyableCode code="target_tracking_scaling_policy_configuration" /></td><td><code>object</code></td><td>A target tracking scaling policy.</td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="step_scaling_policy_configuration" /></td><td><code>object</code></td><td>A step scaling policy.</td></tr>
<tr><td><CopyableCode code="predictive_scaling_policy_configuration" /></td><td><code>object</code></td><td>The predictive scaling policy configuration.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationautoscaling-scalingpolicy.html"><code>AWS::ApplicationAutoScaling::ScalingPolicy</code></a>.

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
    <td><CopyableCode code="PolicyName, PolicyType, region" /></td>
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
Gets all <code>scaling_policies</code> in a region.
```sql
SELECT
region,
policy_type,
resource_id,
scaling_target_id,
policy_name,
service_namespace,
scalable_dimension,
target_tracking_scaling_policy_configuration,
arn,
step_scaling_policy_configuration,
predictive_scaling_policy_configuration
FROM aws.applicationautoscaling.scaling_policies
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>scaling_policy</code>.
```sql
SELECT
region,
policy_type,
resource_id,
scaling_target_id,
policy_name,
service_namespace,
scalable_dimension,
target_tracking_scaling_policy_configuration,
arn,
step_scaling_policy_configuration,
predictive_scaling_policy_configuration
FROM aws.applicationautoscaling.scaling_policies
WHERE region = 'us-east-1' AND data__Identifier = '<Arn>|<ScalableDimension>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>scaling_policy</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.applicationautoscaling.scaling_policies (
 PolicyType,
 PolicyName,
 region
)
SELECT 
'{{ PolicyType }}',
 '{{ PolicyName }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.applicationautoscaling.scaling_policies (
 PolicyType,
 ResourceId,
 ScalingTargetId,
 PolicyName,
 ServiceNamespace,
 ScalableDimension,
 TargetTrackingScalingPolicyConfiguration,
 StepScalingPolicyConfiguration,
 PredictiveScalingPolicyConfiguration,
 region
)
SELECT 
 '{{ PolicyType }}',
 '{{ ResourceId }}',
 '{{ ScalingTargetId }}',
 '{{ PolicyName }}',
 '{{ ServiceNamespace }}',
 '{{ ScalableDimension }}',
 '{{ TargetTrackingScalingPolicyConfiguration }}',
 '{{ StepScalingPolicyConfiguration }}',
 '{{ PredictiveScalingPolicyConfiguration }}',
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
  - name: scaling_policy
    props:
      - name: PolicyType
        value: '{{ PolicyType }}'
      - name: ResourceId
        value: '{{ ResourceId }}'
      - name: ScalingTargetId
        value: '{{ ScalingTargetId }}'
      - name: PolicyName
        value: '{{ PolicyName }}'
      - name: ServiceNamespace
        value: '{{ ServiceNamespace }}'
      - name: ScalableDimension
        value: '{{ ScalableDimension }}'
      - name: TargetTrackingScalingPolicyConfiguration
        value:
          ScaleOutCooldown: '{{ ScaleOutCooldown }}'
          TargetValue: null
          CustomizedMetricSpecification:
            MetricName: '{{ MetricName }}'
            Metrics:
              - ReturnData: '{{ ReturnData }}'
                Expression: '{{ Expression }}'
                Label: '{{ Label }}'
                MetricStat:
                  Stat: '{{ Stat }}'
                  Metric:
                    MetricName: '{{ MetricName }}'
                    Dimensions:
                      - Value: '{{ Value }}'
                        Name: '{{ Name }}'
                    Namespace: '{{ Namespace }}'
                  Unit: '{{ Unit }}'
                Id: '{{ Id }}'
            Statistic: '{{ Statistic }}'
            Dimensions:
              - Value: '{{ Value }}'
                Name: '{{ Name }}'
            Unit: '{{ Unit }}'
            Namespace: '{{ Namespace }}'
          DisableScaleIn: '{{ DisableScaleIn }}'
          ScaleInCooldown: '{{ ScaleInCooldown }}'
          PredefinedMetricSpecification:
            PredefinedMetricType: '{{ PredefinedMetricType }}'
            ResourceLabel: '{{ ResourceLabel }}'
      - name: StepScalingPolicyConfiguration
        value:
          MetricAggregationType: '{{ MetricAggregationType }}'
          Cooldown: '{{ Cooldown }}'
          StepAdjustments:
            - MetricIntervalUpperBound: null
              MetricIntervalLowerBound: null
              ScalingAdjustment: '{{ ScalingAdjustment }}'
          MinAdjustmentMagnitude: '{{ MinAdjustmentMagnitude }}'
          AdjustmentType: '{{ AdjustmentType }}'
      - name: PredictiveScalingPolicyConfiguration
        value:
          MaxCapacityBreachBehavior: '{{ MaxCapacityBreachBehavior }}'
          MaxCapacityBuffer: '{{ MaxCapacityBuffer }}'
          Mode: '{{ Mode }}'
          MetricSpecifications:
            - CustomizedLoadMetricSpecification:
                MetricDataQueries:
                  - ReturnData: '{{ ReturnData }}'
                    Expression: '{{ Expression }}'
                    Label: '{{ Label }}'
                    MetricStat:
                      Stat: '{{ Stat }}'
                      Metric:
                        MetricName: '{{ MetricName }}'
                        Dimensions:
                          - Value: '{{ Value }}'
                            Name: '{{ Name }}'
                        Namespace: '{{ Namespace }}'
                      Unit: '{{ Unit }}'
                    Id: '{{ Id }}'
              PredefinedLoadMetricSpecification:
                PredefinedMetricType: '{{ PredefinedMetricType }}'
                ResourceLabel: '{{ ResourceLabel }}'
              TargetValue: null
              PredefinedScalingMetricSpecification:
                PredefinedMetricType: '{{ PredefinedMetricType }}'
                ResourceLabel: '{{ ResourceLabel }}'
              CustomizedCapacityMetricSpecification:
                MetricDataQueries:
                  - null
              CustomizedScalingMetricSpecification:
                MetricDataQueries:
                  - null
              PredefinedMetricPairSpecification:
                PredefinedMetricType: '{{ PredefinedMetricType }}'
                ResourceLabel: '{{ ResourceLabel }}'
          SchedulingBufferTime: '{{ SchedulingBufferTime }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.applicationautoscaling.scaling_policies
WHERE data__Identifier = '<Arn|ScalableDimension>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>scaling_policies</code> resource, the following permissions are required:

### Read
```json
application-autoscaling:DescribeScalingPolicies
```

### Create
```json
application-autoscaling:DescribeScalingPolicies,
application-autoscaling:PutScalingPolicy,
cloudwatch:GetMetricData
```

### Update
```json
application-autoscaling:DescribeScalingPolicies,
application-autoscaling:PutScalingPolicy,
cloudwatch:GetMetricData
```

### List
```json
application-autoscaling:DescribeScalingPolicies
```

### Delete
```json
application-autoscaling:DescribeScalingPolicies,
application-autoscaling:DeleteScalingPolicy
```
