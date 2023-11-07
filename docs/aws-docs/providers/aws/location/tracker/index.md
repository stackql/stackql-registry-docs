---
title: tracker
hide_title: false
hide_table_of_contents: false
keywords:
  - tracker
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
Gets an individual <code>tracker</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>tracker</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>tracker</td></tr>
<tr><td><b>Id</b></td><td><code>aws.location.tracker</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>CreateTime</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>Description</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>KmsKeyId</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>PricingPlan</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>PricingPlanDataSource</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>PositionFiltering</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>TrackerArn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>Arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>TrackerName</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>UpdateTime</code></td><td><code>string</code></td><td></td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT *<br/>FROM aws.location.tracker<br/>WHERE region = 'us-east-1'<br/>AND data__Identifier = '&lt;TrackerName&gt;'
</pre>
