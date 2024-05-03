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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';

Used to retrieve a list of <code>template_group_access_control_entries</code> in a region or create a <code>template_group_access_control_entries</code> resource, use <code>template_group_access_control_entry</code> to operate on an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>template_group_access_control_entries</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::PCAConnectorAD::TemplateGroupAccessControlEntry Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.pcaconnectorad.template_group_access_control_entries" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="group_security_identifier" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="template_arn" /></td><td><code>string</code></td><td></td></tr>
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
    <td><CopyableCode code="create_resource" /></td>
    <td><code>INSERT</code></td>
    <td><CopyableCode code="data__DesiredState, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="list_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
group_security_identifier,
template_arn
FROM aws.pcaconnectorad.template_group_access_control_entries
WHERE region = 'us-east-1'
```

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

