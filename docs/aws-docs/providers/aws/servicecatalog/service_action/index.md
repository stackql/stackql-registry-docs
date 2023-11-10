---
title: service_action
hide_title: false
hide_table_of_contents: false
keywords:
  - service_action
  - servicecatalog
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>service_action</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>service_action</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>service_action</td></tr>
<tr><td><b>Id</b></td><td><code>aws.servicecatalog.service_action</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>accept_language</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>definition_type</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>definition</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
accept_language,
name,
definition_type,
definition,
description,
id
FROM aws.servicecatalog.service_action
WHERE region = 'us-east-1'
AND data__Identifier = '<Id>'
```
