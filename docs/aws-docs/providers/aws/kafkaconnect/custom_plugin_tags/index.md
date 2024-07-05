---
title: custom_plugin_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - custom_plugin_tags
  - kafkaconnect
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

Expands all tag keys and values for <code>custom_plugins</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>custom_plugin_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>An example resource schema demonstrating some basic constructs and validation rules.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.kafkaconnect.custom_plugin_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name of the custom plugin.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>A summary description of the custom plugin.</td></tr>
<tr><td><CopyableCode code="custom_plugin_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the custom plugin to use.</td></tr>
<tr><td><CopyableCode code="content_type" /></td><td><code>string</code></td><td>The type of the plugin file.</td></tr>
<tr><td><CopyableCode code="file_description" /></td><td><code>object</code></td><td>Details about the custom plugin file.</td></tr>
<tr><td><CopyableCode code="location" /></td><td><code>object</code></td><td>Information about the location of a custom plugin.</td></tr>
<tr><td><CopyableCode code="revision" /></td><td><code>integer</code></td><td>The revision of the custom plugin.</td></tr>
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
Expands tags for all <code>custom_plugins</code> in a region.
```sql
SELECT
region,
name,
description,
custom_plugin_arn,
content_type,
file_description,
location,
revision,
tag_key,
tag_value
FROM aws.kafkaconnect.custom_plugin_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>custom_plugin_tags</code> resource, see <a href="/providers/aws/kafkaconnect/custom_plugins/#permissions"><code>custom_plugins</code></a>


