---
title: replication_config_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - replication_config_tags
  - dms
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

Expands all tag keys and values for <code>replication_configs</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>replication_config_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>A replication configuration that you later provide to configure and start a AWS DMS Serverless replication</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.dms.replication_config_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="replication_config_identifier" /></td><td><code>string</code></td><td>A unique identifier of replication configuration</td></tr>
<tr><td><CopyableCode code="replication_config_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the Replication Config</td></tr>
<tr><td><CopyableCode code="source_endpoint_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the source endpoint for this AWS DMS Serverless replication configuration</td></tr>
<tr><td><CopyableCode code="target_endpoint_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the target endpoint for this AWS DMS Serverless replication configuration</td></tr>
<tr><td><CopyableCode code="replication_type" /></td><td><code>string</code></td><td>The type of AWS DMS Serverless replication to provision using this replication configuration</td></tr>
<tr><td><CopyableCode code="compute_config" /></td><td><code>object</code></td><td>Configuration parameters for provisioning a AWS DMS Serverless replication</td></tr>
<tr><td><CopyableCode code="replication_settings" /></td><td><code>object</code></td><td>JSON settings for Servereless replications that are provisioned using this replication configuration</td></tr>
<tr><td><CopyableCode code="supplemental_settings" /></td><td><code>object</code></td><td>JSON settings for specifying supplemental data</td></tr>
<tr><td><CopyableCode code="resource_identifier" /></td><td><code>string</code></td><td>A unique value or name that you get set for a given resource that can be used to construct an Amazon Resource Name (ARN) for that resource</td></tr>
<tr><td><CopyableCode code="table_mappings" /></td><td><code>object</code></td><td>JSON table mappings for AWS DMS Serverless replications that are provisioned using this replication configuration</td></tr>
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
Expands tags for all <code>replication_configs</code> in a region.
```sql
SELECT
region,
replication_config_identifier,
replication_config_arn,
source_endpoint_arn,
target_endpoint_arn,
replication_type,
compute_config,
replication_settings,
supplemental_settings,
resource_identifier,
table_mappings,
tag_key,
tag_value
FROM aws.dms.replication_config_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>replication_config_tags</code> resource, see <a href="/providers/aws/dms/replication_configs/#permissions"><code>replication_configs</code></a>

