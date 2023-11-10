---
title: virtual_cluster
hide_title: false
hide_table_of_contents: false
keywords:
  - virtual_cluster
  - emrcontainers
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>virtual_cluster</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>virtual_cluster</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>virtual_cluster</td></tr>
<tr><td><b>Id</b></td><td><code>aws.emrcontainers.virtual_cluster</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>container_provider</code></td><td><code>object</code></td><td>Container provider of the virtual cluster.</td></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td>Id of the virtual cluster.</td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td>Name of the virtual cluster.</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>An array of key-value pairs to apply to this virtual cluster.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
arn,
container_provider,
id,
name,
tags
FROM aws.emrcontainers.virtual_cluster
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;Id&gt;'
```
