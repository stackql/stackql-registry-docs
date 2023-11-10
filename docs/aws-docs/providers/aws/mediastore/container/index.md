---
title: container
hide_title: false
hide_table_of_contents: false
keywords:
  - container
  - mediastore
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>container</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>container</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>container</td></tr>
<tr><td><b>Id</b></td><td><code>aws.mediastore.container</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>policy</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>metric_policy</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>endpoint</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>container_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>cors_policy</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>lifecycle_policy</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>access_logging_enabled</code></td><td><code>boolean</code></td><td></td></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
policy,
metric_policy,
endpoint,
container_name,
cors_policy,
lifecycle_policy,
access_logging_enabled,
id,
tags
FROM aws.mediastore.container
WHERE region = 'us-east-1'
AND data__Identifier = '<Id>'
```
