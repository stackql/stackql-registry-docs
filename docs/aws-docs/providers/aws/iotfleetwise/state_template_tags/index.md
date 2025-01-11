---
title: state_template_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - state_template_tags
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

Expands all tag keys and values for <code>state_templates</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>state_template_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::IoTFleetWise::StateTemplate Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.iotfleetwise.state_template_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="creation_time" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="last_modification_time" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="signal_catalog_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="state_template_properties" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="data_extra_dimensions" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="metadata_extra_dimensions" /></td><td><code>array</code></td><td></td></tr>
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
Expands tags for all <code>state_templates</code> in a region.
```sql
SELECT
region,
arn,
creation_time,
description,
last_modification_time,
name,
signal_catalog_arn,
state_template_properties,
data_extra_dimensions,
metadata_extra_dimensions,
tag_key,
tag_value
FROM aws.iotfleetwise.state_template_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>state_template_tags</code> resource, see <a href="/providers/aws/iotfleetwise/state_templates/#permissions"><code>state_templates</code></a>

