---
title: listeners
hide_title: false
hide_table_of_contents: false
keywords:
  - listeners
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
Retrieves a list of <code>listeners</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>listeners</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.elasticloadbalancingv2.listeners</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>SslPolicy</code></td><td><code>string</code></td><td></td></tr><tr><td><code>LoadBalancerArn</code></td><td><code>string</code></td><td></td></tr><tr><td><code>DefaultActions</code></td><td><code>array</code></td><td></td></tr><tr><td><code>Port</code></td><td><code>integer</code></td><td></td></tr><tr><td><code>Certificates</code></td><td><code>array</code></td><td></td></tr><tr><td><code>Protocol</code></td><td><code>string</code></td><td></td></tr><tr><td><code>ListenerArn</code></td><td><code>string</code></td><td></td></tr><tr><td><code>AlpnPolicy</code></td><td><code>array</code></td><td></td></tr>
</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT * 
FROM aws.elasticloadbalancingv2.listeners
WHERE region = 'us-east-1'
```
