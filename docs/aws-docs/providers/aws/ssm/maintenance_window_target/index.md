---
title: maintenance_window_target
hide_title: false
hide_table_of_contents: false
keywords:
  - maintenance_window_target
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
Gets an individual <code>maintenance_window_target</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>maintenance_window_target</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>maintenance_window_target</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ssm.maintenance_window_target</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>owner_information</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>window_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>resource_type</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>targets</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
owner_information,
description,
window_id,
resource_type,
targets,
id,
name
FROM aws.ssm.maintenance_window_target
WHERE region = 'us-east-1'
AND data__Identifier = '<Id>'
```
