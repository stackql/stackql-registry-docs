---
title: place_index
hide_title: false
hide_table_of_contents: false
keywords:
  - place_index
  - location
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>place_index</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>place_index</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>place_index</td></tr>
<tr><td><b>Id</b></td><td><code>aws.location.place_index</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>CreateTime</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>DataSource</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>DataSourceConfiguration</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>Description</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>IndexArn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>Arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>IndexName</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>PricingPlan</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>UpdateTime</code></td><td><code>undefined</code></td><td></td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT *<br/>FROM aws.location.place_index<br/>WHERE region = 'us-east-1'<br/>AND data__Identifier = '&lt;IndexName&gt;'
</pre>
