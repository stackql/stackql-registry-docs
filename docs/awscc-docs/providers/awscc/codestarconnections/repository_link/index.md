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
Gets an individual <code>repository_link</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>repository_link</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>repository_link</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.codestarconnections.repository_link</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>connection_arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the CodeStarConnection. The ARN is used as the connection reference when the connection is shared between AWS services.</td></tr>
<tr><td><code>provider_type</code></td><td><code>string</code></td><td>The name of the external provider where your third-party code repository is configured.</td></tr>
<tr><td><code>owner_id</code></td><td><code>string</code></td><td>the ID of the entity that owns the repository.</td></tr>
<tr><td><code>repository_name</code></td><td><code>string</code></td><td>The repository for which the link is being created.</td></tr>
<tr><td><code>encryption_key_arn</code></td><td><code>string</code></td><td>The ARN of the KMS key that the customer can optionally specify to use to encrypt RepositoryLink properties. If not specified, a default key will be used.</td></tr>
<tr><td><code>repository_link_id</code></td><td><code>string</code></td><td>A UUID that uniquely identifies the RepositoryLink.</td></tr>
<tr><td><code>repository_link_arn</code></td><td><code>string</code></td><td>A unique Amazon Resource Name (ARN) to designate the repository link.</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>Specifies the tags applied to a RepositoryLink.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
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
FROM awscc.codestarconnections.repository_link
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

