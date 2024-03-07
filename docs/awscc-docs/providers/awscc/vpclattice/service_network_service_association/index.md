---
title: service_network_service_association
hide_title: false
hide_table_of_contents: false
keywords:
  - service_network_service_association
  - vpclattice
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>service_network_service_association</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>service_network_service_association</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>service_network_service_association</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.vpclattice.service_network_service_association</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>created_at</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>dns_entry</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>service_network_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>service_network_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>service_network_identifier</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>service_network_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>service_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>service_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>service_identifier</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>service_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>status</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
arn,
created_at,
dns_entry,
id,
service_network_arn,
service_network_id,
service_network_identifier,
service_network_name,
service_arn,
service_id,
service_identifier,
service_name,
status,
tags
FROM awscc.vpclattice.service_network_service_association
WHERE region = 'us-east-1'
AND data__Identifier = '{Arn}';
```

## Permissions

To operate on the <code>service_network_service_association</code> resource, the following permissions are required:

### Read
```json
vpc-lattice:GetServiceNetworkServiceAssociation,
vpc-lattice:ListTagsForResource
```

### Update
```json
vpc-lattice:TagResource,
vpc-lattice:UntagResource,
vpc-lattice:GetServiceNetworkServiceAssociation,
vpc-lattice:ListTagsForResource
```

### Delete
```json
vpc-lattice:DeleteServiceNetworkServiceAssociation,
vpc-lattice:GetServiceNetworkServiceAssociation
```

