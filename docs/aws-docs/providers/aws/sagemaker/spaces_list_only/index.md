---
title: spaces_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - spaces_list_only
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

Lists <code>spaces</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/spaces/"><code>spaces</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>spaces_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::SageMaker::Space</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.sagemaker.spaces_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="space_arn" /></td><td><code>string</code></td><td>The space Amazon Resource Name (ARN).</td></tr>
<tr><td><CopyableCode code="domain_id" /></td><td><code>string</code></td><td>The ID of the associated Domain.</td></tr>
<tr><td><CopyableCode code="space_name" /></td><td><code>string</code></td><td>A name for the Space.</td></tr>
<tr><td><CopyableCode code="space_settings" /></td><td><code>object</code></td><td>A collection of settings.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>A list of tags to apply to the space.</td></tr>
<tr><td><CopyableCode code="ownership_settings" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="space_sharing_settings" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="space_display_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="url" /></td><td><code>string</code></td><td></td></tr>
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
Lists all <code>spaces</code> in a region.
```sql
SELECT
region,
domain_id,
space_name
FROM aws.sagemaker.spaces_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>spaces_list_only</code> resource, see <a href="/providers/aws/sagemaker/spaces/#permissions"><code>spaces</code></a>


