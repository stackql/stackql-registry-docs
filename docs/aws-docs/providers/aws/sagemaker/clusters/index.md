---
title: clusters
hide_title: false
hide_table_of_contents: false
keywords:
  - clusters
  - sagemaker
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

Creates, updates, deletes or gets a <code>cluster</code> resource or lists <code>clusters</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>clusters</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::SageMaker::Cluster</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.sagemaker.clusters" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="cluster_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the HyperPod Cluster.</td></tr>
<tr><td><CopyableCode code="vpc_config" /></td><td><code>object</code></td><td>Specifies a VPC that your training jobs and hosted models have access to. Control access to and from your training and model containers by configuring the VPC.</td></tr>
<tr><td><CopyableCode code="node_recovery" /></td><td><code>string</code></td><td>If node auto-recovery is set to true, faulty nodes will be replaced or rebooted when a failure is detected. If set to false, nodes will be labelled when a fault is detected.</td></tr>
<tr><td><CopyableCode code="creation_time" /></td><td><code>string</code></td><td>The time at which the HyperPod cluster was created.</td></tr>
<tr><td><CopyableCode code="instance_groups" /></td><td><code>array</code></td><td>The instance groups of the SageMaker HyperPod cluster.</td></tr>
<tr><td><CopyableCode code="cluster_name" /></td><td><code>string</code></td><td>The name of the HyperPod Cluster.</td></tr>
<tr><td><CopyableCode code="failure_message" /></td><td><code>string</code></td><td>The failure message of the HyperPod Cluster.</td></tr>
<tr><td><CopyableCode code="orchestrator" /></td><td><code>object</code></td><td>Specifies parameter(s) specific to the orchestrator, e.g. specify the EKS cluster.</td></tr>
<tr><td><CopyableCode code="cluster_status" /></td><td><code>string</code></td><td>The status of the HyperPod Cluster.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>Custom tags for managing the SageMaker HyperPod cluster as an AWS resource. You can add tags to your cluster in the same way you add them in other AWS services that support tagging.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-cluster.html"><code>AWS::SageMaker::Cluster</code></a>.

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
    <td><CopyableCode code="InstanceGroups, region" /></td>
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
Gets all <code>clusters</code> in a region.
```sql
SELECT
region,
cluster_arn,
vpc_config,
node_recovery,
creation_time,
instance_groups,
cluster_name,
failure_message,
orchestrator,
cluster_status,
tags
FROM aws.sagemaker.clusters
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>cluster</code>.
```sql
SELECT
region,
cluster_arn,
vpc_config,
node_recovery,
creation_time,
instance_groups,
cluster_name,
failure_message,
orchestrator,
cluster_status,
tags
FROM aws.sagemaker.clusters
WHERE region = 'us-east-1' AND data__Identifier = '<ClusterArn>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>cluster</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.sagemaker.clusters (
 InstanceGroups,
 region
)
SELECT 
'{{ InstanceGroups }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.sagemaker.clusters (
 VpcConfig,
 NodeRecovery,
 InstanceGroups,
 ClusterName,
 Orchestrator,
 Tags,
 region
)
SELECT 
 '{{ VpcConfig }}',
 '{{ NodeRecovery }}',
 '{{ InstanceGroups }}',
 '{{ ClusterName }}',
 '{{ Orchestrator }}',
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
  - name: cluster
    props:
      - name: VpcConfig
        value:
          SecurityGroupIds:
            - '{{ SecurityGroupIds[0] }}'
          Subnets:
            - '{{ Subnets[0] }}'
      - name: NodeRecovery
        value: '{{ NodeRecovery }}'
      - name: InstanceGroups
        value:
          - OverrideVpcConfig: null
            InstanceCount: '{{ InstanceCount }}'
            OnStartDeepHealthChecks:
              - '{{ OnStartDeepHealthChecks[0] }}'
            InstanceGroupName: '{{ InstanceGroupName }}'
            InstanceStorageConfigs:
              - {}
            CurrentCount: '{{ CurrentCount }}'
            LifeCycleConfig:
              SourceS3Uri: '{{ SourceS3Uri }}'
              OnCreate: '{{ OnCreate }}'
            InstanceType: '{{ InstanceType }}'
            ThreadsPerCore: '{{ ThreadsPerCore }}'
            ExecutionRole: '{{ ExecutionRole }}'
      - name: ClusterName
        value: '{{ ClusterName }}'
      - name: Orchestrator
        value:
          Eks:
            ClusterArn: '{{ ClusterArn }}'
      - name: Tags
        value:
          - Value: '{{ Value }}'
            Key: '{{ Key }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.sagemaker.clusters
WHERE data__Identifier = '<ClusterArn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>clusters</code> resource, the following permissions are required:

### Read
```json
sagemaker:DescribeCluster,
sagemaker:ListTags
```

### Create
```json
sagemaker:CreateCluster,
sagemaker:DescribeCluster,
sagemaker:AddTags,
sagemaker:ListTags,
eks:DescribeAccessEntry,
eks:DescribeCluster,
eks:CreateAccessEntry,
eks:DeleteAccessEntry,
eks:AssociateAccessPolicy,
iam:CreateServiceLinkedRole,
iam:PassRole
```

### Update
```json
sagemaker:UpdateCluster,
sagemaker:DescribeCluster,
sagemaker:ListTags,
sagemaker:AddTags,
sagemaker:DeleteTags,
eks:DescribeAccessEntry,
eks:DescribeCluster,
eks:CreateAccessEntry,
eks:DeleteAccessEntry,
iam:PassRole
```

### List
```json
sagemaker:ListClusters
```

### Delete
```json
sagemaker:DeleteCluster,
sagemaker:DescribeCluster,
eks:DescribeAccessEntry,
eks:DeleteAccessEntry
```
