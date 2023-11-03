---
title: instance_storage_config
hide_title: false
hide_table_of_contents: false
keywords:
  - instance_storage_config
  - connect
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>instance_storage_config</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>instance_storage_config</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.connect.instance_storage_config</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>InstanceArn</code></td><td><code>string</code></td><td>Connect Instance ID with which the storage config will be associated</td></tr><tr><td><code>ResourceType</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>AssociationId</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>StorageType</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>S3Config</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>KinesisVideoStreamConfig</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>KinesisStreamConfig</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>KinesisFirehoseConfig</code></td><td><code>undefined</code></td><td></td></tr>
</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT * 
FROM aws.connect.instance_storage_config
WHERE region = 'us-east-1' AND data__Identifier = '{InstanceArn}' AND data__Identifier = '{AssociationId}' AND data__Identifier = '{ResourceType}'
```
