---
title: documentation_versions_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - documentation_versions_list_only
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

Lists <code>documentation_versions</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/documentation_versions/"><code>documentation_versions</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>documentation_versions_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The <code>AWS::ApiGateway::DocumentationVersion</code> resource creates a snapshot of the documentation for an API. For more information, see &#91;Representation of API Documentation in API Gateway&#93;(https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-documenting-api-content-representation.html) in the *API Gateway Developer Guide*.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.apigateway.documentation_versions_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>A description about the new documentation snapshot.</td></tr>
<tr><td><CopyableCode code="documentation_version" /></td><td><code>string</code></td><td>The version identifier of the to-be-updated documentation version.</td></tr>
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
Lists all <code>documentation_versions</code> in a region.
```sql
SELECT
region,
documentation_version,
rest_api_id
FROM aws.apigateway.documentation_versions_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>documentation_versions_list_only</code> resource, see <a href="/providers/aws/apigateway/documentation_versions/#permissions"><code>documentation_versions</code></a>


