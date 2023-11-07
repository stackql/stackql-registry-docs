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
<tr><td><code>Arn</code></td><td><code>string</code></td><td>Room ARN is automatically generated on creation and assigned as the unique identifier.</td></tr>
<tr><td><code>Id</code></td><td><code>string</code></td><td>The system-generated ID of the room.</td></tr>
<tr><td><code>Name</code></td><td><code>string</code></td><td>The name of the room. The value does not need to be unique.</td></tr>
<tr><td><code>LoggingConfigurationIdentifiers</code></td><td><code>array</code></td><td>Array of logging configuration identifiers attached to the room.</td></tr>
<tr><td><code>MaximumMessageLength</code></td><td><code>integer</code></td><td>The maximum number of characters in a single message.</td></tr>
<tr><td><code>MaximumMessageRatePerSecond</code></td><td><code>integer</code></td><td>The maximum number of messages per second that can be sent to the room.</td></tr>
<tr><td><code>MessageReviewHandler</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>Tags</code></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT *<br/>FROM aws.ivschat.room<br/>WHERE region = 'us-east-1'<br/>AND data__Identifier = '&lt;Arn&gt;'
</pre>
