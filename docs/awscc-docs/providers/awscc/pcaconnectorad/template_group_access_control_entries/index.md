---
title: template_group_access_control_entries
hide_title: false
hide_table_of_contents: false
keywords:
  - template_group_access_control_entries
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
Retrieves a list of <code>template_group_access_control_entries</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>template_group_access_control_entries</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>template_group_access_control_entries</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.pcaconnectorad.template_group_access_control_entries</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>group_security_identifier</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>template_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>template_group_access_control_entries</code> resource, the following permissions are required:

### Create
```json
pca-connector-ad:CreateTemplateGroupAccessControlEntry
```

### List
```json
pca-connector-ad:ListTemplateGroupAccessControlEntries
```


## Example
```sql
SELECT
region,
group_security_identifier,
template_arn
FROM awscc.pcaconnectorad.template_group_access_control_entries
WHERE region = 'us-east-1'
```
