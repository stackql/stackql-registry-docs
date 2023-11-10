---
title: campaign
hide_title: false
hide_table_of_contents: false
keywords:
  - campaign
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
Gets an individual <code>campaign</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>campaign</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>campaign</td></tr>
<tr><td><b>Id</b></td><td><code>aws.pinpoint.campaign</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>segment_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>priority</code></td><td><code>integer</code></td><td></td></tr>
<tr><td><code>template_configuration</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>is_paused</code></td><td><code>boolean</code></td><td></td></tr>
<tr><td><code>additional_treatments</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>segment_version</code></td><td><code>integer</code></td><td></td></tr>
<tr><td><code>treatment_description</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>message_configuration</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>limits</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>campaign_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>holdout_percent</code></td><td><code>integer</code></td><td></td></tr>
<tr><td><code>schedule</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>custom_delivery_configuration</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>application_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>campaign_hook</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>treatment_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
description,
segment_id,
priority,
template_configuration,
is_paused,
additional_treatments,
name,
segment_version,
treatment_description,
message_configuration,
limits,
campaign_id,
holdout_percent,
schedule,
custom_delivery_configuration,
arn,
application_id,
campaign_hook,
tags,
treatment_name
FROM aws.pinpoint.campaign
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;CampaignId&gt;'
```
