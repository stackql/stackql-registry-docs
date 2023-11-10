---
title: resource_data_sync
hide_title: false
hide_table_of_contents: false
keywords:
  - resource_data_sync
  - ssm
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>resource_data_sync</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>resource_data_sync</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>resource_data_sync</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ssm.resource_data_sync</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>s3_destination</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>k_ms_key_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>sync_source</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>bucket_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>bucket_region</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>sync_format</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>sync_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>sync_type</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>bucket_prefix</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
s3_destination,
k_ms_key_arn,
sync_source,
bucket_name,
bucket_region,
sync_format,
sync_name,
sync_type,
bucket_prefix
FROM aws.ssm.resource_data_sync
WHERE region = 'us-east-1'
AND data__Identifier = '<SyncName>'
```
