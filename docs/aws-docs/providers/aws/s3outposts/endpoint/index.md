---
title: endpoint
hide_title: false
hide_table_of_contents: false
keywords:
  - endpoint
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


Gets or updates an individual <code>endpoint</code> resource, use <code>endpoints</code> to retrieve a list of resources or to create or delete a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>endpoint</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type Definition for AWS::S3Outposts::Endpoint</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.s3outposts.endpoint" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the endpoint.</td></tr>
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
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
arn,
cidr_block,
creation_time,
id,
network_interfaces,
outpost_id,
security_group_id,
status,
subnet_id,
access_type,
customer_owned_ipv4_pool,
failed_reason
FROM aws.s3outposts.endpoint
WHERE region = 'us-east-1' AND data__Identifier = '<Arn>';
```


## Permissions

To operate on the <code>endpoint</code> resource, the following permissions are required:

### Read
```json
s3-outposts:ListEndpoints
```

