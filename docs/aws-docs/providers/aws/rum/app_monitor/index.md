---
title: app_monitor
hide_title: false
hide_table_of_contents: false
keywords:
  - app_monitor
  - rum
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>app_monitor</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>app_monitor</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>app_monitor</td></tr>
<tr><td><b>Id</b></td><td><code>aws.rum.app_monitor</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>Id</code></td><td><code>string</code></td><td>The unique ID of the new app monitor.</td></tr>
<tr><td><code>Name</code></td><td><code>string</code></td><td>A name for the app monitor</td></tr>
<tr><td><code>Domain</code></td><td><code>string</code></td><td>The top-level internet domain name for which your application has administrative authority.</td></tr>
<tr><td><code>CwLogEnabled</code></td><td><code>boolean</code></td><td>Data collected by RUM is kept by RUM for 30 days and then deleted. This parameter specifies whether RUM sends a copy of this telemetry data to CWLlong in your account. This enables you to keep the telemetry data for more than 30 days, but it does incur CWLlong charges. If you omit this parameter, the default is false</td></tr>
<tr><td><code>Tags</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>AppMonitorConfiguration</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>CustomEvents</code></td><td><code>undefined</code></td><td></td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.rum.app_monitor
WHERE region = 'us-east-1' AND data__Identifier = '&lt;Name&gt;'
</pre>
