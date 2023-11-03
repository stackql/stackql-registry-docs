---
title: elastic_load_balancer_attachment
hide_title: false
hide_table_of_contents: false
keywords:
  - elastic_load_balancer_attachment
  - opsworks
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>elastic_load_balancer_attachment</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>elastic_load_balancer_attachment</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
null
<tr><td><b>Id</b></td><td><code>aws.opsworks.elastic_load_balancer_attachment</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>Id</code></td><td><code>string</code></td><td></td></tr><tr><td><code>ElasticLoadBalancerName</code></td><td><code>string</code></td><td></td></tr><tr><td><code>LayerId</code></td><td><code>string</code></td><td></td></tr>
</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.opsworks.elastic_load_balancer_attachment
WHERE region = 'us-east-1' AND data__Identifier = '<Id>'
</pre>
