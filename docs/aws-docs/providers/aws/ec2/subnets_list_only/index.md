---
title: subnets_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - subnets_list_only
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

Lists <code>subnets</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/subnets/"><code>subnets</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>subnets_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Specifies a subnet for the specified VPC.<br />For an IPv4 only subnet, specify an IPv4 CIDR block. If the VPC has an IPv6 CIDR block, you can create an IPv6 only subnet or a dual stack subnet instead. For an IPv6 only subnet, specify an IPv6 CIDR block. For a dual stack subnet, specify both an IPv4 CIDR block and an IPv6 CIDR block.<br />For more information, see &#91;Subnets for your VPC&#93;(https://docs.aws.amazon.com/vpc/latest/userguide/configure-subnets.html) in the *Amazon VPC User Guide*.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2.subnets_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="subnet_id" /></td><td><code>string</code></td><td></td></tr>
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
Lists all <code>subnets</code> in a region.
```sql
SELECT
region,
subnet_id
FROM aws.ec2.subnets_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>subnets_list_only</code> resource, see <a href="/providers/aws/ec2/subnets/#permissions"><code>subnets</code></a>

