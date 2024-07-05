---
title: campaign_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - campaign_tags
  - iotfleetwise
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

Expands all tag keys and values for <code>campaigns</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>campaign_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::IoTFleetWise::Campaign Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.iotfleetwise.campaign_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="status" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="action" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="creation_time" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="compression" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="priority" /></td><td><code>integer</code></td><td></td></tr>
<tr><td><CopyableCode code="signals_to_collect" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="data_destination_configs" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="start_time" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="expiry_time" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="last_modification_time" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="spooling_mode" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="signal_catalog_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="post_trigger_collection_duration" /></td><td><code>number</code></td><td></td></tr>
<tr><td><CopyableCode code="data_extra_dimensions" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="diagnostics_mode" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="target_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="collection_scheme" /></td><td><code>undefined</code></td><td></td></tr>
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
Expands tags for all <code>campaigns</code> in a region.
```sql
SELECT
region,
status,
action,
creation_time,
compression,
description,
priority,
signals_to_collect,
data_destination_configs,
start_time,
name,
expiry_time,
last_modification_time,
spooling_mode,
signal_catalog_arn,
post_trigger_collection_duration,
data_extra_dimensions,
diagnostics_mode,
target_arn,
arn,
collection_scheme,
tag_key,
tag_value
FROM aws.iotfleetwise.campaign_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>campaign_tags</code> resource, see <a href="/providers/aws/iotfleetwise/campaigns/#permissions"><code>campaigns</code></a>


