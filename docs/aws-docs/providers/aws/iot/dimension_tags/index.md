---
title: dimension_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - dimension_tags
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

Expands all tag keys and values for <code>dimensions</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>dimension_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>A dimension can be used to limit the scope of a metric used in a security profile for AWS IoT Device Defender.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.iot.dimension_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>A unique identifier for the dimension.</td></tr>
<tr><td><CopyableCode code="type" /></td><td><code>string</code></td><td>Specifies the type of the dimension.</td></tr>
<tr><td><CopyableCode code="string_values" /></td><td><code>array</code></td><td>Specifies the value or list of values for the dimension.</td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The ARN (Amazon resource name) of the created dimension.</td></tr>
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
Expands tags for all <code>dimensions</code> in a region.
```sql
SELECT
region,
name,
type,
string_values,
arn,
tag_key,
tag_value
FROM aws.iot.dimension_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>dimension_tags</code> resource, see <a href="/providers/aws/iot/dimensions/#permissions"><code>dimensions</code></a>


