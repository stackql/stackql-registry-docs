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
Gets an individual <code>cluster_policy</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>cluster_policy</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>cluster_policy</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.msk.cluster_policy</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>policy</code></td><td><code>object</code></td><td>A policy document containing permissions to add to the specified cluster.</td></tr>
<tr><td><code>cluster_arn</code></td><td><code>string</code></td><td>The arn of the cluster for the resource policy.</td></tr>
<tr><td><code>current_version</code></td><td><code>string</code></td><td>The current version of the policy attached to the specified cluster</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

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

### Delete
```json
kafka:DeleteClusterPolicy,
kafka:GetClusterPolicy
```


## Example
```sql
SELECT
region,
policy,
cluster_arn,
current_version
FROM awscc.msk.cluster_policy
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;ClusterArn&gt;'
```
