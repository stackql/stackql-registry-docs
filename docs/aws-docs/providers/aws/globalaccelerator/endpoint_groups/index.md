---
title: endpoint_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - endpoint_groups
  - globalaccelerator
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>endpoint_groups</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>endpoint_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>endpoint_groups</td></tr>
<tr><td><b>Id</b></td><td><code>aws.globalaccelerator.endpoint_groups</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>endpoint_group_arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the endpoint group</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
endpoint_group_arn
FROM aws.globalaccelerator.endpoint_groups
WHERE region = 'us-east-1'
```
