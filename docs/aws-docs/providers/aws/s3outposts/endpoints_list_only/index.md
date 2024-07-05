---
title: endpoints_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - endpoints_list_only
  - s3outposts
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

Lists <code>endpoints</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/endpoints/"><code>endpoints</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>endpoints_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type Definition for AWS::S3Outposts::Endpoint</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.s3outposts.endpoints_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the endpoint.</td></tr>
<tr><td><CopyableCode code="cidr_block" /></td><td><code>string</code></td><td>The VPC CIDR committed by this endpoint.</td></tr>
<tr><td><CopyableCode code="creation_time" /></td><td><code>string</code></td><td>The time the endpoint was created.</td></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td>The ID of the endpoint.</td></tr>
<tr><td><CopyableCode code="network_interfaces" /></td><td><code>array</code></td><td>The network interfaces of the endpoint.</td></tr>
<tr><td><CopyableCode code="outpost_id" /></td><td><code>string</code></td><td>The id of the customer outpost on which the bucket resides.</td></tr>
<tr><td><CopyableCode code="security_group_id" /></td><td><code>string</code></td><td>The ID of the security group to use with the endpoint.</td></tr>
<tr><td><CopyableCode code="status" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="subnet_id" /></td><td><code>string</code></td><td>The ID of the subnet in the selected VPC. The subnet must belong to the Outpost.</td></tr>
<tr><td><CopyableCode code="access_type" /></td><td><code>string</code></td><td>The type of access for the on-premise network connectivity for the Outpost endpoint. To access endpoint from an on-premises network, you must specify the access type and provide the customer owned Ipv4 pool.</td></tr>
<tr><td><CopyableCode code="customer_owned_ipv4_pool" /></td><td><code>string</code></td><td>The ID of the customer-owned IPv4 pool for the Endpoint. IP addresses will be allocated from this pool for the endpoint.</td></tr>
<tr><td><CopyableCode code="failed_reason" /></td><td><code>object</code></td><td>The failure reason, if any, for a create or delete endpoint operation.</td></tr>
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
Lists all <code>endpoints</code> in a region.
```sql
SELECT
region,
arn
FROM aws.s3outposts.endpoints_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>endpoints_list_only</code> resource, see <a href="/providers/aws/s3outposts/endpoints/#permissions"><code>endpoints</code></a>


