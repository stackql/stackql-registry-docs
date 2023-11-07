---
title: dataset
hide_title: false
hide_table_of_contents: false
keywords:
  - dataset
  - iotanalytics
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>dataset</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>dataset</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>dataset</td></tr>
<tr><td><b>Id</b></td><td><code>aws.iotanalytics.dataset</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>Actions</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>LateDataRules</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>DatasetName</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>ContentDeliveryRules</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>Triggers</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>VersioningConfiguration</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>Id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>RetentionPeriod</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>Tags</code></td><td><code>array</code></td><td></td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT *<br/>FROM aws.iotanalytics.dataset<br/>WHERE region = 'us-east-1'<br/>AND data__Identifier = '&lt;DatasetName&gt;'
</pre>
