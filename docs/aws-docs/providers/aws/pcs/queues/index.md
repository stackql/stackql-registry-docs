---
title: queues
hide_title: false
hide_table_of_contents: false
keywords:
  - queues
  - pcs
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

Creates, updates, deletes or gets a <code>queue</code> resource or lists <code>queues</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>queues</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>AWS::PCS::Queue resource creates an AWS PCS queue.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.pcs.queues" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The unique Amazon Resource Name (ARN) of the queue.</td></tr>
<tr><td><CopyableCode code="cluster_id" /></td><td><code>string</code></td><td>The ID of the cluster of the queue.</td></tr>
<tr><td><CopyableCode code="compute_node_group_configurations" /></td><td><code>array</code></td><td>The list of compute node group configurations associated with the queue. Queues assign jobs to associated compute node groups.</td></tr>
<tr><td><CopyableCode code="error_info" /></td><td><code>array</code></td><td>The list of errors that occurred during queue provisioning.</td></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td>The generated unique ID of the queue.</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name that identifies the queue.</td></tr>
<tr><td><CopyableCode code="status" /></td><td><code>string</code></td><td>The provisioning status of the queue. The provisioning status doesn't indicate the overall health of the queue.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>object</code></td><td>1 or more tags added to the resource. Each tag consists of a tag key and tag value. The tag value is optional and can be an empty string.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pcs-queue.html"><code>AWS::PCS::Queue</code></a>.

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
    <td><CopyableCode code="ClusterId, region" /></td>
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
Gets all <code>queues</code> in a region.
```sql
SELECT
region,
arn,
cluster_id,
compute_node_group_configurations,
error_info,
id,
name,
status,
tags
FROM aws.pcs.queues
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>queue</code>.
```sql
SELECT
region,
arn,
cluster_id,
compute_node_group_configurations,
error_info,
id,
name,
status,
tags
FROM aws.pcs.queues
WHERE region = 'us-east-1' AND data__Identifier = '<Arn>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>queue</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.pcs.queues (
 ClusterId,
 region
)
SELECT 
'{{ ClusterId }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.pcs.queues (
 ClusterId,
 ComputeNodeGroupConfigurations,
 Name,
 Tags,
 region
)
SELECT 
 '{{ ClusterId }}',
 '{{ ComputeNodeGroupConfigurations }}',
 '{{ Name }}',
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
  - name: queue
    props:
      - name: ClusterId
        value: '{{ ClusterId }}'
      - name: ComputeNodeGroupConfigurations
        value:
          - ComputeNodeGroupId: '{{ ComputeNodeGroupId }}'
      - name: Name
        value: '{{ Name }}'
      - name: Tags
        value: {}

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.pcs.queues
WHERE data__Identifier = '<Arn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>queues</code> resource, the following permissions are required:

### Create
```json
ec2:CreateNetworkInterface,
ec2:DescribeVpcs,
ec2:DescribeSubnets,
ec2:DescribeSecurityGroups,
ec2:GetSecurityGroupsForVpc,
iam:CreateServiceLinkedRole,
secretsmanager:CreateSecret,
secretsmanager:TagResource,
pcs:CreateQueue,
pcs:GetQueue,
pcs:ListTagsForResource,
pcs:TagResource
```

### Read
```json
pcs:GetQueue,
pcs:ListTagsForResource
```

### Update
```json
pcs:GetQueue,
pcs:UpdateQueue,
pcs:ListTagsForResource,
pcs:TagResource,
pcs:UntagResource
```

### Delete
```json
pcs:DeleteQueue,
pcs:GetQueue
```

### List
```json
pcs:ListClusters,
pcs:ListQueues
```
