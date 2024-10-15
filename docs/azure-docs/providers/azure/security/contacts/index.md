---
title: contacts
hide_title: false
hide_table_of_contents: false
keywords:
  - contacts
  - security
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

Creates, updates, deletes, gets or lists a <code>contacts</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>contacts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.security.contacts" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_contacts', value: 'view', },
        { label: 'contacts', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource Id |
| <CopyableCode code="name" /> | `text` | Resource name |
| <CopyableCode code="emails" /> | `text` | field from the `properties` object |
| <CopyableCode code="is_enabled" /> | `text` | field from the `properties` object |
| <CopyableCode code="notifications_by_role" /> | `text` | field from the `properties` object |
| <CopyableCode code="notifications_sources" /> | `text` | field from the `properties` object |
| <CopyableCode code="phone" /> | `text` | field from the `properties` object |
| <CopyableCode code="securityContactName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Resource type |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id |
| <CopyableCode code="name" /> | `string` | Resource name |
| <CopyableCode code="properties" /> | `object` | Describes security contact properties |
| <CopyableCode code="type" /> | `string` | Resource type |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="securityContactName, subscriptionId" /> | Get Default Security contact configurations for the subscription |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | List all security contact configurations for the subscription |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="securityContactName, subscriptionId" /> | Create security contact configurations for the subscription |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="securityContactName, subscriptionId" /> | Delete security contact configurations for the subscription |

## `SELECT` examples

List all security contact configurations for the subscription

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_contacts', value: 'view', },
        { label: 'contacts', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
emails,
is_enabled,
notifications_by_role,
notifications_sources,
phone,
securityContactName,
subscriptionId,
type
FROM azure.security.vw_contacts
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
properties,
type
FROM azure.security.contacts
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>contacts</code> resource.

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
INSERT INTO azure.security.contacts (
securityContactName,
subscriptionId,
properties
)
SELECT 
'{{ securityContactName }}',
'{{ subscriptionId }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: properties
      value:
        - name: emails
          value: string
        - name: phone
          value: string
        - name: isEnabled
          value: boolean
        - name: notificationsSources
          value:
            - - name: sourceType
                value: string
        - name: notificationsByRole
          value:
            - name: state
              value: string
            - name: roles
              value:
                - []
    - name: id
      value: string
    - name: name
      value: string
    - name: type
      value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>contacts</code> resource.

```sql
/*+ delete */
DELETE FROM azure.security.contacts
WHERE securityContactName = '{{ securityContactName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
