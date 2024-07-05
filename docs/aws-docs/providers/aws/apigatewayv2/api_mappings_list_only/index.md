---
title: api_mappings_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - api_mappings_list_only
  - apigatewayv2
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

Lists <code>api_mappings</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/api_mappings/"><code>api_mappings</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>api_mappings_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The <code>AWS::ApiGatewayV2::ApiMapping</code> resource contains an API mapping. An API mapping relates a path of your custom domain name to a stage of your API. A custom domain name can have multiple API mappings, but the paths can't overlap. A custom domain can map only to APIs of the same protocol type. For more information, see &#91;CreateApiMapping&#93;(https://docs.aws.amazon.com/apigatewayv2/latest/api-reference/domainnames-domainname-apimappings.html#CreateApiMapping) in the *Amazon API Gateway V2 API Reference*.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.apigatewayv2.api_mappings_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="api_mapping_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="domain_name" /></td><td><code>string</code></td><td>The domain name.</td></tr>
<tr><td><CopyableCode code="stage" /></td><td><code>string</code></td><td>The API stage.</td></tr>
<tr><td><CopyableCode code="api_mapping_key" /></td><td><code>string</code></td><td>The API mapping key.</td></tr>
<tr><td><CopyableCode code="api_id" /></td><td><code>string</code></td><td>The identifier of the API.</td></tr>
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
Lists all <code>api_mappings</code> in a region.
```sql
SELECT
region,
api_mapping_id,
domain_name
FROM aws.apigatewayv2.api_mappings_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>api_mappings_list_only</code> resource, see <a href="/providers/aws/apigatewayv2/api_mappings/#permissions"><code>api_mappings</code></a>


