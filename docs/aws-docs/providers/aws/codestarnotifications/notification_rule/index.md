---
title: notification_rule
hide_title: false
hide_table_of_contents: false
keywords:
  - notification_rule
  - codestarnotifications
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>notification_rule</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>notification_rule</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>notification_rule</td></tr>
<tr><td><b>Id</b></td><td><code>aws.codestarnotifications.notification_rule</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>event_type_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>created_by</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>target_address</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>event_type_ids</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>status</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>detail_type</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>resource</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>targets</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
event_type_id,
created_by,
target_address,
event_type_ids,
status,
detail_type,
resource,
targets,
tags,
name,
arn
FROM aws.codestarnotifications.notification_rule
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;Arn&gt;'
```
