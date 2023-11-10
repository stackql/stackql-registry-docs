---
title: virtual_service
hide_title: false
hide_table_of_contents: false
keywords:
  - virtual_service
  - appmesh
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>virtual_service</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>virtual_service</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>virtual_service</td></tr>
<tr><td><b>Id</b></td><td><code>aws.appmesh.virtual_service</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>uid</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>mesh_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>mesh_owner</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>resource_owner</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>virtual_service_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>spec</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
uid,
mesh_name,
mesh_owner,
resource_owner,
id,
virtual_service_name,
arn,
spec,
tags
FROM aws.appmesh.virtual_service
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;Id&gt;'
```
