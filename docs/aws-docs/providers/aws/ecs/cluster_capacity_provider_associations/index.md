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
Gets an individual <code>cluster_capacity_provider_associations</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>cluster_capacity_provider_associations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>cluster_capacity_provider_associations</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ecs.cluster_capacity_provider_associations</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>capacity_providers</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>cluster</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>default_capacity_provider_strategy</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
capacity_providers,
cluster,
default_capacity_provider_strategy
FROM aws.ecs.cluster_capacity_provider_associations
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;Cluster&gt;'
```
