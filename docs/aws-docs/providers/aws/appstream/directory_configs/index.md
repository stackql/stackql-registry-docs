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


Used to retrieve a list of <code>directory_configs</code> in a region or to create or delete a <code>directory_configs</code> resource, use <code>directory_config</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>directory_configs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::AppStream::DirectoryConfig</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.appstream.directory_configs" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="directory_name" /></td><td><code>string</code></td><td></td></tr>
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
directory_name
FROM aws.appstream.directory_configs
WHERE region = 'us-east-1';
```

## `INSERT` Example

<Tabs
    defaultValue="required"
    values={[
      { label: 'Required Properties', value: 'required', },
      { label: 'All Properties', value: 'all', },
    ]
}>
<TabItem value="required">

```sql
<<<json
{
 "OrganizationalUnitDistinguishedNames": [
  "{{ OrganizationalUnitDistinguishedNames[0] }}"
 ],
 "ServiceAccountCredentials": {
  "AccountName": "{{ AccountName }}",
  "AccountPassword": "{{ AccountPassword }}"
 },
 "DirectoryName": "{{ DirectoryName }}"
}
>>>
--required properties only
INSERT INTO aws.appstream.directory_configs (
 OrganizationalUnitDistinguishedNames,
 ServiceAccountCredentials,
 DirectoryName,
 region
)
SELECT 
{{ .OrganizationalUnitDistinguishedNames }},
 {{ .ServiceAccountCredentials }},
 {{ .DirectoryName }},
'us-east-1';
```
</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "OrganizationalUnitDistinguishedNames": [
  "{{ OrganizationalUnitDistinguishedNames[0] }}"
 ],
 "ServiceAccountCredentials": {
  "AccountName": "{{ AccountName }}",
  "AccountPassword": "{{ AccountPassword }}"
 },
 "DirectoryName": "{{ DirectoryName }}",
 "CertificateBasedAuthProperties": {
  "Status": "{{ Status }}",
  "CertificateAuthorityArn": "{{ CertificateAuthorityArn }}"
 }
}
>>>
--all properties
INSERT INTO aws.appstream.directory_configs (
 OrganizationalUnitDistinguishedNames,
 ServiceAccountCredentials,
 DirectoryName,
 CertificateBasedAuthProperties,
 region
)
SELECT 
 {{ .OrganizationalUnitDistinguishedNames }},
 {{ .ServiceAccountCredentials }},
 {{ .DirectoryName }},
 {{ .CertificateBasedAuthProperties }},
 'us-east-1';
```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
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

