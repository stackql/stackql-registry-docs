---
title: environment_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - environment_tags
  - finspace
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

Expands all tag keys and values for <code>environments</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>environment_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>An example resource schema demonstrating some basic constructs and validation rules.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.finspace.environment_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="environment_id" /></td><td><code>string</code></td><td>Unique identifier for representing FinSpace Environment</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>Name of the Environment</td></tr>
<tr><td><CopyableCode code="aws_account_id" /></td><td><code>string</code></td><td>AWS account ID associated with the Environment</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>Description of the Environment</td></tr>
<tr><td><CopyableCode code="status" /></td><td><code>string</code></td><td>State of the Environment</td></tr>
<tr><td><CopyableCode code="environment_url" /></td><td><code>string</code></td><td>URL used to login to the Environment</td></tr>
<tr><td><CopyableCode code="environment_arn" /></td><td><code>string</code></td><td>ARN of the Environment</td></tr>
<tr><td><CopyableCode code="sage_maker_studio_domain_url" /></td><td><code>string</code></td><td>SageMaker Studio Domain URL associated with the Environment</td></tr>
<tr><td><CopyableCode code="kms_key_id" /></td><td><code>string</code></td><td>KMS key used to encrypt customer data within FinSpace Environment infrastructure</td></tr>
<tr><td><CopyableCode code="dedicated_service_account_id" /></td><td><code>string</code></td><td>ID for FinSpace created account used to store Environment artifacts</td></tr>
<tr><td><CopyableCode code="federation_mode" /></td><td><code>string</code></td><td>Federation mode used with the Environment</td></tr>
<tr><td><CopyableCode code="federation_parameters" /></td><td><code>object</code></td><td>Additional parameters to identify Federation mode</td></tr>
<tr><td><CopyableCode code="superuser_parameters" /></td><td><code>object</code></td><td>Parameters of the first Superuser for the FinSpace Environment</td></tr>
<tr><td><CopyableCode code="data_bundles" /></td><td><code>array</code></td><td>ARNs of FinSpace Data Bundles to install</td></tr>
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
Expands tags for all <code>environments</code> in a region.
```sql
SELECT
region,
environment_id,
name,
aws_account_id,
description,
status,
environment_url,
environment_arn,
sage_maker_studio_domain_url,
kms_key_id,
dedicated_service_account_id,
federation_mode,
federation_parameters,
superuser_parameters,
data_bundles,
tag_key,
tag_value
FROM aws.finspace.environment_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>environment_tags</code> resource, see <a href="/providers/aws/finspace/environments/#permissions"><code>environments</code></a>


