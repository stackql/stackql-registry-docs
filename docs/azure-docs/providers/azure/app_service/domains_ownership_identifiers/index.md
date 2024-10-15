---
title: domains_ownership_identifiers
hide_title: false
hide_table_of_contents: false
keywords:
  - domains_ownership_identifiers
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

Creates, updates, deletes, gets or lists a <code>domains_ownership_identifiers</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>domains_ownership_identifiers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.app_service.domains_ownership_identifiers" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id. |
| <CopyableCode code="name" /> | `string` | Resource Name. |
| <CopyableCode code="kind" /> | `string` | Kind of resource. |
| <CopyableCode code="properties" /> | `object` | DomainOwnershipIdentifier resource specific properties |
| <CopyableCode code="type" /> | `string` | Resource type. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="domainName, name, resourceGroupName, subscriptionId" /> | Description for Get ownership identifier for domain |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="domainName, resourceGroupName, subscriptionId" /> | Description for Lists domain ownership identifiers. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="domainName, name, resourceGroupName, subscriptionId" /> | Description for Creates an ownership identifier for a domain or updates identifier details for an existing identifier |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="domainName, name, resourceGroupName, subscriptionId" /> | Description for Delete ownership identifier for domain |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="domainName, name, resourceGroupName, subscriptionId" /> | Description for Creates an ownership identifier for a domain or updates identifier details for an existing identifier |

## `SELECT` examples

Description for Lists domain ownership identifiers.


```sql
SELECT
id,
name,
kind,
properties,
type
FROM azure.app_service.domains_ownership_identifiers
WHERE domainName = '{{ domainName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>domains_ownership_identifiers</code> resource.

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
INSERT INTO azure.app_service.domains_ownership_identifiers (
domainName,
name,
resourceGroupName,
subscriptionId,
kind,
properties
)
SELECT 
'{{ domainName }}',
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
        - name: ownershipId
          value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>domains_ownership_identifiers</code> resource.

```sql
/*+ update */
UPDATE azure.app_service.domains_ownership_identifiers
SET 
kind = '{{ kind }}',
properties = '{{ properties }}'
WHERE 
domainName = '{{ domainName }}'
AND name = '{{ name }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>domains_ownership_identifiers</code> resource.

```sql
/*+ delete */
DELETE FROM azure.app_service.domains_ownership_identifiers
WHERE domainName = '{{ domainName }}'
AND name = '{{ name }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
