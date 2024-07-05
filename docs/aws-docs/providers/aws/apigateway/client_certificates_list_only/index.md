---
title: client_certificates_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - client_certificates_list_only
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

Lists <code>client_certificates</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/client_certificates/"><code>client_certificates</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>client_certificates_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The <code>AWS::ApiGateway::ClientCertificate</code> resource creates a client certificate that API Gateway uses to configure client-side SSL authentication for sending requests to the integration endpoint.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.apigateway.client_certificates_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="client_certificate_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>The description of the client certificate.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>The collection of tags. Each tag element is associated with a given resource.</td></tr>
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
Lists all <code>client_certificates</code> in a region.
```sql
SELECT
region,
client_certificate_id
FROM aws.apigateway.client_certificates_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>client_certificates_list_only</code> resource, see <a href="/providers/aws/apigateway/client_certificates/#permissions"><code>client_certificates</code></a>


