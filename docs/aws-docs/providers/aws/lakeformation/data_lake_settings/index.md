---
title: data_lake_settings
hide_title: false
hide_table_of_contents: false
keywords:
  - data_lake_settings
  - lakeformation
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>data_lake_settings</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>data_lake_settings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>data_lake_settings</td></tr>
<tr><td><b>Id</b></td><td><code>aws.lakeformation.data_lake_settings</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>allow_external_data_filtering</code></td><td><code>boolean</code></td><td></td></tr>
<tr><td><code>external_data_filtering_allow_list</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>create_table_default_permissions</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>parameters</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>admins</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>create_database_default_permissions</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>authorized_session_tag_value_list</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>trusted_resource_owners</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
allow_external_data_filtering,
external_data_filtering_allow_list,
create_table_default_permissions,
parameters,
admins,
create_database_default_permissions,
id,
authorized_session_tag_value_list,
trusted_resource_owners
FROM aws.lakeformation.data_lake_settings
WHERE region = 'us-east-1'
AND data__Identifier = '<Id>'
```
