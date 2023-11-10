---
title: application_settings
hide_title: false
hide_table_of_contents: false
keywords:
  - application_settings
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
Gets an individual <code>application_settings</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>application_settings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>application_settings</td></tr>
<tr><td><b>Id</b></td><td><code>aws.pinpoint.application_settings</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>quiet_time</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>limits</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>application_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>campaign_hook</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>cloud_watch_metrics_enabled</code></td><td><code>boolean</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
id,
quiet_time,
limits,
application_id,
campaign_hook,
cloud_watch_metrics_enabled
FROM aws.pinpoint.application_settings
WHERE region = 'us-east-1'
AND data__Identifier = '<Id>'
```
