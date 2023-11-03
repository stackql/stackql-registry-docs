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
<tr><td><b>Id</b></td><td><code>aws.ssm.resource_data_sync</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>S3Destination</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>KMSKeyArn</code></td><td><code>string</code></td><td></td></tr><tr><td><code>SyncSource</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>BucketName</code></td><td><code>string</code></td><td></td></tr><tr><td><code>BucketRegion</code></td><td><code>string</code></td><td></td></tr><tr><td><code>SyncFormat</code></td><td><code>string</code></td><td></td></tr><tr><td><code>SyncName</code></td><td><code>string</code></td><td></td></tr><tr><td><code>SyncType</code></td><td><code>string</code></td><td></td></tr><tr><td><code>BucketPrefix</code></td><td><code>string</code></td><td></td></tr>
</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT * 
FROM aws.ssm.resource_data_sync
WHERE region = 'us-east-1' AND data__Identifier = '{SyncName}'
```
