---
title: workgroup
hide_title: false
hide_table_of_contents: false
keywords:
  - workgroup
  - redshiftserverless
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>workgroup</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>workgroup</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>workgroup</td></tr>
<tr><td><b>Id</b></td><td><code>aws.redshiftserverless.workgroup</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>workgroup_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>namespace_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>base_capacity</code></td><td><code>integer</code></td><td></td></tr>
<tr><td><code>enhanced_vpc_routing</code></td><td><code>boolean</code></td><td></td></tr>
<tr><td><code>config_parameters</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>security_group_ids</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>subnet_ids</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>publicly_accessible</code></td><td><code>boolean</code></td><td></td></tr>
<tr><td><code>port</code></td><td><code>integer</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>workgroup</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
workgroup_name,
namespace_name,
base_capacity,
enhanced_vpc_routing,
config_parameters,
security_group_ids,
subnet_ids,
publicly_accessible,
port,
tags,
workgroup
FROM aws.redshiftserverless.workgroup
WHERE region = 'us-east-1'
AND data__Identifier = '<WorkgroupName>'
```
