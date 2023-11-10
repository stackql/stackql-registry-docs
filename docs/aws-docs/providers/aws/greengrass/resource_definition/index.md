---
title: resource_definition
hide_title: false
hide_table_of_contents: false
keywords:
  - resource_definition
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
Gets an individual <code>resource_definition</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>resource_definition</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>resource_definition</td></tr>
<tr><td><b>Id</b></td><td><code>aws.greengrass.resource_definition</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>latest_version_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>initial_version</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
id,
arn,
latest_version_arn,
tags,
name,
initial_version
FROM aws.greengrass.resource_definition
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;Id&gt;'
```
