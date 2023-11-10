---
title: load_balancer_tls_certificates
hide_title: false
hide_table_of_contents: false
keywords:
  - load_balancer_tls_certificates
  - lightsail
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>load_balancer_tls_certificates</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>load_balancer_tls_certificates</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>load_balancer_tls_certificates</td></tr>
<tr><td><b>Id</b></td><td><code>aws.lightsail.load_balancer_tls_certificates</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>certificate_name</code></td><td><code>string</code></td><td>The SSL&#x2F;TLS certificate name.</td></tr>
<tr><td><code>load_balancer_name</code></td><td><code>string</code></td><td>The name of your load balancer.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
certificate_name,
load_balancer_name
FROM aws.lightsail.load_balancer_tls_certificates
WHERE region = 'us-east-1'
```
