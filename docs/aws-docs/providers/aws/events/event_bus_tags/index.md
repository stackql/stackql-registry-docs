---
title: event_bus_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - event_bus_tags
  - events
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

Expands all tag keys and values for <code>event_buses</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>event_bus_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource type definition for AWS::Events::EventBus</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.events.event_bus_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="event_source_name" /></td><td><code>string</code></td><td>If you are creating a partner event bus, this specifies the partner event source that the new event bus will be matched with.</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name of the event bus.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>The description of the event bus.</td></tr>
<tr><td><CopyableCode code="kms_key_identifier" /></td><td><code>string</code></td><td>Kms Key Identifier used to encrypt events at rest in the event bus.</td></tr>
<tr><td><CopyableCode code="policy" /></td><td><code>object</code></td><td>A JSON string that describes the permission policy statement for the event bus.</td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) for the event bus.</td></tr>
<tr><td><CopyableCode code="dead_letter_config" /></td><td><code>object</code></td><td>Dead Letter Queue for the event bus.</td></tr>
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
Expands tags for all <code>event_buses</code> in a region.
```sql
SELECT
region,
event_source_name,
name,
description,
kms_key_identifier,
policy,
arn,
dead_letter_config,
tag_key,
tag_value
FROM aws.events.event_bus_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>event_bus_tags</code> resource, see <a href="/providers/aws/events/event_buses/#permissions"><code>event_buses</code></a>


