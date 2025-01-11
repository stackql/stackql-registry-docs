---
title: channel_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - channel_tags
  - mediapackage
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
<tr><td><b>Description</b></td><td>Resource schema for AWS::MediaPackage::Channel</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.mediapackage.channel_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) assigned to the Channel.</td></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td>The ID of the Channel.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>A short text description of the Channel.</td></tr>
<tr><td><CopyableCode code="hls_ingest" /></td><td><code>object</code></td><td>An HTTP Live Streaming (HLS) ingest resource configuration.</td></tr>
<tr><td><CopyableCode code="egress_access_logs" /></td><td><code>object</code></td><td>The configuration parameters for egress access logging.</td></tr>
<tr><td><CopyableCode code="ingress_access_logs" /></td><td><code>object</code></td><td>The configuration parameters for egress access logging.</td></tr>
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
arn,
id,
description,
hls_ingest,
egress_access_logs,
ingress_access_logs,
tag_key,
tag_value
FROM aws.mediapackage.channel_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>channel_tags</code> resource, see <a href="/providers/aws/mediapackage/channels/#permissions"><code>channels</code></a>

