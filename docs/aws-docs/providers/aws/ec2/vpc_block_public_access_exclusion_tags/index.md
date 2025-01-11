---
title: vpc_block_public_access_exclusion_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - vpc_block_public_access_exclusion_tags
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

Expands all tag keys and values for <code>vpc_block_public_access_exclusions</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>vpc_block_public_access_exclusion_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::EC2::VPCBlockPublicAccessExclusion.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2.vpc_block_public_access_exclusion_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="exclusion_id" /></td><td><code>string</code></td><td>The ID of the exclusion</td></tr>
<tr><td><CopyableCode code="internet_gateway_exclusion_mode" /></td><td><code>string</code></td><td>The desired Block Public Access Exclusion Mode for a specific VPC/Subnet.</td></tr>
<tr><td><CopyableCode code="vpc_id" /></td><td><code>string</code></td><td>The ID of the vpc. Required only if you don't specify SubnetId.</td></tr>
<tr><td><CopyableCode code="subnet_id" /></td><td><code>string</code></td><td>The ID of the subnet. Required only if you don't specify VpcId</td></tr>
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
Expands tags for all <code>vpc_block_public_access_exclusions</code> in a region.
```sql
SELECT
region,
exclusion_id,
internet_gateway_exclusion_mode,
vpc_id,
subnet_id,
tag_key,
tag_value
FROM aws.ec2.vpc_block_public_access_exclusion_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>vpc_block_public_access_exclusion_tags</code> resource, see <a href="/providers/aws/ec2/vpc_block_public_access_exclusions/#permissions"><code>vpc_block_public_access_exclusions</code></a>

