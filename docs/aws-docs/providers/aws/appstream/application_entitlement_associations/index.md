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

Creates, updates, deletes or gets an <code>application_entitlement_association</code> resource or lists <code>application_entitlement_associations</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>application_entitlement_associations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::AppStream::ApplicationEntitlementAssociation</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.appstream.application_entitlement_associations" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="stack_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="entitlement_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="application_identifier" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-applicationentitlementassociation.html"><code>AWS::AppStream::ApplicationEntitlementAssociation</code></a>.

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
    <td><CopyableCode code="StackName, EntitlementName, ApplicationIdentifier, region" /></td>
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

## `SELECT` examples

Gets all properties from an individual <code>application_entitlement_association</code>.
```sql
SELECT
region,
stack_name,
entitlement_name,
application_identifier
FROM aws.appstream.application_entitlement_associations
WHERE region = 'us-east-1' AND data__Identifier = '<StackName>|<EntitlementName>|<ApplicationIdentifier>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>application_entitlement_association</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

<Tabs
    defaultValue="required"
    values={[
      { label: 'Required Properties', value: 'required', },
      { label: 'All Properties', value: 'all', },
      { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="required">

```sql
/*+ create */
INSERT INTO aws.appstream.application_entitlement_associations (
 StackName,
 EntitlementName,
 ApplicationIdentifier,
 region
)
SELECT 
'{{ StackName }}',
 '{{ EntitlementName }}',
 '{{ ApplicationIdentifier }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.appstream.application_entitlement_associations (
 StackName,
 EntitlementName,
 ApplicationIdentifier,
 region
)
SELECT 
 '{{ StackName }}',
 '{{ EntitlementName }}',
 '{{ ApplicationIdentifier }}',
 '{{ region }}';
```
</TabItem>
<TabItem value="manifest">

```yaml
version: 1
name: stack name
description: stack description
providers:
  - aws
globals:
  - name: region
    value: '{{ vars.AWS_REGION }}'
resources:
  - name: application_entitlement_association
    props:
      - name: StackName
        value: '{{ StackName }}'
      - name: EntitlementName
        value: '{{ EntitlementName }}'
      - name: ApplicationIdentifier
        value: '{{ ApplicationIdentifier }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
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

### Read
```json
appstream:ListEntitledApplications
```

### Delete
```json
appstream:DisassociateApplicationFromEntitlement,
appstream:ListEntitledApplications
```
