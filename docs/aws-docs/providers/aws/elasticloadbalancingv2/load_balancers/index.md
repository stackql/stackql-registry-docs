---
title: load_balancers
hide_title: false
hide_table_of_contents: false
keywords:
  - load_balancers
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
Retrieves a list of <code>load_balancers</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>load_balancers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
null
<tr><td><b>Id</b></td><td><code>aws.elasticloadbalancingv2.load_balancers</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>IpAddressType</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>SecurityGroups</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>LoadBalancerAttributes</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>Scheme</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>DNSName</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>Name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>LoadBalancerName</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>Subnets</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>Type</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>CanonicalHostedZoneID</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>Id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>Tags</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>LoadBalancerFullName</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>SubnetMappings</code></td><td><code>array</code></td><td></td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.elasticloadbalancingv2.load_balancers
WHERE region = 'us-east-1'
</pre>
