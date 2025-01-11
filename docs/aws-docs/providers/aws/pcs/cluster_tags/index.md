---
title: cluster_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - cluster_tags
  - pcs
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

Expands all tag keys and values for <code>clusters</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>cluster_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>AWS::PCS::Cluster resource creates an AWS PCS cluster.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.pcs.cluster_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The unique Amazon Resource Name (ARN) of the cluster.</td></tr>
<tr><td><CopyableCode code="endpoints" /></td><td><code>array</code></td><td>The list of endpoints available for interaction with the scheduler.</td></tr>
<tr><td><CopyableCode code="error_info" /></td><td><code>array</code></td><td>The list of errors that occurred during cluster provisioning.</td></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td>The generated unique ID of the cluster.</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name that identifies the cluster.</td></tr>
<tr><td><CopyableCode code="networking" /></td><td><code>object</code></td><td>The networking configuration for the cluster's control plane.</td></tr>
<tr><td><CopyableCode code="scheduler" /></td><td><code>object</code></td><td>The cluster management and job scheduling software associated with the cluster.</td></tr>
<tr><td><CopyableCode code="size" /></td><td><code>string</code></td><td>The size of the cluster.</td></tr>
<tr><td><CopyableCode code="slurm_configuration" /></td><td><code>object</code></td><td>Additional options related to the Slurm scheduler.</td></tr>
<tr><td><CopyableCode code="status" /></td><td><code>string</code></td><td>The provisioning status of the cluster. The provisioning status doesn't indicate the overall health of the cluster.</td></tr>
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
Expands tags for all <code>clusters</code> in a region.
```sql
SELECT
region,
arn,
endpoints,
error_info,
id,
name,
networking,
scheduler,
size,
slurm_configuration,
status,
tag_key,
tag_value
FROM aws.pcs.cluster_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>cluster_tags</code> resource, see <a href="/providers/aws/pcs/clusters/#permissions"><code>clusters</code></a>

