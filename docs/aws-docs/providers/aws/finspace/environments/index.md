---
title: environments
hide_title: false
hide_table_of_contents: false
keywords:
  - environments
  - finspace
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

Creates, updates, deletes or gets an <code>environment</code> resource or lists <code>environments</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>environments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>An example resource schema demonstrating some basic constructs and validation rules.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.finspace.environments" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="environment_id" /></td><td><code>string</code></td><td>Unique identifier for representing FinSpace Environment</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>Name of the Environment</td></tr>
<tr><td><CopyableCode code="aws_account_id" /></td><td><code>string</code></td><td>AWS account ID associated with the Environment</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>Description of the Environment</td></tr>
<tr><td><CopyableCode code="status" /></td><td><code>string</code></td><td>State of the Environment</td></tr>
<tr><td><CopyableCode code="environment_url" /></td><td><code>string</code></td><td>URL used to login to the Environment</td></tr>
<tr><td><CopyableCode code="environment_arn" /></td><td><code>string</code></td><td>ARN of the Environment</td></tr>
<tr><td><CopyableCode code="sage_maker_studio_domain_url" /></td><td><code>string</code></td><td>SageMaker Studio Domain URL associated with the Environment</td></tr>
<tr><td><CopyableCode code="kms_key_id" /></td><td><code>string</code></td><td>KMS key used to encrypt customer data within FinSpace Environment infrastructure</td></tr>
<tr><td><CopyableCode code="dedicated_service_account_id" /></td><td><code>string</code></td><td>ID for FinSpace created account used to store Environment artifacts</td></tr>
<tr><td><CopyableCode code="federation_mode" /></td><td><code>string</code></td><td>Federation mode used with the Environment</td></tr>
<tr><td><CopyableCode code="federation_parameters" /></td><td><code>object</code></td><td>Additional parameters to identify Federation mode</td></tr>
<tr><td><CopyableCode code="superuser_parameters" /></td><td><code>object</code></td><td>Parameters of the first Superuser for the FinSpace Environment</td></tr>
<tr><td><CopyableCode code="data_bundles" /></td><td><code>array</code></td><td>ARNs of FinSpace Data Bundles to install</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
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
    <td><CopyableCode code="Name, region" /></td>
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
    <td><CopyableCode code="list_resource" /></td>
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
List all <code>environments</code> in a region.
```sql
SELECT
region,
environment_id
FROM aws.finspace.environments
WHERE region = 'us-east-1';
```
Gets all properties from an <code>environment</code>.
```sql
SELECT
region,
environment_id,
name,
aws_account_id,
description,
status,
environment_url,
environment_arn,
sage_maker_studio_domain_url,
kms_key_id,
dedicated_service_account_id,
federation_mode,
federation_parameters,
superuser_parameters,
data_bundles,
tags
FROM aws.finspace.environments
WHERE region = 'us-east-1' AND data__Identifier = '<EnvironmentId>';
```


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>environment</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.finspace.environments (
 Name,
 region
)
SELECT 
'{{ Name }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.finspace.environments (
 Name,
 Description,
 KmsKeyId,
 FederationMode,
 FederationParameters,
 SuperuserParameters,
 DataBundles,
 Tags,
 region
)
SELECT 
 '{{ Name }}',
 '{{ Description }}',
 '{{ KmsKeyId }}',
 '{{ FederationMode }}',
 '{{ FederationParameters }}',
 '{{ SuperuserParameters }}',
 '{{ DataBundles }}',
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
  - name: environment
    props:
      - name: Name
        value: '{{ Name }}'
      - name: Description
        value: '{{ Description }}'
      - name: KmsKeyId
        value: '{{ KmsKeyId }}'
      - name: FederationMode
        value: '{{ FederationMode }}'
      - name: FederationParameters
        value:
          SamlMetadataURL: '{{ SamlMetadataURL }}'
          FederationProviderName: '{{ FederationProviderName }}'
          SamlMetadataDocument: '{{ SamlMetadataDocument }}'
          ApplicationCallBackURL: '{{ ApplicationCallBackURL }}'
          FederationURN: '{{ FederationURN }}'
          AttributeMap:
            - Key: '{{ Key }}'
              Value: '{{ Value }}'
      - name: SuperuserParameters
        value:
          FirstName: '{{ FirstName }}'
          LastName: '{{ LastName }}'
          EmailAddress: '{{ EmailAddress }}'
      - name: DataBundles
        value:
          - '{{ DataBundles[0] }}'
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
DELETE FROM aws.finspace.environments
WHERE data__Identifier = '<EnvironmentId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>environments</code> resource, the following permissions are required:

### Create
```json
finspace:CreateEnvironment,
finspace:GetEnvironment,
finspace:ListEnvironments,
sts:AssumeRole
```

### Read
```json
finspace:GetEnvironment
```

### Update
```json
finspace:UpdateEnvironment
```

### Delete
```json
finspace:DeleteEnvironment,
finspace:GetEnvironment
```

### List
```json
finspace:ListEnvironments
```

