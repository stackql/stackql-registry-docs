---
title: listener
hide_title: false
hide_table_of_contents: false
keywords:
  - listener
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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';

Gets or operates on an individual <code>listener</code> resource, use <code>listeners</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>listener</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Creates a listener for a service. Before you start using your Amazon VPC Lattice service, you must add one or more listeners. A listener is a process that checks for connection requests to your services.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.vpclattice.listener" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="default_action" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="port" /></td><td><code>integer</code></td><td></td></tr>
<tr><td><CopyableCode code="protocol" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="service_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="service_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="service_identifier" /></td><td><code>string</code></td><td></td></tr>
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
arn,
default_action,
id,
name,
port,
protocol,
service_arn,
service_id,
service_identifier,
tags
FROM aws.vpclattice.listener
WHERE data__Identifier = '<Arn>';
```

## Permissions

To operate on the <code>listener</code> resource, the following permissions are required:

### Read
```json
vpc-lattice:GetListener,
vpc-lattice:ListTagsForResource
```

### Update
```json
vpc-lattice:UpdateListener,
vpc-lattice:TagResource,
vpc-lattice:UntagResource,
vpc-lattice:GetListener,
vpc-lattice:ListTagsForResource
```

### Delete
```json
vpc-lattice:DeleteListener
```

