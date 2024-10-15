---
title: domain_ownership_identifiers
hide_title: false
hide_table_of_contents: false
keywords:
  - domain_ownership_identifiers
  - app_service
  - google
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/google/stackql-google-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>domain_ownership_identifiers</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>domain_ownership_identifiers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.app_service.domain_ownership_identifiers" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id. |
| <CopyableCode code="name" /> | `string` | Resource Name. |
| <CopyableCode code="kind" /> | `string` | Kind of resource. |
| <CopyableCode code="properties" /> | `object` | Identifier resource specific properties |
| <CopyableCode code="type" /> | `string` | Resource type. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="domainOwnershipIdentifierName, name, resourceGroupName, subscriptionId" /> | Description for Get domain ownership identifier for web app. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="name, resourceGroupName, subscriptionId" /> | Description for Lists ownership identifiers for domain associated with web app. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="domainOwnershipIdentifierName, name, resourceGroupName, subscriptionId" /> | Description for Creates a domain ownership identifier for web app, or updates an existing ownership identifier. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="domainOwnershipIdentifierName, name, resourceGroupName, subscriptionId" /> | Description for Deletes a domain ownership identifier for a web app. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="domainOwnershipIdentifierName, name, resourceGroupName, subscriptionId" /> | Description for Creates a domain ownership identifier for web app, or updates an existing ownership identifier. |

## `SELECT` examples

Description for Lists ownership identifiers for domain associated with web app.


```sql
SELECT
id,
name,
kind,
properties,
type
FROM azure.app_service.domain_ownership_identifiers
WHERE name = '{{ name }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>domain_ownership_identifiers</code> resource.

<Tabs
    defaultValue="all"
    values={[
        { label: 'All Properties', value: 'all', },
        { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO azure.app_service.domain_ownership_identifiers (
domainOwnershipIdentifierName,
name,
resourceGroupName,
subscriptionId,
kind,
properties
)
SELECT 
'{{ domainOwnershipIdentifierName }}',
'{{ name }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ kind }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: id
      value: string
    - name: name
      value: string
    - name: kind
      value: string
    - name: type
      value: string
    - name: properties
      value:
        - name: id
          value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>domain_ownership_identifiers</code> resource.

```sql
/*+ update */
UPDATE azure.app_service.domain_ownership_identifiers
SET 
kind = '{{ kind }}',
properties = '{{ properties }}'
WHERE 
domainOwnershipIdentifierName = '{{ domainOwnershipIdentifierName }}'
AND name = '{{ name }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>domain_ownership_identifiers</code> resource.

```sql
/*+ delete */
DELETE FROM azure.app_service.domain_ownership_identifiers
WHERE domainOwnershipIdentifierName = '{{ domainOwnershipIdentifierName }}'
AND name = '{{ name }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
