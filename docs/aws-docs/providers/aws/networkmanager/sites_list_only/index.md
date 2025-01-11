---
title: sites_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - sites_list_only
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

Lists <code>sites</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/sites/"><code>sites</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>sites_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::NetworkManager::Site type describes a site.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.networkmanager.sites_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="site_id" /></td><td><code>string</code></td><td>The ID of the site.</td></tr>
<tr><td><CopyableCode code="global_network_id" /></td><td><code>string</code></td><td>The ID of the global network.</td></tr>
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
Lists all <code>sites</code> in a region.
```sql
SELECT
region,
global_network_id,
site_id
FROM aws.networkmanager.sites_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>sites_list_only</code> resource, see <a href="/providers/aws/networkmanager/sites/#permissions"><code>sites</code></a>

