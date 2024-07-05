---
title: applications_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - applications_list_only
  - emrserverless
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

Lists <code>applications</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/applications/"><code>applications</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>applications_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::EMRServerless::Application Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.emrserverless.applications_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="architecture" /></td><td><code>string</code></td><td>The cpu architecture of an application.</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>User friendly Application name.</td></tr>
<tr><td><CopyableCode code="release_label" /></td><td><code>string</code></td><td>EMR release label.</td></tr>
<tr><td><CopyableCode code="type" /></td><td><code>string</code></td><td>The type of the application</td></tr>
<tr><td><CopyableCode code="initial_capacity" /></td><td><code>array</code></td><td>Initial capacity initialized when an Application is started.</td></tr>
<tr><td><CopyableCode code="maximum_capacity" /></td><td><code>object</code></td><td>Maximum allowed cumulative resources for an Application. No new resources will be created once the limit is hit.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>Tag map with key and value</td></tr>
<tr><td><CopyableCode code="auto_start_configuration" /></td><td><code>object</code></td><td>Configuration for Auto Start of Application.</td></tr>
<tr><td><CopyableCode code="auto_stop_configuration" /></td><td><code>object</code></td><td>Configuration for Auto Stop of Application.</td></tr>
<tr><td><CopyableCode code="image_configuration" /></td><td><code>object</code></td><td>The image configuration.</td></tr>
<tr><td><CopyableCode code="monitoring_configuration" /></td><td><code>object</code></td><td>Monitoring configuration for batch and interactive JobRun.</td></tr>
<tr><td><CopyableCode code="runtime_configuration" /></td><td><code>array</code></td><td>Runtime configuration for batch and interactive JobRun.</td></tr>
<tr><td><CopyableCode code="network_configuration" /></td><td><code>object</code></td><td>Network Configuration for customer VPC connectivity.</td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the EMR Serverless Application.</td></tr>
<tr><td><CopyableCode code="application_id" /></td><td><code>string</code></td><td>The ID of the EMR Serverless Application.</td></tr>
<tr><td><CopyableCode code="worker_type_specifications" /></td><td><code>object</code></td><td>The key-value pairs that specify worker type to WorkerTypeSpecificationInput. This parameter must contain all valid worker types for a Spark or Hive application. Valid worker types include Driver and Executor for Spark applications and HiveDriver and TezTask for Hive applications. You can either set image details in this parameter for each worker type, or in imageConfiguration for all worker types.</td></tr>
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
Lists all <code>applications</code> in a region.
```sql
SELECT
region,
application_id
FROM aws.emrserverless.applications_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>applications_list_only</code> resource, see <a href="/providers/aws/emrserverless/applications/#permissions"><code>applications</code></a>


