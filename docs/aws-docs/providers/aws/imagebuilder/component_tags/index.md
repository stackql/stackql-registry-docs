---
title: component_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - component_tags
  - imagebuilder
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

Expands all tag keys and values for <code>components</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>component_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::ImageBuilder::Component</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.imagebuilder.component_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the component.</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name of the component.</td></tr>
<tr><td><CopyableCode code="version" /></td><td><code>string</code></td><td>The version of the component.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>The description of the component.</td></tr>
<tr><td><CopyableCode code="change_description" /></td><td><code>string</code></td><td>The change description of the component.</td></tr>
<tr><td><CopyableCode code="type" /></td><td><code>string</code></td><td>The type of the component denotes whether the component is used to build the image or only to test it.</td></tr>
<tr><td><CopyableCode code="platform" /></td><td><code>string</code></td><td>The platform of the component.</td></tr>
<tr><td><CopyableCode code="data" /></td><td><code>string</code></td><td>The data of the component.</td></tr>
<tr><td><CopyableCode code="kms_key_id" /></td><td><code>string</code></td><td>The KMS key identifier used to encrypt the component.</td></tr>
<tr><td><CopyableCode code="encrypted" /></td><td><code>boolean</code></td><td>The encryption status of the component.</td></tr>
<tr><td><CopyableCode code="uri" /></td><td><code>string</code></td><td>The uri of the component.</td></tr>
<tr><td><CopyableCode code="supported_os_versions" /></td><td><code>array</code></td><td>The operating system (OS) version supported by the component.</td></tr>
<tr><td><CopyableCode code="tag_key" /></td><td><code>string</code></td><td>Tag key.</td></tr>
<tr><td><CopyableCode code="tag_value" /></td><td><code>string</code></td><td>Tag value.</td></tr>
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
Expands tags for all <code>components</code> in a region.
```sql
SELECT
region,
arn,
name,
version,
description,
change_description,
type,
platform,
data,
kms_key_id,
encrypted,
uri,
supported_os_versions,
tag_key,
tag_value
FROM aws.imagebuilder.component_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>component_tags</code> resource, see <a href="/providers/aws/imagebuilder/components/#permissions"><code>components</code></a>

