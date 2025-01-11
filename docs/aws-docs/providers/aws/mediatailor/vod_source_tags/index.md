---
title: vod_source_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - vod_source_tags
  - mediatailor
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

Expands all tag keys and values for <code>vod_sources</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>vod_source_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::MediaTailor::VodSource Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.mediatailor.vod_source_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td><p>The ARN of the VOD source.</p></td></tr>
<tr><td><CopyableCode code="http_package_configurations" /></td><td><code>array</code></td><td><p>A list of HTTP package configuration parameters for this VOD source.</p></td></tr>
<tr><td><CopyableCode code="source_location_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="vod_source_name" /></td><td><code>string</code></td><td></td></tr>
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
Expands tags for all <code>vod_sources</code> in a region.
```sql
SELECT
region,
arn,
http_package_configurations,
source_location_name,
vod_source_name,
tag_key,
tag_value
FROM aws.mediatailor.vod_source_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>vod_source_tags</code> resource, see <a href="/providers/aws/mediatailor/vod_sources/#permissions"><code>vod_sources</code></a>

