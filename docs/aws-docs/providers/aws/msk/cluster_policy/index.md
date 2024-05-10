---
title: cluster_policy
hide_title: false
hide_table_of_contents: false
keywords:
  - cluster_policy
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


Gets or updates an individual <code>cluster_policy</code> resource, use <code>cluster_policies</code> to retrieve a list of resources or to create or delete a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>cluster_policy</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::MSK::ClusterPolicy</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.msk.cluster_policy" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="policy" /></td><td><code>object</code></td><td>A policy document containing permissions to add to the specified cluster.</td></tr>
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
    <td><CopyableCode code="update_resource" /></td>
    <td><code>UPDATE</code></td>
    <td><CopyableCode code="data__Identifier, data__PatchDocument, region" /></td>
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
policy,
cluster_arn,
current_version
FROM aws.msk.cluster_policy
WHERE region = 'us-east-1' AND data__Identifier = '<ClusterArn>';
```


## Permissions

To operate on the <code>cluster_policy</code> resource, the following permissions are required:

### Read
```json
kafka:GetClusterPolicy
```

### Update
```json
kafka:PutClusterPolicy,
kafka:GetClusterPolicy
```

