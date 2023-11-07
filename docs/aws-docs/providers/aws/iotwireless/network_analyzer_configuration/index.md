---
title: network_analyzer_configuration
hide_title: false
hide_table_of_contents: false
keywords:
  - network_analyzer_configuration
  - iotwireless
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>network_analyzer_configuration</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>network_analyzer_configuration</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
null
<tr><td><b>Id</b></td><td><code>aws.iotwireless.network_analyzer_configuration</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>Name</code></td><td><code>string</code></td><td>Name of the network analyzer configuration</td></tr>
<tr><td><code>Description</code></td><td><code>string</code></td><td>The description of the new resource</td></tr>
<tr><td><code>TraceContent</code></td><td><code>object</code></td><td>Trace content for your wireless gateway and wireless device resources</td></tr>
<tr><td><code>WirelessDevices</code></td><td><code>array</code></td><td>List of wireless gateway resources that have been added to the network analyzer configuration</td></tr>
<tr><td><code>WirelessGateways</code></td><td><code>array</code></td><td>List of wireless gateway resources that have been added to the network analyzer configuration</td></tr>
<tr><td><code>Arn</code></td><td><code>string</code></td><td>Arn for network analyzer configuration, Returned upon successful create.</td></tr>
<tr><td><code>Tags</code></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.iotwireless.network_analyzer_configuration
WHERE region = 'us-east-1' AND data__Identifier = '&lt;Name&gt;'
</pre>
