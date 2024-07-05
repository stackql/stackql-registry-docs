---
title: ipams_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - ipams_list_only
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

Lists <code>ipams</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/ipams/"><code>ipams</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>ipams_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Schema of AWS::EC2::IPAM Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2.ipams_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="ipam_id" /></td><td><code>string</code></td><td>Id of the IPAM.</td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the IPAM.</td></tr>
<tr><td><CopyableCode code="default_resource_discovery_id" /></td><td><code>string</code></td><td>The Id of the default resource discovery, created with this IPAM.</td></tr>
<tr><td><CopyableCode code="default_resource_discovery_association_id" /></td><td><code>string</code></td><td>The Id of the default association to the default resource discovery, created with this IPAM.</td></tr>
<tr><td><CopyableCode code="resource_discovery_association_count" /></td><td><code>integer</code></td><td>The count of resource discoveries associated with this IPAM.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="public_default_scope_id" /></td><td><code>string</code></td><td>The Id of the default scope for publicly routable IP space, created with this IPAM.</td></tr>
<tr><td><CopyableCode code="private_default_scope_id" /></td><td><code>string</code></td><td>The Id of the default scope for publicly routable IP space, created with this IPAM.</td></tr>
<tr><td><CopyableCode code="scope_count" /></td><td><code>integer</code></td><td>The number of scopes that currently exist in this IPAM.</td></tr>
<tr><td><CopyableCode code="operating_regions" /></td><td><code>array</code></td><td>The regions IPAM is enabled for. Allows pools to be created in these regions, as well as enabling monitoring</td></tr>
<tr><td><CopyableCode code="tier" /></td><td><code>string</code></td><td>The tier of the IPAM.</td></tr>
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
    <td><CopyableCode code="list_resources" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples
Lists all <code>ipams</code> in a region.
```sql
SELECT
region,
ipam_id
FROM aws.ec2.ipams_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>ipams_list_only</code> resource, see <a href="/providers/aws/ec2/ipams/#permissions"><code>ipams</code></a>


