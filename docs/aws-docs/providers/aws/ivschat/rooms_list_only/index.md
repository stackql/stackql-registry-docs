---
title: rooms_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - rooms_list_only
  - ivschat
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

Lists <code>rooms</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/rooms/"><code>rooms</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>rooms_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource type definition for AWS::IVSChat::Room.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ivschat.rooms_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>Room ARN is automatically generated on creation and assigned as the unique identifier.</td></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td>The system-generated ID of the room.</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name of the room. The value does not need to be unique.</td></tr>
<tr><td><CopyableCode code="logging_configuration_identifiers" /></td><td><code>array</code></td><td>Array of logging configuration identifiers attached to the room.</td></tr>
<tr><td><CopyableCode code="maximum_message_length" /></td><td><code>integer</code></td><td>The maximum number of characters in a single message.</td></tr>
<tr><td><CopyableCode code="maximum_message_rate_per_second" /></td><td><code>integer</code></td><td>The maximum number of messages per second that can be sent to the room.</td></tr>
<tr><td><CopyableCode code="message_review_handler" /></td><td><code>object</code></td><td>Configuration information for optional review of messages.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
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
Lists all <code>rooms</code> in a region.
```sql
SELECT
region,
arn
FROM aws.ivschat.rooms_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>rooms_list_only</code> resource, see <a href="/providers/aws/ivschat/rooms/#permissions"><code>rooms</code></a>


