---
title: access_log_subscription
hide_title: false
hide_table_of_contents: false
keywords:
  - access_log_subscription
  - vpclattice
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>access_log_subscription</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>access_log_subscription</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>access_log_subscription</td></tr>
<tr><td><b>Id</b></td><td><code>aws.vpclattice.access_log_subscription</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>destination_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>resource_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>resource_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>resource_identifier</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
arn,
destination_arn,
id,
resource_arn,
resource_id,
resource_identifier,
tags
FROM aws.vpclattice.access_log_subscription
WHERE region = 'us-east-1'
AND data__Identifier = '<Arn>'
```
