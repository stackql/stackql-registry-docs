---
title: scaling_policies_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - scaling_policies_list_only
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

Lists <code>scaling_policies</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/scaling_policies/"><code>scaling_policies</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>scaling_policies_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The <code>AWS::ApplicationAutoScaling::ScalingPolicy</code> resource defines a scaling policy that Application Auto Scaling uses to adjust the capacity of a scalable target. <br />For more information, see &#91;Target tracking scaling policies&#93;(https://docs.aws.amazon.com/autoscaling/application/userguide/application-auto-scaling-target-tracking.html) and &#91;Step scaling policies&#93;(https://docs.aws.amazon.com/autoscaling/application/userguide/application-auto-scaling-step-scaling-policies.html) in the *Application Auto Scaling User Guide*.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.applicationautoscaling.scaling_policies_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="scalable_dimension" /></td><td><code>string</code></td><td>The scalable dimension. This string consists of the service namespace, resource type, and scaling property.<br />+ <code>ecs:service:DesiredCount</code> - The task count of an ECS service.<br />+ <code>elasticmapreduce:instancegroup:InstanceCount</code> - The instance count of an EMR Instance Group.<br />+ <code>ec2:spot-fleet-request:TargetCapacity</code> - The target capacity of a Spot Fleet.<br />+ <code>appstream:fleet:DesiredCapacity</code> - The capacity of an AppStream 2.0 fleet.<br />+ <code>dynamodb:table:ReadCapacityUnits</code> - The provisioned read capacity for a DynamoDB table.<br />+ <code>dynamodb:table:WriteCapacityUnits</code> - The provisioned write capacity for a DynamoDB table.<br />+ <code>dynamodb:index:ReadCapacityUnits</code> - The provisioned read capacity for a DynamoDB global secondary index.<br />+ <code>dynamodb:index:WriteCapacityUnits</code> - The provisioned write capacity for a DynamoDB global secondary index.<br />+ <code>rds:cluster:ReadReplicaCount</code> - The count of Aurora Replicas in an Aurora DB cluster. Available for Aurora MySQL-compatible edition and Aurora PostgreSQL-compatible edition.<br />+ <code>sagemaker:variant:DesiredInstanceCount</code> - The number of EC2 instances for a SageMaker model endpoint variant.<br />+ <code>custom-resource:ResourceType:Property</code> - The scalable dimension for a custom resource provided by your own application or service.<br />+ <code>comprehend:document-classifier-endpoint:DesiredInferenceUnits</code> - The number of inference units for an Amazon Comprehend document classification endpoint.<br />+ <code>comprehend:entity-recognizer-endpoint:DesiredInferenceUnits</code> - The number of inference units for an Amazon Comprehend entity recognizer endpoint.<br />+ <code>lambda:function:ProvisionedConcurrency</code> - The provisioned concurrency for a Lambda function.<br />+ <code>cassandra:table:ReadCapacityUnits</code> - The provisioned read capacity for an Amazon Keyspaces table.<br />+ <code>cassandra:table:WriteCapacityUnits</code> - The provisioned write capacity for an Amazon Keyspaces table.<br />+ <code>kafka:broker-storage:VolumeSize</code> - The provisioned volume size (in GiB) for brokers in an Amazon MSK cluster.<br />+ <code>elasticache:replication-group:NodeGroups</code> - The number of node groups for an Amazon ElastiCache replication group.<br />+ <code>elasticache:replication-group:Replicas</code> - The number of replicas per node group for an Amazon ElastiCache replication group.<br />+ <code>neptune:cluster:ReadReplicaCount</code> - The count of read replicas in an Amazon Neptune DB cluster.<br />+ <code>sagemaker:variant:DesiredProvisionedConcurrency</code> - The provisioned concurrency for a SageMaker serverless endpoint.<br />+ <code>sagemaker:inference-component:DesiredCopyCount</code> - The number of copies across an endpoint for a SageMaker inference component.<br />+ <code>workspaces:workspacespool:DesiredUserSessions</code> - The number of user sessions for the WorkSpaces in the pool.</td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td></td></tr>
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
    <td><CopyableCode code="list_resources" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples
Lists all <code>scaling_policies</code> in a region.
```sql
SELECT
region,
arn,
scalable_dimension
FROM aws.applicationautoscaling.scaling_policies_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>scaling_policies_list_only</code> resource, see <a href="/providers/aws/applicationautoscaling/scaling_policies/#permissions"><code>scaling_policies</code></a>

