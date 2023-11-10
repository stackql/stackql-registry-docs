---
title: group_version
hide_title: false
hide_table_of_contents: false
keywords:
  - group_version
  - greengrass
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>group_version</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>group_version</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>group_version</td></tr>
<tr><td><b>Id</b></td><td><code>aws.greengrass.group_version</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>logger_definition_version_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>device_definition_version_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>function_definition_version_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>core_definition_version_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>resource_definition_version_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>connector_definition_version_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>subscription_definition_version_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>group_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
id,
logger_definition_version_arn,
device_definition_version_arn,
function_definition_version_arn,
core_definition_version_arn,
resource_definition_version_arn,
connector_definition_version_arn,
subscription_definition_version_arn,
group_id
FROM aws.greengrass.group_version
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;Id&gt;'
```
