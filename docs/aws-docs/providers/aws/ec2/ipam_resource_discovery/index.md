---
title: ipam_resource_discovery
hide_title: false
hide_table_of_contents: false
keywords:
  - ipam_resource_discovery
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


Gets or updates an individual <code>ipam_resource_discovery</code> resource, use <code>ipam_resource_discoveries</code> to retrieve a list of resources or to create or delete a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>ipam_resource_discovery</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Schema of AWS::EC2::IPAMResourceDiscovery Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2.ipam_resource_discovery" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="ipam_resource_discovery_id" /></td><td><code>string</code></td><td>Id of the IPAM Pool.</td></tr>
<tr><td><CopyableCode code="owner_id" /></td><td><code>string</code></td><td>Owner Account ID of the Resource Discovery</td></tr>
<tr><td><CopyableCode code="operating_regions" /></td><td><code>array</code></td><td>The regions Resource Discovery is enabled for. Allows resource discoveries to be created in these regions, as well as enabling monitoring</td></tr>
<tr><td><CopyableCode code="ipam_resource_discovery_region" /></td><td><code>string</code></td><td>The region the resource discovery is setup in. </td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="is_default" /></td><td><code>boolean</code></td><td>Determines whether or not address space from this pool is publicly advertised. Must be set if and only if the pool is IPv6.</td></tr>
<tr><td><CopyableCode code="ipam_resource_discovery_arn" /></td><td><code>string</code></td><td>Amazon Resource Name (Arn) for the Resource Discovery.</td></tr>
<tr><td><CopyableCode code="state" /></td><td><code>string</code></td><td>The state of this Resource Discovery.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
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
    <td><CopyableCode code="update_resource" /></td>
    <td><code>UPDATE</code></td>
    <td><CopyableCode code="data__Identifier, data__PatchDocument, region" /></td>
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
ipam_resource_discovery_id,
owner_id,
operating_regions,
ipam_resource_discovery_region,
description,
is_default,
ipam_resource_discovery_arn,
state,
tags
FROM aws.ec2.ipam_resource_discovery
WHERE region = 'us-east-1' AND data__Identifier = '<IpamResourceDiscoveryId>';
```


## Permissions

To operate on the <code>ipam_resource_discovery</code> resource, the following permissions are required:

### Read
```json
ec2:DescribeIpamResourceDiscoveries
```

### Update
```json
ec2:ModifyIpamResourceDiscovery,
ec2:DescribeIpamResourceDiscoveries,
ec2:CreateTags,
ec2:DeleteTags
```

