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

Creates, updates, deletes or gets a <code>fhir_datastore</code> resource or lists <code>fhir_datastores</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>fhir_datastores</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>HealthLake FHIR Datastore</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.healthlake.fhir_datastores" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="created_at" /></td><td><code>object</code></td><td>The time that a Data Store was created.</td></tr>
<tr><td><CopyableCode code="datastore_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name used in the creation of the Data Store.</td></tr>
<tr><td><CopyableCode code="datastore_endpoint" /></td><td><code>string</code></td><td>The AWS endpoint for the Data Store. Each Data Store will have it's own endpoint with Data Store ID in the endpoint URL.</td></tr>
<tr><td><CopyableCode code="datastore_id" /></td><td><code>string</code></td><td>The AWS-generated ID number for the Data Store.</td></tr>
<tr><td><CopyableCode code="datastore_name" /></td><td><code>string</code></td><td>The user-generated name for the Data Store.</td></tr>
<tr><td><CopyableCode code="datastore_status" /></td><td><code>string</code></td><td>The status of the Data Store. Possible statuses are 'CREATING', 'ACTIVE', 'DELETING', or 'DELETED'.</td></tr>
<tr><td><CopyableCode code="datastore_type_version" /></td><td><code>string</code></td><td>The FHIR version. Only R4 version data is supported.</td></tr>
<tr><td><CopyableCode code="preload_data_config" /></td><td><code>object</code></td><td>The preloaded data configuration for the Data Store. Only data preloaded from Synthea is supported.</td></tr>
<tr><td><CopyableCode code="sse_configuration" /></td><td><code>object</code></td><td>The server-side encryption key configuration for a customer provided encryption key.</td></tr>
<tr><td><CopyableCode code="identity_provider_configuration" /></td><td><code>object</code></td><td>The identity provider configuration for the datastore</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td></td></tr>
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
    <td><CopyableCode code="DatastoreTypeVersion, region" /></td>
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
Gets all <code>fhir_datastores</code> in a region.
```sql
SELECT
region,
created_at,
datastore_arn,
datastore_endpoint,
datastore_id,
datastore_name,
datastore_status,
datastore_type_version,
preload_data_config,
sse_configuration,
identity_provider_configuration,
tags
FROM aws.healthlake.fhir_datastores
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>fhir_datastore</code>.
```sql
SELECT
region,
created_at,
datastore_arn,
datastore_endpoint,
datastore_id,
datastore_name,
datastore_status,
datastore_type_version,
preload_data_config,
sse_configuration,
identity_provider_configuration,
tags
FROM aws.healthlake.fhir_datastores
WHERE region = 'us-east-1' AND data__Identifier = '<DatastoreId>';
```

## `INSERT` example

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
/*+ create */
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
/*+ create */
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

## `DELETE` example

```sql
/*+ delete */
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

### Read
```json
healthlake:DescribeFHIRDatastore,
healthlake:ListTagsForResource
```

### Update
```json
healthlake:TagResource,
healthlake:UntagResource,
healthlake:ListTagsForResource,
healthlake:DescribeFHIRDatastore,
iam:PassRole,
iam:GetRole,
iam:CreateServiceLinkedRole
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

