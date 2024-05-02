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
Gets or operates on an individual <code>hook_type_config</code> resource, use <code>hook_type_configs</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>hook_type_config</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Specifies the configuration data for a registered hook in CloudFormation Registry.</td></tr>
<tr><td><b>Id</b></td><td><code>aws.cloudformation.hook_type_config</code></td></tr>
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

<table><tbody>
  <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
  </tr>
  <tr>
    <td><code>update_resource</code></td>
    <td><code>UPDATE</code></td>
    <td><code>data__Identifier, data__PatchDocument, region</code></td>
  </tr>
  <tr>
    <td><code>delete_resource</code></td>
    <td><code>DELETE</code></td>
    <td><code>data__Identifier, region</code></td>
  </tr>
  <tr>
    <td><code>get_resource</code></td>
    <td><code>SELECT</code></td>
    <td><code>data__Identifier, region</code></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
type_arn,
type_name,
configuration_arn,
configuration,
configuration_alias
FROM aws.cloudformation.hook_type_config
WHERE data__Identifier = '<ConfigurationArn>';
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

