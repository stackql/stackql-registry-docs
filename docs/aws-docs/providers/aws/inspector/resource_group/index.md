---
title: resource_group
hide_title: false
hide_table_of_contents: false
keywords:
  - resource_group
  - inspector
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>resource_group</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>resource_group</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>resource_group</td></tr>
<tr><td><b>Id</b></td><td><code>aws.inspector.resource_group</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>resource_group_tags</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
arn,
resource_group_tags
FROM aws.inspector.resource_group
WHERE region = 'us-east-1'
AND data__Identifier = '<Arn>'
```
