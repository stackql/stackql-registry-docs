---
title: repository_link
hide_title: false
hide_table_of_contents: false
keywords:
  - repository_link
  - codestarconnections
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

Gets or operates on an individual <code>repository_link</code> resource, use <code>repository_links</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>repository_link</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Schema for AWS::CodeStarConnections::RepositoryLink resource which is used to aggregate repository metadata relevant to synchronizing source provider content to AWS Resources.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.codestarconnections.repository_link" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="connection_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the CodeStarConnection. The ARN is used as the connection reference when the connection is shared between AWS services.</td></tr>
<tr><td><CopyableCode code="provider_type" /></td><td><code>string</code></td><td>The name of the external provider where your third-party code repository is configured.</td></tr>
<tr><td><CopyableCode code="owner_id" /></td><td><code>string</code></td><td>the ID of the entity that owns the repository.</td></tr>
<tr><td><CopyableCode code="repository_name" /></td><td><code>string</code></td><td>The repository for which the link is being created.</td></tr>
<tr><td><CopyableCode code="encryption_key_arn" /></td><td><code>string</code></td><td>The ARN of the KMS key that the customer can optionally specify to use to encrypt RepositoryLink properties. If not specified, a default key will be used.</td></tr>
<tr><td><CopyableCode code="repository_link_id" /></td><td><code>string</code></td><td>A UUID that uniquely identifies the RepositoryLink.</td></tr>
<tr><td><CopyableCode code="repository_link_arn" /></td><td><code>string</code></td><td>A unique Amazon Resource Name (ARN) to designate the repository link.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>Specifies the tags applied to a RepositoryLink.</td></tr>
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
connection_arn,
provider_type,
owner_id,
repository_name,
encryption_key_arn,
repository_link_id,
repository_link_arn,
tags
FROM aws.codestarconnections.repository_link
WHERE data__Identifier = '<RepositoryLinkArn>';
```

## Permissions

To operate on the <code>repository_link</code> resource, the following permissions are required:

### Update
```json
codestar-connections:GetConnection,
codestar-connections:ListTagsForResource,
codestar-connections:PassConnection,
codestar-connections:UseConnection,
codestar-connections:TagResource,
codestar-connections:UntagResource,
codestar-connections:UpdateRepositoryLink
```

### Read
```json
codestar-connections:GetRepositoryLink,
codestar-connections:ListTagsForResource,
codestar-connections:GetConnection
```

### Delete
```json
codestar-connections:GetRepositoryLink,
codestar-connections:DeleteRepositoryLink,
codestar-connections:GetConnection
```

