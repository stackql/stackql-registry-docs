---
title: service_network_vpc_association
hide_title: false
hide_table_of_contents: false
keywords:
  - service_network_vpc_association
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
Gets an individual <code>service_network_vpc_association</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>service_network_vpc_association</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
null
<tr><td><b>Id</b></td><td><code>aws.vpclattice.service_network_vpc_association</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>Arn</code></td><td><code>string</code></td><td></td></tr><tr><td><code>CreatedAt</code></td><td><code>string</code></td><td></td></tr><tr><td><code>SecurityGroupIds</code></td><td><code>array</code></td><td></td></tr><tr><td><code>Id</code></td><td><code>string</code></td><td></td></tr><tr><td><code>ServiceNetworkArn</code></td><td><code>string</code></td><td></td></tr><tr><td><code>ServiceNetworkId</code></td><td><code>string</code></td><td></td></tr><tr><td><code>ServiceNetworkIdentifier</code></td><td><code>string</code></td><td></td></tr><tr><td><code>ServiceNetworkName</code></td><td><code>string</code></td><td></td></tr><tr><td><code>Status</code></td><td><code>string</code></td><td></td></tr><tr><td><code>VpcId</code></td><td><code>string</code></td><td></td></tr><tr><td><code>VpcIdentifier</code></td><td><code>string</code></td><td></td></tr><tr><td><code>Tags</code></td><td><code>array</code></td><td></td></tr>
</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.vpclattice.service_network_vpc_association
WHERE region = 'us-east-1' AND data__Identifier = '<Arn>'
</pre>
