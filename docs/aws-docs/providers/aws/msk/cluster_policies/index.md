---
title: cluster_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - cluster_policies
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

Creates, updates, deletes or gets a <code>cluster_policy</code> resource or lists <code>cluster_policies</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>cluster_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::MSK::ClusterPolicy</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.msk.cluster_policies" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="policy" /></td><td><code>object</code></td><td>A policy document containing permissions to add to the specified cluster.</td></tr>
<tr><td><CopyableCode code="cluster_arn" /></td><td><code>string</code></td><td>The arn of the cluster for the resource policy.</td></tr>
<tr><td><CopyableCode code="current_version" /></td><td><code>string</code></td><td>The current version of the policy attached to the specified cluster</td></tr>
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
    <td><CopyableCode code="Policy, ClusterArn, region" /></td>
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
Gets all <code>cluster_policies</code> in a region.
```sql
SELECT
region,
policy,
cluster_arn,
current_version
FROM aws.msk.cluster_policies
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>cluster_policy</code>.
```sql
SELECT
region,
policy,
cluster_arn,
current_version
FROM aws.msk.cluster_policies
WHERE region = 'us-east-1' AND data__Identifier = '<ClusterArn>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>cluster_policy</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.msk.cluster_policies (
 Policy,
 ClusterArn,
 region
)
SELECT 
'{{ Policy }}',
 '{{ ClusterArn }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.msk.cluster_policies (
 Policy,
 ClusterArn,
 region
)
SELECT 
 '{{ Policy }}',
 '{{ ClusterArn }}',
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
  - name: cluster_policy
    props:
      - name: Policy
        value: {}
      - name: ClusterArn
        value: '{{ ClusterArn }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.msk.cluster_policies
WHERE data__Identifier = '<ClusterArn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>cluster_policies</code> resource, the following permissions are required:

### Create
```json
kafka:PutClusterPolicy,
kafka:GetClusterPolicy
```

### Read
```json
kafka:GetClusterPolicy
```

### List
```json
kafka:GetClusterPolicy
```

### Update
```json
kafka:PutClusterPolicy,
kafka:GetClusterPolicy
```

### Delete
```json
kafka:DeleteClusterPolicy,
kafka:GetClusterPolicy
```

