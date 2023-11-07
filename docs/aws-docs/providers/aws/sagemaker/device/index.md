---
title: device
hide_title: false
hide_table_of_contents: false
keywords:
  - device
  - sagemaker
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>device</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>device</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>device</td></tr>
<tr><td><b>Id</b></td><td><code>aws.sagemaker.device</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>DeviceFleetName</code></td><td><code>string</code></td><td>The name of the edge device fleet</td></tr>
<tr><td><code>Device</code></td><td><code>object</code></td><td>The Edge Device you want to register against a device fleet</td></tr>
<tr><td><code>Tags</code></td><td><code>array</code></td><td>Associate tags with the resource</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT *<br/>FROM aws.sagemaker.device<br/>WHERE region = 'us-east-1'<br/>AND data__Identifier = '&lt;Device/DeviceName&gt;'
</pre>
