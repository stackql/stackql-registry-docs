---
title: health_checks
hide_title: false
hide_table_of_contents: false
keywords:
  - health_checks
  - route53
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>health_checks</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>health_checks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.route53.health_checks</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>HealthCheckId</code></td><td><code>string</code></td><td></td></tr><tr><td><code>HealthCheckConfig</code></td><td><code>object</code></td><td>A complex type that contains information about the health check.</td></tr><tr><td><code>HealthCheckTags</code></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT * 
FROM aws.route53.health_checks
WHERE region = 'us-east-1'
```
