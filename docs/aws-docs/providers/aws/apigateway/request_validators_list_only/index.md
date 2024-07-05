---
title: request_validators_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - request_validators_list_only
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

Lists <code>request_validators</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/request_validators/"><code>request_validators</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>request_validators_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The <code>AWS::ApiGateway::RequestValidator</code> resource sets up basic validation rules for incoming requests to your API. For more information, see &#91;Enable Basic Request Validation for an API in API Gateway&#93;(https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-method-request-validation.html) in the *API Gateway Developer Guide*.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.apigateway.request_validators_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="request_validator_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name of this RequestValidator</td></tr>
<tr><td><CopyableCode code="rest_api_id" /></td><td><code>string</code></td><td>The string identifier of the associated RestApi.</td></tr>
<tr><td><CopyableCode code="validate_request_body" /></td><td><code>boolean</code></td><td>A Boolean flag to indicate whether to validate a request body according to the configured Model schema.</td></tr>
<tr><td><CopyableCode code="validate_request_parameters" /></td><td><code>boolean</code></td><td>A Boolean flag to indicate whether to validate request parameters (<code>true</code>) or not (<code>false</code>).</td></tr>
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
Lists all <code>request_validators</code> in a region.
```sql
SELECT
region,
rest_api_id,
request_validator_id
FROM aws.apigateway.request_validators_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>request_validators_list_only</code> resource, see <a href="/providers/aws/apigateway/request_validators/#permissions"><code>request_validators</code></a>


