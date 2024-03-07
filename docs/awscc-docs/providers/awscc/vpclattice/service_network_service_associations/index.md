---
title: service_network_service_associations
hide_title: false
hide_table_of_contents: false
keywords:
  - service_network_service_associations
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
Retrieves a list of <code>service_network_service_associations</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>service_network_service_associations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>service_network_service_associations</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.vpclattice.service_network_service_associations</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
arn
FROM awscc.vpclattice.service_network_service_associations
WHERE region = 'us-east-1'
```

## Permissions

To operate on the <code>service_network_service_associations</code> resource, the following permissions are required:

### Create
```json
vpc-lattice:CreateServiceNetworkServiceAssociation,
vpc-lattice:GetServiceNetworkServiceAssociation,
vpc-lattice:TagResource,
vpc-lattice:ListTagsForResource
```

### List
```json
vpc-lattice:ListServiceNetworkServiceAssociations
```

