---
title: repository
hide_title: false
hide_table_of_contents: false
keywords:
  - repository
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
Gets an individual <code>repository</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>repository</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>repository</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.ecr.repository</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>empty_on_delete</code></td><td><code>boolean</code></td><td></td></tr>
<tr><td><code>lifecycle_policy</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>repository_name</code></td><td><code>string</code></td><td>The name to use for the repository. The repository name may be specified on its own (such as nginx-web-app) or it can be prepended with a namespace to group the repository into a category (such as project-a&#x2F;nginx-web-app). If you don't specify a name, AWS CloudFormation generates a unique physical ID and uses that ID for the repository name. For more information, see https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;AWSCloudFormation&#x2F;latest&#x2F;UserGuide&#x2F;aws-properties-name.html.</td></tr>
<tr><td><code>repository_policy_text</code></td><td><code>object</code></td><td>The JSON repository policy text to apply to the repository. For more information, see https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;AmazonECR&#x2F;latest&#x2F;userguide&#x2F;RepositoryPolicyExamples.html in the Amazon Elastic Container Registry User Guide. </td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>repository_uri</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>image_tag_mutability</code></td><td><code>string</code></td><td>The image tag mutability setting for the repository.</td></tr>
<tr><td><code>image_scanning_configuration</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>encryption_configuration</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
empty_on_delete,
lifecycle_policy,
repository_name,
repository_policy_text,
tags,
arn,
repository_uri,
image_tag_mutability,
image_scanning_configuration,
encryption_configuration
FROM awscc.ecr.repository
WHERE region = 'us-east-1'
AND data__Identifier = '{RepositoryName}';
```

## Permissions

To operate on the <code>repository</code> resource, the following permissions are required:

### Read
```json
ecr:DescribeRepositories,
ecr:GetLifecyclePolicy,
ecr:GetRepositoryPolicy,
ecr:ListTagsForResource
```

### Update
```json
ecr:DescribeRepositories,
ecr:PutLifecyclePolicy,
ecr:SetRepositoryPolicy,
ecr:ListTagsForResource,
ecr:TagResource,
ecr:UntagResource,
ecr:DeleteLifecyclePolicy,
ecr:DeleteRepositoryPolicy,
ecr:PutImageScanningConfiguration,
ecr:PutImageTagMutability,
kms:DescribeKey,
kms:CreateGrant,
kms:RetireGrant
```

### Delete
```json
ecr:DeleteRepository,
kms:RetireGrant
```

