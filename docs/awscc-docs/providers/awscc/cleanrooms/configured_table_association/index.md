---
title: configured_table_association
hide_title: false
hide_table_of_contents: false
keywords:
  - configured_table_association
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
Gets an individual <code>configured_table_association</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>configured_table_association</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>configured_table_association</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.cleanrooms.configured_table_association</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>An arbitrary set of tags (key-value pairs) for this cleanrooms collaboration.</td></tr>
<tr><td><code>configured_table_association_identifier</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>configured_table_identifier</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>membership_identifier</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>role_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>configured_table_association</code> resource, the following permissions are required:

### Read
```json
cleanrooms:GetConfiguredTableAssociation,
cleanrooms:ListTagsForResource
```

### Update
```json
cleanrooms:UpdateConfiguredTableAssociation,
cleanrooms:GetConfiguredTableAssociation,
iam:PassRole,
cleanrooms:ListTagsForResource,
cleanrooms:TagResource,
cleanrooms:UntagResource
```

### Delete
```json
cleanrooms:DeleteConfiguredTableAssociation,
cleanrooms:GetConfiguredTableAssociation,
cleanrooms:ListConfiguredTableAssociations,
cleanrooms:ListTagsForResource,
cleanrooms:UntagResource
```


## Example
```sql
SELECT
region,
arn,
tags,
configured_table_association_identifier,
configured_table_identifier,
description,
membership_identifier,
name,
role_arn
FROM awscc.cleanrooms.configured_table_association
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;ConfiguredTableAssociationIdentifier&gt;'
AND data__Identifier = '&lt;MembershipIdentifier&gt;'
```
