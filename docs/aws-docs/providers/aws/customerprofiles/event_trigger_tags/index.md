---
title: event_trigger_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - event_trigger_tags
  - customerprofiles
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

Expands all tag keys and values for <code>event_triggers</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>event_trigger_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>An event trigger resource of Amazon Connect Customer Profiles</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.customerprofiles.event_trigger_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="domain_name" /></td><td><code>string</code></td><td>The unique name of the domain.</td></tr>
<tr><td><CopyableCode code="event_trigger_name" /></td><td><code>string</code></td><td>The unique name of the event trigger.</td></tr>
<tr><td><CopyableCode code="object_type_name" /></td><td><code>string</code></td><td>The unique name of the object type.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>The description of the event trigger.</td></tr>
<tr><td><CopyableCode code="event_trigger_conditions" /></td><td><code>array</code></td><td>A list of conditions that determine when an event should trigger the destination.</td></tr>
<tr><td><CopyableCode code="event_trigger_limits" /></td><td><code>object</code></td><td>Defines limits controlling whether an event triggers the destination, based on ingestion latency and the number of invocations per profile over specific time periods.</td></tr>
<tr><td><CopyableCode code="segment_filter" /></td><td><code>string</code></td><td>The destination is triggered only for profiles that meet the criteria of a segment definition.</td></tr>
<tr><td><CopyableCode code="created_at" /></td><td><code>string</code></td><td>The timestamp of when the event trigger was created.</td></tr>
<tr><td><CopyableCode code="last_updated_at" /></td><td><code>string</code></td><td>The timestamp of when the event trigger was most recently updated.</td></tr>
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
Expands tags for all <code>event_triggers</code> in a region.
```sql
SELECT
region,
domain_name,
event_trigger_name,
object_type_name,
description,
event_trigger_conditions,
event_trigger_limits,
segment_filter,
created_at,
last_updated_at,
tag_key,
tag_value
FROM aws.customerprofiles.event_trigger_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>event_trigger_tags</code> resource, see <a href="/providers/aws/customerprofiles/event_triggers/#permissions"><code>event_triggers</code></a>

