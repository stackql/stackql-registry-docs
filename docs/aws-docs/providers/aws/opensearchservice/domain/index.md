---
title: domain
hide_title: false
hide_table_of_contents: false
keywords:
  - domain
  - opensearchservice
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

Gets or operates on an individual <code>domain</code> resource, use <code>domains</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>domain</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>An example resource schema demonstrating some basic constructs and validation rules.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.opensearchservice.domain" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="cluster_config" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="domain_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="access_policies" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="ip_address_type" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="engine_version" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="advanced_options" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="log_publishing_options" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="snapshot_options" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="vpc_options" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="node_to_node_encryption_options" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="domain_endpoint_options" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="cognito_options" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="advanced_security_options" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="domain_endpoint" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="domain_endpoint_v2" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="domain_endpoints" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="ebs_options" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="domain_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="encryption_at_rest_options" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>An arbitrary set of tags (key-value pairs) for this Domain.</td></tr>
<tr><td><CopyableCode code="service_software_options" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="off_peak_window_options" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="software_update_options" /></td><td><code>object</code></td><td></td></tr>
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
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
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
cluster_config,
domain_name,
access_policies,
ip_address_type,
engine_version,
advanced_options,
log_publishing_options,
snapshot_options,
vpc_options,
node_to_node_encryption_options,
domain_endpoint_options,
cognito_options,
advanced_security_options,
domain_endpoint,
domain_endpoint_v2,
domain_endpoints,
ebs_options,
id,
arn,
domain_arn,
encryption_at_rest_options,
tags,
service_software_options,
off_peak_window_options,
software_update_options
FROM aws.opensearchservice.domain
WHERE data__Identifier = '<DomainName>';
```

## Permissions

To operate on the <code>domain</code> resource, the following permissions are required:

### Read
```json
es:DescribeDomain,
es:ListTags
```

### Update
```json
es:UpdateDomain,
es:UpgradeDomain,
es:DescribeDomain,
es:AddTags,
es:RemoveTags,
es:ListTags,
es:DescribeDomainChangeProgress
```

### Delete
```json
es:DeleteDomain,
es:DescribeDomain
```

