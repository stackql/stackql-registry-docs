---
title: tls_inspection_configuration
hide_title: false
hide_table_of_contents: false
keywords:
  - tls_inspection_configuration
  - networkfirewall
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


Gets or updates an individual <code>tls_inspection_configuration</code> resource, use <code>tls_inspection_configurations</code> to retrieve a list of resources or to create or delete a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>tls_inspection_configuration</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource type definition for AWS::NetworkFirewall::TLSInspectionConfiguration</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.networkfirewall.tls_inspection_configuration" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="tls_inspection_configuration_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="tls_inspection_configuration_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="tls_inspection_configuration" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="tls_inspection_configuration_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td></td></tr>
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
tls_inspection_configuration_name,
tls_inspection_configuration_arn,
tls_inspection_configuration,
tls_inspection_configuration_id,
description,
tags
FROM aws.networkfirewall.tls_inspection_configuration
WHERE region = 'us-east-1' AND data__Identifier = '<TLSInspectionConfigurationArn>';
```


## Permissions

To operate on the <code>tls_inspection_configuration</code> resource, the following permissions are required:

### Read
```json
network-firewall:DescribeTLSInspectionConfiguration,
network-firewall:ListTagsForResources
```

### Update
```json
network-firewall:UpdateTLSInspectionConfiguration,
network-firewall:DescribeTLSInspectionConfiguration,
network-firewall:TagResource,
network-firewall:UntagResource
```

