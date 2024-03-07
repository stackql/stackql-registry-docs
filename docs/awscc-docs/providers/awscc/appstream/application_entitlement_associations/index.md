---
title: application_entitlement_associations
hide_title: false
hide_table_of_contents: false
keywords:
  - application_entitlement_associations
  - appstream
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>application_entitlement_associations</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>application_entitlement_associations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>application_entitlement_associations</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.appstream.application_entitlement_associations</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>stack_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>entitlement_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>application_identifier</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>application_entitlement_associations</code> resource, the following permissions are required:

### Create
<pre>
appstream:AssociateApplicationToEntitlement,
appstream:ListEntitledApplications</pre>


## Example
```sql
SELECT
region,
stack_name,
entitlement_name,
application_identifier
FROM awscc.appstream.application_entitlement_associations
WHERE region = 'us-east-1'
```
