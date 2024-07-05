---
title: image_versions_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - image_versions_list_only
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

Lists <code>image_versions</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/image_versions/"><code>image_versions</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>image_versions_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::SageMaker::ImageVersion</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.sagemaker.image_versions_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="image_name" /></td><td><code>string</code></td><td>The name of the image this version belongs to.</td></tr>
<tr><td><CopyableCode code="image_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the parent image.</td></tr>
<tr><td><CopyableCode code="image_version_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the image version.</td></tr>
<tr><td><CopyableCode code="base_image" /></td><td><code>string</code></td><td>The registry path of the container image on which this image version is based.</td></tr>
<tr><td><CopyableCode code="container_image" /></td><td><code>string</code></td><td>The image to use for the container that will be materialized for the inference component</td></tr>
<tr><td><CopyableCode code="version" /></td><td><code>integer</code></td><td>The version number of the image version.</td></tr>
<tr><td><CopyableCode code="alias" /></td><td><code>string</code></td><td>The alias of the image version.</td></tr>
<tr><td><CopyableCode code="aliases" /></td><td><code>array</code></td><td>List of aliases for the image version.</td></tr>
<tr><td><CopyableCode code="vendor_guidance" /></td><td><code>string</code></td><td>The availability of the image version specified by the maintainer.</td></tr>
<tr><td><CopyableCode code="job_type" /></td><td><code>string</code></td><td>Indicates SageMaker job type compatibility.</td></tr>
<tr><td><CopyableCode code="ml_framework" /></td><td><code>string</code></td><td>The machine learning framework vended in the image version.</td></tr>
<tr><td><CopyableCode code="programming_lang" /></td><td><code>string</code></td><td>The supported programming language and its version.</td></tr>
<tr><td><CopyableCode code="processor" /></td><td><code>string</code></td><td>Indicates CPU or GPU compatibility.</td></tr>
<tr><td><CopyableCode code="horovod" /></td><td><code>boolean</code></td><td>Indicates Horovod compatibility.</td></tr>
<tr><td><CopyableCode code="release_notes" /></td><td><code>string</code></td><td>The maintainer description of the image version.</td></tr>
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
    <td><CopyableCode code="list_resources" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples
Lists all <code>image_versions</code> in a region.
```sql
SELECT
region,
image_version_arn
FROM aws.sagemaker.image_versions_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>image_versions_list_only</code> resource, see <a href="/providers/aws/sagemaker/image_versions/#permissions"><code>image_versions</code></a>


