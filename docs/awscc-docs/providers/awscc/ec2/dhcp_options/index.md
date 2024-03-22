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
Gets an individual <code>dhcp_options</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>dhcp_options</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>dhcp_options</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.ec2.dhcp_options</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>netbios_name_servers</code></td><td><code>array</code></td><td>The IPv4 addresses of up to four NetBIOS name servers.</td></tr>
<tr><td><code>ntp_servers</code></td><td><code>array</code></td><td>The IPv4 addresses of up to four Network Time Protocol (NTP) servers.</td></tr>
<tr><td><code>dhcp_options_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>domain_name</code></td><td><code>string</code></td><td>This value is used to complete unqualified DNS hostnames.</td></tr>
<tr><td><code>netbios_node_type</code></td><td><code>integer</code></td><td>The NetBIOS node type (1, 2, 4, or 8).</td></tr>
<tr><td><code>domain_name_servers</code></td><td><code>array</code></td><td>The IPv4 addresses of up to four domain name servers, or AmazonProvidedDNS.</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>Any tags assigned to the DHCP options set.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
netbios_name_servers,
ntp_servers,
dhcp_options_id,
domain_name,
netbios_node_type,
domain_name_servers,
tags
FROM awscc.ec2.dhcp_options
WHERE data__Identifier = '<DhcpOptionsId>';
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

### Delete
```json
ec2:DeleteDhcpOptions,
ec2:DeleteTags,
ec2:DescribeDhcpOptions
```

