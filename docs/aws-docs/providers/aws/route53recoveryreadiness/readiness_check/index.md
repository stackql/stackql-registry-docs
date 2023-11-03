---
title: readiness_check
hide_title: false
hide_table_of_contents: false
keywords:
  - readiness_check
  - route53recoveryreadiness
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>readiness_check</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>readiness_check</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.route53recoveryreadiness.readiness_check</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>ResourceSetName</code></td><td><code>string</code></td><td>The name of the resource set to check.</td></tr><tr><td><code>ReadinessCheckName</code></td><td><code>string</code></td><td>Name of the ReadinessCheck to create.</td></tr><tr><td><code>ReadinessCheckArn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the readiness check.</td></tr><tr><td><code>Tags</code></td><td><code>array</code></td><td>A collection of tags associated with a resource.</td></tr>
</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT * 
FROM aws.route53recoveryreadiness.readiness_check
WHERE region = 'us-east-1' AND data__Identifier = '{ReadinessCheckName}'
```
