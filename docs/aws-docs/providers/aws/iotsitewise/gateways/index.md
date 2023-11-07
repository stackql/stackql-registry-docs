---
title: gateways
hide_title: false
hide_table_of_contents: false
keywords:
  - gateways
  - iotsitewise
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>gateways</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>gateways</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
null
<tr><td><b>Id</b></td><td><code>aws.iotsitewise.gateways</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>GatewayName</code></td><td><code>string</code></td><td>A unique, friendly name for the gateway.</td></tr>
<tr><td><code>GatewayPlatform</code></td><td><code>undefined</code></td><td>The gateway's platform. You can only specify one platform in a gateway.</td></tr>
<tr><td><code>Tags</code></td><td><code>array</code></td><td>A list of key-value pairs that contain metadata for the gateway.</td></tr>
<tr><td><code>GatewayId</code></td><td><code>string</code></td><td>The ID of the gateway device.</td></tr>
<tr><td><code>GatewayCapabilitySummaries</code></td><td><code>array</code></td><td>A list of gateway capability summaries that each contain a namespace and status.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.iotsitewise.gateways
WHERE region = 'us-east-1'
</pre>
