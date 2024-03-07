---
title: hook_type_config
hide_title: false
hide_table_of_contents: false
keywords:
  - hook_type_config
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
Gets an individual <code>hook_type_config</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>hook_type_config</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>hook_type_config</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.cloudformation.hook_type_config</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>type_arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the type without version number.</td></tr>
<tr><td><code>type_name</code></td><td><code>string</code></td><td>The name of the type being registered.&lt;br&#x2F;&gt;&lt;br&#x2F;&gt;We recommend that type names adhere to the following pattern: company_or_organization::service::type.</td></tr>
<tr><td><code>configuration_arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) for the configuration data, in this account and region.</td></tr>
<tr><td><code>configuration</code></td><td><code>string</code></td><td>The configuration data for the extension, in this account and region.</td></tr>
<tr><td><code>configuration_alias</code></td><td><code>string</code></td><td>An alias by which to refer to this extension configuration data.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
type_arn,
type_name,
configuration_arn,
configuration,
configuration_alias
FROM awscc.cloudformation.hook_type_config
WHERE region = 'us-east-1'
AND data__Identifier = '{ConfigurationArn}';
```

## Permissions

To operate on the <code>hook_type_config</code> resource, the following permissions are required:

### Read
```json
cloudformation:BatchDescribeTypeConfigurations
```

### Update
```json
cloudformation:SetTypeConfiguration
```

### Delete
```json
cloudformation:SetTypeConfiguration
```

