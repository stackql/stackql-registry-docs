---
title: resource_update_constraints
hide_title: false
hide_table_of_contents: false
keywords:
  - resource_update_constraints
  - servicecatalog
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>resource_update_constraints</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>resource_update_constraints</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>resource_update_constraints</td></tr>
<tr><td><b>Id</b></td><td><code>aws.servicecatalog.resource_update_constraints</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
id
FROM aws.servicecatalog.resource_update_constraints
WHERE region = 'us-east-1'
```
