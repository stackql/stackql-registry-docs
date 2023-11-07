---
title: geofence_collections
hide_title: false
hide_table_of_contents: false
keywords:
  - geofence_collections
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
Retrieves a list of <code>geofence_collections</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>geofence_collections</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>geofence_collections</td></tr>
<tr><td><b>Id</b></td><td><code>aws.location.geofence_collections</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>CollectionArn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>Arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>CollectionName</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>CreateTime</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>Description</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>KmsKeyId</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>PricingPlan</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>PricingPlanDataSource</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>UpdateTime</code></td><td><code>undefined</code></td><td></td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT *<br/>FROM aws.location.geofence_collections<br/>WHERE region = 'us-east-1'
</pre>
