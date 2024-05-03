---
title: project
hide_title: false
hide_table_of_contents: false
keywords:
  - project
  - sagemaker
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

Gets or operates on an individual <code>project</code> resource, use <code>projects</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>project</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::SageMaker::Project</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.sagemaker.project" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
<tr><td><CopyableCode code="project_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="project_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="project_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="project_description" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="creation_time" /></td><td><code>string</code></td><td>The time at which the project was created.</td></tr>
<tr><td><CopyableCode code="service_catalog_provisioning_details" /></td><td><code>object</code></td><td>Input ServiceCatalog Provisioning Details</td></tr>
<tr><td><CopyableCode code="service_catalog_provisioned_product_details" /></td><td><code>object</code></td><td>Provisioned ServiceCatalog  Details</td></tr>
<tr><td><CopyableCode code="project_status" /></td><td><code>string</code></td><td>The status of a project.</td></tr>
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
tags,
project_arn,
project_id,
project_name,
project_description,
creation_time,
service_catalog_provisioning_details,
service_catalog_provisioned_product_details,
project_status
FROM aws.sagemaker.project
WHERE data__Identifier = '<ProjectArn>';
```

## Permissions

To operate on the <code>project</code> resource, the following permissions are required:

### Read
```json
sagemaker:DescribeProject,
sagemaker:ListTags
```

### Update
```json
sagemaker:DescribeProject,
sagemaker:ListTags,
sagemaker:AddTags,
sagemaker:DeleteTags
```

### Delete
```json
sagemaker:DeleteProject,
sagemaker:DescribeProject,
servicecatalog:TerminateProvisionedProduct,
servicecatalog:DescribeRecord
```

