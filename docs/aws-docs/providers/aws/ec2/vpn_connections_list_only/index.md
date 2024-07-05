---
title: vpn_connections_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - vpn_connections_list_only
  - ec2
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Lists <code>vpn_connections</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/vpn_connections/"><code>vpn_connections</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>vpn_connections_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::EC2::VPNConnection</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2.vpn_connections_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="vpn_connection_id" /></td><td><code>string</code></td><td>The provider-assigned unique ID for this managed resource</td></tr>
<tr><td><CopyableCode code="customer_gateway_id" /></td><td><code>string</code></td><td>The ID of the customer gateway at your end of the VPN connection.</td></tr>
<tr><td><CopyableCode code="static_routes_only" /></td><td><code>boolean</code></td><td>Indicates whether the VPN connection uses static routes only.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>Any tags assigned to the VPN connection.</td></tr>
<tr><td><CopyableCode code="transit_gateway_id" /></td><td><code>string</code></td><td>The ID of the transit gateway associated with the VPN connection.</td></tr>
<tr><td><CopyableCode code="type" /></td><td><code>string</code></td><td>The type of VPN connection.</td></tr>
<tr><td><CopyableCode code="vpn_gateway_id" /></td><td><code>string</code></td><td>The ID of the virtual private gateway at the AWS side of the VPN connection.</td></tr>
<tr><td><CopyableCode code="vpn_tunnel_options_specifications" /></td><td><code>array</code></td><td>The tunnel options for the VPN connection.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

## Methods

<table><tbody>
  <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
  </tr>
  <tr>
    <td><CopyableCode code="list_resources" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples
Lists all <code>vpn_connections</code> in a region.
```sql
SELECT
region,
vpn_connection_id
FROM aws.ec2.vpn_connections_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>vpn_connections_list_only</code> resource, see <a href="/providers/aws/ec2/vpn_connections/#permissions"><code>vpn_connections</code></a>


