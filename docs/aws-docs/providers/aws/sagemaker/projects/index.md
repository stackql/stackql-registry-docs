---
title: projects
hide_title: false
hide_table_of_contents: false
keywords:
  - projects
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
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes or gets a <code>project</code> resource or lists <code>projects</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>projects</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::SageMaker::Project</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.sagemaker.projects" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
<tr><td><CopyableCode code="project_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the Project.</td></tr>
<tr><td><CopyableCode code="project_id" /></td><td><code>string</code></td><td>Project Id.</td></tr>
<tr><td><CopyableCode code="project_name" /></td><td><code>string</code></td><td>The name of the project.</td></tr>
<tr><td><CopyableCode code="project_description" /></td><td><code>string</code></td><td>The description of the project.</td></tr>
<tr><td><CopyableCode code="creation_time" /></td><td><code>string</code></td><td>The time at which the project was created.</td></tr>
<tr><td><CopyableCode code="service_catalog_provisioning_details" /></td><td><code>object</code></td><td>Input ServiceCatalog Provisioning Details</td></tr>
<tr><td><CopyableCode code="service_catalog_provisioned_product_details" /></td><td><code>object</code></td><td>Provisioned ServiceCatalog Details</td></tr>
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
    <td><CopyableCode code="create_resource" /></td>
    <td><code>INSERT</code></td>
    <td><CopyableCode code="ProjectName, ServiceCatalogProvisioningDetails, region" /></td>
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
Gets all <code>projects</code> in a region.
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
FROM aws.sagemaker.projects
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>project</code>.
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
FROM aws.sagemaker.projects
WHERE region = 'us-east-1' AND data__Identifier = '<ProjectArn>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>project</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.sagemaker.projects (
 ProjectName,
 ServiceCatalogProvisioningDetails,
 region
)
SELECT 
'{{ ProjectName }}',
 '{{ ServiceCatalogProvisioningDetails }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.sagemaker.projects (
 Tags,
 ProjectName,
 ProjectDescription,
 ServiceCatalogProvisioningDetails,
 ServiceCatalogProvisionedProductDetails,
 region
)
SELECT 
 '{{ Tags }}',
 '{{ ProjectName }}',
 '{{ ProjectDescription }}',
 '{{ ServiceCatalogProvisioningDetails }}',
 '{{ ServiceCatalogProvisionedProductDetails }}',
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
  - name: project
    props:
      - name: Tags
        value:
          - Value: '{{ Value }}'
            Key: '{{ Key }}'
      - name: ProjectName
        value: '{{ ProjectName }}'
      - name: ProjectDescription
        value: '{{ ProjectDescription }}'
      - name: ServiceCatalogProvisioningDetails
        value:
          ProductId: '{{ ProductId }}'
          ProvisioningArtifactId: '{{ ProvisioningArtifactId }}'
          PathId: '{{ PathId }}'
          ProvisioningParameters:
            - Key: '{{ Key }}'
              Value: '{{ Value }}'
      - name: ServiceCatalogProvisionedProductDetails
        value:
          ProvisionedProductId: null
          ProvisionedProductStatusMessage: '{{ ProvisionedProductStatusMessage }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.sagemaker.projects
WHERE data__Identifier = '<ProjectArn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>projects</code> resource, the following permissions are required:

### Create
```json
sagemaker:AddTags,
sagemaker:CreateProject,
sagemaker:DescribeProject,
sagemaker:ListTags,
servicecatalog:DescribeProduct,
servicecatalog:DescribeProvisioningArtifact,
servicecatalog:ProvisionProduct,
servicecatalog:DescribeProvisionedProduct,
servicecatalog:TerminateProvisionedProduct
```

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

### List
```json
sagemaker:ListProjects
```

