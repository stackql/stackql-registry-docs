---
title: vpn_gateways_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - vpn_gateways_list_only
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

Lists <code>vpn_gateways</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/vpn_gateways/"><code>vpn_gateways</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>vpn_gateways_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Specifies a virtual private gateway. A virtual private gateway is the endpoint on the VPC side of your VPN connection. You can create a virtual private gateway before creating the VPC itself.<br />For more information, see &#91;&#93;(https://docs.aws.amazon.com/vpn/latest/s2svpn/VPC_VPN.html) in the *User Guide*.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2.vpn_gateways_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="v_pn_gateway_id" /></td><td><code>string</code></td><td></td></tr>
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
Lists all <code>vpn_gateways</code> in a region.
```sql
SELECT
region,
v_pn_gateway_id
FROM aws.ec2.vpn_gateways_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>vpn_gateways_list_only</code> resource, see <a href="/providers/aws/ec2/vpn_gateways/#permissions"><code>vpn_gateways</code></a>

