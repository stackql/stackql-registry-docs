---
title: mitigation_action
hide_title: false
hide_table_of_contents: false
keywords:
  - mitigation_action
  - iot
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>mitigation_action</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>mitigation_action</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>mitigation_action</td></tr>
<tr><td><b>Id</b></td><td><code>aws.iot.mitigation_action</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>action_name</code></td><td><code>string</code></td><td>A unique identifier for the mitigation action.</td></tr>
<tr><td><code>role_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
<tr><td><code>action_params</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>mitigation_action_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>mitigation_action_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
action_name,
role_arn,
tags,
action_params,
mitigation_action_arn,
mitigation_action_id
FROM aws.iot.mitigation_action
WHERE region = 'us-east-1'
AND data__Identifier = '<ActionName>'
```
