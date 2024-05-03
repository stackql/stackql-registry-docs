---
title: clusters
hide_title: false
hide_table_of_contents: false
keywords:
  - clusters
  - memorydb
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

Used to retrieve a list of <code>clusters</code> in a region or create a <code>clusters</code> resource, use <code>cluster</code> to operate on an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>clusters</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::MemoryDB::Cluster resource creates an Amazon MemoryDB Cluster.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.memorydb.clusters" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="cluster_name" /></td><td><code>string</code></td><td>The name of the cluster. This value must be unique as it also serves as the cluster identifier.</td></tr>
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
    <td><CopyableCode code="data__DesiredState, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="list_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
cluster_name
FROM aws.memorydb.clusters
WHERE region = 'us-east-1'
```

## Permissions

To operate on the <code>clusters</code> resource, the following permissions are required:

### Create
```json
memorydb:CreateCluster,
memorydb:DescribeClusters,
memorydb:ListTags
```

### List
```json
memorydb:DescribeClusters
```

