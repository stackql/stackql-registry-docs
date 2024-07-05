---
title: dataset_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - dataset_tags
  - iotanalytics
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

Expands all tag keys and values for <code>datasets</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>dataset_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::IoTAnalytics::Dataset</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.iotanalytics.dataset_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="actions" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="late_data_rules" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="dataset_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="content_delivery_rules" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="triggers" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="versioning_configuration" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="retention_period" /></td><td><code>object</code></td><td></td></tr>
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
Expands tags for all <code>datasets</code> in a region.
```sql
SELECT
region,
actions,
late_data_rules,
dataset_name,
content_delivery_rules,
triggers,
versioning_configuration,
id,
retention_period,
tag_key,
tag_value
FROM aws.iotanalytics.dataset_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>dataset_tags</code> resource, see <a href="/providers/aws/iotanalytics/datasets/#permissions"><code>datasets</code></a>


