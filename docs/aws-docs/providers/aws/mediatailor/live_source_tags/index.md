---
title: live_source_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - live_source_tags
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

Expands all tag keys and values for <code>live_sources</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>live_source_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::MediaTailor::LiveSource Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.mediatailor.live_source_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td><p>The ARN of the live source.</p></td></tr>
<tr><td><CopyableCode code="http_package_configurations" /></td><td><code>array</code></td><td><p>A list of HTTP package configuration parameters for this live source.</p></td></tr>
<tr><td><CopyableCode code="live_source_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="source_location_name" /></td><td><code>string</code></td><td></td></tr>
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
Expands tags for all <code>live_sources</code> in a region.
```sql
SELECT
region,
arn,
http_package_configurations,
live_source_name,
source_location_name,
tag_key,
tag_value
FROM aws.mediatailor.live_source_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>live_source_tags</code> resource, see <a href="/providers/aws/mediatailor/live_sources/#permissions"><code>live_sources</code></a>

