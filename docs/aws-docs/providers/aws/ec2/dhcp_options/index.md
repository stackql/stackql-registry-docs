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

Creates, updates, deletes or gets a <code>dhcp_option</code> resource or lists <code>dhcp_options</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>dhcp_options</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::EC2::DHCPOptions</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2.dhcp_options" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="dhcp_options_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="domain_name" /></td><td><code>string</code></td><td>This value is used to complete unqualified DNS hostnames.</td></tr>
<tr><td><CopyableCode code="domain_name_servers" /></td><td><code>array</code></td><td>The IPv4 addresses of up to four domain name servers, or AmazonProvidedDNS.</td></tr>
<tr><td><CopyableCode code="netbios_name_servers" /></td><td><code>array</code></td><td>The IPv4 addresses of up to four NetBIOS name servers.</td></tr>
<tr><td><CopyableCode code="netbios_node_type" /></td><td><code>integer</code></td><td>The NetBIOS node type (1, 2, 4, or 8).</td></tr>
<tr><td><CopyableCode code="ntp_servers" /></td><td><code>array</code></td><td>The IPv4 addresses of up to four Network Time Protocol (NTP) servers.</td></tr>
<tr><td><CopyableCode code="ipv6_address_preferred_lease_time" /></td><td><code>integer</code></td><td>The preferred Lease Time for ipV6 address in seconds.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>Any tags assigned to the DHCP options set.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-dhcpoption.html"><code>AWS::EC2::DHCPOptions</code></a>.

## Methods

<table><tbody>
  <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
  </tr>
  <tr>
    <td><CopyableCode code="create_resource" /></td>
    <td><code>INSERT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="update_resource" /></td>
    <td><code>UPDATE</code></td>
    <td><CopyableCode code="data__Identifier, data__PatchDocument, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="list_resources" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples
Gets all <code>dhcp_options</code> in a region.
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
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>dhcp_option</code>.
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

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>dhcp_option</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

<Tabs
    defaultValue="required"
    values={[
      { label: 'Required Properties', value: 'required', },
      { label: 'All Properties', value: 'all', },
      { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="required">

```sql
/*+ create */
INSERT INTO aws.ec2.dhcp_options (
 DomainName,
 DomainNameServers,
 NetbiosNameServers,
 NetbiosNodeType,
 NtpServers,
 Ipv6AddressPreferredLeaseTime,
 Tags,
 region
)
SELECT 
'{{ DomainName }}',
 '{{ DomainNameServers }}',
 '{{ NetbiosNameServers }}',
 '{{ NetbiosNodeType }}',
 '{{ NtpServers }}',
 '{{ Ipv6AddressPreferredLeaseTime }}',
 '{{ Tags }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.ec2.dhcp_options (
 DomainName,
 DomainNameServers,
 NetbiosNameServers,
 NetbiosNodeType,
 NtpServers,
 Ipv6AddressPreferredLeaseTime,
 Tags,
 region
)
SELECT 
 '{{ DomainName }}',
 '{{ DomainNameServers }}',
 '{{ NetbiosNameServers }}',
 '{{ NetbiosNodeType }}',
 '{{ NtpServers }}',
 '{{ Ipv6AddressPreferredLeaseTime }}',
 '{{ Tags }}',
 '{{ region }}';
```
</TabItem>
<TabItem value="manifest">

```yaml
version: 1
name: stack name
description: stack description
providers:
  - aws
globals:
  - name: region
    value: '{{ vars.AWS_REGION }}'
resources:
  - name: dhcp_option
    props:
      - name: DomainName
        value: '{{ DomainName }}'
      - name: DomainNameServers
        value:
          - '{{ DomainNameServers[0] }}'
      - name: NetbiosNameServers
        value:
          - '{{ NetbiosNameServers[0] }}'
      - name: NetbiosNodeType
        value: '{{ NetbiosNodeType }}'
      - name: NtpServers
        value:
          - '{{ NtpServers[0] }}'
      - name: Ipv6AddressPreferredLeaseTime
        value: '{{ Ipv6AddressPreferredLeaseTime }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.ec2.dhcp_options
WHERE data__Identifier = '<DhcpOptionsId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>dhcp_options</code> resource, the following permissions are required:

### Create
```json
ec2:CreateDhcpOptions,
ec2:DescribeDhcpOptions,
ec2:CreateTags
```

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

### List
```json
ec2:DescribeDhcpOptions
```
