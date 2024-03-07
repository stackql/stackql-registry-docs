---
title: configured_table_associations
hide_title: false
hide_table_of_contents: false
keywords:
  - configured_table_associations
  - cleanrooms
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>configured_table_associations</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>configured_table_associations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>configured_table_associations</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.cleanrooms.configured_table_associations</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>configured_table_association_identifier</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>membership_identifier</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>configured_table_associations</code> resource, the following permissions are required:

### Create
<pre>
cleanrooms:CreateConfiguredTableAssociation,
iam:PassRole,
cleanrooms:ListTagsForResource,
cleanrooms:TagResource,
cleanrooms:GetConfiguredTableAssociation,
cleanrooms:ListConfiguredTableAssociations</pre>

### List
<pre>
cleanrooms:ListConfiguredTableAssociations</pre>


## Example
```sql
SELECT
region,
configured_table_association_identifier,
membership_identifier
FROM awscc.cleanrooms.configured_table_associations
WHERE region = 'us-east-1'
```
