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
<tr><td><b>Description</b></td><td>The ``AWS::ECR::Repository`` resource specifies an Amazon Elastic Container Registry (Amazon ECR) repository, where users can push and pull Docker images, Open Container Initiative (OCI) images, and OCI compatible artifacts. For more information, see &#91;Amazon ECR private repositories&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;AmazonECR&#x2F;latest&#x2F;userguide&#x2F;Repositories.html) in the *Amazon ECR User Guide*.</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ecr.repository</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>empty_on_delete</code></td><td><code>boolean</code></td><td>If true, deleting the repository force deletes the contents of the repository. If false, the repository must be empty before attempting to delete it.</td></tr>
<tr><td><code>lifecycle_policy</code></td><td><code>object</code></td><td>Creates or updates a lifecycle policy. For information about lifecycle policy syntax, see &#91;Lifecycle policy template&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;AmazonECR&#x2F;latest&#x2F;userguide&#x2F;LifecyclePolicies.html).</td></tr>
<tr><td><code>repository_name</code></td><td><code>string</code></td><td>The name to use for the repository. The repository name may be specified on its own (such as ``nginx-web-app``) or it can be prepended with a namespace to group the repository into a category (such as ``project-a&#x2F;nginx-web-app``). If you don't specify a name, CFNlong generates a unique physical ID and uses that ID for the repository name. For more information, see &#91;Name type&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;AWSCloudFormation&#x2F;latest&#x2F;UserGuide&#x2F;aws-properties-name.html).&lt;br&#x2F;&gt; The repository name must start with a letter and can only contain lowercase letters, numbers, hyphens, underscores, and forward slashes.&lt;br&#x2F;&gt;  If you specify a name, you cannot perform updates that require replacement of this resource. You can perform updates that require no or some interruption. If you must replace the resource, specify a new name.</td></tr>
<tr><td><code>repository_policy_text</code></td><td><code>object</code></td><td>The JSON repository policy text to apply to the repository. For more information, see &#91;Amazon ECR repository policies&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;AmazonECR&#x2F;latest&#x2F;userguide&#x2F;repository-policy-examples.html) in the *Amazon Elastic Container Registry User Guide*.</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>repository_uri</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>image_tag_mutability</code></td><td><code>string</code></td><td>The tag mutability setting for the repository. If this parameter is omitted, the default setting of ``MUTABLE`` will be used which will allow image tags to be overwritten. If ``IMMUTABLE`` is specified, all image tags within the repository will be immutable which will prevent them from being overwritten.</td></tr>
<tr><td><code>image_scanning_configuration</code></td><td><code>object</code></td><td>The image scanning configuration for the repository. This determines whether images are scanned for known vulnerabilities after being pushed to the repository.</td></tr>
<tr><td><code>encryption_configuration</code></td><td><code>object</code></td><td>The encryption configuration for the repository. This determines how the contents of your repository are encrypted at rest.</td></tr>
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
FROM aws.ecr.repository
WHERE data__Identifier = '<RepositoryName>';
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

