---
title: layer_version_permission
hide_title: false
hide_table_of_contents: false
keywords:
  - layer_version_permission
  - lambda
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>layer_version_permission</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>layer_version_permission</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.lambda.layer_version_permission</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>Id</code></td><td><code>string</code></td><td></td></tr><tr><td><code>Action</code></td><td><code>string</code></td><td></td></tr><tr><td><code>LayerVersionArn</code></td><td><code>string</code></td><td></td></tr><tr><td><code>OrganizationId</code></td><td><code>string</code></td><td></td></tr><tr><td><code>Principal</code></td><td><code>string</code></td><td></td></tr>
</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT * 
FROM aws.lambda.layer_version_permission
WHERE region = 'us-east-1' AND data__Identifier = '{Id}'
```
