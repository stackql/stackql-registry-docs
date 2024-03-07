---
title: custom_data_identifiers
hide_title: false
hide_table_of_contents: false
keywords:
  - custom_data_identifiers
  - macie
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>custom_data_identifiers</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>custom_data_identifiers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>custom_data_identifiers</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.macie.custom_data_identifiers</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td>Custom data identifier ID.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
id
FROM awscc.macie.custom_data_identifiers
WHERE region = 'us-east-1'
```

## Permissions

To operate on the <code>custom_data_identifiers</code> resource, the following permissions are required:

### Create
```json
macie2:CreateCustomDataIdentifier,
macie2:GetCustomDataIdentifier,
macie2:TagResource
```

### List
```json
macie2:ListCustomDataIdentifiers
```

