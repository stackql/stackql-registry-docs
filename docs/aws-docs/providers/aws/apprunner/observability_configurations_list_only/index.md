---
title: observability_configurations_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - observability_configurations_list_only
  - apprunner
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

Lists <code>observability_configurations</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/observability_configurations/"><code>observability_configurations</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>observability_configurations_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::AppRunner::ObservabilityConfiguration resource is an AWS App Runner resource type that specifies an App Runner observability configuration</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.apprunner.observability_configurations_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="observability_configuration_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of this ObservabilityConfiguration</td></tr>
<tr><td><CopyableCode code="observability_configuration_name" /></td><td><code>string</code></td><td>A name for the observability configuration. When you use it for the first time in an AWS Region, App Runner creates revision number 1 of this name. When you use the same name in subsequent calls, App Runner creates incremental revisions of the configuration.</td></tr>
<tr><td><CopyableCode code="observability_configuration_revision" /></td><td><code>integer</code></td><td>The revision of this observability configuration. It's unique among all the active configurations ('Status': 'ACTIVE') that share the same ObservabilityConfigurationName.</td></tr>
<tr><td><CopyableCode code="latest" /></td><td><code>boolean</code></td><td>It's set to true for the configuration with the highest Revision among all configurations that share the same Name. It's set to false otherwise.</td></tr>
<tr><td><CopyableCode code="trace_configuration" /></td><td><code>object</code></td><td>The configuration of the tracing feature within this observability configuration. If you don't specify it, App Runner doesn't enable tracing.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>A list of metadata items that you can associate with your observability configuration resource. A tag is a key-value pair.</td></tr>
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
Lists all <code>observability_configurations</code> in a region.
```sql
SELECT
region,
observability_configuration_arn
FROM aws.apprunner.observability_configurations_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>observability_configurations_list_only</code> resource, see <a href="/providers/aws/apprunner/observability_configurations/#permissions"><code>observability_configurations</code></a>


