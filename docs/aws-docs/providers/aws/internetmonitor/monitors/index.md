---
title: monitors
hide_title: false
hide_table_of_contents: false
keywords:
  - monitors
  - internetmonitor
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>monitors</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>monitors</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>monitors</td></tr>
<tr><td><b>Id</b></td><td><code>aws.internetmonitor.monitors</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>CreatedAt</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>ModifiedAt</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>MonitorArn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>MonitorName</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>ProcessingStatus</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>ProcessingStatusInfo</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>Resources</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>ResourcesToAdd</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>ResourcesToRemove</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>Status</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>Tags</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>MaxCityNetworksToMonitor</code></td><td><code>integer</code></td><td></td></tr>
<tr><td><code>InternetMeasurementsLogDelivery</code></td><td><code>undefined</code></td><td></td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.internetmonitor.monitors
WHERE region = 'us-east-1'
</pre>
