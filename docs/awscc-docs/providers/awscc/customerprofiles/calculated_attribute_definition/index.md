---
title: calculated_attribute_definition
hide_title: false
hide_table_of_contents: false
keywords:
  - calculated_attribute_definition
  - customerprofiles
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>calculated_attribute_definition</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>calculated_attribute_definition</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>calculated_attribute_definition</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.customerprofiles.calculated_attribute_definition</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>domain_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>calculated_attribute_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>display_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>attribute_details</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>conditions</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>statistic</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>created_at</code></td><td><code>string</code></td><td>The timestamp of when the calculated attribute definition was created.</td></tr>
<tr><td><code>last_updated_at</code></td><td><code>string</code></td><td>The timestamp of when the calculated attribute definition was most recently edited.</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
domain_name,
calculated_attribute_name,
display_name,
description,
attribute_details,
conditions,
statistic,
created_at,
last_updated_at,
tags
FROM awscc.customerprofiles.calculated_attribute_definition
WHERE data__Identifier = '<DomainName>|<CalculatedAttributeName>';
```

## Permissions

To operate on the <code>calculated_attribute_definition</code> resource, the following permissions are required:

### Read
```json
profile:GetCalculatedAttributeDefinition
```

### Update
```json
profile:GetCalculatedAttributeDefinition,
profile:UpdateCalculatedAttributeDefinition,
profile:UntagResource,
profile:TagResource
```

### Delete
```json
profile:DeleteCalculatedAttributeDefinition
```

