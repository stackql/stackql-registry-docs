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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';


Used to retrieve a list of <code>application_entitlement_associations</code> in a region or to create or delete a <code>application_entitlement_associations</code> resource, use <code>application_entitlement_association</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>application_entitlement_associations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::AppStream::ApplicationEntitlementAssociation</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.appstream.application_entitlement_associations" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="stack_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="entitlement_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="application_identifier" /></td><td><code>string</code></td><td></td></tr>
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
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
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
stack_name,
entitlement_name,
application_identifier
FROM aws.appstream.application_entitlement_associations
WHERE region = 'us-east-1';
```

## `INSERT` Example

<Tabs
    defaultValue="required"
    values={[
      { label: 'Required Properties', value: 'required', },
      { label: 'All Properties', value: 'all', },

    ]
}>
<TabItem value="required">

```sql
<<<json
{
 "StackName": "{{ StackName }}",
 "EntitlementName": "{{ EntitlementName }}",
 "ApplicationIdentifier": "{{ ApplicationIdentifier }}"
}
>>>
--required properties only
INSERT INTO aws.appstream.application_entitlement_associations (
 StackName,
 EntitlementName,
 ApplicationIdentifier,
 region
)
SELECT 
{{ StackName }},
 {{ EntitlementName }},
 {{ ApplicationIdentifier }},
'us-east-1';
```

</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "StackName": "{{ StackName }}",
 "EntitlementName": "{{ EntitlementName }}",
 "ApplicationIdentifier": "{{ ApplicationIdentifier }}"
}
>>>
--all properties
INSERT INTO aws.appstream.application_entitlement_associations (
 StackName,
 EntitlementName,
 ApplicationIdentifier,
 region
)
SELECT 
 {{ StackName }},
 {{ EntitlementName }},
 {{ ApplicationIdentifier }},
 'us-east-1';
```

</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.appstream.application_entitlement_associations
WHERE data__Identifier = '<StackName|EntitlementName|ApplicationIdentifier>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>application_entitlement_associations</code> resource, the following permissions are required:

### Create
```json
appstream:AssociateApplicationToEntitlement,
appstream:ListEntitledApplications
```

### Delete
```json
appstream:DisassociateApplicationFromEntitlement,
appstream:ListEntitledApplications
```

