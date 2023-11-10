---
title: domain_name
hide_title: false
hide_table_of_contents: false
keywords:
  - domain_name
  - apigatewayv2
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>domain_name</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>domain_name</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>domain_name</td></tr>
<tr><td><b>Id</b></td><td><code>aws.apigatewayv2.domain_name</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>mutual_tls_authentication</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>regional_hosted_zone_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>regional_domain_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>domain_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>domain_name_configurations</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
mutual_tls_authentication,
regional_hosted_zone_id,
regional_domain_name,
domain_name,
domain_name_configurations,
id,
tags
FROM aws.apigatewayv2.domain_name
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;Id&gt;'
```
