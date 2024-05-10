---
title: spaces
hide_title: false
hide_table_of_contents: false
keywords:
  - spaces
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


Used to retrieve a list of <code>spaces</code> in a region or to create or delete a <code>spaces</code> resource, use <code>space</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>spaces</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::SageMaker::Space</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.sagemaker.spaces" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="domain_id" /></td><td><code>string</code></td><td>The ID of the associated Domain.</td></tr>
<tr><td><CopyableCode code="space_name" /></td><td><code>string</code></td><td>A name for the Space.</td></tr>
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
domain_id,
space_name
FROM aws.sagemaker.spaces
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
 "DomainId": "{{ DomainId }}",
 "SpaceName": "{{ SpaceName }}"
}
>>>
--required properties only
INSERT INTO aws.sagemaker.spaces (
 DomainId,
 SpaceName,
 region
)
SELECT 
{{ DomainId }},
 {{ SpaceName }},
'us-east-1';
```

</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "DomainId": "{{ DomainId }}",
 "SpaceName": "{{ SpaceName }}",
 "SpaceSettings": {
  "JupyterServerAppSettings": {
   "DefaultResourceSpec": {
    "InstanceType": "{{ InstanceType }}",
    "SageMakerImageArn": "{{ SageMakerImageArn }}",
    "SageMakerImageVersionArn": "{{ SageMakerImageVersionArn }}"
   }
  },
  "KernelGatewayAppSettings": {
   "CustomImages": [
    {
     "AppImageConfigName": "{{ AppImageConfigName }}",
     "ImageName": "{{ ImageName }}",
     "ImageVersionNumber": "{{ ImageVersionNumber }}"
    }
   ],
   "DefaultResourceSpec": null
  },
  "JupyterLabAppSettings": {
   "DefaultResourceSpec": null,
   "CodeRepositories": [
    {
     "RepositoryUrl": "{{ RepositoryUrl }}"
    }
   ]
  },
  "CodeEditorAppSettings": {
   "DefaultResourceSpec": null
  },
  "SpaceStorageSettings": {
   "EbsStorageSettings": {
    "EbsVolumeSizeInGb": "{{ EbsVolumeSizeInGb }}"
   }
  },
  "AppType": "{{ AppType }}",
  "CustomFileSystems": [
   {
    "EFSFileSystem": {
     "FileSystemId": "{{ FileSystemId }}"
    }
   }
  ]
 },
 "Tags": [
  {
   "Value": "{{ Value }}",
   "Key": "{{ Key }}"
  }
 ],
 "OwnershipSettings": {
  "OwnerUserProfileName": "{{ OwnerUserProfileName }}"
 },
 "SpaceSharingSettings": {
  "SharingType": "{{ SharingType }}"
 },
 "SpaceDisplayName": "{{ SpaceDisplayName }}"
}
>>>
--all properties
INSERT INTO aws.sagemaker.spaces (
 DomainId,
 SpaceName,
 SpaceSettings,
 Tags,
 OwnershipSettings,
 SpaceSharingSettings,
 SpaceDisplayName,
 region
)
SELECT 
 {{ DomainId }},
 {{ SpaceName }},
 {{ SpaceSettings }},
 {{ Tags }},
 {{ OwnershipSettings }},
 {{ SpaceSharingSettings }},
 {{ SpaceDisplayName }},
 'us-east-1';
```

</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.sagemaker.spaces
WHERE data__Identifier = '<DomainId|SpaceName>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>spaces</code> resource, the following permissions are required:

### Create
```json
sagemaker:CreateSpace,
sagemaker:DescribeSpace
```

### Delete
```json
sagemaker:DeleteSpace,
sagemaker:DescribeSpace
```

### List
```json
sagemaker:ListSpaces
```

