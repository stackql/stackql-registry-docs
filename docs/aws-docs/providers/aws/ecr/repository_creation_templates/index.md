---
title: repository_creation_templates
hide_title: false
hide_table_of_contents: false
keywords:
  - repository_creation_templates
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

Creates, updates, deletes or gets a <code>repository_creation_template</code> resource or lists <code>repository_creation_templates</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>repository_creation_templates</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>AWS::ECR::RepositoryCreationTemplate is used to create repository with configuration from a pre-defined template.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ecr.repository_creation_templates" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="prefix" /></td><td><code>string</code></td><td>The prefix use to match the repository name and apply the template.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>The description of the template.</td></tr>
<tr><td><CopyableCode code="image_tag_mutability" /></td><td><code>string</code></td><td>The image tag mutability setting for the repository.</td></tr>
<tr><td><CopyableCode code="repository_policy" /></td><td><code>string</code></td><td>The JSON repository policy text to apply to the repository. For more information, see https://docs.aws.amazon.com/AmazonECR/latest/userguide/RepositoryPolicyExamples.html</td></tr>
<tr><td><CopyableCode code="lifecycle_policy" /></td><td><code>string</code></td><td>The JSON lifecycle policy text to apply to the repository. For information about lifecycle policy syntax, see https://docs.aws.amazon.com/AmazonECR/latest/userguide/LifecyclePolicies.html</td></tr>
<tr><td><CopyableCode code="encryption_configuration" /></td><td><code>object</code></td><td>The encryption configuration for the repository. This determines how the contents of your repository are encrypted at rest. By default, when no encryption configuration is set or the AES256 encryption type is used, Amazon ECR uses server-side encryption with Amazon S3-managed encryption keys which encrypts your data at rest using an AES-256 encryption algorithm. This does not require any action on your part.<br />For more information, see https://docs.aws.amazon.com/AmazonECR/latest/userguide/encryption-at-rest.html</td></tr>
<tr><td><CopyableCode code="resource_tags" /></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
<tr><td><CopyableCode code="applied_for" /></td><td><code>array</code></td><td>A list of enumerable Strings representing the repository creation scenarios that the template will apply towards.</td></tr>
<tr><td><CopyableCode code="custom_role_arn" /></td><td><code>string</code></td><td>The ARN of the role to be assumed by ECR. This role must be in the same account as the registry that you are configuring.</td></tr>
<tr><td><CopyableCode code="created_at" /></td><td><code>string</code></td><td>Create timestamp of the template.</td></tr>
<tr><td><CopyableCode code="updated_at" /></td><td><code>string</code></td><td>Update timestamp of the template.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecr-repositorycreationtemplate.html"><code>AWS::ECR::RepositoryCreationTemplate</code></a>.

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
    <td><CopyableCode code="Prefix, AppliedFor, region" /></td>
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
Gets all <code>repository_creation_templates</code> in a region.
```sql
SELECT
region,
prefix,
description,
image_tag_mutability,
repository_policy,
lifecycle_policy,
encryption_configuration,
resource_tags,
applied_for,
custom_role_arn,
created_at,
updated_at
FROM aws.ecr.repository_creation_templates
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>repository_creation_template</code>.
```sql
SELECT
region,
prefix,
description,
image_tag_mutability,
repository_policy,
lifecycle_policy,
encryption_configuration,
resource_tags,
applied_for,
custom_role_arn,
created_at,
updated_at
FROM aws.ecr.repository_creation_templates
WHERE region = 'us-east-1' AND data__Identifier = '<Prefix>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>repository_creation_template</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.ecr.repository_creation_templates (
 Prefix,
 AppliedFor,
 region
)
SELECT 
'{{ Prefix }}',
 '{{ AppliedFor }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.ecr.repository_creation_templates (
 Prefix,
 Description,
 ImageTagMutability,
 RepositoryPolicy,
 LifecyclePolicy,
 EncryptionConfiguration,
 ResourceTags,
 AppliedFor,
 CustomRoleArn,
 region
)
SELECT 
 '{{ Prefix }}',
 '{{ Description }}',
 '{{ ImageTagMutability }}',
 '{{ RepositoryPolicy }}',
 '{{ LifecyclePolicy }}',
 '{{ EncryptionConfiguration }}',
 '{{ ResourceTags }}',
 '{{ AppliedFor }}',
 '{{ CustomRoleArn }}',
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
  - name: repository_creation_template
    props:
      - name: Prefix
        value: '{{ Prefix }}'
      - name: Description
        value: '{{ Description }}'
      - name: ImageTagMutability
        value: '{{ ImageTagMutability }}'
      - name: RepositoryPolicy
        value: '{{ RepositoryPolicy }}'
      - name: LifecyclePolicy
        value: '{{ LifecyclePolicy }}'
      - name: EncryptionConfiguration
        value:
          EncryptionType: '{{ EncryptionType }}'
          KmsKey: '{{ KmsKey }}'
      - name: ResourceTags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'
      - name: AppliedFor
        value:
          - '{{ AppliedFor[0] }}'
      - name: CustomRoleArn
        value: '{{ CustomRoleArn }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.ecr.repository_creation_templates
WHERE data__Identifier = '<Prefix>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>repository_creation_templates</code> resource, the following permissions are required:

### Create
```json
ecr:CreateRepositoryCreationTemplate,
ecr:PutLifecyclePolicy,
ecr:SetRepositoryPolicy,
ecr:CreateRepository,
iam:CreateServiceLinkedRole,
iam:PassRole
```

### Read
```json
ecr:DescribeRepositoryCreationTemplates
```

### Update
```json
ecr:DescribeRepositoryCreationTemplates,
ecr:UpdateRepositoryCreationTemplate,
ecr:PutLifecyclePolicy,
ecr:SetRepositoryPolicy,
ecr:CreateRepository,
iam:CreateServiceLinkedRole,
iam:PassRole
```

### Delete
```json
ecr:DeleteRepositoryCreationTemplate
```

### List
```json
ecr:DescribeRepositoryCreationTemplates
```
