---
title: devices
hide_title: false
hide_table_of_contents: false
keywords:
  - devices
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
Retrieves a list of <code>devices</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>devices</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>devices</td></tr>
<tr><td><b>Id</b></td><td><code>aws.sagemaker.devices</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>DeviceFleetName</code></td><td><code>string</code></td><td>The name of the edge device fleet</td></tr>
<tr><td><code>Device</code></td><td><code>undefined</code></td><td>The Edge Device you want to register against a device fleet</td></tr>
<tr><td><code>Tags</code></td><td><code>array</code></td><td>Associate tags with the resource</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT *<br/>FROM aws.sagemaker.devices<br/>WHERE region = 'us-east-1'
</pre>
