---
title: privacy_budget_template
hide_title: false
hide_table_of_contents: false
keywords:
  - privacy_budget_template
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
Gets or operates on an individual <code>privacy_budget_template</code> resource, use <code>privacy_budget_templates</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>privacy_budget_template</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Represents a privacy budget within a collaboration</td></tr>
<tr><td><b>Id</b></td><td><code>aws.cleanrooms.privacy_budget_template</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>collaboration_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>collaboration_identifier</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>privacy_budget_template_identifier</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>An arbitrary set of tags (key-value pairs) for this cleanrooms privacy budget template.</td></tr>
<tr><td><code>auto_refresh</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>privacy_budget_type</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>parameters</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>membership_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>membership_identifier</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods

<table><tbody>
  <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
  </tr>
  <tr>
    <td><code>update_resource</code></td>
    <td><code>UPDATE</code></td>
    <td><code>data__Identifier, data__PatchDocument, region</code></td>
  </tr>
  <tr>
    <td><code>delete_resource</code></td>
    <td><code>DELETE</code></td>
    <td><code>data__Identifier, region</code></td>
  </tr>
  <tr>
    <td><code>get_resource</code></td>
    <td><code>SELECT</code></td>
    <td><code>data__Identifier, region</code></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
arn,
collaboration_arn,
collaboration_identifier,
privacy_budget_template_identifier,
tags,
auto_refresh,
privacy_budget_type,
parameters,
membership_arn,
membership_identifier
FROM aws.cleanrooms.privacy_budget_template
WHERE data__Identifier = '<PrivacyBudgetTemplateIdentifier>|<MembershipIdentifier>';
```

## Permissions

To operate on the <code>privacy_budget_template</code> resource, the following permissions are required:

### Read
```json
cleanrooms:GetPrivacyBudgetTemplate,
cleanrooms:ListTagsForResource
```

### Update
```json
cleanrooms:UpdatePrivacyBudgetTemplate,
cleanrooms:GetPrivacyBudgetTemplate,
cleanrooms:ListTagsForResource,
cleanrooms:TagResource,
cleanrooms:UntagResource
```

### Delete
```json
cleanrooms:DeletePrivacyBudgetTemplate,
cleanrooms:GetPrivacyBudgetTemplate,
cleanrooms:ListPrivacyBudgetTemplates,
cleanrooms:ListTagsForResource,
cleanrooms:UntagResource
```

