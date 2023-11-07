---
title: transit_gateway_registration
hide_title: false
hide_table_of_contents: false
keywords:
  - transit_gateway_registration
  - networkmanager
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>transit_gateway_registration</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>transit_gateway_registration</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>transit_gateway_registration</td></tr>
<tr><td><b>Id</b></td><td><code>aws.networkmanager.transit_gateway_registration</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>GlobalNetworkId</code></td><td><code>string</code></td><td>The ID of the global network.</td></tr>
<tr><td><code>TransitGatewayArn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the transit gateway.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.networkmanager.transit_gateway_registration
WHERE region = 'us-east-1' AND data__Identifier = '&lt;GlobalNetworkId&gt;' AND data__Identifier = '&lt;TransitGatewayArn&gt;'
</pre>
