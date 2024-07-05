---
title: compute_environments_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - compute_environments_list_only
  - batch
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

Lists <code>compute_environments</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/compute_environments/"><code>compute_environments</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>compute_environments_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::Batch::ComputeEnvironment</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.batch.compute_environments_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="compute_environment_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="compute_environment_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="compute_resources" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="replace_compute_environment" /></td><td><code>boolean</code></td><td></td></tr>
<tr><td><CopyableCode code="service_role" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="state" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>object</code></td><td>A key-value pair to associate with a resource.</td></tr>
<tr><td><CopyableCode code="type" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="update_policy" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="unmanagedv_cpus" /></td><td><code>integer</code></td><td></td></tr>
<tr><td><CopyableCode code="eks_configuration" /></td><td><code>object</code></td><td></td></tr>
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
Lists all <code>compute_environments</code> in a region.
```sql
SELECT
region,
compute_environment_arn
FROM aws.batch.compute_environments_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>compute_environments_list_only</code> resource, see <a href="/providers/aws/batch/compute_environments/#permissions"><code>compute_environments</code></a>


