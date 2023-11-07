---
title: geofence_collection
hide_title: false
hide_table_of_contents: false
keywords:
  - geofence_collection
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
Gets an individual <code>geofence_collection</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>geofence_collection</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>geofence_collection</td></tr>
<tr><td><b>Id</b></td><td><code>aws.location.geofence_collection</code></td></tr>
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
SELECT *<br/>FROM aws.location.geofence_collection<br/>WHERE region = 'us-east-1'<br/>AND data__Identifier = '&lt;CollectionName&gt;'
</pre>
