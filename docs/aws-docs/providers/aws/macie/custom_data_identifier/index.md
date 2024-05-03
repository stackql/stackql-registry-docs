---
title: custom_data_identifier
hide_title: false
hide_table_of_contents: false
keywords:
  - custom_data_identifier
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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';

Gets or operates on an individual <code>custom_data_identifier</code> resource, use <code>custom_data_identifiers</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>custom_data_identifier</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Macie CustomDataIdentifier resource schema</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.macie.custom_data_identifier" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>Name of custom data identifier.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>Description of custom data identifier.</td></tr>
<tr><td><CopyableCode code="regex" /></td><td><code>string</code></td><td>Regular expression for custom data identifier.</td></tr>
<tr><td><CopyableCode code="maximum_match_distance" /></td><td><code>integer</code></td><td>Maximum match distance.</td></tr>
<tr><td><CopyableCode code="keywords" /></td><td><code>array</code></td><td>Keywords to be matched against.</td></tr>
<tr><td><CopyableCode code="ignore_words" /></td><td><code>array</code></td><td>Words to be ignored.</td></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td>Custom data identifier ID.</td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>Custom data identifier ARN.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>A collection of tags associated with a resource</td></tr>
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
name,
description,
regex,
maximum_match_distance,
keywords,
ignore_words,
id,
arn,
tags
FROM aws.macie.custom_data_identifier
WHERE data__Identifier = '<Id>';
```

## Permissions

To operate on the <code>custom_data_identifier</code> resource, the following permissions are required:

### Read
```json
macie2:GetCustomDataIdentifier
```

### Delete
```json
macie2:DeleteCustomDataIdentifier
```

### Update
```json
macie2:TagResource,
macie2:UntagResource
```

