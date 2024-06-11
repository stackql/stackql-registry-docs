---
title: replicators
hide_title: false
hide_table_of_contents: false
keywords:
  - replicators
  - msk
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

Creates, updates, deletes or gets a <code>replicator</code> resource or lists <code>replicators</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>replicators</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::MSK::Replicator</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.msk.replicators" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="replicator_arn" /></td><td><code>string</code></td><td>Amazon Resource Name for the created replicator.</td></tr>
<tr><td><CopyableCode code="replicator_name" /></td><td><code>string</code></td><td>The name of the replicator.</td></tr>
<tr><td><CopyableCode code="current_version" /></td><td><code>string</code></td><td>The current version of the MSK replicator.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>A summary description of the replicator.</td></tr>
<tr><td><CopyableCode code="kafka_clusters" /></td><td><code>array</code></td><td>Specifies a list of Kafka clusters which are targets of the replicator.</td></tr>
<tr><td><CopyableCode code="replication_info_list" /></td><td><code>array</code></td><td>A list of replication configurations, where each configuration targets a given source cluster to target cluster replication flow.</td></tr>
<tr><td><CopyableCode code="service_execution_role_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the IAM role used by the replicator to access external resources.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>A collection of tags associated with a resource</td></tr>
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
    <td><CopyableCode code="ReplicatorName, ReplicationInfoList, KafkaClusters, ServiceExecutionRoleArn, region" /></td>
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
List all <code>replicators</code> in a region.
```sql
SELECT
region,
replicator_arn
FROM aws.msk.replicators
WHERE region = 'us-east-1';
```
Gets all properties from a <code>replicator</code>.
```sql
SELECT
region,
replicator_arn,
replicator_name,
current_version,
description,
kafka_clusters,
replication_info_list,
service_execution_role_arn,
tags
FROM aws.msk.replicators
WHERE region = 'us-east-1' AND data__Identifier = '<ReplicatorArn>';
```


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>replicator</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.msk.replicators (
 ReplicatorName,
 KafkaClusters,
 ReplicationInfoList,
 ServiceExecutionRoleArn,
 region
)
SELECT 
'{{ ReplicatorName }}',
 '{{ KafkaClusters }}',
 '{{ ReplicationInfoList }}',
 '{{ ServiceExecutionRoleArn }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.msk.replicators (
 ReplicatorName,
 CurrentVersion,
 Description,
 KafkaClusters,
 ReplicationInfoList,
 ServiceExecutionRoleArn,
 Tags,
 region
)
SELECT 
 '{{ ReplicatorName }}',
 '{{ CurrentVersion }}',
 '{{ Description }}',
 '{{ KafkaClusters }}',
 '{{ ReplicationInfoList }}',
 '{{ ServiceExecutionRoleArn }}',
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
  - name: replicator
    props:
      - name: ReplicatorName
        value: '{{ ReplicatorName }}'
      - name: CurrentVersion
        value: '{{ CurrentVersion }}'
      - name: Description
        value: '{{ Description }}'
      - name: KafkaClusters
        value:
          - AmazonMskCluster:
              MskClusterArn: '{{ MskClusterArn }}'
            VpcConfig:
              SecurityGroupIds:
                - '{{ SecurityGroupIds[0] }}'
              SubnetIds:
                - '{{ SubnetIds[0] }}'
      - name: ReplicationInfoList
        value:
          - SourceKafkaClusterArn: '{{ SourceKafkaClusterArn }}'
            TargetKafkaClusterArn: '{{ TargetKafkaClusterArn }}'
            TargetCompressionType: '{{ TargetCompressionType }}'
            TopicReplication:
              TopicsToReplicate:
                - '{{ TopicsToReplicate[0] }}'
              TopicsToExclude:
                - '{{ TopicsToExclude[0] }}'
              CopyTopicConfigurations: '{{ CopyTopicConfigurations }}'
              CopyAccessControlListsForTopics: '{{ CopyAccessControlListsForTopics }}'
              DetectAndCopyNewTopics: '{{ DetectAndCopyNewTopics }}'
              StartingPosition:
                Type: '{{ Type }}'
            ConsumerGroupReplication:
              ConsumerGroupsToReplicate:
                - '{{ ConsumerGroupsToReplicate[0] }}'
              ConsumerGroupsToExclude:
                - '{{ ConsumerGroupsToExclude[0] }}'
              SynchroniseConsumerGroupOffsets: '{{ SynchroniseConsumerGroupOffsets }}'
              DetectAndCopyNewConsumerGroups: '{{ DetectAndCopyNewConsumerGroups }}'
      - name: ServiceExecutionRoleArn
        value: '{{ ServiceExecutionRoleArn }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.msk.replicators
WHERE data__Identifier = '<ReplicatorArn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>replicators</code> resource, the following permissions are required:

### Create
```json
ec2:CreateNetworkInterface,
ec2:DescribeSecurityGroups,
ec2:DescribeSubnets,
ec2:DescribeVpcs,
iam:CreateServiceLinkedRole,
iam:PassRole,
kafka:CreateReplicator,
kafka:CreateReplicatorReference,
kafka:DescribeClusterV2,
kafka:DescribeReplicator,
kafka:GetBootstrapBrokers,
kafka:ListTagsForResource,
kafka:TagResource
```

### Read
```json
kafka:DescribeReplicator,
kafka:ListTagsForResource
```

### Update
```json
kafka:DescribeReplicator,
kafka:ListTagsForResource,
kafka:TagResource,
kafka:UntagResource,
kafka:UpdateReplicationInfo
```

### Delete
```json
kafka:DeleteReplicator,
kafka:DescribeReplicator,
kafka:ListTagsForResource,
kafka:UntagResource
```

### List
```json
kafka:ListReplicators
```

