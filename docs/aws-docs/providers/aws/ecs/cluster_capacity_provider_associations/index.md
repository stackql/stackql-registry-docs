---
title: cluster_capacity_provider_associations
hide_title: false
hide_table_of_contents: false
keywords:
  - cluster_capacity_provider_associations
  - ecs
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

Creates, updates, deletes or gets a <code>cluster_capacity_provider_association</code> resource or lists <code>cluster_capacity_provider_associations</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>cluster_capacity_provider_associations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Associate a set of ECS Capacity Providers with a specified ECS Cluster</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ecs.cluster_capacity_provider_associations" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="capacity_providers" /></td><td><code>array</code></td><td>List of capacity providers to associate with the cluster</td></tr>
<tr><td><CopyableCode code="cluster" /></td><td><code>string</code></td><td>The name of the cluster</td></tr>
<tr><td><CopyableCode code="default_capacity_provider_strategy" /></td><td><code>array</code></td><td>List of capacity providers to associate with the cluster</td></tr>
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
    <td><CopyableCode code="CapacityProviders, Cluster, DefaultCapacityProviderStrategy, region" /></td>
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
Gets all <code>cluster_capacity_provider_associations</code> in a region.
```sql
SELECT
region,
capacity_providers,
cluster,
default_capacity_provider_strategy
FROM aws.ecs.cluster_capacity_provider_associations
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>cluster_capacity_provider_association</code>.
```sql
SELECT
region,
capacity_providers,
cluster,
default_capacity_provider_strategy
FROM aws.ecs.cluster_capacity_provider_associations
WHERE region = 'us-east-1' AND data__Identifier = '<Cluster>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>cluster_capacity_provider_association</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.ecs.cluster_capacity_provider_associations (
 CapacityProviders,
 Cluster,
 DefaultCapacityProviderStrategy,
 region
)
SELECT 
'{{ CapacityProviders }}',
 '{{ Cluster }}',
 '{{ DefaultCapacityProviderStrategy }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.ecs.cluster_capacity_provider_associations (
 CapacityProviders,
 Cluster,
 DefaultCapacityProviderStrategy,
 region
)
SELECT 
 '{{ CapacityProviders }}',
 '{{ Cluster }}',
 '{{ DefaultCapacityProviderStrategy }}',
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
  - name: cluster_capacity_provider_association
    props:
      - name: CapacityProviders
        value:
          - '{{ CapacityProviders[0] }}'
      - name: Cluster
        value: '{{ Cluster }}'
      - name: DefaultCapacityProviderStrategy
        value:
          - Base: '{{ Base }}'
            Weight: '{{ Weight }}'
            CapacityProvider: null

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.ecs.cluster_capacity_provider_associations
WHERE data__Identifier = '<Cluster>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>cluster_capacity_provider_associations</code> resource, the following permissions are required:

### Create
```json
ecs:DescribeClusters,
ecs:PutClusterCapacityProviders
```

### Read
```json
ecs:DescribeClusters
```

### Update
```json
ecs:DescribeClusters,
ecs:PutClusterCapacityProviders
```

### Delete
```json
ecs:PutClusterCapacityProviders,
ecs:DescribeClusters
```

### List
```json
ecs:DescribeClusters,
ecs:ListClusters
```

