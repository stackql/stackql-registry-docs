---
title: custom_metric_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - custom_metric_tags
  - iot
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

Expands all tag keys and values for <code>custom_metrics</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>custom_metric_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>A custom metric published by your devices to Device Defender.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.iot.custom_metric_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="metric_name" /></td><td><code>string</code></td><td>The name of the custom metric. This will be used in the metric report submitted from the device/thing. Shouldn't begin with aws: . Cannot be updated once defined.</td></tr>
<tr><td><CopyableCode code="display_name" /></td><td><code>string</code></td><td>Field represents a friendly name in the console for the custom metric; it doesn't have to be unique. Don't use this name as the metric identifier in the device metric report. Can be updated once defined.</td></tr>
<tr><td><CopyableCode code="metric_type" /></td><td><code>string</code></td><td>The type of the custom metric. Types include string-list, ip-address-list, number-list, and number.</td></tr>
<tr><td><CopyableCode code="metric_arn" /></td><td><code>string</code></td><td>The Amazon Resource Number (ARN) of the custom metric.</td></tr>
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
Expands tags for all <code>custom_metrics</code> in a region.
```sql
SELECT
region,
metric_name,
display_name,
metric_type,
metric_arn,
tag_key,
tag_value
FROM aws.iot.custom_metric_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>custom_metric_tags</code> resource, see <a href="/providers/aws/iot/custom_metrics/#permissions"><code>custom_metrics</code></a>

