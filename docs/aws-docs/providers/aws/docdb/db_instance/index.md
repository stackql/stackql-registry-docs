---
title: db_instance
hide_title: false
hide_table_of_contents: false
keywords:
  - db_instance
  - docdb
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>db_instance</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>db_instance</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>db_instance</td></tr>
<tr><td><b>Id</b></td><td><code>aws.docdb.db_instance</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>endpoint</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>d_binstance_class</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>port</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>d_bcluster_identifier</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>availability_zone</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>preferred_maintenance_window</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>enable_performance_insights</code></td><td><code>boolean</code></td><td></td></tr>
<tr><td><code>auto_minor_version_upgrade</code></td><td><code>boolean</code></td><td></td></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>d_binstance_identifier</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
endpoint,
d_binstance_class,
port,
d_bcluster_identifier,
availability_zone,
preferred_maintenance_window,
enable_performance_insights,
auto_minor_version_upgrade,
id,
d_binstance_identifier,
tags
FROM aws.docdb.db_instance
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;Id&gt;'
```
