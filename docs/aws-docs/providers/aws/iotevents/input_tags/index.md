---
title: input_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - input_tags
  - iotevents
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

Expands all tag keys and values for <code>inputs</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>input_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::IoTEvents::Input resource creates an input. To monitor your devices and processes, they must have a way to get telemetry data into ITE. This is done by sending messages as *inputs* to ITE. For more information, see &#91;How to Use&#93;(https://docs.aws.amazon.com/iotevents/latest/developerguide/how-to-use-iotevents.html) in the *Developer Guide*.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.iotevents.input_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="input_definition" /></td><td><code>object</code></td><td>The definition of the input.</td></tr>
<tr><td><CopyableCode code="input_description" /></td><td><code>string</code></td><td>A brief description of the input.</td></tr>
<tr><td><CopyableCode code="input_name" /></td><td><code>string</code></td><td>The name of the input.</td></tr>
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
Expands tags for all <code>inputs</code> in a region.
```sql
SELECT
region,
input_definition,
input_description,
input_name,
tag_key,
tag_value
FROM aws.iotevents.input_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>input_tags</code> resource, see <a href="/providers/aws/iotevents/inputs/#permissions"><code>inputs</code></a>

