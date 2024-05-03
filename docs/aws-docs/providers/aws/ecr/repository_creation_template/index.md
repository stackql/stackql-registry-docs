---
title: repository_creation_template
hide_title: false
hide_table_of_contents: false
keywords:
  - repository_creation_template
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

Gets or operates on an individual <code>repository_creation_template</code> resource, use <code>repository_creation_templates</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>repository_creation_template</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>AWS::ECR::RepositoryCreationTemplate is used to create repository with configuration from a pre-defined template.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ecr.repository_creation_template" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="prefix" /></td><td><code>string</code></td><td>The prefix use to match the repository name and apply the template.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>The description of the template.</td></tr>
<tr><td><CopyableCode code="image_tag_mutability" /></td><td><code>string</code></td><td>The image tag mutability setting for the repository.</td></tr>
<tr><td><CopyableCode code="repository_policy" /></td><td><code>string</code></td><td>The JSON repository policy text to apply to the repository. For more information, see https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;AmazonECR&#x2F;latest&#x2F;userguide&#x2F;RepositoryPolicyExamples.html</td></tr>
<tr><td><CopyableCode code="lifecycle_policy" /></td><td><code>string</code></td><td>The JSON lifecycle policy text to apply to the repository. For information about lifecycle policy syntax, see https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;AmazonECR&#x2F;latest&#x2F;userguide&#x2F;LifecyclePolicies.html</td></tr>
<tr><td><CopyableCode code="encryption_configuration" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="resource_tags" /></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
<tr><td><CopyableCode code="applied_for" /></td><td><code>array</code></td><td>A list of enumerable Strings representing the repository creation scenarios that the template will apply towards.</td></tr>
<tr><td><CopyableCode code="created_at" /></td><td><code>string</code></td><td>Create timestamp of the template.</td></tr>
<tr><td><CopyableCode code="updated_at" /></td><td><code>string</code></td><td>Update timestamp of the template.</td></tr>
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
prefix,
description,
image_tag_mutability,
repository_policy,
lifecycle_policy,
encryption_configuration,
resource_tags,
applied_for,
created_at,
updated_at
FROM aws.ecr.repository_creation_template
WHERE data__Identifier = '<Prefix>';
```

## Permissions

To operate on the <code>repository_creation_template</code> resource, the following permissions are required:

### Read
```json
ecr:DescribeRepositoryCreationTemplates
```

### Update
```json
ecr:DescribeRepositoryCreationTemplates,
ecr:UpdateRepositoryCreationTemplate,
ecr:PutLifecyclePolicy,
ecr:SetRepositoryPolicy
```

### Delete
```json
ecr:DeleteRepositoryCreationTemplate
```

