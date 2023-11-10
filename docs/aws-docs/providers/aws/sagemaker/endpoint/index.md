---
title: endpoint
hide_title: false
hide_table_of_contents: false
keywords:
  - endpoint
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
Gets an individual <code>endpoint</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>endpoint</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>endpoint</td></tr>
<tr><td><b>Id</b></td><td><code>aws.sagemaker.endpoint</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>retain_all_variant_properties</code></td><td><code>boolean</code></td><td></td></tr>
<tr><td><code>endpoint_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>exclude_retained_variant_properties</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>endpoint_config_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>deployment_config</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>retain_deployment_config</code></td><td><code>boolean</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
retain_all_variant_properties,
endpoint_name,
exclude_retained_variant_properties,
endpoint_config_name,
id,
deployment_config,
retain_deployment_config,
tags
FROM aws.sagemaker.endpoint
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;Id&gt;'
```
