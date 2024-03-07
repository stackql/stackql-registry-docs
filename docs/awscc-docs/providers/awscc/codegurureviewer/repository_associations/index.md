---
title: repository_associations
hide_title: false
hide_table_of_contents: false
keywords:
  - repository_associations
  - codegurureviewer
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>repository_associations</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>repository_associations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>repository_associations</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.codegurureviewer.repository_associations</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>association_arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the repository association.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
association_arn
FROM awscc.codegurureviewer.repository_associations
WHERE region = 'us-east-1'
```

## Permissions

To operate on the <code>repository_associations</code> resource, the following permissions are required:

### Create
```json
codeguru-reviewer:DescribeRepositoryAssociation,
codeguru-reviewer:AssociateRepository,
codeguru-reviewer:TagResource,
iam:CreateServiceLinkedRole,
codecommit:TagResource,
codecommit:GitPull,
codecommit:TagResource,
events:PutRule,
events:PutTargets,
codestar-connections:ListBranches,
codestar-connections:ListRepositories,
codestar-connections:ListTagsForResource,
codestar-connections:PassConnection,
codestar-connections:TagResource,
codestar-connections:UseConnection,
s3:ListBucket
```

### List
```json
codeguru-reviewer:ListRepositoryAssociations
```

