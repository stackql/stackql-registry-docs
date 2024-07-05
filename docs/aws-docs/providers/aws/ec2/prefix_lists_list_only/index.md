---
title: prefix_lists_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - prefix_lists_list_only
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

Lists <code>prefix_lists</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/prefix_lists/"><code>prefix_lists</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>prefix_lists_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema of AWS::EC2::PrefixList Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2.prefix_lists_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="prefix_list_name" /></td><td><code>string</code></td><td>Name of Prefix List.</td></tr>
<tr><td><CopyableCode code="prefix_list_id" /></td><td><code>string</code></td><td>Id of Prefix List.</td></tr>
<tr><td><CopyableCode code="owner_id" /></td><td><code>string</code></td><td>Owner Id of Prefix List.</td></tr>
<tr><td><CopyableCode code="address_family" /></td><td><code>string</code></td><td>Ip Version of Prefix List.</td></tr>
<tr><td><CopyableCode code="max_entries" /></td><td><code>integer</code></td><td>Max Entries of Prefix List.</td></tr>
<tr><td><CopyableCode code="version" /></td><td><code>integer</code></td><td>Version of Prefix List.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>Tags for Prefix List</td></tr>
<tr><td><CopyableCode code="entries" /></td><td><code>array</code></td><td>Entries of Prefix List.</td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the Prefix List.</td></tr>
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
Lists all <code>prefix_lists</code> in a region.
```sql
SELECT
region,
prefix_list_id
FROM aws.ec2.prefix_lists_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>prefix_lists_list_only</code> resource, see <a href="/providers/aws/ec2/prefix_lists/#permissions"><code>prefix_lists</code></a>


