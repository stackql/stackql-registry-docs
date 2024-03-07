---
title: device_fleets
hide_title: false
hide_table_of_contents: false
keywords:
  - device_fleets
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
Retrieves a list of <code>device_fleets</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>device_fleets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>device_fleets</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.sagemaker.device_fleets</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>device_fleet_name</code></td><td><code>string</code></td><td>The name of the edge device fleet</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>device_fleets</code> resource, the following permissions are required:

### Create
<pre>
sagemaker:CreateDeviceFleet,
iam:PassRole</pre>


## Example
```sql
SELECT
region,
device_fleet_name
FROM awscc.sagemaker.device_fleets
WHERE region = 'us-east-1'
```
