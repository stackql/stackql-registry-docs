---
title: cluster
hide_title: false
hide_table_of_contents: false
keywords:
  - cluster
  - route53recoverycontrol
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>cluster</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>cluster</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>cluster</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.route53recoverycontrol.cluster</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td>Name of a Cluster. You can use any non-white space character in the name</td></tr>
<tr><td><code>cluster_arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the cluster.</td></tr>
<tr><td><code>status</code></td><td><code>string</code></td><td>Deployment status of a resource. Status can be one of the following: PENDING, DEPLOYED, PENDING_DELETION.</td></tr>
<tr><td><code>cluster_endpoints</code></td><td><code>array</code></td><td>Endpoints for the cluster.</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>A collection of tags associated with a resource</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
name,
cluster_arn,
status,
cluster_endpoints,
tags
FROM awscc.route53recoverycontrol.cluster
WHERE data__Identifier = '<ClusterArn>';
```

## Permissions

To operate on the <code>cluster</code> resource, the following permissions are required:

### Read
```json
route53-recovery-control-config:DescribeCluster,
route53-recovery-control-config:ListTagsForResource
```

### Delete
```json
route53-recovery-control-config:DescribeCluster,
route53-recovery-control-config:DeleteCluster
```

