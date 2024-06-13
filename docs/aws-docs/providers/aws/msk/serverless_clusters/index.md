---
title: serverless_clusters
hide_title: false
hide_table_of_contents: false
keywords:
  - serverless_clusters
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

Creates, updates, deletes or gets a <code>serverless_cluster</code> resource or lists <code>serverless_clusters</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>serverless_clusters</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::MSK::ServerlessCluster</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.msk.serverless_clusters" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="cluster_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="vpc_configs" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="client_authentication" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>object</code></td><td>A key-value pair to associate with a resource.</td></tr>
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
    <td><CopyableCode code="ClusterName, VpcConfigs, ClientAuthentication, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
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
List all <code>serverless_clusters</code> in a region.
```sql
SELECT
region,
arn
FROM aws.msk.serverless_clusters
WHERE region = 'us-east-1';
```
Gets all properties from a <code>serverless_cluster</code>.
```sql
SELECT
region,
arn,
cluster_name,
vpc_configs,
client_authentication,
tags
FROM aws.msk.serverless_clusters
WHERE region = 'us-east-1' AND data__Identifier = '<Arn>';
```


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>serverless_cluster</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.msk.serverless_clusters (
 ClusterName,
 VpcConfigs,
 ClientAuthentication,
 region
)
SELECT 
'{{ ClusterName }}',
 '{{ VpcConfigs }}',
 '{{ ClientAuthentication }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.msk.serverless_clusters (
 ClusterName,
 VpcConfigs,
 ClientAuthentication,
 Tags,
 region
)
SELECT 
 '{{ ClusterName }}',
 '{{ VpcConfigs }}',
 '{{ ClientAuthentication }}',
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
  - name: serverless_cluster
    props:
      - name: ClusterName
        value: '{{ ClusterName }}'
      - name: VpcConfigs
        value:
          - SecurityGroups:
              - '{{ SecurityGroups[0] }}'
            SubnetIds:
              - '{{ SubnetIds[0] }}'
      - name: ClientAuthentication
        value:
          Sasl:
            Iam:
              Enabled: '{{ Enabled }}'
      - name: Tags
        value: {}

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.msk.serverless_clusters
WHERE data__Identifier = '<Arn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>serverless_clusters</code> resource, the following permissions are required:

### Create
```json
kafka:CreateClusterV2,
kafka:TagResource,
kafka:DescribeClusterV2,
ec2:CreateVpcEndpoint,
ec2:CreateTags,
ec2:DescribeVpcAttribute,
ec2:DescribeSubnets,
ec2:DescribeVpcEndpoints,
ec2:DescribeVpcs,
ec2:DescribeSecurityGroups
```

### Read
```json
kafka:DescribeClusterV2
```

### Delete
```json
kafka:DeleteCluster,
kafka:DescribeClusterV2,
ec2:DeleteVpcEndpoints
```

### List
```json
kafka:ListClustersV2
```

