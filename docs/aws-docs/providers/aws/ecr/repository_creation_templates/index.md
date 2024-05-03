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

Used to retrieve a list of <code>repository_creation_templates</code> in a region or create a <code>repository_creation_templates</code> resource, use <code>repository_creation_template</code> to operate on an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>repository_creation_templates</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>AWS::ECR::RepositoryCreationTemplate is used to create repository with configuration from a pre-defined template.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ecr.repository_creation_templates" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="prefix" /></td><td><code>string</code></td><td>The prefix use to match the repository name and apply the template.</td></tr>
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
    <td><CopyableCode code="data__DesiredState, region" /></td>
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
prefix
FROM aws.ecr.repository_creation_templates
WHERE region = 'us-east-1'
```

## Permissions

To operate on the <code>repository_creation_templates</code> resource, the following permissions are required:

### Create
```json
ecr:CreateRepositoryCreationTemplate,
ecr:PutLifecyclePolicy,
ecr:SetRepositoryPolicy
```

### List
```json
ecr:DescribeRepositoryCreationTemplates
```
