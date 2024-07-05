---
title: cluster_capacity_provider_associations_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - cluster_capacity_provider_associations_list_only
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

Lists <code>cluster_capacity_provider_associations</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/cluster_capacity_provider_associations/"><code>cluster_capacity_provider_associations</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>cluster_capacity_provider_associations_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Associate a set of ECS Capacity Providers with a specified ECS Cluster</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ecs.cluster_capacity_provider_associations_list_only" /></td></tr>
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
    <td><CopyableCode code="list_resources" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples
Lists all <code>cluster_capacity_provider_associations</code> in a region.
```sql
SELECT
region,
cluster
FROM aws.ecs.cluster_capacity_provider_associations_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>cluster_capacity_provider_associations_list_only</code> resource, see <a href="/providers/aws/ecs/cluster_capacity_provider_associations/#permissions"><code>cluster_capacity_provider_associations</code></a>


