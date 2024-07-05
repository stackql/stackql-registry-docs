---
title: channel_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - channel_tags
  - cloudtrail
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

Expands all tag keys and values for <code>channels</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>channel_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>A channel receives events from a specific source (such as an on-premises storage solution or application, or a partner event data source), and delivers the events to one or more event data stores. You use channels to ingest events into CloudTrail from sources outside AWS.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.cloudtrail.channel_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name of the channel.</td></tr>
<tr><td><CopyableCode code="source" /></td><td><code>string</code></td><td>The ARN of an on-premises storage solution or application, or a partner event source.</td></tr>
<tr><td><CopyableCode code="destinations" /></td><td><code>array</code></td><td>One or more resources to which events arriving through a channel are logged and stored.</td></tr>
<tr><td><CopyableCode code="channel_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of a channel.</td></tr>
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
Expands tags for all <code>channels</code> in a region.
```sql
SELECT
region,
name,
source,
destinations,
channel_arn,
tag_key,
tag_value
FROM aws.cloudtrail.channel_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>channel_tags</code> resource, see <a href="/providers/aws/cloudtrail/channels/#permissions"><code>channels</code></a>


