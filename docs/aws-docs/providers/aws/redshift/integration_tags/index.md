---
title: integration_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - integration_tags
  - redshift
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

Expands all tag keys and values for <code>integrations</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>integration_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Integration from a source AWS service to a Redshift cluster</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.redshift.integration_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="integration_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the integration.</td></tr>
<tr><td><CopyableCode code="integration_name" /></td><td><code>string</code></td><td>The name of the integration.</td></tr>
<tr><td><CopyableCode code="source_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the database to use as the source for replication</td></tr>
<tr><td><CopyableCode code="target_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the Redshift data warehouse to use as the target for replication</td></tr>
<tr><td><CopyableCode code="create_time" /></td><td><code>string</code></td><td>The time (UTC) when the integration was created.</td></tr>
<tr><td><CopyableCode code="kms_key_id" /></td><td><code>string</code></td><td>An KMS key identifier for the key to use to encrypt the integration. If you don't specify an encryption key, the default AWS owned KMS key is used.</td></tr>
<tr><td><CopyableCode code="additional_encryption_context" /></td><td><code>object</code></td><td>An optional set of non-secret key–value pairs that contains additional contextual information about the data.</td></tr>
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
Expands tags for all <code>integrations</code> in a region.
```sql
SELECT
region,
integration_arn,
integration_name,
source_arn,
target_arn,
create_time,
kms_key_id,
additional_encryption_context,
tag_key,
tag_value
FROM aws.redshift.integration_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>integration_tags</code> resource, see <a href="/providers/aws/redshift/integrations/#permissions"><code>integrations</code></a>

