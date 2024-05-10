---
title: image_versions
hide_title: false
hide_table_of_contents: false
keywords:
  - image_versions
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


Used to retrieve a list of <code>image_versions</code> in a region or to create or delete a <code>image_versions</code> resource, use <code>image_version</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>image_versions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::SageMaker::ImageVersion</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.sagemaker.image_versions" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="image_version_arn" /></td><td><code>undefined</code></td><td></td></tr>
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
image_version_arn
FROM aws.sagemaker.image_versions
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
 "ImageName": "{{ ImageName }}",
 "BaseImage": "{{ BaseImage }}"
}
>>>
--required properties only
INSERT INTO aws.sagemaker.image_versions (
 ImageName,
 BaseImage,
 region
)
SELECT 
{{ ImageName }},
 {{ BaseImage }},
'us-east-1';
```

</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "ImageName": "{{ ImageName }}",
 "BaseImage": "{{ BaseImage }}",
 "Alias": "{{ Alias }}",
 "Aliases": [
  null
 ],
 "VendorGuidance": "{{ VendorGuidance }}",
 "JobType": "{{ JobType }}",
 "MLFramework": "{{ MLFramework }}",
 "ProgrammingLang": "{{ ProgrammingLang }}",
 "Processor": "{{ Processor }}",
 "Horovod": "{{ Horovod }}",
 "ReleaseNotes": "{{ ReleaseNotes }}"
}
>>>
--all properties
INSERT INTO aws.sagemaker.image_versions (
 ImageName,
 BaseImage,
 Alias,
 Aliases,
 VendorGuidance,
 JobType,
 MLFramework,
 ProgrammingLang,
 Processor,
 Horovod,
 ReleaseNotes,
 region
)
SELECT 
 {{ ImageName }},
 {{ BaseImage }},
 {{ Alias }},
 {{ Aliases }},
 {{ VendorGuidance }},
 {{ JobType }},
 {{ MLFramework }},
 {{ ProgrammingLang }},
 {{ Processor }},
 {{ Horovod }},
 {{ ReleaseNotes }},
 'us-east-1';
```

</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.sagemaker.image_versions
WHERE data__Identifier = '<ImageVersionArn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>image_versions</code> resource, the following permissions are required:

### Create
```json
sagemaker:CreateImageVersion,
sagemaker:DescribeImageVersion
```

### Delete
```json
sagemaker:DeleteImageVersion,
sagemaker:DescribeImageVersion
```

### List
```json
sagemaker:ListImageVersions
```

