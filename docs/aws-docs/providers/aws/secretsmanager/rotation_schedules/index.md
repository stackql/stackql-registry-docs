---
title: rotation_schedules
hide_title: false
hide_table_of_contents: false
keywords:
  - rotation_schedules
  - secretsmanager
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>rotation_schedules</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>rotation_schedules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.secretsmanager.rotation_schedules</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>Id</code></td><td><code>string</code></td><td></td></tr><tr><td><code>RotationLambdaARN</code></td><td><code>string</code></td><td></td></tr><tr><td><code>RotationRules</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>RotateImmediatelyOnUpdate</code></td><td><code>boolean</code></td><td></td></tr><tr><td><code>SecretId</code></td><td><code>string</code></td><td></td></tr><tr><td><code>HostedRotationLambda</code></td><td><code>undefined</code></td><td></td></tr>
</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT * 
FROM aws.secretsmanager.rotation_schedules
WHERE region = 'us-east-1'
```
