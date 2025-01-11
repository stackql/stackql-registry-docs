---
title: event_stream_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - event_stream_tags
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

Expands all tag keys and values for <code>event_streams</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>event_stream_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>An Event Stream resource of Amazon Connect Customer Profiles</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.customerprofiles.event_stream_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="domain_name" /></td><td><code>string</code></td><td>The unique name of the domain.</td></tr>
<tr><td><CopyableCode code="event_stream_name" /></td><td><code>string</code></td><td>The name of the event stream.</td></tr>
<tr><td><CopyableCode code="uri" /></td><td><code>string</code></td><td>The StreamARN of the destination to deliver profile events to. For example, arn:aws:kinesis:region:account-id:stream/stream-name</td></tr>
<tr><td><CopyableCode code="event_stream_arn" /></td><td><code>string</code></td><td>A unique identifier for the event stream.</td></tr>
<tr><td><CopyableCode code="created_at" /></td><td><code>string</code></td><td>The timestamp of when the export was created.</td></tr>
<tr><td><CopyableCode code="state" /></td><td><code>string</code></td><td>The operational state of destination stream for export.</td></tr>
<tr><td><CopyableCode code="destination_details" /></td><td><code>object</code></td><td>Details regarding the Kinesis stream.</td></tr>
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
Expands tags for all <code>event_streams</code> in a region.
```sql
SELECT
region,
domain_name,
event_stream_name,
uri,
event_stream_arn,
created_at,
state,
destination_details,
tag_key,
tag_value
FROM aws.customerprofiles.event_stream_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>event_stream_tags</code> resource, see <a href="/providers/aws/customerprofiles/event_streams/#permissions"><code>event_streams</code></a>

