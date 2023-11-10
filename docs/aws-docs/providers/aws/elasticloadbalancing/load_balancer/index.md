---
title: load_balancer
hide_title: false
hide_table_of_contents: false
keywords:
  - load_balancer
  - elasticloadbalancing
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
<tr><td><b>Id</b></td><td><code>aws.elasticloadbalancing.load_balancer</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>security_groups</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>connection_draining_policy</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>policies</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>scheme</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>availability_zones</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>source_security_group_owner_alias</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>health_check</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>canonical_hosted_zone_name_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>canonical_hosted_zone_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>d_ns_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>access_logging_policy</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>instances</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>load_balancer_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>listeners</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>subnets</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>cross_zone</code></td><td><code>boolean</code></td><td></td></tr>
<tr><td><code>app_cookie_stickiness_policy</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>l_bcookie_stickiness_policy</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>source_security_group_group_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>connection_settings</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
security_groups,
connection_draining_policy,
policies,
scheme,
availability_zones,
source_security_group_owner_alias,
health_check,
canonical_hosted_zone_name_id,
canonical_hosted_zone_name,
d_ns_name,
access_logging_policy,
instances,
load_balancer_name,
listeners,
subnets,
cross_zone,
app_cookie_stickiness_policy,
l_bcookie_stickiness_policy,
id,
source_security_group_group_name,
connection_settings,
tags
FROM aws.elasticloadbalancing.load_balancer
WHERE region = 'us-east-1'
AND data__Identifier = '<Id>'
```
