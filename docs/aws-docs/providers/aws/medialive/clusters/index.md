---
title: clusters
hide_title: false
hide_table_of_contents: false
keywords:
  - clusters
  - medialive
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
<tr><td><b>Description</b></td><td>Definition of AWS::MediaLive::Cluster Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.medialive.clusters" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The ARN of the Cluster.</td></tr>
<tr><td><CopyableCode code="channel_ids" /></td><td><code>array</code></td><td>The MediaLive Channels that are currently running on Nodes in this Cluster.</td></tr>
<tr><td><CopyableCode code="cluster_type" /></td><td><code>string</code></td><td>The hardware type for the cluster.</td></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td>The unique ID of the Cluster.</td></tr>
<tr><td><CopyableCode code="instance_role_arn" /></td><td><code>string</code></td><td>The IAM role your nodes will use.</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The user-specified name of the Cluster to be created.</td></tr>
<tr><td><CopyableCode code="network_settings" /></td><td><code>object</code></td><td>On premises settings which will have the interface network mappings and default Output logical interface</td></tr>
<tr><td><CopyableCode code="state" /></td><td><code>string</code></td><td>The current state of the Cluster.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>A collection of key-value pairs.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-medialive-cluster.html"><code>AWS::MediaLive::Cluster</code></a>.

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
Gets all <code>clusters</code> in a region.
```sql
SELECT
region,
arn,
channel_ids,
cluster_type,
id,
instance_role_arn,
name,
network_settings,
state,
tags
FROM aws.medialive.clusters
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>cluster</code>.
```sql
SELECT
region,
arn,
channel_ids,
cluster_type,
id,
instance_role_arn,
name,
network_settings,
state,
tags
FROM aws.medialive.clusters
WHERE region = 'us-east-1' AND data__Identifier = '<Id>';
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
INSERT INTO aws.medialive.clusters (
 ClusterType,
 InstanceRoleArn,
 Name,
 NetworkSettings,
 Tags,
 region
)
SELECT 
'{{ ClusterType }}',
 '{{ InstanceRoleArn }}',
 '{{ Name }}',
 '{{ NetworkSettings }}',
 '{{ Tags }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.medialive.clusters (
 ClusterType,
 InstanceRoleArn,
 Name,
 NetworkSettings,
 Tags,
 region
)
SELECT 
 '{{ ClusterType }}',
 '{{ InstanceRoleArn }}',
 '{{ Name }}',
 '{{ NetworkSettings }}',
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
      - name: ClusterType
        value: '{{ ClusterType }}'
      - name: InstanceRoleArn
        value: '{{ InstanceRoleArn }}'
      - name: Name
        value: '{{ Name }}'
      - name: NetworkSettings
        value:
          DefaultRoute: '{{ DefaultRoute }}'
          InterfaceMappings:
            - LogicalInterfaceName: '{{ LogicalInterfaceName }}'
              NetworkId: '{{ NetworkId }}'
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
DELETE FROM aws.medialive.clusters
WHERE data__Identifier = '<Id>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>clusters</code> resource, the following permissions are required:

### Create
```json
medialive:CreateCluster,
medialive:DescribeCluster,
medialive:CreateTags,
ecs:CreateCluster,
ecs:RegisterTaskDefinition,
ecs:TagResource,
ecs:CreateService,
iam:PassRole,
medialive:ListTagsForResource
```

### Read
```json
medialive:DescribeCluster,
medialive:ListTagsForResource
```

### Update
```json
medialive:UpdateCluster,
medialive:DescribeCluster,
medialive:CreateTags,
medialive:DeleteTags,
medialive:ListTagsForResource
```

### Delete
```json
medialive:DeleteCluster,
medialive:DescribeCluster,
ecs:DeleteService
```

### List
```json
medialive:ListClusters
```
