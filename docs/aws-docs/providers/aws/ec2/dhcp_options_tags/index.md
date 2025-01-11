---
title: dhcp_options_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - dhcp_options_tags
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

Expands all tag keys and values for <code>dhcp_options</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>dhcp_options_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::EC2::DHCPOptions</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2.dhcp_options_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="dhcp_options_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="domain_name" /></td><td><code>string</code></td><td>This value is used to complete unqualified DNS hostnames.</td></tr>
<tr><td><CopyableCode code="domain_name_servers" /></td><td><code>array</code></td><td>The IPv4 addresses of up to four domain name servers, or AmazonProvidedDNS.</td></tr>
<tr><td><CopyableCode code="netbios_name_servers" /></td><td><code>array</code></td><td>The IPv4 addresses of up to four NetBIOS name servers.</td></tr>
<tr><td><CopyableCode code="netbios_node_type" /></td><td><code>integer</code></td><td>The NetBIOS node type (1, 2, 4, or 8).</td></tr>
<tr><td><CopyableCode code="ntp_servers" /></td><td><code>array</code></td><td>The IPv4 addresses of up to four Network Time Protocol (NTP) servers.</td></tr>
<tr><td><CopyableCode code="ipv6_address_preferred_lease_time" /></td><td><code>integer</code></td><td>The preferred Lease Time for ipV6 address in seconds.</td></tr>
<tr><td><CopyableCode code="tag_key" /></td><td><code>string</code></td><td>Tag key.</td></tr>
<tr><td><CopyableCode code="tag_value" /></td><td><code>string</code></td><td>Tag value.</td></tr>
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
Expands tags for all <code>dhcp_options</code> in a region.
```sql
SELECT
region,
dhcp_options_id,
domain_name,
domain_name_servers,
netbios_name_servers,
netbios_node_type,
ntp_servers,
ipv6_address_preferred_lease_time,
tag_key,
tag_value
FROM aws.ec2.dhcp_options_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>dhcp_options_tags</code> resource, see <a href="/providers/aws/ec2/dhcp_options/#permissions"><code>dhcp_options</code></a>

