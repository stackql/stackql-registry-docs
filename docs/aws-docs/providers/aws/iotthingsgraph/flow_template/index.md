---
title: flow_template
hide_title: false
hide_table_of_contents: false
keywords:
  - flow_template
  - iotthingsgraph
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>flow_template</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>flow_template</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>flow_template</td></tr>
<tr><td><b>Id</b></td><td><code>aws.iotthingsgraph.flow_template</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>compatible_namespace_version</code></td><td><code>number</code></td><td></td></tr>
<tr><td><code>definition</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
id,
compatible_namespace_version,
definition
FROM aws.iotthingsgraph.flow_template
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;Id&gt;'
```