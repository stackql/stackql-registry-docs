---
title: link_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - link_tags
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

Expands all tag keys and values for <code>links</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>link_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::NetworkManager::Link type describes a link.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.networkmanager.link_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="link_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the link.</td></tr>
<tr><td><CopyableCode code="link_id" /></td><td><code>string</code></td><td>The ID of the link.</td></tr>
<tr><td><CopyableCode code="global_network_id" /></td><td><code>string</code></td><td>The ID of the global network.</td></tr>
<tr><td><CopyableCode code="site_id" /></td><td><code>string</code></td><td>The ID of the site</td></tr>
<tr><td><CopyableCode code="bandwidth" /></td><td><code>object</code></td><td>The Bandwidth for the link.</td></tr>
<tr><td><CopyableCode code="provider" /></td><td><code>string</code></td><td>The provider of the link.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>The description of the link.</td></tr>
<tr><td><CopyableCode code="type" /></td><td><code>string</code></td><td>The type of the link.</td></tr>
<tr><td><CopyableCode code="created_at" /></td><td><code>string</code></td><td>The date and time that the device was created.</td></tr>
<tr><td><CopyableCode code="state" /></td><td><code>string</code></td><td>The state of the link.</td></tr>
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
Expands tags for all <code>links</code> in a region.
```sql
SELECT
region,
link_arn,
link_id,
global_network_id,
site_id,
bandwidth,
provider,
description,
type,
created_at,
state,
tag_key,
tag_value
FROM aws.networkmanager.link_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>link_tags</code> resource, see <a href="/providers/aws/networkmanager/links/#permissions"><code>links</code></a>


