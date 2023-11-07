---
title: event_integrations
hide_title: false
hide_table_of_contents: false
keywords:
  - event_integrations
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
Retrieves a list of <code>event_integrations</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>event_integrations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>event_integrations</td></tr>
<tr><td><b>Id</b></td><td><code>aws.appintegrations.event_integrations</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>Description</code></td><td><code>string</code></td><td>The event integration description.</td></tr>
<tr><td><code>EventIntegrationArn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the event integration.</td></tr>
<tr><td><code>Name</code></td><td><code>string</code></td><td>The name of the event integration.</td></tr>
<tr><td><code>EventBridgeBus</code></td><td><code>string</code></td><td>The Amazon Eventbridge bus for the event integration.</td></tr>
<tr><td><code>EventFilter</code></td><td><code>undefined</code></td><td>The EventFilter (source) associated with the event integration.</td></tr>
<tr><td><code>Tags</code></td><td><code>array</code></td><td>The tags (keys and values) associated with the event integration.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.appintegrations.event_integrations
WHERE region = 'us-east-1'
</pre>
