---
title: health_check
hide_title: false
hide_table_of_contents: false
keywords:
  - health_check
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
Gets an individual <code>health_check</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>health_check</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>health_check</td></tr>
<tr><td><b>Id</b></td><td><code>aws.route53.health_check</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>HealthCheckId</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>HealthCheckConfig</code></td><td><code>object</code></td><td>A complex type that contains information about the health check.</td></tr>
<tr><td><code>HealthCheckTags</code></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT *<br/>FROM aws.route53.health_check<br/>WHERE region = 'us-east-1'<br/>AND data__Identifier = '&lt;HealthCheckId&gt;'
</pre>
