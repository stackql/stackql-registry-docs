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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';


Used to retrieve a list of <code>eips</code> in a region or to create or delete a <code>eips</code> resource, use <code>eip</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>eips</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Specifies an Elastic IP (EIP) address and can, optionally, associate it with an Amazon EC2 instance.&lt;br&#x2F;&gt; You can allocate an Elastic IP address from an address pool owned by AWS or from an address pool created from a public IPv4 address range that you have brought to AWS for use with your AWS resources using bring your own IP addresses (BYOIP). For more information, see &#91;Bring Your Own IP Addresses (BYOIP)&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;AWSEC2&#x2F;latest&#x2F;UserGuide&#x2F;ec2-byoip.html) in the *Amazon EC2 User Guide*.&lt;br&#x2F;&gt; For more information, see &#91;Elastic IP Addresses&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;AWSEC2&#x2F;latest&#x2F;UserGuide&#x2F;elastic-ip-addresses-eip.html) in the *Amazon EC2 User Guide*.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2.eips" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="public_ip" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="allocation_id" /></td><td><code>string</code></td><td></td></tr>
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
    <td><CopyableCode code="create_resource" /></td>
    <td><code>INSERT</code></td>
    <td><CopyableCode code="data__DesiredState, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="list_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
public_ip,
allocation_id
FROM aws.ec2.eips
WHERE region = 'us-east-1';
```

## `INSERT` Example

<Tabs
    defaultValue="required"
    values={[
      { label: 'Required Properties', value: 'required', },
      { label: 'All Properties', value: 'all', },

    ]
}>
<TabItem value="required">

```sql
<<<json
{
 "Domain": "{{ Domain }}",
 "NetworkBorderGroup": "{{ NetworkBorderGroup }}",
 "TransferAddress": "{{ TransferAddress }}",
 "InstanceId": "{{ InstanceId }}",
 "PublicIpv4Pool": "{{ PublicIpv4Pool }}",
 "Tags": [
  {
   "Key": "{{ Key }}",
   "Value": "{{ Value }}"
  }
 ]
}
>>>
--required properties only
INSERT INTO aws.ec2.eips (
 Domain,
 NetworkBorderGroup,
 TransferAddress,
 InstanceId,
 PublicIpv4Pool,
 Tags,
 region
)
SELECT 
{{ Domain }},
 {{ NetworkBorderGroup }},
 {{ TransferAddress }},
 {{ InstanceId }},
 {{ PublicIpv4Pool }},
 {{ Tags }},
'us-east-1';
```

</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "Domain": "{{ Domain }}",
 "NetworkBorderGroup": "{{ NetworkBorderGroup }}",
 "TransferAddress": "{{ TransferAddress }}",
 "InstanceId": "{{ InstanceId }}",
 "PublicIpv4Pool": "{{ PublicIpv4Pool }}",
 "Tags": [
  {
   "Key": "{{ Key }}",
   "Value": "{{ Value }}"
  }
 ]
}
>>>
--all properties
INSERT INTO aws.ec2.eips (
 Domain,
 NetworkBorderGroup,
 TransferAddress,
 InstanceId,
 PublicIpv4Pool,
 Tags,
 region
)
SELECT 
 {{ Domain }},
 {{ NetworkBorderGroup }},
 {{ TransferAddress }},
 {{ InstanceId }},
 {{ PublicIpv4Pool }},
 {{ Tags }},
 'us-east-1';
```

</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.ec2.eips
WHERE data__Identifier = '<PublicIp|AllocationId>'
AND region = 'us-east-1';
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

### Delete
```json
ec2:ReleaseAddress,
ec2:DescribeAddresses,
ec2:DisassociateAddress
```

### List
```json
ec2:DescribeAddresses
```

