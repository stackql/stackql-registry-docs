---
title: network_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - network_tags
  - medialive
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

Expands all tag keys and values for <code>networks</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>network_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::MediaLive::Network.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.medialive.network_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The ARN of the Network.</td></tr>
<tr><td><CopyableCode code="associated_cluster_ids" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td>The unique ID of the Network.</td></tr>
<tr><td><CopyableCode code="ip_pools" /></td><td><code>array</code></td><td>The list of IP address cidr pools for the network</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The user-specified name of the Network to be created.</td></tr>
<tr><td><CopyableCode code="routes" /></td><td><code>array</code></td><td>The routes for the network</td></tr>
<tr><td><CopyableCode code="state" /></td><td><code>string</code></td><td>The current state of the Network.</td></tr>
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
Expands tags for all <code>networks</code> in a region.
```sql
SELECT
region,
arn,
associated_cluster_ids,
id,
ip_pools,
name,
routes,
state,
tag_key,
tag_value
FROM aws.medialive.network_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>network_tags</code> resource, see <a href="/providers/aws/medialive/networks/#permissions"><code>networks</code></a>

