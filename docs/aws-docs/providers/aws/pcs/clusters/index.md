---
title: clusters
hide_title: false
hide_table_of_contents: false
keywords:
  - clusters
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

Creates, updates, deletes or gets a <code>cluster</code> resource or lists <code>clusters</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>clusters</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>AWS::PCS::Cluster resource creates an AWS PCS cluster.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.pcs.clusters" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The unique Amazon Resource Name (ARN) of the cluster.</td></tr>
<tr><td><CopyableCode code="endpoints" /></td><td><code>array</code></td><td>The list of endpoints available for interaction with the scheduler.</td></tr>
<tr><td><CopyableCode code="error_info" /></td><td><code>array</code></td><td>The list of errors that occurred during cluster provisioning.</td></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td>The generated unique ID of the cluster.</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name that identifies the cluster.</td></tr>
<tr><td><CopyableCode code="networking" /></td><td><code>object</code></td><td>The networking configuration for the cluster's control plane.</td></tr>
<tr><td><CopyableCode code="scheduler" /></td><td><code>object</code></td><td>The cluster management and job scheduling software associated with the cluster.</td></tr>
<tr><td><CopyableCode code="size" /></td><td><code>string</code></td><td>The size of the cluster.</td></tr>
<tr><td><CopyableCode code="slurm_configuration" /></td><td><code>object</code></td><td>Additional options related to the Slurm scheduler.</td></tr>
<tr><td><CopyableCode code="status" /></td><td><code>string</code></td><td>The provisioning status of the cluster. The provisioning status doesn't indicate the overall health of the cluster.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code></code></td><td>1 or more tags added to the resource. Each tag consists of a tag key and tag value. The tag value is optional and can be an empty string.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pcs-cluster.html"><code>AWS::PCS::Cluster</code></a>.

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
    <td><CopyableCode code="Networking, Scheduler, Size, region" /></td>
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
endpoints,
error_info,
id,
name,
networking,
scheduler,
size,
slurm_configuration,
status,
tags
FROM aws.pcs.clusters
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>cluster</code>.
```sql
SELECT
region,
arn,
endpoints,
error_info,
id,
name,
networking,
scheduler,
size,
slurm_configuration,
status,
tags
FROM aws.pcs.clusters
WHERE region = 'us-east-1' AND data__Identifier = '<Arn>';
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
INSERT INTO aws.pcs.clusters (
 Networking,
 Scheduler,
 Size,
 region
)
SELECT 
'{{ Networking }}',
 '{{ Scheduler }}',
 '{{ Size }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.pcs.clusters (
 Name,
 Networking,
 Scheduler,
 Size,
 SlurmConfiguration,
 Tags,
 region
)
SELECT 
 '{{ Name }}',
 '{{ Networking }}',
 '{{ Scheduler }}',
 '{{ Size }}',
 '{{ SlurmConfiguration }}',
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
      - name: Name
        value: '{{ Name }}'
      - name: Networking
        value:
          SecurityGroupIds:
            - '{{ SecurityGroupIds[0] }}'
          SubnetIds:
            - '{{ SubnetIds[0] }}'
      - name: Scheduler
        value:
          Type: '{{ Type }}'
          Version: '{{ Version }}'
      - name: Size
        value: '{{ Size }}'
      - name: SlurmConfiguration
        value:
          AuthKey:
            SecretArn: '{{ SecretArn }}'
            SecretVersion: '{{ SecretVersion }}'
          ScaleDownIdleTimeInSeconds: '{{ ScaleDownIdleTimeInSeconds }}'
          SlurmCustomSettings:
            - ParameterName: '{{ ParameterName }}'
              ParameterValue: '{{ ParameterValue }}'
      - name: Tags
        value: null

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.pcs.clusters
WHERE data__Identifier = '<Arn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>clusters</code> resource, the following permissions are required:

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
pcs:CreateCluster,
pcs:GetCluster,
pcs:ListTagsForResource,
pcs:TagResource
```

### Read
```json
pcs:GetCluster,
pcs:ListTagsForResource
```

### Update
```json
pcs:GetCluster,
pcs:ListTagsForResource,
pcs:TagResource,
pcs:UntagResource
```

### Delete
```json
pcs:DeleteCluster,
pcs:GetCluster
```

### List
```json
pcs:ListClusters
```
