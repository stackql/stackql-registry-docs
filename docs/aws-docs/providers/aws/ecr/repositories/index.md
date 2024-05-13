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


Used to retrieve a list of <code>repositories</code> in a region or to create or delete a <code>repositories</code> resource, use <code>repository</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>repositories</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The <code>AWS::ECR::Repository</code> resource specifies an Amazon Elastic Container Registry (Amazon ECR) repository, where users can push and pull Docker images, Open Container Initiative (OCI) images, and OCI compatible artifacts. For more information, see &#91;Amazon ECR private repositories&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;AmazonECR&#x2F;latest&#x2F;userguide&#x2F;Repositories.html) in the *Amazon ECR User Guide*.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ecr.repositories" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="repository_name" /></td><td><code>string</code></td><td>The name to use for the repository. The repository name may be specified on its own (such as <code>nginx-web-app</code>) or it can be prepended with a namespace to group the repository into a category (such as <code>project-a&#x2F;nginx-web-app</code>). If you don't specify a name, CFNlong generates a unique physical ID and uses that ID for the repository name. For more information, see &#91;Name type&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;AWSCloudFormation&#x2F;latest&#x2F;UserGuide&#x2F;aws-properties-name.html).&lt;br&#x2F;&gt; The repository name must start with a letter and can only contain lowercase letters, numbers, hyphens, underscores, and forward slashes.&lt;br&#x2F;&gt;  If you specify a name, you cannot perform updates that require replacement of this resource. You can perform updates that require no or some interruption. If you must replace the resource, specify a new name.</td></tr>
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
    <td><CopyableCode code="list_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
repository_name
FROM aws.ecr.repositories
WHERE region = 'us-east-1';
```

## `INSERT` Example

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

## `DELETE` Example

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

### Delete
```json
ecr:DeleteRepository,
kms:RetireGrant
```

### List
```json
ecr:DescribeRepositories
```

