---
title: virtual_cluster
hide_title: false
hide_table_of_contents: false
keywords:
  - virtual_cluster
  - emrcontainers
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

Gets or operates on an individual <code>virtual_cluster</code> resource, use <code>virtual_clusters</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>virtual_cluster</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Schema of AWS::EMRContainers::VirtualCluster Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.emrcontainers.virtual_cluster" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="container_provider" /></td><td><code>object</code></td><td>Container provider of the virtual cluster.</td></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td>Id of the virtual cluster.</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>Name of the virtual cluster.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>An array of key-value pairs to apply to this virtual cluster.</td></tr>
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
arn,
container_provider,
id,
name,
tags
FROM aws.emrcontainers.virtual_cluster
WHERE data__Identifier = '<Id>';
```

## Permissions

To operate on the <code>virtual_cluster</code> resource, the following permissions are required:

### Read
```json
emr-containers:DescribeVirtualCluster
```

### Delete
```json
emr-containers:DeleteVirtualCluster
```

### Update
```json
emr-containers:DescribeVirtualCluster,
emr-containers:ListTagsForResource,
emr-containers:TagResource,
emr-containers:UntagResource
```

