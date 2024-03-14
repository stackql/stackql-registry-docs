---
title: rule
hide_title: false
hide_table_of_contents: false
keywords:
  - rule
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
Gets an individual <code>rule</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>rule</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>rule</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.vpclattice.rule</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>action</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>listener_identifier</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>match</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>priority</code></td><td><code>integer</code></td><td></td></tr>
<tr><td><code>service_identifier</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
action,
arn,
id,
listener_identifier,
match,
name,
priority,
service_identifier,
tags
FROM awscc.vpclattice.rule
WHERE data__Identifier = '<Arn>';
```

## Permissions

To operate on the <code>rule</code> resource, the following permissions are required:

### Read
```json
vpc-lattice:GetRule,
vpc-lattice:ListTagsForResource
```

### Update
```json
vpc-lattice:UpdateRule,
vpc-lattice:GetRule,
vpc-lattice:TagResource,
vpc-lattice:UntagResource
```

### Delete
```json
vpc-lattice:DeleteRule
```

