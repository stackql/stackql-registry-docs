---
title: vpc_peering_connection_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - vpc_peering_connection_tags
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

Expands all tag keys and values for <code>vpc_peering_connections</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>vpc_peering_connection_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::EC2::VPCPeeringConnection</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2.vpc_peering_connection_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="peer_owner_id" /></td><td><code>string</code></td><td>The AWS account ID of the owner of the accepter VPC.</td></tr>
<tr><td><CopyableCode code="peer_region" /></td><td><code>string</code></td><td>The Region code for the accepter VPC, if the accepter VPC is located in a Region other than the Region in which you make the request.</td></tr>
<tr><td><CopyableCode code="peer_role_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the VPC peer role for the peering connection in another AWS account.</td></tr>
<tr><td><CopyableCode code="peer_vpc_id" /></td><td><code>string</code></td><td>The ID of the VPC with which you are creating the VPC peering connection. You must specify this parameter in the request.</td></tr>
<tr><td><CopyableCode code="vpc_id" /></td><td><code>string</code></td><td>The ID of the VPC.</td></tr>
<tr><td><CopyableCode code="tag_key" /></td><td><code>string</code></td><td>Tag key.</td></tr>
<tr><td><CopyableCode code="tag_value" /></td><td><code>string</code></td><td>Tag value.</td></tr>
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
Expands tags for all <code>vpc_peering_connections</code> in a region.
```sql
SELECT
region,
id,
peer_owner_id,
peer_region,
peer_role_arn,
peer_vpc_id,
vpc_id,
tag_key,
tag_value
FROM aws.ec2.vpc_peering_connection_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>vpc_peering_connection_tags</code> resource, see <a href="/providers/aws/ec2/vpc_peering_connections/#permissions"><code>vpc_peering_connections</code></a>


