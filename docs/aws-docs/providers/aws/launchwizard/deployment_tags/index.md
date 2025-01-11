---
title: deployment_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - deployment_tags
  - launchwizard
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

Expands all tag keys and values for <code>deployments</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>deployment_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::LaunchWizard::Deployment Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.launchwizard.deployment_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>ARN of the LaunchWizard deployment</td></tr>
<tr><td><CopyableCode code="created_at" /></td><td><code>string</code></td><td>Timestamp of LaunchWizard deployment creation</td></tr>
<tr><td><CopyableCode code="deleted_at" /></td><td><code>string</code></td><td>Timestamp of LaunchWizard deployment deletion</td></tr>
<tr><td><CopyableCode code="deployment_id" /></td><td><code>string</code></td><td>Deployment ID of the LaunchWizard deployment</td></tr>
<tr><td><CopyableCode code="deployment_pattern_name" /></td><td><code>string</code></td><td>Workload deployment pattern name</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>Name of LaunchWizard deployment</td></tr>
<tr><td><CopyableCode code="resource_group" /></td><td><code>string</code></td><td>Resource Group Name created for LaunchWizard deployment</td></tr>
<tr><td><CopyableCode code="specifications" /></td><td><code>object</code></td><td>LaunchWizard deployment specifications</td></tr>
<tr><td><CopyableCode code="status" /></td><td><code>string</code></td><td>Status of LaunchWizard deployment</td></tr>
<tr><td><CopyableCode code="workload_name" /></td><td><code>string</code></td><td>Workload Name for LaunchWizard deployment</td></tr>
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
Expands tags for all <code>deployments</code> in a region.
```sql
SELECT
region,
arn,
created_at,
deleted_at,
deployment_id,
deployment_pattern_name,
name,
resource_group,
specifications,
status,
workload_name,
tag_key,
tag_value
FROM aws.launchwizard.deployment_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>deployment_tags</code> resource, see <a href="/providers/aws/launchwizard/deployments/#permissions"><code>deployments</code></a>

