---
title: eips
hide_title: false
hide_table_of_contents: false
keywords:
  - eips
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
Used to retrieve a list of <code>eips</code> in a region or create a <code>eips</code> resource, use <code>eip</code> to operate on an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>eips</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Specifies an Elastic IP (EIP) address and can, optionally, associate it with an Amazon EC2 instance.&lt;br&#x2F;&gt; You can allocate an Elastic IP address from an address pool owned by AWS or from an address pool created from a public IPv4 address range that you have brought to AWS for use with your AWS resources using bring your own IP addresses (BYOIP). For more information, see &#91;Bring Your Own IP Addresses (BYOIP)&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;AWSEC2&#x2F;latest&#x2F;UserGuide&#x2F;ec2-byoip.html) in the *Amazon EC2 User Guide*.&lt;br&#x2F;&gt; For more information, see &#91;Elastic IP Addresses&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;AWSEC2&#x2F;latest&#x2F;UserGuide&#x2F;elastic-ip-addresses-eip.html) in the *Amazon EC2 User Guide*.</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ec2.eips</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>public_ip</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>allocation_id</code></td><td><code>string</code></td><td></td></tr>
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
    <td><code>create_resource</code></td>
    <td><code>INSERT</code></td>
    <td><code>data__DesiredState, region</code></td>
  </tr>
  <tr>
    <td><code>list_resource</code></td>
    <td><code>SELECT</code></td>
    <td><code>region</code></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
public_ip,
allocation_id
FROM aws.ec2.eips
WHERE region = 'us-east-1'
```

## Permissions

To operate on the <code>eips</code> resource, the following permissions are required:

### Create
```json
ec2:AllocateAddress,
ec2:AcceptAddressTransfer,
ec2:DescribeAddresses,
ec2:AssociateAddress,
ec2:CreateTags
```

### List
```json
ec2:DescribeAddresses
```

