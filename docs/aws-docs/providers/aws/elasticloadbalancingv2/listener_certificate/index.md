---
title: listener_certificate
hide_title: false
hide_table_of_contents: false
keywords:
  - listener_certificate
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
Gets an individual <code>listener_certificate</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>listener_certificate</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>listener_certificate</td></tr>
<tr><td><b>Id</b></td><td><code>aws.elasticloadbalancingv2.listener_certificate</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>listener_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>certificates</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
listener_arn,
certificates,
id
FROM aws.elasticloadbalancingv2.listener_certificate
WHERE region = 'us-east-1'
AND data__Identifier = '<Id>'
```
