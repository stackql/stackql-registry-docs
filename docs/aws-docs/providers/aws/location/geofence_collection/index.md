---
title: geofence_collection
hide_title: false
hide_table_of_contents: false
keywords:
  - geofence_collection
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
Gets an individual <code>geofence_collection</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>geofence_collection</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>geofence_collection</td></tr>
<tr><td><b>Id</b></td><td><code>aws.location.geofence_collection</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>collection_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>collection_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>create_time</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>kms_key_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>pricing_plan</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>pricing_plan_data_source</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>update_time</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
collection_arn,
arn,
collection_name,
create_time,
description,
kms_key_id,
pricing_plan,
pricing_plan_data_source,
update_time
FROM aws.location.geofence_collection
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;CollectionName&gt;'
```
