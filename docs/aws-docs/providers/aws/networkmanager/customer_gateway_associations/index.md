---
title: customer_gateway_associations
hide_title: false
hide_table_of_contents: false
keywords:
  - customer_gateway_associations
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
Retrieves a list of <code>customer_gateway_associations</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>customer_gateway_associations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>customer_gateway_associations</td></tr>
<tr><td><b>Id</b></td><td><code>aws.networkmanager.customer_gateway_associations</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>GlobalNetworkId</code></td><td><code>string</code></td><td>The ID of the global network.</td></tr>
<tr><td><code>CustomerGatewayArn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the customer gateway.</td></tr>
<tr><td><code>DeviceId</code></td><td><code>string</code></td><td>The ID of the device</td></tr>
<tr><td><code>LinkId</code></td><td><code>string</code></td><td>The ID of the link</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT *<br/>FROM aws.networkmanager.customer_gateway_associations<br/>WHERE region = 'us-east-1'
</pre>
