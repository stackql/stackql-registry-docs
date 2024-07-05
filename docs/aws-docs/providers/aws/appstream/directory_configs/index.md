---
title: directory_configs
hide_title: false
hide_table_of_contents: false
keywords:
  - directory_configs
  - appstream
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

Creates, updates, deletes or gets a <code>directory_config</code> resource or lists <code>directory_configs</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>directory_configs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::AppStream::DirectoryConfig</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.appstream.directory_configs" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="organizational_unit_distinguished_names" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="service_account_credentials" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="directory_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="certificate_based_auth_properties" /></td><td><code>object</code></td><td></td></tr>
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
    <td><CopyableCode code="DirectoryName, OrganizationalUnitDistinguishedNames, ServiceAccountCredentials, region" /></td>
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
Gets all <code>directory_configs</code> in a region.
```sql
SELECT
region,
organizational_unit_distinguished_names,
service_account_credentials,
directory_name,
certificate_based_auth_properties
FROM aws.appstream.directory_configs
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>directory_config</code>.
```sql
SELECT
region,
organizational_unit_distinguished_names,
service_account_credentials,
directory_name,
certificate_based_auth_properties
FROM aws.appstream.directory_configs
WHERE region = 'us-east-1' AND data__Identifier = '<DirectoryName>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>directory_config</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.appstream.directory_configs (
 OrganizationalUnitDistinguishedNames,
 ServiceAccountCredentials,
 DirectoryName,
 region
)
SELECT 
'{{ OrganizationalUnitDistinguishedNames }}',
 '{{ ServiceAccountCredentials }}',
 '{{ DirectoryName }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.appstream.directory_configs (
 OrganizationalUnitDistinguishedNames,
 ServiceAccountCredentials,
 DirectoryName,
 CertificateBasedAuthProperties,
 region
)
SELECT 
 '{{ OrganizationalUnitDistinguishedNames }}',
 '{{ ServiceAccountCredentials }}',
 '{{ DirectoryName }}',
 '{{ CertificateBasedAuthProperties }}',
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
  - name: directory_config
    props:
      - name: OrganizationalUnitDistinguishedNames
        value:
          - '{{ OrganizationalUnitDistinguishedNames[0] }}'
      - name: ServiceAccountCredentials
        value:
          AccountName: '{{ AccountName }}'
          AccountPassword: '{{ AccountPassword }}'
      - name: DirectoryName
        value: '{{ DirectoryName }}'
      - name: CertificateBasedAuthProperties
        value:
          Status: '{{ Status }}'
          CertificateAuthorityArn: '{{ CertificateAuthorityArn }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.appstream.directory_configs
WHERE data__Identifier = '<DirectoryName>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>directory_configs</code> resource, the following permissions are required:

### Create
```json
appstream:CreateDirectoryConfig,
appstream:DeleteDirectoryConfig,
appstream:DescribeDirectoryConfigs,
appstream:UpdateDirectoryConfig,
iam:CreateServiceLinkedRole,
iam:DeleteServiceLinkedRole,
iam:GetServiceLinkedRoleDeletionStatus
```

### Update
```json
appstream:CreateDirectoryConfig,
appstream:DeleteDirectoryConfig,
appstream:DescribeDirectoryConfigs,
appstream:UpdateDirectoryConfig,
iam:CreateServiceLinkedRole,
iam:DeleteServiceLinkedRole,
iam:GetServiceLinkedRoleDeletionStatus
```

### Read
```json
appstream:CreateDirectoryConfig,
appstream:DeleteDirectoryConfig,
appstream:DescribeDirectoryConfigs,
appstream:UpdateDirectoryConfig,
iam:CreateServiceLinkedRole,
iam:DeleteServiceLinkedRole,
iam:GetServiceLinkedRoleDeletionStatus
```

### Delete
```json
appstream:CreateDirectoryConfig,
appstream:DeleteDirectoryConfig,
appstream:DescribeDirectoryConfigs,
appstream:UpdateDirectoryConfig,
iam:CreateServiceLinkedRole,
iam:DeleteServiceLinkedRole,
iam:GetServiceLinkedRoleDeletionStatus
```

### List
```json
appstream:CreateDirectoryConfig,
appstream:DeleteDirectoryConfig,
appstream:DescribeDirectoryConfigs,
appstream:UpdateDirectoryConfig,
iam:CreateServiceLinkedRole,
iam:DeleteServiceLinkedRole,
iam:GetServiceLinkedRoleDeletionStatus
```

