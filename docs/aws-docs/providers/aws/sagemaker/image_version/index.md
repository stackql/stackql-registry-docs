---
title: image_version
hide_title: false
hide_table_of_contents: false
keywords:
  - image_version
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


Gets or updates an individual <code>image_version</code> resource, use <code>image_versions</code> to retrieve a list of resources or to create or delete a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>image_version</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::SageMaker::ImageVersion</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.sagemaker.image_version" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="image_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="image_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="image_version_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="base_image" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="container_image" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="version" /></td><td><code>integer</code></td><td></td></tr>
<tr><td><CopyableCode code="alias" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="aliases" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="vendor_guidance" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="job_type" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="ml_framework" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="programming_lang" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="processor" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="horovod" /></td><td><code>boolean</code></td><td></td></tr>
<tr><td><CopyableCode code="release_notes" /></td><td><code>string</code></td><td></td></tr>
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

## `SELECT` Example
```sql
SELECT
region,
image_name,
image_arn,
image_version_arn,
base_image,
container_image,
version,
alias,
aliases,
vendor_guidance,
job_type,
ml_framework,
programming_lang,
processor,
horovod,
release_notes
FROM aws.sagemaker.image_version
WHERE region = 'us-east-1' AND data__Identifier = '<ImageVersionArn>';
```


## Permissions

To operate on the <code>image_version</code> resource, the following permissions are required:

### Read
```json
sagemaker:DescribeImageVersion
```

### Update
```json
sagemaker:UpdateImageVersion,
sagemaker:DescribeImageVersion,
sagemaker:ListAliases
```

