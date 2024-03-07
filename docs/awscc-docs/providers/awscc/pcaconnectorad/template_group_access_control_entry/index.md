---
title: template_group_access_control_entry
hide_title: false
hide_table_of_contents: false
keywords:
  - template_group_access_control_entry
  - pcaconnectorad
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>template_group_access_control_entry</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>template_group_access_control_entry</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>template_group_access_control_entry</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.pcaconnectorad.template_group_access_control_entry</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>access_rights</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>group_display_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>group_security_identifier</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>template_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
access_rights,
group_display_name,
group_security_identifier,
template_arn
FROM awscc.pcaconnectorad.template_group_access_control_entry
WHERE region = 'us-east-1'
AND data__Identifier = '{GroupSecurityIdentifier}';
AND data__Identifier = '{TemplateArn}';
```

## Permissions

To operate on the <code>template_group_access_control_entry</code> resource, the following permissions are required:

### Read
```json
pca-connector-ad:GetTemplateGroupAccessControlEntry
```

### Update
```json
pca-connector-ad:UpdateTemplateGroupAccessControlEntry
```

### Delete
```json
pca-connector-ad:DeleteTemplateGroupAccessControlEntry,
pca-connector-ad:GetTemplateGroupAccessControlEntry
```

