---
title: load_balancer
hide_title: false
hide_table_of_contents: false
keywords:
  - load_balancer
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
Gets an individual <code>load_balancer</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>load_balancer</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>load_balancer</td></tr>
<tr><td><b>Id</b></td><td><code>aws.elasticloadbalancingv2.load_balancer</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>ip_address_type</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>security_groups</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>load_balancer_attributes</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>scheme</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>d_ns_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>load_balancer_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>subnets</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>type</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>canonical_hosted_zone_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>load_balancer_full_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>subnet_mappings</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
ip_address_type,
security_groups,
load_balancer_attributes,
scheme,
d_ns_name,
name,
load_balancer_name,
subnets,
type,
canonical_hosted_zone_id,
id,
tags,
load_balancer_full_name,
subnet_mappings
FROM aws.elasticloadbalancingv2.load_balancer
WHERE region = 'us-east-1'
AND data__Identifier = '<Id>'
```
