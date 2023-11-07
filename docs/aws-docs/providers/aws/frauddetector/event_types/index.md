---
title: event_types
hide_title: false
hide_table_of_contents: false
keywords:
  - event_types
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
Retrieves a list of <code>event_types</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>event_types</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>event_types</td></tr>
<tr><td><b>Id</b></td><td><code>aws.frauddetector.event_types</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>Name</code></td><td><code>string</code></td><td>The name for the event type</td></tr>
<tr><td><code>Tags</code></td><td><code>array</code></td><td>Tags associated with this event type.</td></tr>
<tr><td><code>Description</code></td><td><code>string</code></td><td>The description of the event type.</td></tr>
<tr><td><code>EventVariables</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>Labels</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>EntityTypes</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>Arn</code></td><td><code>string</code></td><td>The ARN of the event type.</td></tr>
<tr><td><code>CreatedTime</code></td><td><code>string</code></td><td>The time when the event type was created.</td></tr>
<tr><td><code>LastUpdatedTime</code></td><td><code>string</code></td><td>The time when the event type was last updated.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT *<br/>FROM aws.frauddetector.event_types<br/>WHERE region = 'us-east-1'
</pre>
