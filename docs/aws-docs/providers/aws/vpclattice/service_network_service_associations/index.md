---
title: service_network_service_associations
hide_title: false
hide_table_of_contents: false
keywords:
  - service_network_service_associations
  - vpclattice
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>service_network_service_associations</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>service_network_service_associations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>service_network_service_associations</td></tr>
<tr><td><b>Id</b></td><td><code>aws.vpclattice.service_network_service_associations</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>Arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>CreatedAt</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>DnsEntry</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>Id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>ServiceNetworkArn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>ServiceNetworkId</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>ServiceNetworkIdentifier</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>ServiceNetworkName</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>ServiceArn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>ServiceId</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>ServiceIdentifier</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>ServiceName</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>Status</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>Tags</code></td><td><code>array</code></td><td></td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT *<br/>FROM aws.vpclattice.service_network_service_associations<br/>WHERE region = 'us-east-1'
</pre>
