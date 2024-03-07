---
title: serverless_clusters
hide_title: false
hide_table_of_contents: false
keywords:
  - serverless_clusters
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
Retrieves a list of <code>serverless_clusters</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>serverless_clusters</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>serverless_clusters</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.msk.serverless_clusters</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>serverless_clusters</code> resource, the following permissions are required:

### Create
<pre>
kafka:CreateClusterV2,
kafka:TagResource,
kafka:DescribeClusterV2,
ec2:CreateVpcEndpoint,
ec2:CreateTags,
ec2:DescribeVpcAttribute,
ec2:DescribeSubnets,
ec2:DescribeVpcEndpoints,
ec2:DescribeVpcs,
ec2:DescribeSecurityGroups</pre>

### List
<pre>
kafka:ListClustersV2</pre>


## Example
```sql
SELECT
region,
arn
FROM awscc.msk.serverless_clusters
WHERE region = 'us-east-1'
```
