---
title: service_principal_names
hide_title: false
hide_table_of_contents: false
keywords:
  - service_principal_names
  - pcaconnectorad
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


Used to retrieve a list of <code>service_principal_names</code> in a region or to create or delete a <code>service_principal_names</code> resource, use <code>service_principal_name</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>service_principal_names</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::PCAConnectorAD::ServicePrincipalName Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.pcaconnectorad.service_principal_names" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="connector_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="directory_registration_arn" /></td><td><code>string</code></td><td></td></tr>
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
connector_arn,
directory_registration_arn
FROM aws.pcaconnectorad.service_principal_names
WHERE region = 'us-east-1';
```

## `INSERT` Example

Use the following StackQL query and manifest file to create a new <code>service_principal_name</code> resource, using <a ref="https://pypi.org/project/stack-deploy/" target="_blank"><code><b>stack-deploy</b></code></a>.

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
-- service_principal_name.iql (required properties only)
INSERT INTO aws.pcaconnectorad.service_principal_names (
 ConnectorArn,
 DirectoryRegistrationArn,
 region
)
SELECT 
'{{ ConnectorArn }}',
 '{{ DirectoryRegistrationArn }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
-- service_principal_name.iql (all properties)
INSERT INTO aws.pcaconnectorad.service_principal_names (
 ConnectorArn,
 DirectoryRegistrationArn,
 region
)
SELECT 
 '{{ ConnectorArn }}',
 '{{ DirectoryRegistrationArn }}',
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
  - name: service_principal_name
    props:
      - name: ConnectorArn
        value: '{{ ConnectorArn }}'
      - name: DirectoryRegistrationArn
        value: '{{ DirectoryRegistrationArn }}'

```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.pcaconnectorad.service_principal_names
WHERE data__Identifier = '<ConnectorArn|DirectoryRegistrationArn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>service_principal_names</code> resource, the following permissions are required:

### Create
```json
ds:UpdateAuthorizedApplication,
pca-connector-ad:GetServicePrincipalName,
pca-connector-ad:CreateServicePrincipalName
```

### Delete
```json
ds:UpdateAuthorizedApplication,
pca-connector-ad:GetServicePrincipalName,
pca-connector-ad:DeleteServicePrincipalName
```

### List
```json
pca-connector-ad:ListServicePrincipalNames
```

