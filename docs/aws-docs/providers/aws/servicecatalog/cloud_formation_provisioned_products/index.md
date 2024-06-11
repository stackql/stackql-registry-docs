---
title: cloud_formation_provisioned_products
hide_title: false
hide_table_of_contents: false
keywords:
  - cloud_formation_provisioned_products
  - servicecatalog
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

Creates, updates, deletes or gets a <code>cloud_formation_provisioned_product</code> resource or lists <code>cloud_formation_provisioned_products</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>cloud_formation_provisioned_products</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Schema for AWS::ServiceCatalog::CloudFormationProvisionedProduct</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.servicecatalog.cloud_formation_provisioned_products" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="accept_language" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="notification_arns" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="path_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="path_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="product_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="product_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="provisioned_product_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="provisioning_artifact_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="provisioning_artifact_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="provisioning_parameters" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="provisioning_preferences" /></td><td><code>undefined</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="provisioned_product_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="record_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="cloudformation_stack_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="outputs" /></td><td><code>object</code></td><td>List of key-value pair outputs.</td></tr>
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
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples

Gets all properties from a <code>cloud_formation_provisioned_product</code>.
```sql
SELECT
region,
accept_language,
notification_arns,
path_id,
path_name,
product_id,
product_name,
provisioned_product_name,
provisioning_artifact_id,
provisioning_artifact_name,
provisioning_parameters,
provisioning_preferences,
tags,
provisioned_product_id,
record_id,
cloudformation_stack_arn,
outputs
FROM aws.servicecatalog.cloud_formation_provisioned_products
WHERE region = 'us-east-1' AND data__Identifier = '<ProvisionedProductId>';
```


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>cloud_formation_provisioned_product</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.servicecatalog.cloud_formation_provisioned_products (
 AcceptLanguage,
 NotificationArns,
 PathId,
 PathName,
 ProductId,
 ProductName,
 ProvisionedProductName,
 ProvisioningArtifactId,
 ProvisioningArtifactName,
 ProvisioningParameters,
 ProvisioningPreferences,
 Tags,
 region
)
SELECT 
'{{ AcceptLanguage }}',
 '{{ NotificationArns }}',
 '{{ PathId }}',
 '{{ PathName }}',
 '{{ ProductId }}',
 '{{ ProductName }}',
 '{{ ProvisionedProductName }}',
 '{{ ProvisioningArtifactId }}',
 '{{ ProvisioningArtifactName }}',
 '{{ ProvisioningParameters }}',
 '{{ ProvisioningPreferences }}',
 '{{ Tags }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.servicecatalog.cloud_formation_provisioned_products (
 AcceptLanguage,
 NotificationArns,
 PathId,
 PathName,
 ProductId,
 ProductName,
 ProvisionedProductName,
 ProvisioningArtifactId,
 ProvisioningArtifactName,
 ProvisioningParameters,
 ProvisioningPreferences,
 Tags,
 region
)
SELECT 
 '{{ AcceptLanguage }}',
 '{{ NotificationArns }}',
 '{{ PathId }}',
 '{{ PathName }}',
 '{{ ProductId }}',
 '{{ ProductName }}',
 '{{ ProvisionedProductName }}',
 '{{ ProvisioningArtifactId }}',
 '{{ ProvisioningArtifactName }}',
 '{{ ProvisioningParameters }}',
 '{{ ProvisioningPreferences }}',
 '{{ Tags }}',
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
  - name: cloud_formation_provisioned_product
    props:
      - name: AcceptLanguage
        value: '{{ AcceptLanguage }}'
      - name: NotificationArns
        value:
          - '{{ NotificationArns[0] }}'
      - name: PathId
        value: '{{ PathId }}'
      - name: PathName
        value: '{{ PathName }}'
      - name: ProductId
        value: '{{ ProductId }}'
      - name: ProductName
        value: '{{ ProductName }}'
      - name: ProvisionedProductName
        value: '{{ ProvisionedProductName }}'
      - name: ProvisioningArtifactId
        value: '{{ ProvisioningArtifactId }}'
      - name: ProvisioningArtifactName
        value: '{{ ProvisioningArtifactName }}'
      - name: ProvisioningParameters
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'
      - name: ProvisioningPreferences
        value:
          StackSetAccounts:
            - '{{ StackSetAccounts[0] }}'
          StackSetFailureToleranceCount: '{{ StackSetFailureToleranceCount }}'
          StackSetFailureTolerancePercentage: '{{ StackSetFailureTolerancePercentage }}'
          StackSetMaxConcurrencyCount: '{{ StackSetMaxConcurrencyCount }}'
          StackSetMaxConcurrencyPercentage: '{{ StackSetMaxConcurrencyPercentage }}'
          StackSetOperationType: '{{ StackSetOperationType }}'
          StackSetRegions:
            - '{{ StackSetRegions[0] }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.servicecatalog.cloud_formation_provisioned_products
WHERE data__Identifier = '<ProvisionedProductId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>cloud_formation_provisioned_products</code> resource, the following permissions are required:

### Create
```json
*
```

### Read
```json
*
```

### Update
```json
*
```

### Delete
```json
*
```

