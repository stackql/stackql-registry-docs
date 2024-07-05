---
title: eip_associations_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - eip_associations_list_only
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

Lists <code>eip_associations</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/eip_associations/"><code>eip_associations</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>eip_associations_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for EC2 EIP association.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2.eip_associations_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td>Composite ID of non-empty properties, to determine the identification.</td></tr>
<tr><td><CopyableCode code="allocation_id" /></td><td><code>string</code></td><td>The allocation ID. This is required for EC2-VPC.</td></tr>
<tr><td><CopyableCode code="network_interface_id" /></td><td><code>string</code></td><td>The ID of the network interface.</td></tr>
<tr><td><CopyableCode code="instance_id" /></td><td><code>string</code></td><td>The ID of the instance.</td></tr>
<tr><td><CopyableCode code="private_ip_address" /></td><td><code>string</code></td><td>The primary or secondary private IP address to associate with the Elastic IP address.</td></tr>
<tr><td><CopyableCode code="e_ip" /></td><td><code>string</code></td><td>The Elastic IP address to associate with the instance.</td></tr>
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
Lists all <code>eip_associations</code> in a region.
```sql
SELECT
region,
id
FROM aws.ec2.eip_associations_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>eip_associations_list_only</code> resource, see <a href="/providers/aws/ec2/eip_associations/#permissions"><code>eip_associations</code></a>


