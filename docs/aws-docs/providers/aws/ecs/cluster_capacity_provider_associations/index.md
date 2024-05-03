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

Gets or operates on an individual <code>cluster_capacity_provider_associations</code> resource, use <code>cluster_capacity_provider_associations</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>cluster_capacity_provider_associations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Associate a set of ECS Capacity Providers with a specified ECS Cluster</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ecs.cluster_capacity_provider_associations" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="capacity_providers" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="cluster" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="default_capacity_provider_strategy" /></td><td><code>array</code></td><td></td></tr>
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
    <td><CopyableCode code="update_resource" /></td>
    <td><code>UPDATE</code></td>
    <td><CopyableCode code="data__Identifier, data__PatchDocument, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
capacity_providers,
cluster,
default_capacity_provider_strategy
FROM aws.ecs.cluster_capacity_provider_associations
WHERE data__Identifier = '<Cluster>';
```

## Permissions

To operate on the <code>cluster_capacity_provider_associations</code> resource, the following permissions are required:

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

