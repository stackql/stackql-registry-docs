---
title: resources_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - resources_list_only
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

Lists <code>resources</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/resources/"><code>resources</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>resources_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The <code>AWS::ApiGateway::Resource</code> resource creates a resource in an API.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.apigateway.resources_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="parent_id" /></td><td><code>string</code></td><td>The parent resource's identifier.</td></tr>
<tr><td><CopyableCode code="path_part" /></td><td><code>string</code></td><td>The last path segment for this resource.</td></tr>
<tr><td><CopyableCode code="resource_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="rest_api_id" /></td><td><code>string</code></td><td>The string identifier of the associated RestApi.</td></tr>
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
Lists all <code>resources</code> in a region.
```sql
SELECT
region,
rest_api_id,
resource_id
FROM aws.apigateway.resources_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>resources_list_only</code> resource, see <a href="/providers/aws/apigateway/resources/#permissions"><code>resources</code></a>


