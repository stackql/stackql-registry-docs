---
title: resource_specific_loggings
hide_title: false
hide_table_of_contents: false
keywords:
  - resource_specific_loggings
  - iot
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>resource_specific_loggings</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>resource_specific_loggings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>resource_specific_loggings</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.iot.resource_specific_loggings</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>target_id</code></td><td><code>string</code></td><td>Unique Id for a Target (TargetType:TargetName), this will be internally built to serve as primary identifier for a log target.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>resource_specific_loggings</code> resource, the following permissions are required:

### Create
<pre>
iot:ListV2LoggingLevels,
iot:SetV2LoggingLevel</pre>

### List
<pre>
iot:ListV2LoggingLevels</pre>


## Example
```sql
SELECT
region,
target_id
FROM awscc.iot.resource_specific_loggings
WHERE region = 'us-east-1'
```
