---
title: configuration_recorder
hide_title: false
hide_table_of_contents: false
keywords:
  - configuration_recorder
  - config
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>configuration_recorder</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>configuration_recorder</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>configuration_recorder</td></tr>
<tr><td><b>Id</b></td><td><code>aws.config.configuration_recorder</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>recording_group</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>role_ar_n</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
id,
recording_group,
role_ar_n,
name
FROM aws.config.configuration_recorder
WHERE region = 'us-east-1'
AND data__Identifier = '<Id>'
```
