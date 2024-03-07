---
title: tracker
hide_title: false
hide_table_of_contents: false
keywords:
  - tracker
  - location
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>tracker</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>tracker</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>tracker</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.location.tracker</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>create_time</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>event_bridge_enabled</code></td><td><code>boolean</code></td><td></td></tr>
<tr><td><code>kms_key_enable_geospatial_queries</code></td><td><code>boolean</code></td><td></td></tr>
<tr><td><code>kms_key_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>position_filtering</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>pricing_plan</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>pricing_plan_data_source</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
<tr><td><code>tracker_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>tracker_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>update_time</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>tracker</code> resource, the following permissions are required:

### Read
```json
geo:DescribeTracker,
kms:DescribeKey
```

### Update
```json
geo:CreateTracker,
geo:DescribeTracker,
geo:TagResource,
geo:UntagResource,
kms:DescribeKey,
kms:CreateGrant,
geo:UpdateTracker
```

### Delete
```json
geo:DeleteTracker,
geo:DescribeTracker
```


## Example
```sql
SELECT
region,
create_time,
description,
event_bridge_enabled,
kms_key_enable_geospatial_queries,
kms_key_id,
position_filtering,
pricing_plan,
pricing_plan_data_source,
tags,
tracker_arn,
tracker_name,
update_time,
arn
FROM awscc.location.tracker
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;TrackerName&gt;'
```
