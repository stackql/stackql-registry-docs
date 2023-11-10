---
title: attribute_group
hide_title: false
hide_table_of_contents: false
keywords:
  - attribute_group
  - servicecatalogappregistry
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>attribute_group</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>attribute_group</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>attribute_group</td></tr>
<tr><td><b>Id</b></td><td><code>aws.servicecatalogappregistry.attribute_group</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td>The name of the attribute group. </td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td>The description of the attribute group. </td></tr>
<tr><td><code>attributes</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
id,
arn,
name,
description,
attributes,
tags
FROM aws.servicecatalogappregistry.attribute_group
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;Id&gt;'
```
