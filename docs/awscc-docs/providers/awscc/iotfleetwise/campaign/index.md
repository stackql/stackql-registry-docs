---
title: campaign
hide_title: false
hide_table_of_contents: false
keywords:
  - campaign
  - iotfleetwise
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
<tr><td><b>Id</b></td><td><code>awscc.iotfleetwise.campaign</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>status</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>action</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>creation_time</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>compression</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>priority</code></td><td><code>integer</code></td><td></td></tr>
<tr><td><code>signals_to_collect</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>data_destination_configs</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>start_time</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>expiry_time</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>last_modification_time</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>spooling_mode</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>signal_catalog_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>post_trigger_collection_duration</code></td><td><code>number</code></td><td></td></tr>
<tr><td><code>data_extra_dimensions</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>diagnostics_mode</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>target_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>collection_scheme</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>campaign</code> resource, the following permissions are required:

### Read
<pre>
iotfleetwise:GetCampaign,
iotfleetwise:ListTagsForResource</pre>

### Update
<pre>
iotfleetwise:GetCampaign,
iotfleetwise:ListTagsForResource,
iotfleetwise:UpdateCampaign,
iotfleetwise:TagResource,
iotfleetwise:UntagResource</pre>

### Delete
<pre>
iotfleetwise:DeleteCampaign,
iotfleetwise:GetCampaign</pre>


## Example
```sql
SELECT
region,
status,
action,
creation_time,
compression,
description,
priority,
signals_to_collect,
data_destination_configs,
start_time,
name,
expiry_time,
last_modification_time,
spooling_mode,
signal_catalog_arn,
post_trigger_collection_duration,
data_extra_dimensions,
diagnostics_mode,
target_arn,
arn,
collection_scheme,
tags
FROM awscc.iotfleetwise.campaign
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;Name&gt;'
```
