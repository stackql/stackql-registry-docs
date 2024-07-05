---
title: ipam_pool_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - ipam_pool_tags
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

Expands all tag keys and values for <code>ipam_pools</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>ipam_pool_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Schema of AWS::EC2::IPAMPool Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2.ipam_pool_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="ipam_pool_id" /></td><td><code>string</code></td><td>Id of the IPAM Pool.</td></tr>
<tr><td><CopyableCode code="address_family" /></td><td><code>string</code></td><td>The address family of the address space in this pool. Either IPv4 or IPv6.</td></tr>
<tr><td><CopyableCode code="allocation_min_netmask_length" /></td><td><code>integer</code></td><td>The minimum allowed netmask length for allocations made from this pool.</td></tr>
<tr><td><CopyableCode code="allocation_default_netmask_length" /></td><td><code>integer</code></td><td>The default netmask length for allocations made from this pool. This value is used when the netmask length of an allocation isn't specified.</td></tr>
<tr><td><CopyableCode code="allocation_max_netmask_length" /></td><td><code>integer</code></td><td>The maximum allowed netmask length for allocations made from this pool.</td></tr>
<tr><td><CopyableCode code="allocation_resource_tags" /></td><td><code>array</code></td><td>When specified, an allocation will not be allowed unless a resource has a matching set of tags.</td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the IPAM Pool.</td></tr>
<tr><td><CopyableCode code="auto_import" /></td><td><code>boolean</code></td><td>Determines what to do if IPAM discovers resources that haven't been assigned an allocation. If set to true, an allocation will be made automatically.</td></tr>
<tr><td><CopyableCode code="aws_service" /></td><td><code>string</code></td><td>Limits which service in Amazon Web Services that the pool can be used in.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="ipam_scope_id" /></td><td><code>string</code></td><td>The Id of the scope this pool is a part of.</td></tr>
<tr><td><CopyableCode code="ipam_scope_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the scope this pool is a part of.</td></tr>
<tr><td><CopyableCode code="ipam_scope_type" /></td><td><code>string</code></td><td>Determines whether this scope contains publicly routable space or space for a private network</td></tr>
<tr><td><CopyableCode code="ipam_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the IPAM this pool is a part of.</td></tr>
<tr><td><CopyableCode code="locale" /></td><td><code>string</code></td><td>The region of this pool. If not set, this will default to "None" which will disable non-custom allocations. If the locale has been specified for the source pool, this value must match.</td></tr>
<tr><td><CopyableCode code="pool_depth" /></td><td><code>integer</code></td><td>The depth of this pool in the source pool hierarchy.</td></tr>
<tr><td><CopyableCode code="provisioned_cidrs" /></td><td><code>array</code></td><td>A list of cidrs representing the address space available for allocation in this pool.</td></tr>
<tr><td><CopyableCode code="public_ip_source" /></td><td><code>string</code></td><td>The IP address source for pools in the public scope. Only used for provisioning IP address CIDRs to pools in the public scope. Default is `byoip`.</td></tr>
<tr><td><CopyableCode code="publicly_advertisable" /></td><td><code>boolean</code></td><td>Determines whether or not address space from this pool is publicly advertised. Must be set if and only if the pool is IPv6.</td></tr>
<tr><td><CopyableCode code="source_ipam_pool_id" /></td><td><code>string</code></td><td>The Id of this pool's source. If set, all space provisioned in this pool must be free space provisioned in the parent pool.</td></tr>
<tr><td><CopyableCode code="source_resource" /></td><td><code>object</code></td><td>The resource associated with this pool's space. Depending on the ResourceType, setting a SourceResource changes which space can be provisioned in this pool and which types of resources can receive allocations</td></tr>
<tr><td><CopyableCode code="state" /></td><td><code>string</code></td><td>The state of this pool. This can be one of the following values: "create-in-progress", "create-complete", "modify-in-progress", "modify-complete", "delete-in-progress", or "delete-complete"</td></tr>
<tr><td><CopyableCode code="state_message" /></td><td><code>string</code></td><td>An explanation of how the pool arrived at it current state.</td></tr>
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
Expands tags for all <code>ipam_pools</code> in a region.
```sql
SELECT
region,
ipam_pool_id,
address_family,
allocation_min_netmask_length,
allocation_default_netmask_length,
allocation_max_netmask_length,
allocation_resource_tags,
arn,
auto_import,
aws_service,
description,
ipam_scope_id,
ipam_scope_arn,
ipam_scope_type,
ipam_arn,
locale,
pool_depth,
provisioned_cidrs,
public_ip_source,
publicly_advertisable,
source_ipam_pool_id,
source_resource,
state,
state_message,
tag_key,
tag_value
FROM aws.ec2.ipam_pool_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>ipam_pool_tags</code> resource, see <a href="/providers/aws/ec2/ipam_pools/#permissions"><code>ipam_pools</code></a>


