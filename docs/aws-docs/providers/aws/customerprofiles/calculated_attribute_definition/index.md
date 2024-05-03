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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';

Gets or operates on an individual <code>calculated_attribute_definition</code> resource, use <code>calculated_attribute_definitions</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>calculated_attribute_definition</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>A calculated attribute definition for Customer Profiles</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.customerprofiles.calculated_attribute_definition" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="domain_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="calculated_attribute_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="display_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="attribute_details" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="conditions" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="statistic" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="created_at" /></td><td><code>string</code></td><td>The timestamp of when the calculated attribute definition was created.</td></tr>
<tr><td><CopyableCode code="last_updated_at" /></td><td><code>string</code></td><td>The timestamp of when the calculated attribute definition was most recently edited.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods

<table><tbody>
  <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
  </tr>
  <tr>
    <td><CopyableCode code="update_resource" /></td>
    <td><code>UPDATE</code></td>
    <td><CopyableCode code="data__Identifier, data__PatchDocument, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
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
FROM aws.customerprofiles.calculated_attribute_definition
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

