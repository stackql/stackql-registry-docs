---
title: repository_association
hide_title: false
hide_table_of_contents: false
keywords:
  - repository_association
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
Gets an individual <code>repository_association</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>repository_association</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>repository_association</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.codegurureviewer.repository_association</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td>Name of the repository to be associated.</td></tr>
<tr><td><code>type</code></td><td><code>string</code></td><td>The type of repository to be associated.</td></tr>
<tr><td><code>owner</code></td><td><code>string</code></td><td>The owner of the repository. For a Bitbucket repository, this is the username for the account that owns the repository.</td></tr>
<tr><td><code>bucket_name</code></td><td><code>string</code></td><td>The name of the S3 bucket associated with an associated S3 repository. It must start with `codeguru-reviewer-`.</td></tr>
<tr><td><code>connection_arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of an AWS CodeStar Connections connection.</td></tr>
<tr><td><code>association_arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the repository association.</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>The tags associated with a repository association.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>repository_association</code> resource, the following permissions are required:

### Read
```json
codeguru-reviewer:DescribeRepositoryAssociation,
codeguru-reviewer:ListTagsForResource
```

### Delete
```json
codeguru-reviewer:DescribeRepositoryAssociation,
codeguru-reviewer:DisassociateRepository,
codecommit:UntagResource,
events:DeleteRule,
events:RemoveTargets,
codestar-connections:UntagResource,
codestar-connections:ListTagsForResource
```


## Example
```sql
SELECT
region,
name,
type,
owner,
bucket_name,
connection_arn,
association_arn,
tags
FROM awscc.codegurureviewer.repository_association
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;AssociationArn&gt;'
```
