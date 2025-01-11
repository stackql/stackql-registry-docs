---
title: stages_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - stages_list_only
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

Lists <code>stages</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/stages/"><code>stages</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>stages_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The <code>AWS::ApiGateway::Stage</code> resource creates a stage for a deployment.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.apigateway.stages_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="rest_api_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="stage_name" /></td><td><code>string</code></td><td></td></tr>
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
Lists all <code>stages</code> in a region.
```sql
SELECT
region,
rest_api_id,
stage_name
FROM aws.apigateway.stages_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>stages_list_only</code> resource, see <a href="/providers/aws/apigateway/stages/#permissions"><code>stages</code></a>

