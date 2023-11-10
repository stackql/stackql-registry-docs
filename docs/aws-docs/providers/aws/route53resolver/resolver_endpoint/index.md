---
title: resolver_endpoint
hide_title: false
hide_table_of_contents: false
keywords:
  - resolver_endpoint
  - route53resolver
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>resolver_endpoint</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>resolver_endpoint</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>resolver_endpoint</td></tr>
<tr><td><b>Id</b></td><td><code>aws.route53resolver.resolver_endpoint</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>ip_addresses</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>resolver_endpoint_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>ip_address_count</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>outpost_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>preferred_instance_type</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>resolver_endpoint_type</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>direction</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>host_vp_cid</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>security_group_ids</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
ip_addresses,
resolver_endpoint_id,
ip_address_count,
outpost_arn,
preferred_instance_type,
resolver_endpoint_type,
arn,
direction,
host_vp_cid,
security_group_ids,
tags,
name
FROM aws.route53resolver.resolver_endpoint
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;ResolverEndpointId&gt;'
```
