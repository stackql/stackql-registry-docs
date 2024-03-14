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
Gets an individual <code>project</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>project</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>project</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.sagemaker.project</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
<tr><td><code>project_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>project_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>project_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>project_description</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>creation_time</code></td><td><code>string</code></td><td>The time at which the project was created.</td></tr>
<tr><td><code>service_catalog_provisioning_details</code></td><td><code>object</code></td><td>Input ServiceCatalog Provisioning Details</td></tr>
<tr><td><code>service_catalog_provisioned_product_details</code></td><td><code>object</code></td><td>Provisioned ServiceCatalog  Details</td></tr>
<tr><td><code>project_status</code></td><td><code>string</code></td><td>The status of a project.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
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
FROM awscc.sagemaker.project
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

