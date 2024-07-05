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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes or gets a <code>repository</code> resource or lists <code>repositories</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>repositories</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The <code>AWS::ECR::Repository</code> resource specifies an Amazon Elastic Container Registry (Amazon ECR) repository, where users can push and pull Docker images, Open Container Initiative (OCI) images, and OCI compatible artifacts. For more information, see &#91;Amazon ECR private repositories&#93;(https://docs.aws.amazon.com/AmazonECR/latest/userguide/Repositories.html) in the *Amazon ECR User Guide*.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ecr.repositories" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="empty_on_delete" /></td><td><code>boolean</code></td><td>If true, deleting the repository force deletes the contents of the repository. If false, the repository must be empty before attempting to delete it.</td></tr>
<tr><td><CopyableCode code="lifecycle_policy" /></td><td><code>object</code></td><td>Creates or updates a lifecycle policy. For information about lifecycle policy syntax, see &#91;Lifecycle policy template&#93;(https://docs.aws.amazon.com/AmazonECR/latest/userguide/LifecyclePolicies.html).</td></tr>
<tr><td><CopyableCode code="repository_name" /></td><td><code>string</code></td><td>The name to use for the repository. The repository name may be specified on its own (such as <code>nginx-web-app</code>) or it can be prepended with a namespace to group the repository into a category (such as <code>project-a/nginx-web-app</code>). If you don't specify a name, CFNlong generates a unique physical ID and uses that ID for the repository name. For more information, see &#91;Name type&#93;(https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-name.html).<br />The repository name must start with a letter and can only contain lowercase letters, numbers, hyphens, underscores, and forward slashes.<br />If you specify a name, you cannot perform updates that require replacement of this resource. You can perform updates that require no or some interruption. If you must replace the resource, specify a new name.</td></tr>
<tr><td><CopyableCode code="repository_policy_text" /></td><td><code>object</code></td><td>The JSON repository policy text to apply to the repository. For more information, see &#91;Amazon ECR repository policies&#93;(https://docs.aws.amazon.com/AmazonECR/latest/userguide/repository-policy-examples.html) in the *Amazon Elastic Container Registry User Guide*.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="repository_uri" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="image_tag_mutability" /></td><td><code>string</code></td><td>The tag mutability setting for the repository. If this parameter is omitted, the default setting of <code>MUTABLE</code> will be used which will allow image tags to be overwritten. If <code>IMMUTABLE</code> is specified, all image tags within the repository will be immutable which will prevent them from being overwritten.</td></tr>
<tr><td><CopyableCode code="image_scanning_configuration" /></td><td><code>object</code></td><td>The image scanning configuration for the repository. This determines whether images are scanned for known vulnerabilities after being pushed to the repository.</td></tr>
<tr><td><CopyableCode code="encryption_configuration" /></td><td><code>object</code></td><td>The encryption configuration for the repository. This determines how the contents of your repository are encrypted at rest.</td></tr>
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
    <td><CopyableCode code="create_resource" /></td>
    <td><code>INSERT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="update_resource" /></td>
    <td><code>UPDATE</code></td>
    <td><CopyableCode code="data__Identifier, data__PatchDocument, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="list_resources" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples
Gets all <code>repositories</code> in a region.
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
FROM aws.ecr.repositories
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>repository</code>.
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
FROM aws.ecr.repositories
WHERE region = 'us-east-1' AND data__Identifier = '<RepositoryName>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>repository</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

<Tabs
    defaultValue="required"
    values={[
      { label: 'Required Properties', value: 'required', },
      { label: 'All Properties', value: 'all', },
      { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="required">

```sql
/*+ create */
INSERT INTO aws.ecr.repositories (
 EmptyOnDelete,
 LifecyclePolicy,
 RepositoryName,
 RepositoryPolicyText,
 Tags,
 ImageTagMutability,
 ImageScanningConfiguration,
 EncryptionConfiguration,
 region
)
SELECT 
'{{ EmptyOnDelete }}',
 '{{ LifecyclePolicy }}',
 '{{ RepositoryName }}',
 '{{ RepositoryPolicyText }}',
 '{{ Tags }}',
 '{{ ImageTagMutability }}',
 '{{ ImageScanningConfiguration }}',
 '{{ EncryptionConfiguration }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.ecr.repositories (
 EmptyOnDelete,
 LifecyclePolicy,
 RepositoryName,
 RepositoryPolicyText,
 Tags,
 ImageTagMutability,
 ImageScanningConfiguration,
 EncryptionConfiguration,
 region
)
SELECT 
 '{{ EmptyOnDelete }}',
 '{{ LifecyclePolicy }}',
 '{{ RepositoryName }}',
 '{{ RepositoryPolicyText }}',
 '{{ Tags }}',
 '{{ ImageTagMutability }}',
 '{{ ImageScanningConfiguration }}',
 '{{ EncryptionConfiguration }}',
 '{{ region }}';
```
</TabItem>
<TabItem value="manifest">

```yaml
version: 1
name: stack name
description: stack description
providers:
  - aws
globals:
  - name: region
    value: '{{ vars.AWS_REGION }}'
resources:
  - name: repository
    props:
      - name: EmptyOnDelete
        value: '{{ EmptyOnDelete }}'
      - name: LifecyclePolicy
        value:
          LifecyclePolicyText: '{{ LifecyclePolicyText }}'
          RegistryId: '{{ RegistryId }}'
      - name: RepositoryName
        value: '{{ RepositoryName }}'
      - name: RepositoryPolicyText
        value: {}
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'
      - name: ImageTagMutability
        value: '{{ ImageTagMutability }}'
      - name: ImageScanningConfiguration
        value:
          ScanOnPush: '{{ ScanOnPush }}'
      - name: EncryptionConfiguration
        value:
          EncryptionType: '{{ EncryptionType }}'
          KmsKey: '{{ KmsKey }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.ecr.repositories
WHERE data__Identifier = '<RepositoryName>'
AND region = 'us-east-1';
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

### List
```json
ecr:DescribeRepositories
```

