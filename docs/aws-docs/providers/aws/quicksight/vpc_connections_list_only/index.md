---
title: vpc_connections_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - vpc_connections_list_only
  - quicksight
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

Lists <code>vpc_connections</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/vpc_connections/"><code>vpc_connections</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>vpc_connections_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of the AWS::QuickSight::VPCConnection Resource Type.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.quicksight.vpc_connections_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td><p>The Amazon Resource Name (ARN) of the VPC connection.</p></td></tr>
<tr><td><CopyableCode code="availability_status" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="aws_account_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="created_time" /></td><td><code>string</code></td><td><p>The time that the VPC connection was created.</p></td></tr>
<tr><td><CopyableCode code="dns_resolvers" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="last_updated_time" /></td><td><code>string</code></td><td><p>The time that the VPC connection was last updated.</p></td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="network_interfaces" /></td><td><code>array</code></td><td><p>A list of network interfaces.</p></td></tr>
<tr><td><CopyableCode code="role_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="security_group_ids" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="status" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="subnet_ids" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="vpc_connection_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="vpc_id" /></td><td><code>string</code></td><td><p>The Amazon EC2 VPC ID associated with the VPC connection.</p></td></tr>
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
Lists all <code>vpc_connections</code> in a region.
```sql
SELECT
region,
aws_account_id,
vpc_connection_id
FROM aws.quicksight.vpc_connections_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>vpc_connections_list_only</code> resource, see <a href="/providers/aws/quicksight/vpc_connections/#permissions"><code>vpc_connections</code></a>


