---
title: option_group
hide_title: false
hide_table_of_contents: false
keywords:
  - option_group
  - rds
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>option_group</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>option_group</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>option_group</td></tr>
<tr><td><b>Id</b></td><td><code>aws.rds.option_group</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>option_group_name</code></td><td><code>string</code></td><td>Specifies the name of the option group.</td></tr>
<tr><td><code>option_group_description</code></td><td><code>string</code></td><td>Provides a description of the option group.</td></tr>
<tr><td><code>engine_name</code></td><td><code>string</code></td><td>Indicates the name of the engine that this option group can be applied to.</td></tr>
<tr><td><code>major_engine_version</code></td><td><code>string</code></td><td>Indicates the major engine version associated with this option group.</td></tr>
<tr><td><code>option_configurations</code></td><td><code>array</code></td><td>Indicates what options are available in the option group.</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
option_group_name,
option_group_description,
engine_name,
major_engine_version,
option_configurations,
tags
FROM aws.rds.option_group
WHERE region = 'us-east-1'
AND data__Identifier = '<OptionGroupName>'
```
