---
title: core_networks_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - core_networks_list_only
  - networkmanager
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

Lists <code>core_networks</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/core_networks/"><code>core_networks</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>core_networks_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>AWS::NetworkManager::CoreNetwork Resource Type Definition.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.networkmanager.core_networks_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="global_network_id" /></td><td><code>string</code></td><td>The ID of the global network that your core network is a part of.</td></tr>
<tr><td><CopyableCode code="core_network_id" /></td><td><code>string</code></td><td>The Id of core network</td></tr>
<tr><td><CopyableCode code="core_network_arn" /></td><td><code>string</code></td><td>The ARN (Amazon resource name) of core network</td></tr>
<tr><td><CopyableCode code="policy_document" /></td><td><code>object</code></td><td>Live policy document for the core network, you must provide PolicyDocument in Json Format</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>The description of core network</td></tr>
<tr><td><CopyableCode code="created_at" /></td><td><code>string</code></td><td>The creation time of core network</td></tr>
<tr><td><CopyableCode code="state" /></td><td><code>string</code></td><td>The state of core network</td></tr>
<tr><td><CopyableCode code="segments" /></td><td><code>array</code></td><td>The segments within a core network.</td></tr>
<tr><td><CopyableCode code="edges" /></td><td><code>array</code></td><td>The edges within a core network.</td></tr>
<tr><td><CopyableCode code="owner_account" /></td><td><code>string</code></td><td>Owner of the core network</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>The tags for the global network.</td></tr>
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
Lists all <code>core_networks</code> in a region.
```sql
SELECT
region,
core_network_id
FROM aws.networkmanager.core_networks_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>core_networks_list_only</code> resource, see <a href="/providers/aws/networkmanager/core_networks/#permissions"><code>core_networks</code></a>


