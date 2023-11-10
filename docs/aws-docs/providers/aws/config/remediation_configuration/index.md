---
title: remediation_configuration
hide_title: false
hide_table_of_contents: false
keywords:
  - remediation_configuration
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
Gets an individual <code>remediation_configuration</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>remediation_configuration</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>remediation_configuration</td></tr>
<tr><td><b>Id</b></td><td><code>aws.config.remediation_configuration</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>target_version</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>execution_controls</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>parameters</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>target_type</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>config_rule_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>resource_type</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>retry_attempt_seconds</code></td><td><code>integer</code></td><td></td></tr>
<tr><td><code>maximum_automatic_attempts</code></td><td><code>integer</code></td><td></td></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>target_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>automatic</code></td><td><code>boolean</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
target_version,
execution_controls,
parameters,
target_type,
config_rule_name,
resource_type,
retry_attempt_seconds,
maximum_automatic_attempts,
id,
target_id,
automatic
FROM aws.config.remediation_configuration
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;Id&gt;'
```
