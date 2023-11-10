---
title: voice_channel
hide_title: false
hide_table_of_contents: false
keywords:
  - voice_channel
  - pinpoint
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>voice_channel</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>voice_channel</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>voice_channel</td></tr>
<tr><td><b>Id</b></td><td><code>aws.pinpoint.voice_channel</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>enabled</code></td><td><code>boolean</code></td><td></td></tr>
<tr><td><code>application_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
id,
enabled,
application_id
FROM aws.pinpoint.voice_channel
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;Id&gt;'
```