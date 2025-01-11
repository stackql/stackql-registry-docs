---
title: eips_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - eips_list_only
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

Lists <code>eips</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/eips/"><code>eips</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>eips_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Specifies an Elastic IP (EIP) address and can, optionally, associate it with an Amazon EC2 instance.<br />You can allocate an Elastic IP address from an address pool owned by AWS or from an address pool created from a public IPv4 address range that you have brought to AWS for use with your AWS resources using bring your own IP addresses (BYOIP). For more information, see &#91;Bring Your Own IP Addresses (BYOIP)&#93;(https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-byoip.html) in the *Amazon EC2 User Guide*.<br />For more information, see &#91;Elastic IP Addresses&#93;(https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/elastic-ip-addresses-eip.html) in the *Amazon EC2 User Guide*.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2.eips_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="public_ip" /></td><td><code>string</code></td><td></td></tr>
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
    <td><CopyableCode code="list_resources" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples
Lists all <code>eips</code> in a region.
```sql
SELECT
region,
public_ip,
allocation_id
FROM aws.ec2.eips_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>eips_list_only</code> resource, see <a href="/providers/aws/ec2/eips/#permissions"><code>eips</code></a>

