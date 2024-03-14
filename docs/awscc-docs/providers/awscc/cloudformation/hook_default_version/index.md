---
title: hook_default_version
hide_title: false
hide_table_of_contents: false
keywords:
  - hook_default_version
  - cloudformation
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>hook_default_version</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>hook_default_version</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>hook_default_version</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.cloudformation.hook_default_version</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>type_version_arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the type version.</td></tr>
<tr><td><code>type_name</code></td><td><code>string</code></td><td>The name of the type being registered.&lt;br&#x2F;&gt;&lt;br&#x2F;&gt;We recommend that type names adhere to the following pattern: company_or_organization::service::type.</td></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the type. This is used to uniquely identify a HookDefaultVersion</td></tr>
<tr><td><code>version_id</code></td><td><code>string</code></td><td>The ID of an existing version of the hook to set as the default.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
type_version_arn,
type_name,
arn,
version_id
FROM awscc.cloudformation.hook_default_version
WHERE data__Identifier = '<Arn>';
```

## Permissions

To operate on the <code>hook_default_version</code> resource, the following permissions are required:

### Read
```json
cloudformation:DescribeType
```

### Update
```json
cloudformation:SetTypeDefaultVersion
```

