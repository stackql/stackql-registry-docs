---
title: trust_stores
hide_title: false
hide_table_of_contents: false
keywords:
  - trust_stores
  - elasticloadbalancingv2
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>trust_stores</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>trust_stores</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::ElasticLoadBalancingV2::TrustStore</td></tr>
<tr><td><b>Id</b></td><td><code>aws.elasticloadbalancingv2.trust_stores</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>trust_store_arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the trust store.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods

<table><tbody>
  <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
  </tr>
  <tr>
    <td><code>create_resource</code></td>
    <td><code>INSERT</code></td>
    <td><code>data__DesiredState, region</code></td>
  </tr>
  <tr>
    <td><code>list_resource</code></td>
    <td><code>SELECT</code></td>
    <td><code>region</code></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
trust_store_arn
FROM aws.elasticloadbalancingv2.trust_stores
WHERE region = 'us-east-1'
```

## Permissions

To operate on the <code>trust_stores</code> resource, the following permissions are required:

### Create
```json
elasticloadbalancing:CreateTrustStore,
elasticloadbalancing:DescribeTrustStores,
elasticloadbalancing:AddTags,
s3:GetObject,
s3:GetObjectVersion
```

### List
```json
elasticloadbalancing:DescribeTrustStores,
s3:GetObject,
s3:GetObjectVersion
```

