---
title: registry_policy
hide_title: false
hide_table_of_contents: false
keywords:
  - registry_policy
  - eventschemas
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

Gets or operates on an individual <code>registry_policy</code> resource, use <code>registry_policies</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>registry_policy</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::EventSchemas::RegistryPolicy</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.eventschemas.registry_policy" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="policy" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="registry_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="revision_id" /></td><td><code>string</code></td><td></td></tr>
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
id,
policy,
registry_name,
revision_id
FROM aws.eventschemas.registry_policy
WHERE data__Identifier = '<Id>';
```

## Permissions

To operate on the <code>registry_policy</code> resource, the following permissions are required:

### Delete
```json
schemas:DeleteResourcePolicy,
schemas:GetResourcePolicy
```

### Update
```json
schemas:PutResourcePolicy,
schemas:GetResourcePolicy
```

### Read
```json
schemas:GetResourcePolicy
```

