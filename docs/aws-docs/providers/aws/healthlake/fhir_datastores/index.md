---
title: fhir_datastores
hide_title: false
hide_table_of_contents: false
keywords:
  - fhir_datastores
  - healthlake
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


Used to retrieve a list of <code>fhir_datastores</code> in a region or to create or delete a <code>fhir_datastores</code> resource, use <code>fhir_datastore</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>fhir_datastores</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>HealthLake FHIR Datastore</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.healthlake.fhir_datastores" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="datastore_id" /></td><td><code>undefined</code></td><td></td></tr>
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
datastore_id
FROM aws.healthlake.fhir_datastores
WHERE region = 'us-east-1';
```

## `INSERT` Example

Use the following StackQL query and manifest file to create a new <code>fhir_datastore</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
-- fhir_datastore.iql (required properties only)
INSERT INTO aws.healthlake.fhir_datastores (
 DatastoreTypeVersion,
 region
)
SELECT 
'{{ DatastoreTypeVersion }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
-- fhir_datastore.iql (all properties)
INSERT INTO aws.healthlake.fhir_datastores (
 DatastoreName,
 DatastoreTypeVersion,
 PreloadDataConfig,
 SseConfiguration,
 IdentityProviderConfiguration,
 Tags,
 region
)
SELECT 
 '{{ DatastoreName }}',
 '{{ DatastoreTypeVersion }}',
 '{{ PreloadDataConfig }}',
 '{{ SseConfiguration }}',
 '{{ IdentityProviderConfiguration }}',
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
  - name: fhir_datastore
    props:
      - name: DatastoreName
        value: '{{ DatastoreName }}'
      - name: DatastoreTypeVersion
        value: '{{ DatastoreTypeVersion }}'
      - name: PreloadDataConfig
        value:
          PreloadDataType: '{{ PreloadDataType }}'
      - name: SseConfiguration
        value:
          KmsEncryptionConfig:
            CmkType: '{{ CmkType }}'
            KmsKeyId: '{{ KmsKeyId }}'
      - name: IdentityProviderConfiguration
        value:
          AuthorizationStrategy: '{{ AuthorizationStrategy }}'
          FineGrainedAuthorizationEnabled: '{{ FineGrainedAuthorizationEnabled }}'
          Metadata: '{{ Metadata }}'
          IdpLambdaArn: '{{ IdpLambdaArn }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'

```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.healthlake.fhir_datastores
WHERE data__Identifier = '<DatastoreId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>fhir_datastores</code> resource, the following permissions are required:

### Create
```json
healthlake:CreateFHIRDatastore,
healthlake:DescribeFHIRDatastore,
iam:PassRole,
kms:DescribeKey,
kms:CreateGrant,
kms:GenerateDataKey,
kms:Decrypt,
iam:GetRole,
iam:CreateServiceLinkedRole,
ram:GetResourceShareInvitations,
ram:AcceptResourceShareInvitation,
glue:CreateDatabase,
glue:DeleteDatabase,
lambda:InvokeFunction,
healthlake:TagResource,
healthlake:UntagResource,
healthlake:ListTagsForResource
```

### Delete
```json
healthlake:DeleteFHIRDatastore,
healthlake:DescribeFHIRDatastore,
iam:PassRole,
iam:GetRole,
iam:CreateServiceLinkedRole,
ram:GetResourceShareInvitations,
ram:AcceptResourceShareInvitation,
glue:CreateDatabase,
glue:DeleteDatabase
```

### List
```json
healthlake:ListFHIRDatastores
```

