---
title: webacl_association
hide_title: false
hide_table_of_contents: false
keywords:
  - webacl_association
  - wafv2
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>webacl_association</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>webacl_association</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>webacl_association</td></tr>
<tr><td><b>Id</b></td><td><code>aws.wafv2.webacl_association</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>resource_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>web_ac_larn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
resource_arn,
web_ac_larn
FROM aws.wafv2.webacl_association
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;ResourceArn&gt;'
AND data__Identifier = '&lt;WebACLArn&gt;'
```
