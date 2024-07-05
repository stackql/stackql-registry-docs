---
title: document_classifiers_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - document_classifiers_list_only
  - comprehend
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

Lists <code>document_classifiers</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/document_classifiers/"><code>document_classifiers</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>document_classifiers_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Document Classifier enables training document classifier models.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.comprehend.document_classifiers_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="data_access_role_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="input_data_config" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="output_data_config" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="language_code" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="model_kms_key_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="model_policy" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="document_classifier_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="mode" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="version_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="volume_kms_key_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="vpc_config" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td></td></tr>
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
Lists all <code>document_classifiers</code> in a region.
```sql
SELECT
region,
arn
FROM aws.comprehend.document_classifiers_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>document_classifiers_list_only</code> resource, see <a href="/providers/aws/comprehend/document_classifiers/#permissions"><code>document_classifiers</code></a>


