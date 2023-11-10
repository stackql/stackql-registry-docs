---
title: workteam
hide_title: false
hide_table_of_contents: false
keywords:
  - workteam
  - sagemaker
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>workteam</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>workteam</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>workteam</td></tr>
<tr><td><b>Id</b></td><td><code>aws.sagemaker.workteam</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>notification_configuration</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>workteam_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>member_definitions</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>workforce_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
description,
notification_configuration,
workteam_name,
member_definitions,
id,
workforce_name,
tags
FROM aws.sagemaker.workteam
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;Id&gt;'
```
