---
title: event_integration
hide_title: false
hide_table_of_contents: false
keywords:
  - event_integration
  - appintegrations
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>event_integration</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>event_integration</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>event_integration</td></tr>
<tr><td><b>Id</b></td><td><code>aws.appintegrations.event_integration</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td>The event integration description.</td></tr>
<tr><td><code>event_integration_arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the event integration.</td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td>The name of the event integration.</td></tr>
<tr><td><code>event_bridge_bus</code></td><td><code>string</code></td><td>The Amazon Eventbridge bus for the event integration.</td></tr>
<tr><td><code>event_filter</code></td><td><code>object</code></td><td>The EventFilter (source) associated with the event integration.</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>The tags (keys and values) associated with the event integration.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
description,
event_integration_arn,
name,
event_bridge_bus,
event_filter,
tags
FROM aws.appintegrations.event_integration
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;Name&gt;'
```
