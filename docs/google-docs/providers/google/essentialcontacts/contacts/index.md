---
title: contacts
hide_title: false
hide_table_of_contents: false
keywords:
  - contacts
  - essentialcontacts
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
<tr><td><b>Id</b></td><td><CopyableCode code="google.essentialcontacts.contacts" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. The identifier for the contact. Format: {resource_type}/{resource_id}/contacts/{contact_id} |
| <CopyableCode code="email" /> | `string` | Required. The email address to send notifications to. The email address does not need to be a Google Account. |
| <CopyableCode code="languageTag" /> | `string` | Required. The preferred language for notifications, as a ISO 639-1 language code. See [Supported languages](https://cloud.google.com/resource-manager/docs/managing-notification-contacts#supported-languages) for a list of supported languages. |
| <CopyableCode code="notificationCategorySubscriptions" /> | `array` | Required. The categories of notifications that the contact will receive communications for. |
| <CopyableCode code="validateTime" /> | `string` | The last time the validation_state was updated, either manually or automatically. A contact is considered stale if its validation state was updated more than 1 year ago. |
| <CopyableCode code="validationState" /> | `string` | Output only. The validity of the contact. A contact is considered valid if it is the correct recipient for notifications for a particular resource. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="folders_contacts_get" /> | `SELECT` | <CopyableCode code="contactsId, foldersId" /> | Gets a single contact. |
| <CopyableCode code="folders_contacts_list" /> | `SELECT` | <CopyableCode code="foldersId" /> | Lists the contacts that have been set on a resource. |
| <CopyableCode code="organizations_contacts_get" /> | `SELECT` | <CopyableCode code="contactsId, organizationsId" /> | Gets a single contact. |
| <CopyableCode code="organizations_contacts_list" /> | `SELECT` | <CopyableCode code="organizationsId" /> | Lists the contacts that have been set on a resource. |
| <CopyableCode code="projects_contacts_get" /> | `SELECT` | <CopyableCode code="contactsId, projectsId" /> | Gets a single contact. |
| <CopyableCode code="projects_contacts_list" /> | `SELECT` | <CopyableCode code="projectsId" /> | Lists the contacts that have been set on a resource. |
| <CopyableCode code="folders_contacts_create" /> | `INSERT` | <CopyableCode code="foldersId" /> | Adds a new contact for a resource. |
| <CopyableCode code="organizations_contacts_create" /> | `INSERT` | <CopyableCode code="organizationsId" /> | Adds a new contact for a resource. |
| <CopyableCode code="projects_contacts_create" /> | `INSERT` | <CopyableCode code="projectsId" /> | Adds a new contact for a resource. |
| <CopyableCode code="folders_contacts_delete" /> | `DELETE` | <CopyableCode code="contactsId, foldersId" /> | Deletes a contact. |
| <CopyableCode code="organizations_contacts_delete" /> | `DELETE` | <CopyableCode code="contactsId, organizationsId" /> | Deletes a contact. |
| <CopyableCode code="projects_contacts_delete" /> | `DELETE` | <CopyableCode code="contactsId, projectsId" /> | Deletes a contact. |
| <CopyableCode code="folders_contacts_patch" /> | `UPDATE` | <CopyableCode code="contactsId, foldersId" /> | Updates a contact. Note: A contact's email address cannot be changed. |
| <CopyableCode code="organizations_contacts_patch" /> | `UPDATE` | <CopyableCode code="contactsId, organizationsId" /> | Updates a contact. Note: A contact's email address cannot be changed. |
| <CopyableCode code="projects_contacts_patch" /> | `UPDATE` | <CopyableCode code="contactsId, projectsId" /> | Updates a contact. Note: A contact's email address cannot be changed. |
| <CopyableCode code="folders_contacts_compute" /> | `EXEC` | <CopyableCode code="foldersId" /> | Lists all contacts for the resource that are subscribed to the specified notification categories, including contacts inherited from any parent resources. |
| <CopyableCode code="folders_contacts_send_test_message" /> | `EXEC` | <CopyableCode code="foldersId" /> | Allows a contact admin to send a test message to contact to verify that it has been configured correctly. |
| <CopyableCode code="organizations_contacts_compute" /> | `EXEC` | <CopyableCode code="organizationsId" /> | Lists all contacts for the resource that are subscribed to the specified notification categories, including contacts inherited from any parent resources. |
| <CopyableCode code="organizations_contacts_send_test_message" /> | `EXEC` | <CopyableCode code="organizationsId" /> | Allows a contact admin to send a test message to contact to verify that it has been configured correctly. |
| <CopyableCode code="projects_contacts_compute" /> | `EXEC` | <CopyableCode code="projectsId" /> | Lists all contacts for the resource that are subscribed to the specified notification categories, including contacts inherited from any parent resources. |
| <CopyableCode code="projects_contacts_send_test_message" /> | `EXEC` | <CopyableCode code="projectsId" /> | Allows a contact admin to send a test message to contact to verify that it has been configured correctly. |

## `SELECT` examples

Lists the contacts that have been set on a resource.

```sql
SELECT
name,
email,
languageTag,
notificationCategorySubscriptions,
validateTime,
validationState
FROM google.essentialcontacts.contacts
WHERE foldersId = '{{ foldersId }}';
```

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
INSERT INTO google.essentialcontacts.contacts (
foldersId,
email,
notificationCategorySubscriptions,
validateTime,
languageTag
)
SELECT 
'{{ foldersId }}',
'{{ email }}',
'{{ notificationCategorySubscriptions }}',
'{{ validateTime }}',
'{{ languageTag }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: validationState
      value: string
    - name: email
      value: string
    - name: notificationCategorySubscriptions
      value:
        - string
    - name: validateTime
      value: string
    - name: languageTag
      value: string
    - name: name
      value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>contacts</code> resource.

```sql
/*+ update */
UPDATE google.essentialcontacts.contacts
SET 
email = '{{ email }}',
notificationCategorySubscriptions = '{{ notificationCategorySubscriptions }}',
validateTime = '{{ validateTime }}',
languageTag = '{{ languageTag }}'
WHERE 
contactsId = '{{ contactsId }}'
AND foldersId = '{{ foldersId }}';
```

## `DELETE` example

Deletes the specified <code>contacts</code> resource.

```sql
/*+ delete */
DELETE FROM google.essentialcontacts.contacts
WHERE contactsId = '{{ contactsId }}'
AND foldersId = '{{ foldersId }}';
```
