---
title: device_fleet
hide_title: false
hide_table_of_contents: false
keywords:
  - device_fleet
  - sagemaker
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>device_fleet</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>device_fleet</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.sagemaker.device_fleet</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>Description</code></td><td><code>string</code></td><td>Description for the edge device fleet</td></tr><tr><td><code>DeviceFleetName</code></td><td><code>string</code></td><td>The name of the edge device fleet</td></tr><tr><td><code>OutputConfig</code></td><td><code>undefined</code></td><td>S3 bucket and an ecryption key id (if available) to store outputs for the fleet</td></tr><tr><td><code>RoleArn</code></td><td><code>string</code></td><td>Role associated with the device fleet</td></tr><tr><td><code>Tags</code></td><td><code>array</code></td><td>Associate tags with the resource</td></tr>
</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT * 
FROM aws.sagemaker.device_fleet
WHERE region = 'us-east-1' AND data__Identifier = '{DeviceFleetName}'
```
