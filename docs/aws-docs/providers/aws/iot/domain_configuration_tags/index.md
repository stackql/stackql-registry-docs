---
title: domain_configuration_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - domain_configuration_tags
  - iot
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

Expands all tag keys and values for <code>domain_configurations</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>domain_configuration_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Create and manage a Domain Configuration</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.iot.domain_configuration_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="domain_configuration_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="authorizer_config" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="domain_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="server_certificate_arns" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="service_type" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="validation_certificate_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="domain_configuration_status" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="domain_type" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="server_certificate_config" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="server_certificates" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="tls_config" /></td><td><code>object</code></td><td></td></tr>
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
Expands tags for all <code>domain_configurations</code> in a region.
```sql
SELECT
region,
domain_configuration_name,
authorizer_config,
domain_name,
server_certificate_arns,
service_type,
validation_certificate_arn,
arn,
domain_configuration_status,
domain_type,
server_certificate_config,
server_certificates,
tls_config,
tag_key,
tag_value
FROM aws.iot.domain_configuration_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>domain_configuration_tags</code> resource, see <a href="/providers/aws/iot/domain_configurations/#permissions"><code>domain_configurations</code></a>


