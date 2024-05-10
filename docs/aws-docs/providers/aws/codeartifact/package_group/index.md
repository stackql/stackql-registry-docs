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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';


Gets or updates an individual <code>package_group</code> resource, use <code>package_groups</code> to retrieve a list of resources or to create or delete a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>package_group</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The resource schema to create a CodeArtifact package group.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.codeartifact.package_group" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="domain_name" /></td><td><code>string</code></td><td>The name of the domain that contains the package group.</td></tr>
<tr><td><CopyableCode code="domain_owner" /></td><td><code>string</code></td><td>The 12-digit account ID of the AWS account that owns the domain.</td></tr>
<tr><td><CopyableCode code="pattern" /></td><td><code>string</code></td><td>The package group pattern that is used to gather packages.</td></tr>
<tr><td><CopyableCode code="contact_info" /></td><td><code>string</code></td><td>The contact info of the package group.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>The text description of the package group.</td></tr>
<tr><td><CopyableCode code="origin_configuration" /></td><td><code>object</code></td><td>The package origin configuration of the package group.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>An array of key-value pairs to apply to the package group.</td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The ARN of the package group.</td></tr>
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
domain_owner,
pattern,
contact_info,
description,
origin_configuration,
tags,
arn
FROM aws.codeartifact.package_group
WHERE region = 'us-east-1' AND data__Identifier = '<Arn>';
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

