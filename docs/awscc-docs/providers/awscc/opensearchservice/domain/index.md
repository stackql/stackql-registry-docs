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
Gets an individual <code>domain</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>domain</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>domain</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.opensearchservice.domain</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>cluster_config</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>domain_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>access_policies</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>ip_address_type</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>engine_version</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>advanced_options</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>log_publishing_options</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>snapshot_options</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>vpc_options</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>node_to_node_encryption_options</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>domain_endpoint_options</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>cognito_options</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>advanced_security_options</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>domain_endpoint</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>domain_endpoint_v2</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>domain_endpoints</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>ebs_options</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>domain_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>encryption_at_rest_options</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>An arbitrary set of tags (key-value pairs) for this Domain.</td></tr>
<tr><td><code>service_software_options</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>off_peak_window_options</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>software_update_options</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
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
FROM awscc.opensearchservice.domain
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

