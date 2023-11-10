---
title: room
hide_title: false
hide_table_of_contents: false
keywords:
  - room
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
Gets an individual <code>room</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>room</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>room</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ivschat.room</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td>Room ARN is automatically generated on creation and assigned as the unique identifier.</td></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td>The system-generated ID of the room.</td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td>The name of the room. The value does not need to be unique.</td></tr>
<tr><td><code>logging_configuration_identifiers</code></td><td><code>array</code></td><td>Array of logging configuration identifiers attached to the room.</td></tr>
<tr><td><code>maximum_message_length</code></td><td><code>integer</code></td><td>The maximum number of characters in a single message.</td></tr>
<tr><td><code>maximum_message_rate_per_second</code></td><td><code>integer</code></td><td>The maximum number of messages per second that can be sent to the room.</td></tr>
<tr><td><code>message_review_handler</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
arn,
id,
name,
logging_configuration_identifiers,
maximum_message_length,
maximum_message_rate_per_second,
message_review_handler,
tags
FROM aws.ivschat.room
WHERE region = 'us-east-1'
AND data__Identifier = '<Arn>'
```
