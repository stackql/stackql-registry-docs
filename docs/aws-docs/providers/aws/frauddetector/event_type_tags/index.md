---
title: event_type_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - event_type_tags
  - frauddetector
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

Expands all tag keys and values for <code>event_types</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>event_type_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>A resource schema for an EventType in Amazon Fraud Detector.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.frauddetector.event_type_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name for the event type</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>The description of the event type.</td></tr>
<tr><td><CopyableCode code="event_variables" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="labels" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="entity_types" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The ARN of the event type.</td></tr>
<tr><td><CopyableCode code="created_time" /></td><td><code>string</code></td><td>The time when the event type was created.</td></tr>
<tr><td><CopyableCode code="last_updated_time" /></td><td><code>string</code></td><td>The time when the event type was last updated.</td></tr>
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
Expands tags for all <code>event_types</code> in a region.
```sql
SELECT
region,
name,
description,
event_variables,
labels,
entity_types,
arn,
created_time,
last_updated_time,
tag_key,
tag_value
FROM aws.frauddetector.event_type_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>event_type_tags</code> resource, see <a href="/providers/aws/frauddetector/event_types/#permissions"><code>event_types</code></a>


