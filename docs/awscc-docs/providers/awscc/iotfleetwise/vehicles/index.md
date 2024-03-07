---
title: vehicles
hide_title: false
hide_table_of_contents: false
keywords:
  - vehicles
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
Retrieves a list of <code>vehicles</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>vehicles</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>vehicles</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.iotfleetwise.vehicles</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>vehicles</code> resource, the following permissions are required:

### Create
<pre>
iotfleetwise:GetVehicle,
iotfleetwise:CreateVehicle,
iot:CreateThing,
iot:DescribeThing,
iotfleetwise:ListTagsForResource,
iotfleetwise:ListVehicles,
iotfleetwise:TagResource</pre>

### List
<pre>
iotfleetwise:ListVehicles</pre>


## Example
```sql
SELECT
region,
name
FROM awscc.iotfleetwise.vehicles
WHERE region = 'us-east-1'
```
