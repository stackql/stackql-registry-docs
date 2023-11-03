---
title: event_subscription
hide_title: false
hide_table_of_contents: false
keywords:
  - event_subscription
  - dms
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>event_subscription</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>event_subscription</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
null
<tr><td><b>Id</b></td><td><code>aws.dms.event_subscription</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>SourceType</code></td><td><code>string</code></td><td></td></tr><tr><td><code>EventCategories</code></td><td><code>array</code></td><td></td></tr><tr><td><code>Enabled</code></td><td><code>boolean</code></td><td></td></tr><tr><td><code>SubscriptionName</code></td><td><code>string</code></td><td></td></tr><tr><td><code>SnsTopicArn</code></td><td><code>string</code></td><td></td></tr><tr><td><code>SourceIds</code></td><td><code>array</code></td><td></td></tr><tr><td><code>Id</code></td><td><code>string</code></td><td></td></tr><tr><td><code>Tags</code></td><td><code>array</code></td><td></td></tr>
</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.dms.event_subscription
WHERE region = 'us-east-1' AND data__Identifier = '<Id>'
</pre>
