---
title: stage_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - stage_tags
  - apigateway
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

Expands all tag keys and values for <code>stages</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>stage_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The <code>AWS::ApiGateway::Stage</code> resource creates a stage for a deployment.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.apigateway.stage_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="access_log_setting" /></td><td><code>object</code></td><td>The <code>AccessLogSetting</code> property type specifies settings for logging access in this stage.<br /><code>AccessLogSetting</code> is a property of the &#91;AWS::ApiGateway::Stage&#93;(https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-stage.html) resource.</td></tr>
<tr><td><CopyableCode code="cache_cluster_enabled" /></td><td><code>boolean</code></td><td></td></tr>
<tr><td><CopyableCode code="cache_cluster_size" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="canary_setting" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="client_certificate_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="deployment_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="documentation_version" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="method_settings" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="rest_api_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="stage_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="tracing_enabled" /></td><td><code>boolean</code></td><td></td></tr>
<tr><td><CopyableCode code="variables" /></td><td><code>object</code></td><td>A map (string-to-string map) that defines the stage variables, where the variable name is the key and the variable value is the value. Variable names are limited to alphanumeric characters. Values must match the following regular expression: <code>&#91;A-Za-z0-9-._~:/?#&=,&#93;+</code>.</td></tr>
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
Expands tags for all <code>stages</code> in a region.
```sql
SELECT
region,
access_log_setting,
cache_cluster_enabled,
cache_cluster_size,
canary_setting,
client_certificate_id,
deployment_id,
description,
documentation_version,
method_settings,
rest_api_id,
stage_name,
tracing_enabled,
variables,
tag_key,
tag_value
FROM aws.apigateway.stage_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>stage_tags</code> resource, see <a href="/providers/aws/apigateway/stages/#permissions"><code>stages</code></a>

