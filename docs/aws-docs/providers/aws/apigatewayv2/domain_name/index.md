---
title: domain_name
hide_title: false
hide_table_of_contents: false
keywords:
  - domain_name
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


Gets or updates an individual <code>domain_name</code> resource, use <code>domain_names</code> to retrieve a list of resources or to create or delete a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>domain_name</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The ``AWS::ApiGatewayV2::DomainName`` resource specifies a custom domain name for your API in Amazon API Gateway (API Gateway). &lt;br&#x2F;&gt; You can use a custom domain name to provide a URL that's more intuitive and easier to recall. For more information about using custom domain names, see &#91;Set up Custom Domain Name for an API in API Gateway&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;apigateway&#x2F;latest&#x2F;developerguide&#x2F;how-to-custom-domains.html) in the *API Gateway Developer Guide*.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.apigatewayv2.domain_name" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="mutual_tls_authentication" /></td><td><code>object</code></td><td>The mutual TLS authentication configuration for a custom domain name.</td></tr>
<tr><td><CopyableCode code="regional_hosted_zone_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="regional_domain_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="domain_name" /></td><td><code>string</code></td><td>The custom domain name for your API in Amazon API Gateway. Uppercase letters are not supported.</td></tr>
<tr><td><CopyableCode code="domain_name_configurations" /></td><td><code>array</code></td><td>The domain name configurations.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>object</code></td><td>The collection of tags associated with a domain name.</td></tr>
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
    <td><CopyableCode code="update_resource" /></td>
    <td><code>UPDATE</code></td>
    <td><CopyableCode code="data__Identifier, data__PatchDocument, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
mutual_tls_authentication,
regional_hosted_zone_id,
regional_domain_name,
domain_name,
domain_name_configurations,
tags
FROM aws.apigatewayv2.domain_name
WHERE region = 'us-east-1' AND data__Identifier = '<DomainName>';
```


## Permissions

To operate on the <code>domain_name</code> resource, the following permissions are required:

### Update
```json
apigateway:PATCH,
apigateway:GET,
apigateway:PUT
```

### Read
```json
apigateway:GET
```

