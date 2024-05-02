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
Gets or operates on an individual <code>dhcp_options</code> resource, use <code>dhcp_options</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>dhcp_options</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::EC2::DHCPOptions</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ec2.dhcp_options</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>dhcp_options_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>domain_name</code></td><td><code>string</code></td><td>This value is used to complete unqualified DNS hostnames.</td></tr>
<tr><td><code>domain_name_servers</code></td><td><code>array</code></td><td>The IPv4 addresses of up to four domain name servers, or AmazonProvidedDNS.</td></tr>
<tr><td><code>netbios_name_servers</code></td><td><code>array</code></td><td>The IPv4 addresses of up to four NetBIOS name servers.</td></tr>
<tr><td><code>netbios_node_type</code></td><td><code>integer</code></td><td>The NetBIOS node type (1, 2, 4, or 8).</td></tr>
<tr><td><code>ntp_servers</code></td><td><code>array</code></td><td>The IPv4 addresses of up to four Network Time Protocol (NTP) servers.</td></tr>
<tr><td><code>ipv6_address_preferred_lease_time</code></td><td><code>integer</code></td><td>The preferred Lease Time for ipV6 address in seconds.</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>Any tags assigned to the DHCP options set.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods

<table><tbody>
  <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
  </tr>
  <tr>
    <td><code>update_resource</code></td>
    <td><code>UPDATE</code></td>
    <td><code>data__Identifier, data__PatchDocument, region</code></td>
  </tr>
  <tr>
    <td><code>delete_resource</code></td>
    <td><code>DELETE</code></td>
    <td><code>data__Identifier, region</code></td>
  </tr>
  <tr>
    <td><code>get_resource</code></td>
    <td><code>SELECT</code></td>
    <td><code>data__Identifier, region</code></td>
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

