---
title: segment
hide_title: false
hide_table_of_contents: false
keywords:
  - segment
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
Gets an individual <code>segment</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>segment</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>segment</td></tr>
<tr><td><b>Id</b></td><td><code>aws.pinpoint.segment</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>segment_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>segment_groups</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>dimensions</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>application_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
segment_id,
arn,
segment_groups,
dimensions,
application_id,
tags,
name
FROM aws.pinpoint.segment
WHERE region = 'us-east-1'
AND data__Identifier = '<SegmentId>'
```
