---
title: package_group
hide_title: false
hide_table_of_contents: false
keywords:
  - package_group
  - codeartifact
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>package_group</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>package_group</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The resource schema to create a CodeArtifact package group.</td></tr>
<tr><td><b>Id</b></td><td><code>aws.codeartifact.package_group</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>domain_name</code></td><td><code>string</code></td><td>The name of the domain that contains the package group.</td></tr>
<tr><td><code>domain_owner</code></td><td><code>string</code></td><td>The 12-digit account ID of the AWS account that owns the domain.</td></tr>
<tr><td><code>pattern</code></td><td><code>string</code></td><td>The package group pattern that is used to gather packages.</td></tr>
<tr><td><code>contact_info</code></td><td><code>string</code></td><td>The contact info of the package group.</td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td>The text description of the package group.</td></tr>
<tr><td><code>origin_configuration</code></td><td><code>object</code></td><td>The package origin configuration of the package group.</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>An array of key-value pairs to apply to the package group.</td></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td>The ARN of the package group.</td></tr>
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
domain_name,
domain_owner,
pattern,
contact_info,
description,
origin_configuration,
tags,
arn
FROM aws.codeartifact.package_group
WHERE data__Identifier = '<Arn>';
```

## Permissions

To operate on the <code>package_group</code> resource, the following permissions are required:

### Read
```json
codeartifact:DescribePackageGroup,
codeartifact:ListAllowedRepositoriesForGroup,
codeartifact:ListTagsForResource
```

### Update
```json
codeartifact:UpdatePackageGroup,
codeartifact:UpdatePackageGroupOriginConfiguration,
codeartifact:DescribePackageGroup,
codeartifact:ListAllowedRepositoriesForGroup,
codeartifact:ListTagsForResource,
codeartifact:TagResource,
codeartifact:UntagResource
```

### Delete
```json
codeartifact:DeletePackageGroup,
codeartifact:DescribePackageGroup
```

