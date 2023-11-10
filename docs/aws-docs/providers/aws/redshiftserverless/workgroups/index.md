---
title: workgroups
hide_title: false
hide_table_of_contents: false
keywords:
  - workgroups
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
Retrieves a list of <code>workgroups</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>workgroups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>workgroups</td></tr>
<tr><td><b>Id</b></td><td><code>aws.redshiftserverless.workgroups</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>workgroup_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
workgroup_name
FROM aws.redshiftserverless.workgroups
WHERE region = 'us-east-1'
```
