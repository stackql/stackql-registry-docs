---
title: dhcp_options
hide_title: false
hide_table_of_contents: false
keywords:
  - dhcp_options
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


Gets or updates an individual <code>dhcp_options</code> resource, use <code>dhcp_options</code> to retrieve a list of resources or to create or delete a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>dhcp_options</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::EC2::DHCPOptions</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2.dhcp_options" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="dhcp_options_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="domain_name" /></td><td><code>string</code></td><td>This value is used to complete unqualified DNS hostnames.</td></tr>
<tr><td><CopyableCode code="domain_name_servers" /></td><td><code>array</code></td><td>The IPv4 addresses of up to four domain name servers, or AmazonProvidedDNS.</td></tr>
<tr><td><CopyableCode code="netbios_name_servers" /></td><td><code>array</code></td><td>The IPv4 addresses of up to four NetBIOS name servers.</td></tr>
<tr><td><CopyableCode code="netbios_node_type" /></td><td><code>integer</code></td><td>The NetBIOS node type (1, 2, 4, or 8).</td></tr>
<tr><td><CopyableCode code="ntp_servers" /></td><td><code>array</code></td><td>The IPv4 addresses of up to four Network Time Protocol (NTP) servers.</td></tr>
<tr><td><CopyableCode code="ipv6_address_preferred_lease_time" /></td><td><code>integer</code></td><td>The preferred Lease Time for ipV6 address in seconds.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>Any tags assigned to the DHCP options set.</td></tr>
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
    <td><CopyableCode code="update_resource" /></td>
    <td><code>UPDATE</code></td>
    <td><CopyableCode code="data__Identifier, data__PatchDocument, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
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
tags
FROM aws.ec2.dhcp_options
WHERE region = 'us-east-1' AND data__Identifier = '<DhcpOptionsId>';
```


## Permissions

To operate on the <code>dhcp_options</code> resource, the following permissions are required:

### Read
```json
ec2:DescribeDhcpOptions,
ec2:DescribeTags
```

### Update
```json
ec2:CreateTags,
ec2:DescribeDhcpOptions,
ec2:DeleteTags
```

