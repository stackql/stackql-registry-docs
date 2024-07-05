---
title: workflows_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - workflows_list_only
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

Lists <code>workflows</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/workflows/"><code>workflows</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>workflows_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::ImageBuilder::Workflow</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.imagebuilder.workflows_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the workflow.</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name of the workflow.</td></tr>
<tr><td><CopyableCode code="version" /></td><td><code>string</code></td><td>The version of the workflow.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>The description of the workflow.</td></tr>
<tr><td><CopyableCode code="change_description" /></td><td><code>string</code></td><td>The change description of the workflow.</td></tr>
<tr><td><CopyableCode code="type" /></td><td><code>string</code></td><td>The type of the workflow denotes whether the workflow is used to build, test, or distribute.</td></tr>
<tr><td><CopyableCode code="data" /></td><td><code>string</code></td><td>The data of the workflow.</td></tr>
<tr><td><CopyableCode code="uri" /></td><td><code>string</code></td><td>The uri of the workflow.</td></tr>
<tr><td><CopyableCode code="kms_key_id" /></td><td><code>string</code></td><td>The KMS key identifier used to encrypt the workflow.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>object</code></td><td>The tags associated with the workflow.</td></tr>
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
Lists all <code>workflows</code> in a region.
```sql
SELECT
region,
arn
FROM aws.imagebuilder.workflows_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>workflows_list_only</code> resource, see <a href="/providers/aws/imagebuilder/workflows/#permissions"><code>workflows</code></a>


