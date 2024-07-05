---
title: security_configs_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - security_configs_list_only
  - opensearchserverless
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

Lists <code>security_configs</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/security_configs/"><code>security_configs</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>security_configs_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Amazon OpenSearchServerless security config resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.opensearchserverless.security_configs_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>Security config description</td></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td>The identifier of the security config</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The friendly name of the security config</td></tr>
<tr><td><CopyableCode code="saml_options" /></td><td><code>object</code></td><td>Describes saml options in form of key value map</td></tr>
<tr><td><CopyableCode code="type" /></td><td><code>string</code></td><td>Config type for security config</td></tr>
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
Lists all <code>security_configs</code> in a region.
```sql
SELECT
region,
id
FROM aws.opensearchserverless.security_configs_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>security_configs_list_only</code> resource, see <a href="/providers/aws/opensearchserverless/security_configs/#permissions"><code>security_configs</code></a>


