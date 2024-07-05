---
title: channel_group_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - channel_group_tags
  - mediapackagev2
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

Expands all tag keys and values for <code>channel_groups</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>channel_group_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td><p>Represents a channel group that facilitates the grouping of multiple channels.</p></td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.mediapackagev2.channel_group_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td><p>The Amazon Resource Name (ARN) associated with the resource.</p></td></tr>
<tr><td><CopyableCode code="channel_group_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="created_at" /></td><td><code>string</code></td><td><p>The date and time the channel group was created.</p></td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td><p>Enter any descriptive text that helps you to identify the channel group.</p></td></tr>
<tr><td><CopyableCode code="egress_domain" /></td><td><code>string</code></td><td><p>The output domain where the source stream should be sent. Integrate the domain with a downstream CDN (such as Amazon CloudFront) or playback device.</p></td></tr>
<tr><td><CopyableCode code="modified_at" /></td><td><code>string</code></td><td><p>The date and time the channel group was modified.</p></td></tr>
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
Expands tags for all <code>channel_groups</code> in a region.
```sql
SELECT
region,
arn,
channel_group_name,
created_at,
description,
egress_domain,
modified_at,
tag_key,
tag_value
FROM aws.mediapackagev2.channel_group_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>channel_group_tags</code> resource, see <a href="/providers/aws/mediapackagev2/channel_groups/#permissions"><code>channel_groups</code></a>


