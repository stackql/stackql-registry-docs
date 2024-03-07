---
title: repositories
hide_title: false
hide_table_of_contents: false
keywords:
  - repositories
  - ecr
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>repositories</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>repositories</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>repositories</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.ecr.repositories</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>repository_name</code></td><td><code>string</code></td><td>The name to use for the repository. The repository name may be specified on its own (such as nginx-web-app) or it can be prepended with a namespace to group the repository into a category (such as project-a&#x2F;nginx-web-app). If you don't specify a name, AWS CloudFormation generates a unique physical ID and uses that ID for the repository name. For more information, see https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;AWSCloudFormation&#x2F;latest&#x2F;UserGuide&#x2F;aws-properties-name.html.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
repository_name
FROM awscc.ecr.repositories
WHERE region = 'us-east-1'
```

## Permissions

To operate on the <code>repositories</code> resource, the following permissions are required:

### Create
```json
ecr:CreateRepository,
ecr:PutLifecyclePolicy,
ecr:SetRepositoryPolicy,
ecr:TagResource,
kms:DescribeKey,
kms:CreateGrant,
kms:RetireGrant
```

### List
```json
ecr:DescribeRepositories
```

